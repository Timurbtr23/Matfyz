# Tasks 08 (student badretdt)

| Total                                            |    20 |
|--------------------------------------------------|------:|
| 08/timeconv.sh                                   |     0 |
| 08/ip.sh                                         |    20 |
| 08/normalize.sh                                  |     0 |
| 08/markdown.sh                                   |     0 |

If you see an issue with the grading, please
[open a **Confidential Issue**](https://gitlab.mff.cuni.cz/teaching/nswi177/2022/common/forum/-/issues/new?issue[confidential]=true&issue[title]=Grading+Tasks+08)
in the _Forum_.


For assignments with automated tests you will see a TAP-style result output
that you are familiar with from your pipeline tests in GitLab.

The tests also contains information about points assigned (or subtracted)
for that particular test. There are also tests with _zero points_ that
are informative only (kind of like warnings from your compiler: you
should pay attention but they are not crucial).

## 08/timeconv.sh

✅ **Submitted** (passed, informative only)

✅ **Executable** (passed, +0 points)

✅ **Shebang** (passed, +0 points)

✅ **Shellcheck errors** (passed, +0 points)

✅ **Shellcheck warnings** (passed, +0 points)

❌ **Shellcheck infos** (failed, informative only) \

```
-- Shellcheck found following issues (severity info) --
08/timeconv.sh:5:7: note: read without -r will mangle backslashes. [SC2162]
08/timeconv.sh:6:27: note: Double quote to prevent globbing and word splitting. [SC2086]
08/timeconv.sh:7:27: note: Double quote to prevent globbing and word splitting. [SC2086]
--
```

❌ **Shellcheck stylistic** (failed, informative only) \

```
-- Shellcheck found following issues (severity style) --
08/timeconv.sh:5:7: note: read without -r will mangle backslashes. [SC2162]
08/timeconv.sh:6:9: note: See if you can use ${variable//search/replace} instead. [SC2001]
08/timeconv.sh:6:27: note: Double quote to prevent globbing and word splitting. [SC2086]
08/timeconv.sh:7:9: note: See if you can use ${variable//search/replace} instead. [SC2001]
08/timeconv.sh:7:27: note: Double quote to prevent globbing and word splitting. [SC2086]
--
```

❌ **Example run** (failed, worth 7 points) \

```
-- Program output mismatch --
actual (2 lines):
  The event starts at 15:25 and is expected to end at 18:17.
  Registration will be opened from 09:00 until 18:00 .
expected (2 lines):
  The event starts at 15:25 and is expected to end at 18:17.
  Registration will be opened from 09:00 until 06:00 PM.
input (2 lines):
  The event starts at 03:25PM and is expected to end at 06:17PM.
  Registration will be opened from 09:00AM until 06:00 PM.
stderr (0 lines):
--
```

❌ **All AM times** (failed, worth 5 points) \

```
-- Program output mismatch --
actual   : 12:13 13:14 14:15 15:16 16:17 17:18 18:19 19:08 08:09 09:10 10:11 11:12
expected : 00:01 01:02 02:03 03:04 04:05 05:06 06:07 07:08 08:09 09:10 10:11 11:12
input    : 12:01AM 01:02AM 02:03AM 03:04AM 04:05AM 05:06AM 06:07AM 07:08AM 08:09AM 09:10AM 10:11AM 11:12AM
stderr   :
--
```

❌ **All PM times** (failed, worth 5 points) \

```
-- Program output mismatch --
actual   : 12:13 13:14 14:15 15:16 16:17 17:18 18:19 19:08 08:09 09:10 10:11 11:12
expected : 12:01 13:02 14:03 15:04 16:05 17:06 18:07 19:08 20:09 21:10 22:11 23:12
input    : 12:01PM 01:02PM 02:03PM 03:04PM 04:05PM 05:06PM 06:07PM 07:08PM 08:09PM 09:10PM 10:11PM 11:12PM
stderr   :
--
```

❌ **Ignored entries** (failed, worth 3 points) \

```
-- Program output mismatch --
actual   : 12:13  or simple 15:42 or 15 and 16:2 or 13:00 or 13:00
expected : 12:01 PM or simple 15:42 or 15AM and 16:2PM or 13:00PM or 13:00AM
input    : 12:01 PM or simple 15:42 or 15AM and 16:2PM or 13:00PM or 13:00AM
stderr   :
--
```

✅ **No modifications to files in CWD** (passed, informative only)

✅ **Temporary files properly removed** (passed, informative only)



### General notes (collected from all solutions)

We greatly appreciate that several of you actually tried to build
the whole script in `sed`. The solutions that we have seen were however
incomplete and unfortunately did not work in all cases.

Otherwise, it makes perfect sense to build the script like this:

```
#!/bin/sed -f

s/12:\([0-5][0-9]\)PM/12:\1/g
...
```

Try to avoid needless memory consumption. We have seen the following
snippet too many times to leave it without comment.

```shell
input="$( cat "$input_file" )"
echo "$input" | sed ...
```

Imagine a 4GB file where each line is less than 1KB long. The above script
would read the whole file into memory into `$input` variable. Calling `echo`
could easily lead to allocation to another 4GB for the parameter inside
`echo` ;-). Actually, there is a rather small limit on the lenght of the
command line (about 2MB) so it would not even work for some inputs.

