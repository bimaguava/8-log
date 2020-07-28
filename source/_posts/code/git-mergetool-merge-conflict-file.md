---
draft: true
comments: true
toc: true
title: 'merge conflict file with git mergetool'
date: 2020-04-16T09:05:00+07:00
updated: 2020-04-16T09:05:00+07:00
category:
- git
tags:
- repair
keywords: []
---

The problem is..

when forked and make changes to the project

and I will push...

    $ git push -u origin master
    Warning: Permanently added the RSA host key for IP address '13.229.188.59' to the list of known hosts.
    Enter passphrase for key '/home/bima/.ssh/id_rsa': 
    To github.com:bimagv/hexo-theme-3-hexo.git
     ! [rejected]        master -> master (fetch first)
    error: failed to push some refs to 'git@github.com:bimagv/hexo-theme-3-hexo.git'
    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    
    $ git pull                                                                                                            ↵
    Enter passphrase for key '/home/bima/.ssh/id_rsa': 
    remote: Enumerating objects: 22, done.
    remote: Counting objects: 100% (22/22), done.
    remote: Compressing objects: 100% (18/18), done.
    remote: Total 2230 (delta 5), reused 13 (delta 4), pack-reused 2208
    Receiving objects: 100% (2230/2230), 1.41 MiB | 179.00 KiB/s, done.
    Resolving deltas: 100% (1264/1264), done.
    From github.com:bimagv/hexo-theme-3-hexo
     * [new branch]      changeIcon -> origin/changeIcon
     * [new branch]      master     -> origin/master
    There is no tracking information for the current branch.
    Please specify which branch you want to merge with.
    See git-pull(1) for details.
    
        git pull <remote> <branch>
    
    If you wish to set tracking information for this branch you can do so with:
    
        git branch --set-upstream-to=origin/<branch> master

‌

Yeah, you could specify what branch you want to pull:

    git pull origin master

But, you got this

    $ git pull origin master                                                                                              ↵
    Enter passphrase for key '/home/bima/.ssh/id_rsa': 
    From github.com:bimagv/hexo-theme-3-hexo
     * branch            master     -> FETCH_HEAD
    fatal: refusing to merge unrelated histories

Explanation: [https://www.educative.io/edpresso/the-fatal-refusing-to-merge-unrelated-histories-git-error](https://www.educative.io/edpresso/the-fatal-refusing-to-merge-unrelated-histories-git-error "https://www.educative.io/edpresso/the-fatal-refusing-to-merge-unrelated-histories-git-error")

    git pull origin master --allow-unrelated-histories

omg, file conflict

    $ git pull origin master --allow-unrelated-histories                                                                  ↵
    Enter passphrase for key '/home/bima/.ssh/id_rsa': 
    From github.com:bimagv/hexo-theme-3-hexo
     * branch            master     -> FETCH_HEAD
    warning: Cannot merge binary files: source/img/avatar.jpg (HEAD vs. a03c17f85c8d81dd92952c65ab70416f42746cac)
    CONFLICT (add/add): Merge conflict in source/js/search.js
    Auto-merging source/js/search.js
    CONFLICT (add/add): Merge conflict in source/js/script.js
    Auto-merging source/js/script.js
    CONFLICT (add/add): Merge conflict in source/js/jquery.pjax.js
    ...

with --force

    $ git pull origin master --allow-unrelated-histories --force                                                          ↵
    error: Pulling is not possible because you have unmerged files.
    hint: Fix them up in the work tree, and then use 'git add/rm <file>'
    hint: as appropriate to mark resolution and make a commit.
    fatal: Exiting because of an unresolved conflict.

and solution is just merge it manually

    git mergetool -y

If you're on Vscode after merge you can see lot of .orig file then the line current change and incoming change

![Images001a](https://res.cloudinary.com/bimagv/image/upload/v1593780594/2020-04/images001a_mrjs0f.png)

On terminal

    $ cd themes/hexo-theme-3-hexo/
    $ ls
    _config.yml*  _config.yml.orig*  layout/  LICENSE*  README.md*  README.md.orig*  source/
    $ find . -name '*.orig' -delete 
    $ ls
    _config.yml*  layout/  LICENSE*  README.md*  source/

on powershell

    cd \your\repo\directory
    Get-ChildItem -Recurse -Filter '*.orig' | Remove-Item

finally

    git add --all
    git commit -m "mama I can git pull"
    git push -u origin master

on your vscode tap F5 and [Merge Conflict:Accept All Current](https://github.com/bimagv/hexo-theme-3-hexo/commit/dd01cfcd5769615298b7f7b6612ac692dd7d0b73) or Accept incoming change