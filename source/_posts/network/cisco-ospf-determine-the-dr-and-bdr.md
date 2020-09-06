---
draft: true
comments: true
toc: true
title: 'Cisco: OSPF Determine the DR and BDR'
date: 2020-08-24T18:00:00.000+00:00
updated: 
category:
- network
- ensa
tags:
- cisco
keywords: []

---
# **Overview**

Di materi ini akan membahas tentang dasar-dasar dari bagaimana untuk dapat bekerja menggunakan sebuah Designated Router (DR) dan Backup Designated Router (BDR) pada OSPF.

Yang mana kalau sudah membaca pada [OSPF intro](https://8log.js.org/2020/08/22/network/cisco-ospf-intro/) kita tahu bahwa ada 3 hal dalam proses seleksi DR dan BDR, yaitu:

* Dengan memilih Router ID yang tertinggi
* Kalau tidak ada router ID, maka dilihat dari IP loopbacknya
* Dan kalau tidak ada IP loopback, maka IP Interfacenya

Selain itu, juga kita sudah mengetahui bahwa untuk mengkonfigurasi OSPF ada 3 cara, yaitu:

* dengan memasukkan network2 dan wilcard mask _e.g:_ `network 10.1.1.0 0 0.0.0.3 area 0`
* dengan memasukkan IP address dari interfaces dan zero quad mask _e.g:_ `network 10.1.1.2 0.0.0.0 area 0`
* atau dengan menyetel langsung di interfacesnya 

Sekarang kita akan mengembangkan materi kita untuk lebih memahami untuk dapat bekerja dengan OSPF sebagai protokol routing yang termasuk di Interior Gateway Protokcol (IGP).

# **Lab**

![](/images/2020-06-09-min-21-44-36.png)