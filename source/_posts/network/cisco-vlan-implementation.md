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

Untuk teori silahkan baca di [sini]() karena sebelum membuat VLAN ada baiknya mengetahui kapan kita membutuhkan VLAN, dll.

Pada materi ini kita akan belajar bagaimana suatu VLAN bekerja, untuk yang ingin belajar konfigurasi VLAN silahkan ke [sini](8log.netlify.app/2020/07/26/network/cisco-vlan-configuration "sini")

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

| --- | --- | --- | --- | --- |
| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| S1 | VLAN 99 | 172.17.99.31 | 255.255.255.0 | N/A |
| S2 | VLAN 99 | 172.17.99.32 | 255.255.255.0 | N/A |
| S3 | VLAN 99 | 172.17.99.33 | 255.255.255.0 | N/A |
| PC1 | NIC | 172.17.10.21 | 255.255.255.0 | 172.17.10.1 |
| PC2 | NIC | 172.17.20.22 | 255.255.255.0 | 172.17.20.1 |
| PC3 | NIC | 172.17.30.23 | 255.255.255.0 | 172.17.30.1 |
| PC4 | NIC | 172.17.10.24 | 255.255.255.0 | 172.17.10.1 |
| PC5 | NIC | 172.17.20.25 | 255.255.255.0 | 172.17.20.1 |
| PC6 | NIC | 172.17.30.26 | 255.255.255.0 | 172.17.30.1 |
| PC7 | NIC | 172.17.10.27 | 255.255.255.0 | 172.17.10.1 |
| PC8 | NIC | 172.17.20.28 | 255.255.255.0 | 172.17.20.1 |
| PC9 | NIC | 172.17.30.29 | 255.255.255.0 | 172.17.30.1 |

Paket yang berlajan dari Network yang berbeda, yaitu **PC1: 172.17.10.21** dan **PC2: 172.17.30.26**