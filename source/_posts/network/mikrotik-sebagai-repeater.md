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

Untuk dapat menggunakan fitur `wireless-rep` di mikrotik ini musti ada package wireless atau setidaknya router dengan versi 6.37. kalau

## Guidelines

Dalam contoh ini misal kita mempunyai 1 router mikrotik yang ingin dihubungkan secara wireless ke Access Point WiFi guna untuk memperluas area sinyal WiFi.

Maka kita butuh:

* router AP dengan mode **AP-Bridge** alias berfungsi sebagai access point
* router RP dengan mode **Station** alias berfungsi sebagai wireless client

## Contoh 1

Untuk area-area publik atau disebut outdoor tentunya dibutuhkan jangkauan wireless yang dapat menjangkau area yang cukup luas.

Selain menjangkau area yang cukup luas kita juga butuh mengcover banyaknya client yang terhubung kedalam hotspot itu. Solusi untuk ini sebetulnya bisa dengan menyetel hanya ada satu hotspot server dalam jaringan tersebut.

### Skema

![](/images/untitled-document.jpg)

Perhatikan pada Koneksi dari **Access Point ke MikroTik**, disana untuk terhubung mereka menggunakan koneksi wireless.

Lalu nanti mikrotik akan membroadcast DHCP ke client supaya client bisa internetan dengan hotspot dari Access Point.

Dalam hal ini yang bertindak menjadi hotspot server yakni si Access Point. Mikrotik hanya sebagai range extender saja.

### 1. Menghubungkan mikrotik ke Hotspot AP

Kita akan menghubungkannya ke AP melalui interface wlan1 tersebut dengan mode station.

**Pada bagian ini kita ingin menghubungkan mikrotik ke AP melalui interface wlan1**

Langkah-langkahnya seperti berikiut.

* Masuk ke menu **Wireless Tables,** lalu pilih **tab interface**

  Dalam contoh ini mikrotiknya yang digunakan hanya mempunyai 1 interface wireless.

  ![](/images/screenshot-from-2020-08-20-17-03-13.png)
* Sekarang masuk ke **interface wlan1**, lalu kita akan memulai setting pada interface ini

  ![](/images/screenshot-from-2020-08-20-17-23-16.png)

  kita ingin router bisa terhubung dengan AP, maka kita dapat menyetel...

  **Mode**nya menjadi: `station`

  **SSID**nya di set ke WiFi hotspot milik AP. Caranya tinggal menjalankan `Scan` dan pilih WiFi dari AP seperti berikut.

  ![](/images/screenshot-from-2020-08-20-17-06-20.png)

### 2. Menyetel DHCP Client

**Pada bagian ini kita menginginkan agar mikrotik bisa membroadcast DHCP agar klien bisa mendapatkan koneksi dynamic dari hotspot Access point**

Setelah menjadikan mikrotik ini menjadi sebuah repeater dari hotspot TP Link, sekarang tinggal menjadikannya sebagai DHCP client supaya bisa membroadcast DHCP dari access point

Masuk ke menu **IP**>**DHCP Client**, lalu tambah baru "New DHCP Client"

![](/images/screenshot-from-2020-08-20-17-32-13.png)interfacenya dipilih interface`wlan 1`, interface yang terhubung langsung ke access point secara wireless

### 3. Menyetel Gateway, DNS untuk terhubung ke internet

**Pada bagian ini kita ingin mendapatkan koneksi internet pada router mikrotik**

Menyetel gateway tinggal buka menu **IP>Routes** dan tambahkan IP gateway dalam hal ini adalah `192.168.43.1`

Dan juga Dst. Address yang mengarah ke luar (internet) dengan IP `0.0.0.0/0`

![](/images/screenshot-from-2020-08-20-17-40-33.png)

Kalau sudah, pastikan statusnya sudah reachable.

Setelah gatewaynya sudah ada, maka kita perlu menyetel DNS Server dulu, bisa menggunakan opendns (8.8.8.8) atau bisa mengarahkan DNS ke gateway alias Access Point.

