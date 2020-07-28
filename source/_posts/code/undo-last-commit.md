---
draft: true
comments: true
toc: true
title: "Git: Undo last commit"
date: 2020-04-15T11:59:00+07:00
updated: 2020-04-15T11:59:00+07:00
category:
- git
tags: []
keywords: []

---
so..

    D:\Assets\hugo-arabic-tile>git reset --hard HEAD~1
    HEAD is now at d100567 readme

now, check commit sha1

    D:\Assets\Themes\hugo\arabic\themes\hugo-arabic-tile>git reflog
    d100567 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
    17929a9 (origin/master) HEAD@{1}: commit: readmeen
    d100567 (HEAD -> master) HEAD@{2}: pull: Fast-forward
    bd435c6 HEAD@{3}: reset: moving to HEAD~2
    1889655 HEAD@{4}: pull: Merge made by the 'recursive' strategy.
    fb4cb8e HEAD@{5}: commit: readmo
    bd435c6 HEAD@{6}: reset: moving to HEAD~1
    d100567 (HEAD -> master) HEAD@{7}: pull origin master: Fast-forward
    bd435c6 HEAD@{8}: reset: moving to HEAD~1
    d100567 (HEAD -> master) HEAD@{9}: pull: Fast-forward
    bd435c6 HEAD@{10}: reset: moving to HEAD~1
    d100567 (HEAD -> master) HEAD@{11}: pull: Fast-forward
    bd435c6 HEAD@{12}: reset: moving to HEAD~1
    ...

where d100567 is the `discarded commit`.

Now just move the head to that commit::

    D:\Assets\hugo-arabic-tile>git reset --hard d100567
    HEAD is now at d100567 readme

then push

    D:\Assets\hugo-arabic-tile>git push -u origin master
    To https://github.com/bimagv/hugo-arabic-tile.git
     ! [rejected]        master -> master (non-fast-forward)
    error: failed to push some refs to 'https://github.com/bimagv/hugo-arabic-tile.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Integrate the remote changes (e.g.
    hint: 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    
    ##oh no with --force
    
    D:\Assets\hugo-arabic-tile>git push -u origin master --force
    Total 0 (delta 0), reused 0 (delta 0)
    To https://github.com/bimagv/hugo-arabic-tile.git
     + 17929a9...d100567 master -> master (forced update)
    Branch 'master' set up to track remote branch 'master' from 'origin'.
    
    D:\Assets\Themes\hugo\arabic\themes\hugo-arabic-tile>