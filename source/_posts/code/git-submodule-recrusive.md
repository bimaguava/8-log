---
draft: true
comments: true
toc: true
title: git submodule recrusive
date: 2020-04-19T11:00:00+07:00
updated: 2020-04-19T11:00:00+07:00
category:
- git
tags: []
keywords: []

---
Jadi sekarang alur kerjanya terlihat seperti ini:‌

klon project, saat perubahan baru telah dibuat kita bisa mengupdate commit baru tersebut ke struktur folder project kita, lalu ```git pull```

    $ git clone --recursive git@github.com:bimagv/gitbook.app-r.git
    Cloning into 'gitbook.app-r'...
    Enter passphrase for key '/home/bima/.ssh/id_rsa':
    remote: Enumerating objects: 51, done.
    remote: Counting objects: 100% (51/51), done.
    remote: Compressing objects: 100% (45/45), done.
    remote: Total 51 (delta 4), reused 0 (delta 0), pack-reused 0
    Receiving objects: 100% (51/51), 3.61 MiB | 225.00 KiB/s, done.
    Resolving deltas: 100% (4/4), done.
    
    $ git checkout master
    Already on 'master'
    Your branch is up to date with 'origin/master'.
    
    $ git submodule update --init --recursive --remote
    
    $ git config submodule.recurse true
    
    $ git pull
    Enter passphrase for key '/home/bima/.ssh/id_rsa':
    remote: Enumerating objects: 6, done.
    remote: Counting objects: 100% (6/6), done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (4/4), 1.06 KiB | 362.00 KiB/s, done.
    From github.com:bimagv/gitbook.app-r
    e5ee910..80113c0  master     -> origin/master
    Updating e5ee910..80113c0
    Fast-forward
    SUMMARY.md       | 1 +
    incoming-call.md | 4 ++++
    2 files changed, 5 insertions(+)
    create mode 100644 incoming-call.md
    $