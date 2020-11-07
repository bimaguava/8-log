---
draft: false
comments: true
toc: true
title: 'IPv6: what the heck it this?'
date: 2020-09-11T12:57:00Z
updated: 
category:
- network
tags:
- ipv6
keywords: []

---
# **Introduction**

![](https://memegenerator.net/img/instances/34434443/prepare-yourself-ipv6-is-coming.jpg)

Bagaimana kabarnya para omnifora? masih setia sama IP versi 4, yakin belum mau coba "aipivi6" yang padahal rumornya IPv4 diduga sudah habis sejak tahun 1990. and we must act.. stop IPv4 and start using IPv6 *fuarkk

> Begitulah cuplikan kata2 media :)

Mungkin iya, tapi yang merasakan dampak itu bukan kita sebagai end user, bagi pengguna internet kita tidak akan merasakan apapun.

Hal itu karena penerimaan IPv6 sudah ada di sebagian besar perangkat, atau dapat diperoleh selama peningkatan perangkat berikutnya.

Jadi, pihak yang sebetulnya merasakan hal ini semestinya ialah penyedia jasa internet alias provider ataupun lembaga-lembaga.

Karena hal itu maka pemakaian IPv4 (Public IP) sehingga akan berganti-gantian seiring berjalannya kebutuhan akan IP yang prosesnya mendapatkannya akan seperti langganan sebuah domain.

Tapi, walaupun keadaan Public IP IPv4 seperti lebih sedikit hal itu tidak menjadikannya barang yang mahal, karena kenyataanya harga sewa IPv6-lah yang lebih mahal :)

# **What we talk about?**

Sekarang kita ingin mengetahui beberapa perbedaan yang mendasar antara IPv4 dan IPv6

## Panjang prefix

Dimulai dari bentuk dari IPv6 itu sendiri, panjang prefix IPv6 adalah 128 bit.

![](https://res.cloudinary.com/bimagv/image/upload/v1599983691/2020-09/1_mambum.png)

Sedangkan pada IPv4 ialah 32 bit dan memiliki 4 kolom yang mana setiap 1 kolom berisi 8 bit yang merupakan bilangan biner.

![](https://res.cloudinary.com/bimagv/image/upload/v1599983691/2020-09/2_mtodbi.png)

Tentang IPv4 silahkan lihat disini: [http://www.mikrotik.co.id/artikel_lihat.php?id=64](http://www.mikrotik.co.id/artikel_lihat.php?id=64 "http://www.mikrotik.co.id/artikel_lihat.php?id=64")

IPv6 ini memiliki 8 kolom yang setiap 1 kolomnya memiliki 16 bit yang merupakan bilangan hexadecimal contohnya **`2001:db8:23fa:00c8::/64`**

jadi, kalau kita nanti mau menghitung subnet atau prefix alias /-nya maka musti menjadikannya bilangan biner terlebih dahulu.