There are several ways that a task can be concluded:

Finish normally and produce a result (which can be None/Unit).

Report an error.

Be forcibly terminated, possibly leaving the program in an uncertain state.

Coroutines have known safe suspension points so they can automatically produce #1 and #2. Because threads are suspended preemptively, the programmer is responsible for producing #1 and #2. With threads, #3 is always a possibility—the thread can always be killed externally without giving the task any notice or any way to clean itself up and conclude gracefully. The fundamental problem with threads is that you (A) never know when they will be interrupted by an OS context switch and (B) never know when they might be terminated. To reign in this problem, we must eliminate #3 from our concurrency story. With threads, the typical approach is to write the code so A and B don’t matter.

With coroutines, we have mostly-safe context switching (it’s still possible—albeit much harder than with threads—to write code that produces data races in Python and Go, but Rust prevents it). Python’s coroutines have built-in cancellation handling (as I covered here), and this turns out to be tightly coupled with its ability to handle errors.

So, we can create a bunch of tasks that run “at the same time” (different languages/systems have different meanings for that phrase), which means that all these concurrently-running tasks have the ability to express errors “at the same time.”

Now the question is, how and when do we check for errors? If an error occurs in more than one task, what happens if another error occurs “at the same time” in another task? We don’t want one error to somehow erase or otherwise supersede other errors.

Also, what should happen to the other tasks when an error occurs? If there’s a failure in one task, we cannot necessarily rely on anything produced by the other tasks. We can either let those tasks run to completion, capture the results, and let the programmer decide what to do based on the error(s)—Rust’s tokio library does this by default—or assume that all the results in the other tasks are useless and cancel everything, which Python asyncio does because it has a built-in cancellation system. (What does Go do???).

Notice that there’s an implicit assumption in the above description: that there is a group of tasks that start together and have some kind of completion point, where you can handle the error conditions of this group. This is important because we must allow the programmer to handle errors at the lowest possible level of granularity—that is, as close as possible to the point where the error occurs, because you know the most at the smallest level of granularity, and can make the most accurate decisions. This isn’t to say you are forced to deal with errors at the smallest granularity, but that a good system will enable that.

Traditional concurrency systems, being based on threads, tend to think of tasks as one-at-a-time activities. However, we virtually always create multiple tasks (otherwise, you’re not getting concurrency benefits). Handling these tasks as cohesive groups is the foundation of structured concurrency. It’s quite similar to our evolution from randomly jumping around a program to restricting ourselves to functions. Structured concurrency creates a finite scope for a group of coroutines, in the same way that a function creates a scope for a piece of code. The constraint of using this scope enables you to know things about how your code works, and elevates the programmer from worrying about small details, increasing productivity and reliability. You can read the seminal introduction to structured concurrency here.

In languages without structured concurrency, the programmer must use some kind of “join” to create a completion point where all the tasks must finish, thus creating a de facto scope (there are usually multiple ways to achieve this “join”). A structured concurrency mechanism explicitly creates this scope, and thus has a completion point where it can return a result containing the results and errors from the individual tasks. The scope provided by structured concurrency gives us the smallest granularity for a group of tasks.

The Rust Approach

Because Rust requires you to use Return to capture errors, it doesn’t need exceptions. This is a feature, because exceptions are side effects, while Return forces you to handle errors at the point where they occur—at that smallest-level-of-granularity.

In the following example, I use the thiserror crate to produce error types that mimic the ones I use in the subsequent Python program. As usual, I default to using the tokio coroutine library because that is far and away the most commonly used.

use std::sync::Arc;
use std::time::Duration;
use thiserror::Error;
use tokio::sync::Mutex;
use tokio::time::sleep;
use FallibleError::*;

#[derive(Error, Debug)]
pub enum FallibleError {
    #[error("V[{0}]")]
    ValueError(i32),
    #[error("T[{0}]")]
    TabError(i32),
    #[error("A[{0}]")]
    AttributeError(i32),
}

async fn fallible(
    i: i32,
    stdout: Arc<Mutex<()>>,
) -> Result<char, FallibleError> {
    sleep(Duration::from_millis(100)).await;
    {
        // Only one task can print at a time:
        let _lock = stdout.lock().await;
        println!("fallible({})", i);
    } // _lock released

    match i {
        1 => Err(ValueError(i)),
        3 => Err(TabError(i)),
        5 | 6 => Err(AttributeError(i)),
        // 7 => panic!("i:{} panicked!", i),
        _ => {
            sleep(Duration::from_secs(3)).await;
            Ok((b'a' + i as u8) as char)
        }
    }
}

