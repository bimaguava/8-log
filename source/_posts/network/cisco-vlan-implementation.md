---
draft: true
comments: true
toc: true
title: 'Cisco: VLAN Implementation'
date: 2020-08-12T17:00:00Z
updated: 
category:
- network
tags:
- cisco
keywords: []

---
## Petunjuk Awal VLAN

tidak ada, lanjut.

## Lab

Download: [https://drive.google.com/file/d/1F78eUuw6BMl43hsats0RJw3C8HiwHRe1/view](https://drive.google.com/file/d/1F78eUuw6BMl43hsats0RJw3C8HiwHRe1/view "https://drive.google.com/file/d/1F78eUuw6BMl43hsats0RJw3C8HiwHRe1/view")

![](/images/screenshot_2020-08-13_23-40-48.png)

jadi, disini kita punya topologi yang memuat beberapa sub network (Lihat IP) yang mana ada 3 VLAN, VLAN 10, 20, dan 30. 

Supaya mudah untuk pahami, tinggal melihat bagian host id dari IP misal 172.17.`10`.21 berarti nanti akan berada pada VLAN 10 seperti itu. Untuk lebih jelasnya silahkan merujuk ke tabel address.

## Tabel Address

![](/images/screenshot_2020-08-13_23-44-33.png)

## What we do?

* Pada bagian 1 kita akan mempelajari broadcast trafik pada topologi VLAN Implementation ini
* Pada bagian 2 kita akan mencoba mempelajari broadcast trafik yang dilakukan tanpa menggunakan VLAN

Intinya kita nanti akan memahami bagaimana suatu paket broadcast yang diforward switch saat pakai VLAN dan tidak memakai VLAN

## 1. Observe Broadcast Traffic in a VLAN Implementation

### 1.A. Ping dari PC1 ke PC6

Mula-mula kita akan melihat dahulu suatu ARP request saat melintasi jaringan.