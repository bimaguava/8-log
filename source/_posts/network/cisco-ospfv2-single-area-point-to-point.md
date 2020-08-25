---
draft: true
comments: true
toc: true
title: 'Cisco: OSPFv2 Single Area Point to Point'
date: 2020-08-16T23:49:00.000+00:00
updated: 
category:
- network
- ensa
tags:
- cisco
keywords: []

---
# **Petunjuk**

Pada materi ini kita akan mencoba belajar bagaimana untuk:

* memberikan `Router-ID`
* mengkonfig network2 untuk routing OSPF
* dan juga menyetel interface yang menuju ke LAN agar menjadi `Passive Interfaces`

# **Lab**

Download: [https://drive.google.com/file/d/1TxsgFsZkkP6cOvu3XonxSSLUzu5K-6sX/view](https://drive.google.com/file/d/1TxsgFsZkkP6cOvu3XonxSSLUzu5K-6sX/view "https://drive.google.com/file/d/1TxsgFsZkkP6cOvu3XonxSSLUzu5K-6sX/view")

![](/images/screenshot_2020-08-17_19-07-45.png)

Berikut adalah topologi point-to-point yang ditambah dengan frame relay yang memang juga bisa ditempatkan di antara LAN seperti itu.

Jadi topologi tersebut cukup sederhana dan tugas kita hanya perlu menghubungkan masing-masing network agar LAN 1 sampai 3 bisa berkomunikasi tentunya dengan proses Dynamic routing, OSPF.

# **Tabel Address**

![](/images/screenshot_2020-08-17_19-09-12.png)

# **1. Configure Router ID**

Router ID adalah sebuah identitas bagi router yang menjalankan OSPF yang mana router id ini nilainya berupa IP.

bisa 1.1.1.1 atau seperti 172.16.X.X. Salah satu penggunaan router id yaitu untuk menentukan Designated Router (DR) dengan memilih Router ID dengan nilai yang tertinggi.

Sekarang kita akan memulai OSPF `routing proccess` ke 3 router tersebut dengan menggunakan proccess ID **10**.

    R1(config)# router ospf 10
    R2(config)# router ospf 10
    R3(config)# router ospf 10

Setalah itu jalankan router-id command untuk mengeset OSPF ID dari ketiga router tersebut

    R1(config-router)# router-id 1.1.1.1
    R2(config-router)# router-id 2.2.2.2
    R3(config-router)# router-id 3.3.3.3

# **2. Configure Network**

## 2.A. Cara Mengkonversikan subnet ke desimal

Nah, sebelum ke konfigurasi pastikan kita tahu untuk menghitung wilcard mask. Terutama menghitung subnet mask untuk mengetahui bilangan desimalnya.

**Berikut sedikit contoh:**

> Pada LAN yang terpasang ke R1 ia punya subnet /24. Sekarang kita akan mengubahnya ke desimal

panjangya bit pada ipv4 berjumlah 32 bit. Selanjutnya dari 32 bit itu ada 4 oktet. Maka kelihatannya akan seperti ini

`11111111.11111111.11111111.11111111`

Kalau seperti itu artinya bilangan desimalnya `255.255.255.255`, dikarenakan setiap 1 oktet nilainya 255.

Oke. 

Lanjut.

**Soalnya**: kita ingin menghitung jumlah /24, simpelnya kita hanya tuliskan 1 sampai hitungan ke 24 :)

`11111111.11111111.11111111.00000000`

Kalau udah berarti sisanya di kasih nol.

dan hitung setiap nilai dari 1 oktet, maka dapat `255.255.255.0`

**Bagaimana cara mengetahui wilcard masknya?**

Caranya dengan mengurangi **255.255.255.255** dengan subnet mask kita tadi, `255.255.255.0` maka kita akan mendapatkan `0.0.0.255`.

> Pada Router OSPF networknya menggunakan /30 alias cuma dapat host 2 doang, kita juga harus menghitung subnet mask dan wilcard masknya juga, silahkan hitung ...

## 2.B. Menyetel R1 dengan Network statements dan Wilcard Mask

Commandnya akan seperti ini

> Router(config-router)# **network** network-address wildcard-mask **area** area-id

untuk **network-address** kita lihat yang directly connected ke R1 siapa saja, lihatnya di tabel routing

    R1(config-router)# do show ip route

![](/images/r1.png)

yaitu 10.1.1.0, 10.1.1.4, dan 192.168.10.0

Sekarang wilcardnya.

* 10.1.1.0

  kan dia /30, setelah dihitung wilcardnya 0.0.0.3
* 10.1.1.4

  kan dia /30, setelah dihitung wilcardnya 0.0.0.3
* 192.168.10.0

  kan dia /24, setelah dihitung wilcardnya 0.0.0.255

Sekarang Areanya.

Karena dalam topologi ini ingin membuat semua router dalam satu area, jadi kita kasih area 0 yang sering disebut backbone area.

Masih dalam mode config router ospf tadi, konfignya jadi seperti berikut

    R1(config-router)# network 10.1.1.0 0 0.0.0.3 area 0
    R1(config-router)# network 10.1.1.4 0 0.0.0.3 area 0
    R1(config-router)# network 192.168.10.2 0 0.0.0.255 area 0

## 2.C. Menyetel R2 dengan IP Address interface dan quad-zero masks

Pada R2 sekarang kita akan melakukan konfigurasi yang berbeda, padahal gampangnya ya tinggal pakai command ini sih 

> Router(config-router)# **network** network-address wildcard-mask **area** area-id

Tapi sepertinya ada yang baru, yaitu kita tidak menggunakan `network-statements` alias ip-ip yang directly connected dan juga `wilcard mask`. 

Jadi kita akan gunakan `IP addresses dari interfaces routenya` dan sekarang menggunakan `quad-zero masks` alias 0.0.0.0

Pertama-tama kita cek IP interfaces punya router

    R2(config-router)# do show ip interface brief

![](/images/r2.png)

Sekarang tinggal masukkan tiap ip interface dengan quad zero mask seperti ini

    R2(config-router)# network 192.168.20.1 0.0.0.0 area 0
    R2(config-router)# network 10.1.1.2 0.0.0.0 area 0
    R2(config-router)# network 10.1.1.9 0.0.0.0 area 0

Berikut show runnya

![](/images/r2-2.png)

Dengan cara ini juga router akan mendeteksi router lain yang menjalankan OSPF untuk selanjutnya dipilih menjadi neighbor adjacencynyanya, selanjutnya ada cara lain.

Lanjut.

## 2.D. Menyetel R3 langsung di interfacenya

R3 interfacenya yang bersangkutan ada  `G0/0/0`, `S0/1/0`, dan `S0/1/1`, kita lakukan satu-satu 

    R3(config)# int g0/0/0
    R3(config-if)# ip ospf 10 area 0
    
    R3(config)# int s0/1/0
    R3(config-if)# ip ospf 10 area 0
    
    R3(config)# int s0/1/1
    R3(config-if)# ip ospf 10 area 0

# **Configure Passive Interfaces pada Network LAN**

# **Verify Command**