Compare to simple `sed ... < "$input_file"` where the file would be read
line by line only. Assuming the above mentioned line length, `sed` would
require few kilobytes for building the regular expression and one KB for the
line.

We always execute your tests on small data so it seems this does not matter.
But it does. Shell utilities and pipes are practically useful for filtering
large data and preprocessing them before loading them to more specialized
tools. Get into habit of thinking about the performance a little bit.


## 08/ip.sh

✅ **Submitted** (passed, informative only)

✅ **Executable** (passed, +0 points)

✅ **Shebang** (passed, +0 points)

✅ **Shellcheck errors** (passed, +0 points)

✅ **Shellcheck warnings** (passed, +0 points)

❌ **Shellcheck infos** (failed, informative only) \

```
-- Shellcheck found following issues (severity info) --
08/ip.sh:7:19: note: Double quote to prevent globbing and word splitting. [SC2086]
--
```

❌ **Shellcheck stylistic** (failed, informative only) \

```
-- Shellcheck found following issues (severity style) --
08/ip.sh:7:12: note: Useless echo? Instead of 'cmd $(echo foo)', just use 'cmd foo'. [SC2116]
08/ip.sh:7:19: note: Double quote to prevent globbing and word splitting. [SC2086]
--
```

✅ **Single entry** (passed, +6 points)

✅ **Multiple entries I** (passed, +7 points)

✅ **Multiple entries II** (passed, +7 points)

✅ **No modifications to files in CWD** (passed, informative only)

✅ **Temporary files properly removed** (passed, informative only)



### General notes (collected from all solutions)

Iterating over individual lines is often not needed at all in shell
scripts.

The following snippet is a typical example of completely useless while
loop that only complicates reading and degrades performance (while we
generally do not care much about shell script performance, the difference
between running `sed` once or starting it thousand times could have
serious impact).

```shell
while read -r line; do
    result="$( echo "$line" | sed -e '...' )"
    result="$( echo "$result" | cut ... )"
    echo "$result"
done <"$input"
```

Because the above is completely equivalent to the following pipe ;-)

```shell
<"$input" sed -e '...' | cut ...
```

Many of you decided to use some kind of temporary files to store counters
for each IP address. Funny thing is that with proper filtering, the counting
can be done on the fly quite easily:

```shell
grep 404 # This shall be replaced by matching at the exact position but it
         # is enough to get the right lines
| cut -d ' ' -f 1 # Get the IP address only
# At this point, we are solving a problem of finding the most frequent line
# Hence something along the lines of
| sort | uniq -c | sort -n | tail -n 1
```

No temporary files and actually the whole script can be expressed in two
functions:

```shell
get_malicious_ip_addresses | find_most_frequent_line
```

And what is most important: these two functions can be tested (or debugged)
separately :-)


## 08/normalize.sh

❌ **Submitted** (failed, informative only) \

```
File 08/normalize.sh was not submitted.
```

↷ **Executable** (skipped)

↷ **Shebang** (skipped)

↷ **Shellcheck errors** (skipped)

↷ **Shellcheck warnings** (skipped)

↷ **Shellcheck infos** (skipped)

↷ **Shellcheck stylistic** (skipped)

↷ **Example run I** (skipped)

↷ **Example run II** (skipped)

↷ **Example run III** (skipped)

↷ **Example run IV** (skipped)

↷ **Lots of parent directories** (skipped)

↷ **Special characters** (skipped)

↷ **Complex one** (skipped)

↷ **No modifications to files in CWD** (skipped)

↷ **Temporary files properly removed** (skipped)



### General notes (collected from all solutions)

The most common issue here was handling the repeated replacements.
If the conditional jumps in `sed` seemed frightening to you, simple while
loop can solve it too :-)

```shell
path="$1"

while true; do
    cleaned="$( echo "$path" | sed ... )"
    if [ "$cleaned" = "$path" ]; then
        break
    fi
    path="$cleaned"
done
```

Do not forget that `sed` has the `g` switch for substitutions, thus
removal of `./` can be done in a single run: `s:/[.]/:/:g`.



## 08/markdown.sh

❌ **Submitted** (failed, informative only) \

```
File 08/markdown.sh was not submitted.
```

↷ **Executable** (skipped)

↷ **Shebang** (skipped)

↷ **Shellcheck errors** (skipped)

↷ **Shellcheck warnings** (skipped)

↷ **Shellcheck infos** (skipped)

↷ **Shellcheck stylistic** (skipped)

↷ **Emphasis** (skipped)

↷ **Strong emphasis** (skipped)

↷ **Entities** (skipped)

↷ **Simple link** (skipped)

↷ **Multiple emphasis** (skipped)

↷ **Multiple lines** (skipped)

↷ **Link with query** (skipped)

↷ **Artificial link** (skipped)

↷ **Many links** (skipped)

↷ **No modifications to files in CWD** (skipped)

↷ **Temporary files properly removed** (skipped)



