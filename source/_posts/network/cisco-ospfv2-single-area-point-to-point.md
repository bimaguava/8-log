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

Caranya dengan mengurangi **255.255.255.255** dengan subnet mask kita tadi, `255.255.255.0` maka kita akan mendapatkan 0.0.0.255.

> Pada Router OSPF networknya menggunakan /30 alias cuma dapat host 2 doang, kita juga harus menghitung subnet mask dan wilcard masknya juga, silahkan hitung ...

## 2.B. Menyetel Network dengan Network Command dan Wilcard Mask