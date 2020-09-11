---
title: 'IPv4: Menghitung Jumlah IP untuk Subnet /24 - /32'
date: 2020-07-05
draft: false
categories: network

---
## Menghafal jumlah IPv4 dari prefix

Dalam kelas-kelasnya prefix ada batasan sesuai kelas IPnya

* Kelas A = /18-/30
* Kelas B = /17-/30
* Kelas C = /19-/30

Untuk menghafal dari /24 - /32 caranya seperti ini
patokannya adalah 24 (256), 28 (16), 32 (1)

* Apabila mencari mengetahui jumlah prefix sekian hanya berpatokan pada itu saja.
  Jika naik maka dikali 2 /pangkat 2, jika turun maka dibagi 2

e.g:

/25
jaraknya lebih dekat ke angka patokan /24 (256). Karena /25 ke /24 turun,
maka 256 dibagi 2 = 128

/26
jika melihat ke /28 (16) maka dibagi 4. Jadi, Karena /26 ke /28 naik,
maka 16 dikali 4 = 64

/24	-
/25
/26
/27
/28	-
/29
/30
/31
/32	-

/25 = 128
/26 = 64
/27 = 32
/28 = 16
/29 = 8
/30 = 4
/31 = 2
/32 = 1

***

Perhitungan yang biasa dilakukan dalam subnetting

### Rentang IP

## Untuk menentukan IP awal

23\.51.120.155/27

kita tahu /27 jumlah ipnya ialah 32
Maka caranya ialah

155 dibagi 32 = 4,8xxx
lalu, 4 dikali 32 = 128

## Untuk menentukan IP akhir

* IP awal + jumlah IP -1

jadi 128 + 32 -1 = 159

Hasinya kita tahu sekarang.
Rentang IP dari 23.51.120.155/27 adalah 23.51.120.128 - 23.51.120.159

## IP Network

Rentang IP dari 23.51.120.155/27 adalah 23.51.120.128 - 23.51.120.159

23\.51.120.128 adalah IP Network

## IP Broadcast

23\.51.120.159 adalah IP Broadcast

## IP host

Dan jumlahnya hostnya ialah 30 untuk /27 pada contoh ini

/27 jumlah ipnya 32, Jadi 32 dikurangi 2 = 30
yang 2 itu ialah IP Network (23.51.120.128) dan IP Broadcast (23.51.120.159)

Jadi IP Hostnya, dari 23.51.120.129 - 23.51.120.158

## Subnet Mask

Masih mengacu contoh pada /27

Untuk mendapatkan subnet mask
kita hanya mengurangi 256 dengan jumlah IP dari /27 yaitu 32

256-32=224

jadi 255.255.255.224