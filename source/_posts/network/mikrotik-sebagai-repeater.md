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
# Contoh kasus

![](/images/screenshot-from-2020-08-20-15-09-51.png)

Pada contoh ini kita akan melihat bagaimana mikrotik disetel sebagai repeater. Atau dikenal juga dengan istilah **range extender** yang berfungsi untuk memperluas area sinyal.

# Requirement Software MikroTik

Untuk dapat menggunakan fitur `wireless repeater` di mikrotik ini musti ada package wireless atau setidaknya router dengan versi 6.37.

## Guidelines

Dalam contoh ini misal kita mempunyai 1 router mikrotik yang ingin dihubungkan secara wireless ke Access Point WiFi guna untuk memperluas area sinyal WiFi.

Maka kita butuh:

* router AP dengan mode **AP-Bridge** alias berfungsi sebagai access point
* router RP dengan mode **Station** alias berfungsi sebagai wireless client

## Contoh Implementasi

### Contoh 1

Untuk area-area publik atau disebut outdoor tentunya dibutuhkan jangkauan wireless yang dapat menjangkau area yang cukup luas.

Selain menjangkau area yang cukup luas kita juga butuh mengcover banyaknya client yang terhubung kedalam hotspot itu. Solusi untuk ini sebetulnya bisa dengan menyetel hanya ada satu hotspot server dalam jaringan tersebut.

#### Skema

![](/images/untitled-document.jpg)

Perhatikan pada Koneksi dari **Access Point ke MikroTik**, disana untuk terhubung mereka menggunakan koneksi wireless. 

Lalu nanti mikrotik akan membroadcast DHCP ke client supaya client bisa internetan dengan hotspot dari Access Point.

Dalam hal ini yang bertindak menjadi hotspot server yakni si Access Point. Mikrotik hanya sebagai range extender saja.

#### Menyetel Station: Router mikrotik sebagai repeater

Dalam contoh ini mikrotik yang digunakan hanya mempunyai 1 interface wireless. 

Dan kita akan menghubungkannya ke AP melalui interface wlan1 tersebut dengan mode station.

* Masuk ke menu **Wireless Tables,** lalu pilih **tab interface**

  ![](/images/screenshot-from-2020-08-20-17-03-13.png)
* Sekarang masuk ke **interface wlan1**, lalu kita akan memulai setting pada interface ini

  ![](/images/screenshot-from-2020-08-20-17-23-16.png)

  kita ingin router bisa terhubung dengan AP, maka kita dapat menyetel...

  **Mode**nya menjadi: `station`

  **SSID**nya di set ke WiFi hotspot milik AP. Caranya tinggal menjalankan `Scan` dan pilih WiFi dari AP seperti berikut.

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