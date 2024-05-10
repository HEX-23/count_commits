#! /usr/bin/env python3

import subprocess

if __name__ == '__main__':
    p = subprocess.Popen(['git', 'log', '--numstat', '--oneline'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    src = p.stdout.read()
    # print(src)
    entries = list(map(lambda l : l.strip().split(), src.strip().split(b'\n')))
    commit_count = 0
    def ffn(l):
        if l[0].isdigit() and l[1].isdigit():
            return True
        else:
            global commit_count
            commit_count += 1
            return False
    entries = list(filter(ffn, entries))
    insertions = 0
    deletions = 0
    insertions_by_suf = dict()
    deletions_by_suf = dict()
    insertions_misc = 0
    deletions_misc = 0
    for e in entries:
        insertions += int(e[0])
        deletions += int(e[1])
        if b'.' in e[-1]:
            components = e[-1].split(b'.')
            if len(components) > 1 and len(components[-2]) > 0:
                suf = b'*.' + components[-1]
            else:
                suf = b'.' + components[-1]
            if suf in insertions_by_suf:
                insertions_by_suf[suf] += int(e[0])
                deletions_by_suf[suf] += int(e[1])
            else:
                insertions_by_suf[suf] = int(e[0])
                deletions_by_suf[suf] = int(e[1])
        else:
            insertions_misc += int(e[0])
            deletions_misc += int(e[1])
    print('Repo loc Statistics:')
    print(f'{commit_count} commits in total')
    print(f'{insertions - deletions} loc | {insertions} lines of insertions and {deletions} lines of deletions in all commits')
    lines = []
    for k, i in insertions_by_suf.items():
        lines.append(f'    {i - deletions_by_suf[k]: <5} loc    |    {i: <5} insersions and {deletions_by_suf[k]: <5} deletions in {k.decode("utf-8")}')
    lines.sort(key=lambda s : -int(s.split()[0]) * 100000 - int(s.split()[3]))
    print('\n'.join(lines))
    if insertions_misc > 0 or deletions_misc > 0:
        print(f'    ---\n    {insertions_misc - deletions_misc: <5} loc    |    {insertions_misc: <5} insertions and {deletions_misc: <5} deletions in other files')
