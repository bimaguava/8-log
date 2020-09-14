---
draft: true
comments: true
toc: true
title: "git: Multiple SSH in one machine"
date: 2020-04-18T12:06:00+07:00
updated: 2020-04-18T01:00:00+07:00
category:
- dev
- vcs
tags:
- git
- ssh
keywords: []
---

Contohnya sekarang ada dua akun github yang ingin kita urus dan saya akan menghapus `global config` supaya saya tidak bingung

    $ git config --global --unset user.name
    $ git config --global --unset user.email

## Generate SSH

ini akan menghasilkan dua file `id_rsa_work_bima `dan `id_rsa_work_bima.pub`

    PS C:\Users\bima> cd .ssh
    
    ssh-keygen -t rsa -C "bimaguava@gmail.com" -f "id_rsa_work_bima"
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in id_rsa_work_bima.
    Your public key has been saved in id_rsa_work_bima.pub.
    The key fingerprint is:
    SHA256:4eQcfoKIdnwvhKyABoN0jYJA1VHUmVYYaij86SjKyVE bimaguava@gmail.com
    The key's randomart image is:
    +---[RSA 2048]----+
    |=o.o+.+o..*.     |
    |+.o. o. .*       |
    |+ .o . o=        |
    |o. +oooB o       |
    |o.oE*o+ S .      |
    |.o.ooo . o       |
    | o.. .. .        |
    |+ +    .         |
    |.+               |
    +----[SHA256]-----+

‌

kita tambahkan untuk yang kedua dengan nama yang berbeda

    ssh-keygen -t rsa -C "jacksound.jkt@gmail.com" -f "id_rsa_work_jack"
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in id_rsa_work_jack.
    Your public key has been saved in id_rsa_work_jack.pub.
    The key fingerprint is:
    SHA256:QOH1XSRxAJB3x25rubJeqXKFVwix4E8MemG2ICbY3I4 jacksound.jkt@gmail.com
    The key's randomart image is:
    +---[RSA 2048]----+
    |   +..=.+oB.=*+  |
    |  . o=.o.B.Bo=o  |
    |     oo ..=.=+ . |
    |    E .. . o  + .|
    |        S   .o + |
    |            . *. |
    |             +o. |
    |          . oo.  |
    |           ++o   |
    +----[SHA256]-----+

maka di folder .ssh akan ada file

* id_rsa_work_bima
* id_rsa_work_bima.pub
* id_rsa_work_jack
* id_rsa_work_jack.pub

Jadi setelah itu kita sudah bisa mengcopy public key tersebut ke github sekarang.

## Konfig SSH

pada `~/.ssh/config`

    # first account, - the default config
    Host github.com
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_rsa_work_bima
       
    # second account-1
    Host github.com-work_jack   
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_rsa_work_jack

## Registering SSH Keys to ssh agent

untuk menggunakan key tersebut kita bisa meregistrasikannya ke mesin kita dengan `ssh-agent` agar salah satu key yang kita tambahkan dengan `ssh-add` akan bertindak saat kita bekerja (selama ssh-agent aktif)

    $ eval `ssh-agent -s`
    Agent pid 8916
    $ ssh-add id_rsa_work_bima
    
    $ ssh-add -l
    2048 SHA256:4eQcfoKIdnwvhKyABoN0jYJA1VHUmVYYaij86SjKyVE id_rsa_work_bima (RSA)

‌

dan kita bisa melepaskan private key yang telah di simpan ke `ssh-agent` ini dan menambahkan `key id_rsa_work_jack`

    $ ssh-add -D
    $ ssh add id_rsa_work_jack

setelah koneksi `id_rsa_work_bima` diputus maka kita bisa mulai untuk bekerja dengan key yang kedua dengan menambahkannya ke ssh-agent.

## Saat mengklon repositori

Maka saat mengklon repositori host yang digunakan yaitu yang ada dalam konfig ssh misal dengan host `github.com-work_jack`

    $ git clone git@github.com-work_jack/repo_name.git

## Pada repositori lokal yang telah ada

pada project direktori kita periksa list git remote yang terdaftar dengan `git remote -v` dan kita akan menambahkan

    git remote set-url origin git@github.com-work_jack:work_jack/repo_name.git

## Pada saat membuat repositori baru

biasanya kita inisialisasi project yang ingin kita buat dengan `git init` dan git remote

    git remote add origin git@github.com-work_jack:work_jack/repo_name.git 

catatan ini kesimpulan dari tulisan:

[https://yelog.org/2016/09/30/computer-mutiple-github-account/](https://yelog.org/2016/09/30/computer-mutiple-github-account/ "https://yelog.org/2016/09/30/computer-mutiple-github-account/")