#[tokio::main]
async fn main() {
    // Keeps tasks from interleaving std output:
    let stdout = Arc::new(Mutex::new(()));

    let tasks: Vec<_> = (0..8)
        .map(|i| {
            tokio::spawn(fallible(i, stdout.clone()))
        })
        .collect();

    // Tasks haven't started yet; no contention:
    println!("Tasks created");

    // Start & run all tasks to completion:
    let results: Vec<_> =
        futures::future::join_all(tasks).await;

    for result in results.iter() {
        // Coroutines finished: no lock needed here
        print!("{:?} => ", result);
        match result {
            Ok(Ok(l)) => println!("Letter: {}", l),
            Ok(Err(e)) => println!("Err: {}", e),
            Err(p) => println!("Panic: {:?}", p),
        }
    }
}

The thiserror crate allows you to easily create error types, including numerous formatting options around error results; FallibleError is about the simplest application of this tool.

fallible() attempts to take its i32 argument and turn it into a char, with a failure producing different types of FallibleError. I’ve added sleep()s to make things interesting.

Standard output is a shared resource, which means that if multiple coroutines use this shared resource they may step on each other, producing interleaved output. To prevent this, we create a Mutex called stdout and require that any task that wants to write to standard output must first acquire this lock. Because stdout (created at the beginning of main()) is shared across all the tasks, it must be wrapped in an Arc so it can be cloned.

main() creates a Vec of fallible() tasks. Rust tasks do not start until they are polled, so we see “Tasks created” before any of the tasks start running (and this output doesn’t need protection). The call to join_all() both starts the tasks and runs them all to completion.

Once the tasks are complete, they no longer compete for standard output so displaying results doesn’t need to be mutexed.

In the final pattern match, you can see that a task that returns a result produces Ok(Ok(l)), while a task that returns an error produces Ok(Err(e)). These are produced by the join_all(), which wraps the Result of any task that completes successfully with an Ok which meant that it didn’t panic. If it does panic, we get an Err(p). This way, successful completion, errors, and panics are all handled.

If you uncomment // 7 => panic!("i:{} panicked!", i) you’ll see that the panic is captured by the pattern match, but often the output of the panic will be interleaved with output from other tasks. To solve this you must write a custom panic handler that uses the stdout lock.

Here’s the output. The fallible(n) statements can appear in any order:

Tasks created
fallible(1)
fallible(4)
fallible(2)
fallible(0)
fallible(5)
fallible(6)
fallible(3)
fallible(7)
Ok(Ok('a')) => Letter: a
Ok(Err(ValueError(1))) => Err: V[1]
Ok(Ok('c')) => Letter: c
Ok(Err(TabError(3))) => Err: T[3]
Ok(Ok('e')) => Letter: e
Ok(Err(AttributeError(5))) => Err: A[5]
Ok(Err(AttributeError(6))) => Err: A[6]
Ok(Ok('h')) => Letter: h

You’ll notice that after all the fallible(n) output, there’s a three-second pause. Tokio has no automatic cancellation so despite the fact that there are errors, all the tasks run to completion. (Note: there is work happening on structured concurrency support in Rust, but the current information is spotty at best—there are things like the tokio-scoped library suggesting that you should use async_scoped instead; I was unable to find any complete working examples of the latter.)

The Python Approach

Python supports structured concurrency with asyncio.TaskGroup. If a task in a TaskGroup throws an exception, the rest of the tasks in that group are automatically cancelled. With this concept of the group and its scope, the programmer doesn’t have to do all this rote management.

Here’s the Python version of the fallible() function. I did not encounter any problems with output in the Python example (probably because of the GIL) so I have not investigated that issue (code for all the Python examples):

# fallible.py
import asyncio
from asyncio import CancelledError
from pprint import pformat


async def fallible(i: int) -> str:
    await asyncio.sleep(0.1)
    print(f"fallible({i})")
    match i:
        # Commenting all but '_' shows success.
        case 1:
            raise ValueError(f"V[{i}]")
        case 3:
            raise TabError(f"T[{i}]")
        case 5 | 6:
            raise AttributeError(f"A[{i}]")
        case _:
            await asyncio.sleep(3)
            # Convert number to letter:
            return chr(ord("a") + i)


def display(e: Exception, msg: str = ""):
    print(f"{msg}{type(e).__name__}")
    if not isinstance(e, CancelledError):
        print(
            f"  {pformat(e.args, indent= 2, width=47)}"
        )