Untuk DNSnya tinggal buka saja menu **IP>DNS**

![](/images/screenshot-from-2020-08-20-17-38-16.png)

**Dynamic Servers** diisikan: `192.168.43.1` (IP gateway)

Sampai sini kita mendapatkan router mikrotik sudah bisa terhubung ke internet.

![](/images/screenshot-from-2020-08-20-20-18-46.png)

### 4. Membuat Virtual Address pada interface mikrotik

**Kita sekarang akan membuat sebuah hotspot yang akan digunakan client**

Opsinya ialah:

* tetap menggunakan SSID milik Access Point
* membuat SSID baru

> _Karena kita hanya mempunyai 1 interface wireless kita akan membuat interface wireless kedua dengan **virtual interfaces**_

Virtual interfaces ini dalam contoh ini kita namai dengan wlan2 akan diberi mode AP-Bridge.

Tinggal tambah interface pada menu Wireless Table, pilih **interface virtual**, yang selanjutnya kita beri nama wlan2

![](/images/screenshot-from-2020-08-20-20-45-10.png)

Kalau sudah, buka tab **Wireless**nya, Setel mode `ap bridge` dan kita akan memberi nama SSID nya dengan nama `Hotspot_Gratisan`

![](/images/screenshot-from-2020-08-20-20-46-16.png)

Lalu, OK.

Jangan lupa untuk setel IP addressnya :) pada menu **IP>Addresses**

![](/images/screenshot-from-2020-08-20-20-47-42.png)

Sip..

**Sekarang kita sudah punya 2 interface,**

**wlan1**: sebuah physical interface milik router yang terhubung ke access point dengan mode station

**wlan2**: sebuah virtual interface milik router yang digunakan untuk menyebar internet ke client melalui SSID `hotspot_gratisan`

![](/images/screenshot-from-2020-08-20-20-52-34.png)

Hasilnya sudah tampil `hotspot_gratisan` pada sisi client, tapi belum bisa terhubung untuk bisa mendapatkan IP secara dynamic :(

kalian pasti tahu...

### 5. DHCP Server pada hotspot_gratisan

Yap, untuk itu kita perlu mengkonfig DHCP Server pada wlan2 dengan menjalankan wizard "DHCP Setup"

![](/images/screenshot-from-2020-08-20-20-49-36.png)

Sampai bagian ini klien sudah bisa terhubung dan mendapatkan IP address secara dinamik, tapi saat membuka browser client belum bisa internetan :(

Apa yang terjadi.....

### 6. Agar client dapat terkoneksi ke internet, setel NAT dan Firewall

Hal tersebut karena belum ada jalur untuk client mendapatkan sebuah IP publik,  hal ini dilakukan dengan mengkonfig NAT "srcnat" dan firewall "masquarade".

Dengan men-**NAT (srcnat)** kan mikrotik, akan menstranslasikan IP address local menjadi IP address publik sehingga akan membuka akses kepada client ke internet.

Pada menu **IP>Firewall**, pilih Chain: `srcnat`

![](/images/screenshot-from-2020-08-20-20-48-23.png)

Lalu, setel Firewall sebagai `masquarade` di yang berada di tab **Action**

![](/images/screenshot-from-2020-08-20-20-48-55.png)

Hasilnya client sudah bisa menikmati internetan :)

## Referensi

* [https://www.monitorteknologi.com/menghubungkan-2-router-mikrotik-dengan-wireless/](https://www.monitorteknologi.com/menghubungkan-2-router-mikrotik-dengan-wireless/ "https://www.monitorteknologi.com/menghubungkan-2-router-mikrotik-dengan-wireless/")
* [MikroTIk ID](http://www.mikrotik.co.id/artikel_lihat.php?id=47#:\~:text=Mode%20WDS-Slave,menggunakan%201%20card%20wireless%20card. "MikroTik ID")