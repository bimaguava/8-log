---
title: "Bash: Example argument"
toc: true
date: 2020-04-12 11:11:57
tags: bash
categories: 
- code
---

Tidak semua skrip Bash memerlukan argumen. Mereka ditafsirkan oleh Bash dan bagaimana menggunakannya. Contoh ketika kita menjalankan perintah **ls -l /var/log**, baik -l dan /var/log adalah argumen untuk perintah ls itu sendiri


    $ vim subshell.sh

isikan code berikut

    var1=value1 
    echo $var1

    var2=value2 
    echo $var2

    $(var1=newvar1) 
    echo $var1

    `var2=newvar2` 
    echo $var2

jangan lupa tambahkan shebang supaya skrip bisa dieksekusi

    $ cat ./subshell.sh #!/bin/bash -x

untuk membuat skrip menjadi executable beri beri izin

    $ chmod +x subshell.sh

run file tersebut

    $ ./subshell.sh

    + var1=value1
    + echo value1
    value1
    + var2=value2
    + echo value2
    value2
    ++ var1=newvar1
    + echo value1
    value1
    ++ var2=newvar2
    + echo value2
    value2


Dalam contoh ini, kita mengubah shebang, menambahkan opsi -x flag. Ini menginstruksikan Bash untuk mencetak tambahan output debug. 

Jadi kita bisa lebih mudah melihat perintah yang dieksekusi dan hasilnya. Saat kita melihat outputnya, perhatikan bahwa perintah yang diawali dengan karakter "+" tunggal dieksekusi di shell saat ini dan perintah yang diawali dengan double “++” dieksekusi dalam sebuah subshell.

Contoh penerapan argumen

    $ cat ./arg.sh #!/bin/bash

masukkan kode berikut

    echo "The first two arguments are $1 and $2"

change mode

    $ chmod +x ./arg.sh

maka saat dirun kita bisa memasukkan argumen ke nilai yang telah kita berikan diawal
    $ ./arg.sh hello there
    The first two arguments are hello and there


Berbeda dengan variabel yang mana dinamai tempat untuk menyimpan data **sementara**. Kita dapat mengatur (atau “mendeklarasikan”) suatu variabel, yang ditugaskan
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