The only way a fallible() task will successfully run to completion is case _.

display() provides (and formats) information about an Exception, but it only displays the args if it is not a CancelledError (which doesn’t contain any args).

First let’s look at what is produced by tasks created within a TaskGroup:

# exception_groups_1.py
import asyncio
from fallible import fallible, display


async def main() -> None:
    tasks = []
    try:
        # raise RuntimeError("Outside TaskGroup")
        async with asyncio.TaskGroup() as tg:
            # raise RuntimeError("In TaskGroup")
            tasks = [
                tg.create_task(
                    fallible(i),
                    name=f"Task {i}",
                )
                for i in range(8)
            ]
        print("No exceptions")
    except Exception as e:
        display(e)
    finally:
        print("- Tasks Complete -")

    for t in tasks:
        print(
            f"{t.get_name()} -> "
            + f"cancelled[{t.cancelled()}]"
        )
        if not t.cancelled():
            try:
                # If it failed, t.result() raises
                print(f"\t{t.result()}")
            except Exception as e:
                display(e)


if __name__ == "__main__":
    asyncio.run(main())

Structured concurrency means that when you reach the end of the async with asyncio.TaskGroup() scope, all tasks are guaranteed to be complete, in some form:

The task is complete and returns a value.

The task fails and produces an error by raising an exception.

The task is cancelled, either from an external agent or because another task in the group raised an exception (the latter cancellation occurs automatically).

This example always throws exceptions so it will never get to print("No exceptions"). We only catch a generic Exception to see what happens, and this is illuminated in the output:

fallible(0)
fallible(2)
fallible(6)
fallible(5)
fallible(7)
fallible(4)
fallible(1)
fallible(3)
ExceptionGroup
  ( 'unhandled errors in a TaskGroup',
  [ AttributeError('A[6]'),
    AttributeError('A[5]'),
    ValueError('V[1]'),
    TabError('T[3]')])
- Tasks Complete -
Task 0 -> cancelled[True]
Task 1 -> cancelled[False]
ValueError
  ('V[1]',)
Task 2 -> cancelled[True]
Task 3 -> cancelled[False]
TabError
  ('T[3]',)
Task 4 -> cancelled[True]
Task 5 -> cancelled[False]
AttributeError
  ('A[5]',)
Task 6 -> cancelled[False]
AttributeError
  ('A[6]',)
Task 7 -> cancelled[True]

If a task that throws an exception within a TaskGroup, that exception becomes/is contained in an ExceptionGroup, which is a type of Exception. And notice that all the errors produced by all the tasks in the group are collected into that single ExceptionGroup.

Capturing Exception Groups

Picking apart exception groups made the feature less-palatable, so they added a way to capture specific types within an exception group. To use this, you say except* instead of just except:

# exception_groups_2.py
import asyncio
from fallible import fallible, display
from asyncio import CancelledError


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(fallible(i))
                for i in range(8)
            ]
    except* ValueError as e:
        display(e)
    except* TabError as e:
        display(e)
    except* AttributeError as e:
        display(e)
    except* CancelledError as e:  # Never happens
        display(e)
    finally:
        print("- Tasks Complete -")

    for t in tasks:
        print(f"{t.get_name()} -> ", end="")
        try:  # Raises exception if no t.result():
            print(f"{t.result()}")
        except Exception as e:
            display(e, "Exception: ")
        # CancelledError is a subclass of BaseException:
        except BaseException as e:
            display(e, "BaseException: ")


asyncio.run(main())

The output shows us how this feature works:

fallible(0)
fallible(2)
fallible(6)
fallible(5)
fallible(7)
fallible(4)
fallible(1)
fallible(3)
ExceptionGroup
  ( 'unhandled errors in a TaskGroup',
  [ValueError('V[1]')])
ExceptionGroup
  ( 'unhandled errors in a TaskGroup',
  [TabError('T[3]')])
ExceptionGroup
  ( 'unhandled errors in a TaskGroup',
  [ AttributeError('A[6]'),
    AttributeError('A[5]')])
- Tasks Complete -
Task-2 -> BaseException: CancelledError
Task-3 -> Exception: ValueError
  ('V[1]',)
Task-4 -> BaseException: CancelledError
Task-5 -> Exception: TabError
  ('T[3]',)
Task-6 -> BaseException: CancelledError
Task-7 -> Exception: AttributeError
  ('A[5]',)
Task-8 -> Exception: AttributeError
  ('A[6]',)
Task-9 -> BaseException: CancelledError

