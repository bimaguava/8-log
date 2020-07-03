---
title: Bash Intro
toc: true
date: 2020-04-12 11:11:57
tags: bash
categories: 
- linux
---

Skrip Bash adalah sebuah plain-text file yang berisi serangkaian perintah yang dieksekusi seolah-olah mereka telah diketik di terminal prompt. 

Secara umum, skrip Bash memiliki biasanya memiliki ekstensi **.sh** (untuk kemudahan
Identifikasi), mulai dengan **#!/bin/bash** dan harus memiliki izin yang dapat dieksekusi yang ditetapkan sebelum dapat dieksekusi.

Contoh:


    $ cat ./hello-world.sh #!/bin/bash
    # Hello World Bash Script
    echo "Hello World!"

    $ chmod +x bash.sh
    $ ./hello.sh

* tanda "#" digunakan sebagai comment
* echo "Hello World!" digunakan untuk print string yang diberikan ke terminal
* opsi +x adalah untuk membuat skrip menjadi executable
* **./** adalah untuk me-run file tersebut
* **/bin/bash**, adalah absolut path ke interpreter, yang digunakan untuk menjalankan skrip. Ini adalah apa yang menjadikan "skrip Bash" sebagai kebalikan dari skrip shell jenis lain, seperti "skrip C Shell"

## Variabel

Variabel dinamai tempat untuk menyimpan data **sementara**. Kita dapat mengatur (atau “mendeklarasikan”) suatu variabel, yang ditugaskan
nilai untuk itu, atau membaca variabel, yang akan "memperluas" atau "menyelesaikannya" ke nilai yang disimpan.

Mendeklarasikan variabel bisa melalui beberapa cara, seperti mengatur nilai secara langsung

name=value

    $ first_name=Good
    $ last_name=People

Untuk melakukannya, kita mendahului variabel dengan
"$" Karakter. Setiap kali Bash menemukan sintaks ini dalam suatu perintah, itu menggantikan nama variabel dengan nilai ("perluas" variabel) sebelum eksekusi:


    $ echo $first_name $last_name
    Good People

atau menggunakan command

    bima@x220:~$ user=$(whoami)
    bima@x220:~$ echo $user
    bima