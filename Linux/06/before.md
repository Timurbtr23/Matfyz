# Before class quiz (#6)

The quiz has to be submitted to your GitLab project before your lab starts.

Every question is worth 25 points.

Insert your answer inside the marked block (replace the ellipsis).



## Question Q1

Briefly describe what was the most difficult or challenging part of the
previous lab for you.

Your answer: **[A1]** .Work with variables. Sometimes it's tricky **[/A1]**



## Question Q2

Assuming we are in a directory that contains only `ioargs.py` script
and no other files (of course, there will be always the `.` and `..`
special directories but no other hidden files).

The `ioargs.py` script has the following content (and executable bit
set).

```python
#!/usr/bin/env python3

import sys

def main():
    for i, arg in enumerate(sys.argv):
        print("argv[{}]: '{}'".format(i, arg))
    for line in sys.stdin:
        print("stdin: '{}'".format(line.rstrip('\n')))
    sys.exit(0)

if __name__ == '__main__':
    main()
```

We now invoke the script like this.

```shell
./ioargs.py *.python "< ioargs.py"
```

Select all choices that represent correct statements about
this invocation. When using the word _output_ in the following
statements, we mean standard output, i.e. what we would
see on the screen after executing this program.


1. The invocation is invalid, shell will announce error and not launch
   any program.
2. Output will contain `argv[0]: './ioargs.py'`.
3. Output will contain `stdin: '.'`.
4. Output will contain source code of `ioargs.py` (prefixed with
   `stdin` and each line surrounded by apostrophes).
5. `argv[1]` will be empty as there are no `*.python` files.
6. Program will be waiting for input from the user.
7. Output will contain `argv[1]: '< ioargs.py'`.
8. Standard input will be redirected from `ioargs.py`.

Your answer: **[A2]** 2 5 7 **[/A2]**



## Question Q3

Select all correct statements. You might consider consulting your
manual pages to decide about some of the statements.

1. `uname -r` will print kernel release information
2. `date +%C` will print current year.
3. `mkdir a && mkdir a` will always fail (assuming no other program is running).
4. `fold` reads lines from standard input, printing then in
   reverse order on standard output.
5. `echo -n Hello` will print the string `Hello` without a trailing newline.
6. `ls --full-colors` will terminate with zero exit code (assuming
   standard `ls(1)`).

Your answer: **[A3]** 1 3 5 **[/A3]**



## Question Q4

Select all correct statements. In this question they are related to
Git only.

1. `git clone` uploads new commits to the server.
2. `git add` tells Git to add given files to the next commit.
3. `git log` prints information about existing commits.
4. `git status` cannot work without Internet access
5. `git commit -m "Typo"` will create a commit with commit message `Typo`
   (i.e. commit is created without launching an interactive editor).
6. `git log --format='%s'` will print first line of each commit message
   (subject) when print information about commits.

Your answer: **[A4]** 2 3 5 6 **[/A4]**



