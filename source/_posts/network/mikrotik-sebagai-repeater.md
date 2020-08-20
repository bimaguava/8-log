---
draft: true
comments: true
toc: true
title: MikroTik sebagai Repeater
date: 2020-08-19T20:21:00Z
updated: 
category:
- network
tags:
- mikrotik
keywords: []

---
## Contoh kasus

![](/images/screenshot-from-2020-08-20-15-09-51.png)

Pada contoh ini kita akan melihat bagaimana mikrotik disetel sebagai repeater. Atau dikenal juga dengan istilah **range extender** yang berfungsi untuk memperluas area sinyal.

## Requirement Software MikroTik 

Untuk dapat menggunakan fitur `wireless repeater` di mikrotik ini musti ada package wireless atau setidaknya router dengan versi 6.37.

## Guidelines

## Menghubungkan AP dan Repeater

Dalam contoh ini misal kita mempunyai 2 router mikrotik yang ingin dihubungkan secara wireless guna untuk memperluas area sinyal WiFi.

Maka kita butuh:

* router AP dengan mode **AP-Bridge** alias berfungsi sebagai access point
* router RP dengan mode **Station** alias berfungsi sebagai wireless client

## Mode AP-Bridge

Mode AP-bridge digunakan sebagai Access point atau pemancar yang bisa melayani banyak client atau disebut juga dengan PTMP (Point To Multi Point), mode ini bisa kita gunakan untuk network yang sifatnya Routing ataupun Bridging. Untuk menggunakan mode AP-Bridge ini perangkat Routerboard minimal harus memiliki lisensi level 4.

## Mode Station

Wireless dengan Mode station ini digunakan sebagai wireless client/ penerima pada topologi PTP (Point To Point) atau PTMP (Point To Multi Point), wireless Mode station hanya bisa digunakan untuk membentuk network yang sifatnya routing, sehingga mode ini merupakan salah satu mode yang efektif dan efisian jika pada sisi wireless client/station tidak dibutuhkan bridging

## Contoh Implementasi

### Memperluas signal publik pada area hotspot

Untuk area-area publik atau disebut outdoor tentunya dibutuhkan jangkauan wireless yang dapat menjangkau area yang cukup luas. 

Selain menjangkau area yang cukup luas kita juga butuh mengcover banyaknya client yang terhubung kedalam hotspot itu. Solusi untuk ini sebetulnya bisa dengan menyetel hanya ada satu hotspot server dalam jaringan tersebut.

#### Skema

![](/images/screenshot-from-2020-08-20-17-15-46.png)

#### Menyetel Station: Router RP sebagai repeater 

* Masuk ke menu **Wireless Tables>interface** 

  ![](/images/screenshot-from-2020-08-20-17-03-13.png)
* Klik interface **wlan1>tab Wireless**

  ![](/images/screenshot-from-2020-08-20-17-23-16.png)

  Sekarang kita ingin router bisa terhubung dengan AP TP Link maka kita dapat menyetek 

  **Mode**: station

  **SSID**: (scan dan pilih hotspot punya TP Link)

  caranya tinggal klik scan dan nanti akan muncul SSID dari hotspot TP Link, setelah itu tinggal pilih

  ![](/images/screenshot-from-2020-08-20-17-06-20.png)

#### Menyetel Router RP DHCP client

Setelah menjadikan Router RP ini menjadi sebuah repeater dari hotspot TP Link, sekarang tinggal menjadikannya sebagai DHCP client supaya bisa membroadcast DHCP dari si AP TP Link

Masuk ke menu **IP**>**DHCP Client>Tambah**

![](/images/screenshot-from-2020-08-20-17-32-13.png)

interfacenya dipilih wlan 1, karena kita ingin meneruskan DHCP service ke client.

#### Menyetel DNS untuk terhubung ke internet

Kita bisa mengarahkan DNS ke gateway, buka menu **IP>Routes** untuk melihat gateway

![](/images/screenshot-from-2020-08-20-17-40-33.png)

Dan gatewaynya dalam contoh ini `192.168.43.1`

dan buka menu **IP>DNS** 

![](/images/screenshot-from-2020-08-20-17-38-16.png)

**Dynamic Servers**: isi IP gateway

**Centang Allow Remote Requests** untuk mengarahkan DNSnya ke IP gateway 

Sampai sini kita mendapatkan hasil, yaitu router mikrotik sudah bisa terhubung ke internet.

#### Menyetel AP Bridge: 

## Referensi

* [https://www.monitorteknologi.com/menghubungkan-2-router-mikrotik-dengan-wireless/](https://www.monitorteknologi.com/menghubungkan-2-router-mikrotik-dengan-wireless/ "https://www.monitorteknologi.com/menghubungkan-2-router-mikrotik-dengan-wireless/")


* [MikroTIk ID](http://www.mikrotik.co.id/artikel_lihat.php?id=47#:\~:text=Mode%20WDS-Slave,menggunakan%201%20card%20wireless%20card. "MikroTik ID")