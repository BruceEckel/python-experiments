import functools
import multiprocessing
import trio
import trio_parallel


def loop(n):
    # Arbitrary CPU-bound work
    for _ in range(n):
        pass
    print("Loops completed:", n)


async def amain():
    t0 = trio.current_time()
    async with trio.open_nursery() as nursery:
        # Do CPU-bound work in parallel
        for i in [6, 7, 8] * 4:
            nursery.start_soon(trio_parallel.run_sync, loop, 10**i)
        # Event loop remains responsive
        t1 = trio.current_time()
        await trio.sleep(0)
        print("Scheduling latency:", trio.current_time() - t1)
        # This job could take far too long, make it cancellable!
        nursery.start_soon(
            functools.partial(trio_parallel.run_sync, loop, 10**20, cancellable=True)
        )
        await trio.sleep(2)
        # Only explicitly cancellable jobs are killed on cancel
        nursery.cancel_scope.cancel()
    print("Total runtime:", trio.current_time() - t0)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    trio.run(amain)
