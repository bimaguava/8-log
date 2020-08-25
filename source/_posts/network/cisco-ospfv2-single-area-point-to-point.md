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

Jadi topologi tersebut cukup sederhana dan tugas kita hanya perlu menghubungkan masing-masing network agar LAN 1 sampai 3 bisa berkomunikasi.

# **Tabel Address**

![](/images/screenshot_2020-08-17_19-09-12.png)

# **Configure Router ID**