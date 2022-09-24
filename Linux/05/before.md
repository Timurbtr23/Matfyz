# Before class quiz (#5)

The quiz has to be submitted to your GitLab project before your lab starts.

Every question is worth 25 points.

Insert your answer inside the marked block (replace the ellipsis).



## Question Q1

Briefly describe what was the most difficult or challenging part of the
previous lab for you.

Your answer: **[A1]** I don't understand some scripts such as tr -c -d '0-9' <"$i" | wc -c; but I'll check it what they do **[/A1]**


## Question Q2

Consider the following fragment of a shell script. What text we would
see on the screen?

```shell
COMMAND=echo
MESSAGE=Hello.txt
TARGET=/dev/null
$COMMAND $MESSAGE 2>$TARGET
```

1. Nothing.
2. Contents of file Hello.txt.
3. The string _Hello.txt_.

Your answer: **[A2]** 3 **[/A2]**



## Question Q3

Consider the following fragment of a shell script. Which commands would
be executed? You can safely assume that `/etc/` is a directory.

```shell
if test -d /etc/; then
    head -n 1 /etc/passwd
else
    tail -n 1 /etc/group
fi
```

1. Only `head`.
2. Only `tail`.
3. `test` and `head`.
4. `test` and `tail`.
5. `test`, `head` and `tail`.
6. `head` and `tail` only.

Your answer: **[A3]** 2 **[/A3]**



## Question Q4

Select all choices that represent correct statements about `$PATH`.

1. `$PATH` is an environment variable.
2. Individual entries in `$PATH` are separated by a comma `,`.
3. Empty `$PATH` means we cannot launch any program from a shell
   (but we can run a built-in such as `cd`).
4. `/usr/bin/env` searches `$PATH` when starting a program.
5. `$PATH` contains directories with Git projects.
6. `$PATH` is not searched when the command is specified with a path,
   such as `../ls`.
Your answer: **[A4]** 1 3 4 **[/A4]**



