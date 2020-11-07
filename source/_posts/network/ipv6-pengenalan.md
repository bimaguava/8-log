---
draft: false
comments: true
toc: true
title: IPv6 Pengenalan
date: 2020-09-11T12:57:00Z
updated: 
category:
- network
tags:
- ipv6
keywords: []

---
# **Prakata**

Pada artikel atau post ini kita akan belajar untuk mengenal IPv6. Namun sebagai pembuka mari kita renungi gambar ini.

![https://techno.okezone.com/read/2011/01/21/55/416625/alamat-ip-habis-penemu-ipv4-merasa-bersalah#:\~:text=SYDNEY%20%2D%20Vint%20Cerf%2C%20salah%20satu,ia%20buat%20pada%20tahun%201977.](/images/screen_2020-11-07_23-40-25x.png "https://techno.okezone.com/read/2011/01/21/55/416625/alamat-ip-habis-penemu-ipv4-merasa-bersalah#:~:text=SYDNEY%20%2D%20Vint%20Cerf%2C%20salah%20satu,ia%20buat%20pada%20tahun%201977.")

Beliau adalah bapak Internet Protokol, Vint Cerf. Beliau salah satu orang yang pertama sekali membuat internet dengan menyambungkan komputer ke sebuah address yang pertama kali beliau melakukannya berkat coba-coba (sekitar tahun 1977).

IP Address yang berkembang mulai awal-awal tahun itu terus diperbaharui dan dilegalisir oleh IETF (organisasi pengembang open standar protokol TCP/IP)

IETF menerbitkan IP versi 1 sampai 3 antara tahun 1977 sampai 1979 yang merupakan masa-masa pencarian yang luar biasa sampai dimana keluar memorandum (1981), yaitu RFC11666 yang berkaitan dengan metode dan perilaku IPv4.

Selang 7 tahun setelah dengan penelitian dan perjuangan oleh para senior/ pakar IT di Indonesia akhirnya dapat IP Address pertamanya yang berlokasi di UI, 24 Juni 1988.

![](/images/screen_2020-11-08_00-01-43x.png)

Lantas bagaimana IPv4 dengan format 32 bit bisa melayani kebutuhan seluruh dunia dengan 7K miliar lebih (^_^)

Mungkin kita tidak tahu pembagian IP tersebut seperti apa yang jelas kita sampai 2020 masih bisa menikmati IP versi 4 ini. 

Mungkinkah kalimatnya "habis" seperti itu?

Saya rasa tidak juga. Mungkin "habis" disini ialah yang merasakan dampak itu bukan kita sebagai user. Bagi pengguna internet kita tidak akan merasakan apapun. Bahkan rekan Network Admin mungkin juga tidak (^_^)

Hal itu karena penerimaan IPv6 sudah ada di sebagian besar perangkat, atau dapat diperoleh selama peningkatan perangkat berikutnya.

Jadi, pihak yang sebetulnya merasakan hal ini semestinya ialah penyedia jasa internet alias provider ataupun lembaga-lembaga.

Karena hal itu maka pemakaian IPv4 (Public IP) sehingga akan berganti-gantian seiring berjalannya kebutuhan akan IP yang prosesnya mendapatkannya akan seperti langganan sebuah domain.

Tapi, walaupun keadaan Public IP IPv4 seperti lebih sedikit hal itu tidak menjadikannya barang yang mahal, karena kenyataanya harga sewa IPv6-lah yang lebih mahal :)

# **Pembahasan**

Sekarang kita ingin mengetahui beberapa perbedaan yang mendasar antara IPv4 dan IPv6

## Panjang prefix

Dimulai dari bentuk dari IPv6 itu sendiri, panjang prefix IPv6 adalah 128 bit.

![](https://res.cloudinary.com/bimagv/image/upload/v1599983691/2020-09/1_mambum.png)

Sedangkan pada IPv4 ialah 32 bit dan memiliki 4 kolom yang mana setiap 1 kolom berisi 8 bit yang merupakan bilangan biner.

![](https://res.cloudinary.com/bimagv/image/upload/v1599983691/2020-09/2_mtodbi.png)

Tentang IPv4 silahkan lihat disini: [http://www.mikrotik.co.id/artikel_lihat.php?id=64](http://www.mikrotik.co.id/artikel_lihat.php?id=64 "http://www.mikrotik.co.id/artikel_lihat.php?id=64")

IPv6 ini memiliki 8 kolom yang setiap 1 kolomnya memiliki 16 bit yang merupakan bilangan hexadecimal contohnya **`2001:db8:23fa:00c8::/64`**

jadi, kalau kita nanti mau menghitung subnet atau prefix alias /-nya maka musti menjadikannya bilangan biner terlebih dahulu.