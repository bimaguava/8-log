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