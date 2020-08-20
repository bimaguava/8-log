---
draft: true
comments: true
toc: true
title: MikroTik sebagai Repeater dengan setelan roaming (SSID yang sama)
date: 2020-08-19T20:18:00Z
updated: 
category:
- network
tags:
- mikrotik
keywords: []

---
# Contoh kasus

![](/images/untitled-document-copy.jpg)

Seperti gambar diatas 2 router mikrotik yang nantinya akan melakukan point to point.

# Petunjuk awal

kalau pada materi [sebelumnya](https://8log.js.org/2020/08/19/network/mikrotik-sebagai-repeater/ "sebelumnya") menggunakan Access Point selain mikrotik pada contoh kali ini akan menggunakan mikrotik.

Sehingga nanti kita bisa menggunakan mode yang bernama `station-bridge` yang memang khusus untuk access pointnya yang juga mikrotik.

Setelan pada contoh kali ini akan **menggunakan setelah SSID yang sama** pada sisi repeaternya, hasilnya nanti client bisa terkoneksi ke AP manapun disana yang jangkauan sinyal dari salah satu AP terdekat disisi client.

Dan ketika client berpindah lokasi dan terputus dengan salah satu access point, client akan secara otomastis berpindah ke access point lain yang menjangkau client tersebut (tanpa terputus).

# Contoh 2

Dalam contoh ini saya mengasosiasikan bahwa anda telah membaca materi sebelumnya tentang ["MikroTik sebagai Repeater"](https://8log.js.org/2020/08/19/network/mikrotik-sebagai-repeater/) karena saya akan memberikan poin-poin singkat untuk menunjukkan perbedaannya saja.

Pada contoh ini diasosiasikan saya sudah memiliki sebuah SSID dari Access point.

Langkah dimulai dengan 

* Menyalahkan interface wireless pada router
* 

# Referensi

* [MikroTik ID](http://www.mikrotik.co.id/artikel_lihat.php?id=47#:\~:text=Mode%20WDS-Slave,menggunakan%201%20card%20wireless%20card. "MikroTIk ID")