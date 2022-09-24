# Before class quiz (#4)

The quiz has to be submitted to your GitLab project before your lab starts.

Every question is worth 25 points.

Insert your answer inside the marked block (replace the ellipsis).



## Question Q1

Briefly describe what was the most difficult or challenging part of the
previous lab for you.

Your answer: **[A1]** The part with cut and its arguments **[/A1]**



## Question Q2

We have seen program arguments (`sys.argv`) and standard
input (`sys.stdin`).

Select all choices that represent correct statements.

1. `sys.argv` is actually the same as `sys.stdin`.
2. standard input is _always_ connected to a keyboard.
3. `sys.argv` is usually used to change program behaviour.
4. `sys.stdin` is usually used for reading input data.
5. `sys.argv[1]` always refers to name of the file that is available
   as `sys.stdin`
6. `sys.stdin` is used to print error messages.
7. `sys.argv` can be used to specify program return (exit) code.

Your answer: **[A2]** 3 4 **[/A2]**



## Question Q3

Read the following mini program in Python.

```
#!/usr/bin/env python3

import sys

def usage(output):
    print("Usage: {} NUMBER".format(sys.argv[0]), file=output)
    print("...")

def main():
    if len(sys.argv) != 2:
        usage(sys.stderr)
        sys.exit(2)
    if sys.argv[1] == "--help":
        usage(sys.stdout)
        sys.exit(0)

    try:
        number = int(sys.argv[1])
        if number % 2 == 0:
            sys.exit(0)
        else:
            sys.exit(1)
    except ValueError:
        usage(sys.stderr)
        sys.exit(2)

if __name__ == '__main__':
    main()
```

Select all choices that represent correct statements about the
above program.

1. Invalid program invocation terminates with exit code 2.
2. If a number is provided, the program checks if it is odd or even
   and reports the result via exit code.
3. The input number is read from standard input.
4. The program never prints anything to standard output.
5. Invalid invocation prints a short help to stderr.
6. Invocation with `--help` (as the only argument) prints the short help.
7. Invocation with `--help` (as the only argument) terminates with non-zero exit code.
8. The program name is probably something like `is_even`.

Your answer: **[A3]** 2 5 8 **[/A3]**



## Question Q4

Select all choices that represent correct statements about stdout
and stderr.

1. Stdout and stderr behave as opened (text) files.
2. Stdout and stderr might be connected to the same device but
   they are logically different.
3. In Python, `sys.stdout == sys.stderr` is always true.
4. Program must check for redirection of stdout by checking for
   `>` being a first letter of the last element of `sys.argv`.
5. Stdout redirection is done before a program is launched.
Your answer: **[A4]** 1 4 **[/A4]**



