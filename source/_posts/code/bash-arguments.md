---
title: Bash Arguments
toc: true
date: 2020-04-12 11:11:57
tags: bash
categories: 
- linux
---

Tidak semua skrip Bash memerlukan argumen. mereka ditafsirkan oleh Bash dan bagaimana menggunakannya. Contoh ketika kita menjalankan perintah **ls -l /var/log**, baik -l dan /var/log adalah argumen untuk perintah ls.

```
$ vim subshell.sh

var1=value1 
echo $var1

var2=value2 
echo $var2

$(var1=newvar1) 
echo $var1

`var2=newvar2` 
echo $var2

$ cat ./subshell.sh #!/bin/bash -x
$ chmod +x subshell.sh
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
```

Dalam contoh ini, kita mengubah shebang, menambahkan opsi -x flag. Ini menginstruksikan Bash untuk mencetak tambahan output debug. 

Jadi kita bisa lebih mudah melihat perintah yang dieksekusi dan hasilnya. Saat kita melihat outputnya, perhatikan bahwa perintah yang diawali dengan karakter "+" tunggal dieksekusi di shell saat ini dan perintah yang diawali dengan double “++” dieksekusi dalam sebuah subshell.

Contoh penerapan argumen

```
$ cat ./arg.sh #!/bin/bash
echo "The first two arguments are $1 and $2"

$ chmod +x ./arg.sh
$ ./arg.sh hello there
The first two arguments are hello and there
```