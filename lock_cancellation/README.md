# lock-cancellation

What happens when you cancel a task while that task holds a lock?

The `asyncio` library automatically releases that lock.
