# Description

A simple utility script written in Python 3, which counts lines of insertions & deletions in all commits of a given repo, and prints them by file extension in stdout.

Typical output is like:
```
Repo loc Statistics:
93 commits in total
9400 loc | 10111 lines of insertions and 711 lines of deletions in all commits
    4773  loc    |    5071  insersions and 298   deletions in *.py
    2496  loc    |    2804  insersions and 308   deletions in *.cpp
    778   loc    |    831   insersions and 53    deletions in *.xacro
    336   loc    |    337   insersions and 1     deletions in *.hpp
    308   loc    |    337   insersions and 29    deletions in *.launch
    183   loc    |    184   insersions and 1     deletions in *.txt
    174   loc    |    176   insersions and 2     deletions in *.h
    173   loc    |    179   insersions and 6     deletions in *.xml
    74    loc    |    76    insersions and 2     deletions in *.md
    25    loc    |    28    insersions and 3     deletions in .gitignore
    24    loc    |    29    insersions and 5     deletions in *.sh
    18    loc    |    18    insersions and 0     deletions in .gitmodules
    13    loc    |    13    insersions and 0     deletions in *.material
    10    loc    |    10    insersions and 0     deletions in *.msg
    ---
    15    loc    |    18    insertions and 3     deletions in other files
```

Note: items are sorted by lines, in descending order.

# Usage:

Simply run count_commits.py inside a git repo (you may need to chmod +x .../count_commits.py first)
