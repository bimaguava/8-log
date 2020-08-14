---
draft: true
comments: true
toc: true
title: 'Cisco: Spanning Tree Protocol (STP) Looping prevention'
date: 2020-08-14T06:37:00Z
updated: 
category:
- network
tags:
- cisco
keywords: []

---
## Petunjuk

Pada materi ini, kita akan mengamati status port spanning-tree dan melihat proses dari spanning-tree convergence.

Tujuannya ialah supaya kita mengetahui pengoperasian Spanning Tree Protocol (STP) dan juga memahami bagaimana STP dalam mencegah switching loop pada suatu segmen yang menggunakan  redundansi alias perangkat (switch) yang bertindak menjadi backup-an.

Untuk lebih jelasnya silahkan baca di [sini](https://8log.netlify.app/2020/08/08/network/cisco-spanning-tree-protocol-stp/ "sini")

Lanjut.

## Lab

Download: [https://drive.google.com/file/d/1TjIpCSiWapGEXwTiTN83AT5VrOFPBsKT/view](https://drive.google.com/file/d/1TjIpCSiWapGEXwTiTN83AT5VrOFPBsKT/view "https://drive.google.com/file/d/1TjIpCSiWapGEXwTiTN83AT5VrOFPBsKT/view")

![](/images/screenshot_2020-08-14_13-50-18.png)

Lab ini cukup singkat, karena kita hanya akan mencapai tujuan diatas yaitu untuk memahami pemanfaatan spanning-tree saja juga sebagai pelengkap dari materi sebelumnya yang hanya membahas teori.

## 1. Observe a Converged Spanning-Tree Instance

## 1.A. Mengecek konektivitas

Kita cek dari PC 1 ke destination PC 2 atau 192.168.1.101, dan ping seharusnya berhasil

    C:\>ping 192.168.1.101
    
    Pinging 192.168.1.101 with 32 bytes of data:
    
    Reply from 192.168.1.101: bytes=32 time=2ms TTL=128
    Reply from 192.168.1.101: bytes=32 time<1ms TTL=128

dan statusnya pun reply.. oke, lanjut.

## 1.B. Cek status spanning-tree pada setiap switch