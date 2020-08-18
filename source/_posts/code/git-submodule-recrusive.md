---
draft: true
comments: true
toc: true
title: "git submodule recrusive: fetch a repo with submodules"
date: 2020-04-19T11:00:00+07:00
updated: 2020-04-19T11:00:00+07:00
category:
- dev
tags:
- git
keywords: []

---

Pada umumnya, setiap proyek perangkat lunak yang dikembangkan oleh seseorang, biasanya akan membutuhkan dan atau bergantung pada proyek lain di repositori lain. 

Submodule memungkinkan Kita untuk memasukkan atau menanamkan satu atau lebih repositori sebagai sub-folder di dalam repositori yang sedang kita buat atau kembangkan.

Dalam masalah ini saya perlu mengklon suatu project yang didalamnya ada beberapa submodule dan mengeset branch ke master.

    $ git clone --recursive git@github.com:bimagv/gitbook.app-r.git
    Cloning into 'gitbook.app-r'...
    Enter passphrase for key '/home/bima/.ssh/id_rsa':
    remote: Enumerating objects: 51, done.
    remote: Counting objects: 100% (51/51), done.
    remote: Compressing objects: 100% (45/45), done.
    remote: Total 51 (delta 4), reused 0 (delta 0), pack-reused 0
    Receiving objects: 100% (51/51), 3.61 MiB | 225.00 KiB/s, done.
    Resolving deltas: 100% (4/4), done.
    
setelah kita melakukan recrusive maka branch nya sudah pasti ada di master, coba saja cek dengan memindahkan branch ke master. Maka pesannya **Already on 'master'**

    $ git checkout master
    Already on 'master'
    Your branch is up to date with 'origin/master'.
    
Nah, setelah clone selesai semua submodule telah beres terinisialisasi. Hal ini sama dengan atau sudah termasuk mengupdate submodule. jadi tidak perlu menjalankan ```git submodule update --init --recursive``` setelah proses klon selesai

tidak perlu lagi menjalankan ini

    $ git submodule update --init --recursive --remote

atau 

    $ git submodule update --recursive

Sebelum kita ingin mempull setiap kali ada yang berubah ke upstream supaya git atomatis update semua itu setelah melakukan pull maka aktifkan dengan 

    $ git config submodule.recurse true
    
selesai dah.. jadi besok-besok ada perubahan baru mempull jadi rapi 

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


## Referensi
- https://explainshell.com/explain?cmd=git+clone+--recursive