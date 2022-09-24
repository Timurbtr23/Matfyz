# Tasks 03 (student badretdt)

| Total                                            |    70 |
|--------------------------------------------------|------:|
| 03/Using Git CLI                                 |    20 |
| 03/tree.py                                       |     0 |
| 03/factor.py                                     |    20 |
| 03/architecture.sh                               |    10 |
| 03/git.txt                                       |    20 |

If you see an issue with the grading, please
[open a **Confidential Issue**](https://gitlab.mff.cuni.cz/teaching/nswi177/2022/common/forum/-/issues/new?issue[confidential]=true&issue[title]=Grading+Tasks+03)
in the _Forum_.


For assignments with automated tests you will see a TAP-style result output
that you are familiar with from your pipeline tests in GitLab.

The tests also contains information about points assigned (or subtracted)
for that particular test. There are also tests with _zero points_ that
are informative only (kind of like warnings from your compiler: you
should pay attention but they are not crucial).

## 03/Using Git CLI

✅ **Commit found** (passed, +20 points)



## 03/tree.py

✅ **Submitted** (passed, informative only)

✅ **Correct Python script** (passed, +0 points)

✅ **Module-ready** (passed, +0 points)

❌ **Empty directory** (failed, 5 points subtracted) \

```
-- Tree listing differs --
output (7 lines):
  GRADING-before.md
  architecture.sh
  before.md
  factor.py
  git.txt
  git_cli.txt
  tree.py
expected (0 lines):
--
```

❌ **Files only** (failed, 5 points subtracted) \

```
-- Tree listing differs --
output (7 lines):
  GRADING-before.md
  architecture.sh
  before.md
  factor.py
  git.txt
  git_cli.txt
  tree.py
expected (3 lines):
  alpha.txt
  bravo.txt
  charlie.txt
--
```

❌ **Only directories** (failed, 5 points subtracted) \

```
-- Tree listing differs --
output (7 lines):
  GRADING-before.md
  architecture.sh
  before.md
  factor.py
  git.txt
  git_cli.txt
  tree.py
expected (6 lines):
  alpha/
      bravo/
          charlie/
  delta/
      echo/
  foxtrot/
--
```

❌ **Example from web** (failed, 5 points subtracted) \

```
-- Tree listing differs --
output (7 lines):
  GRADING-before.md
  architecture.sh
  before.md
  factor.py
  git.txt
  git_cli.txt
  tree.py
expected (10 lines):
  01/
      factor.py
  02/
      before.md
      temp/
          file.txt
      wildcards.md
  README.md
  bin/
      run_tests.sh
--
```

❌ **Symlinks** (failed, 5 points subtracted) \

```
-- Tree listing differs --
output (7 lines):
  GRADING-before.md
  architecture.sh
  before.md
  factor.py
  git.txt
  git_cli.txt
  tree.py
expected (2 lines):
  target/
      alpha/
--
```

✅ **Executable** (passed, +8 points)

❌ **Example from web with -d argument** (failed, worth 7 points) \

```
-- Tree listing differs --
output (0 lines):
expected (4 lines):
  01/
  02/
      temp/
  bin/
--
```

✅ **With directory argument** (passed, +5 points)

✅ **With -d followed by directory argument** (passed, +5 points)

✅ **With directory argument followed by -d** (passed, +5 points)



## 03/factor.py

✅ **Submitted** (passed, informative only)

✅ **Executable** (passed, +2 points)

✅ **Correct Python script** (passed, +0 points)

✅ **Module-ready** (passed, +0 points)

✅ **Run with 0** (passed, +3 points)

✅ **Run with 2** (passed, +2 points)

✅ **Run with 3** (passed, +2 points)

✅ **Run with 4** (passed, +2 points)

✅ **Run with 24** (passed, +2 points)

✅ **Run with 2022** (passed, +2 points)

✅ **Run with -17** (passed, +2 points)

✅ **Run with xy** (passed, +3 points)



## 03/architecture.sh

✅ **Submitted** (passed, informative only)

✅ **Works** (passed, +0 points)

✅ **Works in a portable way** (passed, informative only)

✅ **Executable** (passed, +5 points)

✅ **Shebang** (passed, +5 points)



## 03/git.txt

✅ **Submitted** (passed, informative only)

✅ **Reasonable content** (passed, +20 points)



