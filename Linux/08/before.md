# Before class quiz (#8)

The quiz has to be submitted to your GitLab project before your lab starts.

Every question is worth 25 points.

Insert your answer inside the marked block (replace the ellipsis).



## Question Q1

Briefly describe what was the most difficult or challenging part of the
previous lab for you.

Your answer: **[A1]** maybe sed but i got it **[/A1]**



## Question Q2

We have the following extended regular expression.

```
^(a[bc]+[d-z]|A.C*)$
```

Select which of the strings are matched by the expression.

1. `abcd`
2. `acacz`
3. `abbbe`
4. `az`
5. `A.C`
6. `AA`
7. `A`
8. `ABCABC`
9. `ABCCCC`

Your answer: **[A2]** 5 8 9 **[/A2]**



## Question Q3

Select the best description of what the following command does.

```
egrep '[0-9]{4,6}'
```

1. It prints lines containing literally `[0-9]{4,6}`.
2. It prints all numbers from stdin with 4--6 digits, each on a separate line.
3. It prints just lines, which are numbers of 4--6 digits.
4. It prints just lines containing a number, which has at least 4 digits.
5. It prints just lines containing a number, which has at least 4 digits but no more than 6.

Your answer: **[A3]** 5 **[/A3]**



## Question Q4

Select which replacements will be done by the following command.

```
sed 's=\(https\{0,1\}\)://[^/ ]*=\1://example.com='
```

1. `https0://myweb.org` -> `https0://example.com`
2. `://aaa` -> `://example.com`
3. `http://a/b/c` -> `http://example.com`
4. `https://otherweb.com` -> `https://example.com`
5. `http://web1.cz and https://web2.cz` -> `http://example.com and https://example.com`
6. `ftp://abc.org/file1, https://def.org/file2` -> `ftp://abc.org/file1, https://example.com/file2`
7. `HTTPS://ghi.io/` -> `HTTPS://example.com/`
8. `download("http://company.com","~/homepage.html")` -> `download("http://example.com","~/homepage.html")`

Your answer: **[A4]** 1 4 **[/A4]**



