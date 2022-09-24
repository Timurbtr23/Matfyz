# Before class quiz (#11)

The quiz has to be submitted to your GitLab project before your lab starts.

Every question is worth 25 points.

Insert your answer inside the marked block (replace the ellipsis).



## Question Q1

Write here a short feedback about last lab. What was the most
interesting part or what was the most difficult part or any other
thoughts related to the last lab. Please, answer reasonably.

Your answer: **[A1]** Virtualenv was the most interesting part **[/A1]**



## Question Q2

Select from the paragraphs below the one that _best_ describes
the reason why virtual environments are useful.

1. Virtual environment allows the user to clone the project from
   a Git repository without modifying files on the local computer.
2. Virtual environment allows the user to upgrade the project
   dependencies without need to update the operating system first.
3. Virtual environment allows the developer to test the program
   on different operating systems.
4. Virtual environment ensures isolated environment with reproducible
   configuration without changes to the operating system.
5. Virtual environment allows the user to install dependencies
   from PyPI easily.

Your answer: **[A2]** 4 **[/A2]**



## Question Q3

Select from the paragraphs below the ones that provide valid reasons
why directories with virtual environments are usually not committed
to the versioning system (repository).

Multiple answers are possible.

1. Because they can contain system-specific files and would not be
   useful on other systems anyway.
2. Because generally we do not commit files that can be easily
   re-created or re-downloaded.
3. Because Git cannot version directories.
4. Because they might contain configuration files with absolute paths.
5. Because the number of files in such directory is much bigger than
   what Git allows (i.e. it will not be possible to commit all the files
   anyway).

Your answer: **[A3]** 2 **[/A3]**



## Question Q4

Read about Semantic versioning at https://semver.org/ (note that there
are plenty of translations available).

Then decide which of the following statements are correct. We use the
word _requires_ to denote version update that _must_ happen to conform
to semantic versioning. In this sense, fixing a bad code comment might
trigger patch version update (for a library, bad comment can be
considered a bug under certain circumstances) but it is often not
needed.

We are talking in the context of a C library that offers the following
function (for simplicity we do not list other functions but we assume
there is more than one function in the library).

When talking about the changes, we consider rest of the library to
remain unchanged.

```c
int factorial(int number) {
    if (number < 0) {
        return -1;
    } else if (number == 0) {
        return 0;
    } else if (number == 1) {
        return 1;
    } else {
        return number * factorial(number - 1);
    }
}
```

1. Removing the above mentioned `factorial` function requires that we
   increase major version number.
2. Removing the above mentioned `factorial` function requires that we
   increase minor version number.
3. Removing the above mentioned `factorial` function requires that we
   increase patch version number.
4. Adding new function `long factorial_l(long number)` requires that
   we increase major version number.
5. Adding new function `long factorial_l(long number)` requires that
   we increase minor version number.
6. Adding new function `long factorial_l(long number)` requires that
   we increase patch version number.
7. Fixing the value for `0` requires that we increase major version
   number.
8. Fixing the value for `0` requires that we increase minor version
   number.
9. Fixing the value for `0` requires that we increase patch version
   number.
10. Changing the implementation to use a for-loop instead of recursion
    requires that we increase major version number.
11. Changing the implementation to use a for-loop instead of recursion
    requires that we increase minor version number.
12. Changing the implementation to use a for-loop instead of recursion
    requires that we increase patch version number.

Your answer: **[A4]** 1 5 9 11 **[/A4]**



