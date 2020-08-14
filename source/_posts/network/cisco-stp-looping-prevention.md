---
draft: true
comments: true
toc: true
title: 'Cisco: STP Looping prevention'
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

Gunakan perintah `show spanning-tree vlan 1` untuk mendapatkan informasi status spanning tree dari setiap switch

    S1#show spanning-tree vlan 1
    VLAN0001
      Spanning tree enabled protocol ieee
      Root ID    Priority    32769
                 Address     0001.6448.C6E7
                 Cost        4
                 Port        26(GigabitEthernet0/2)
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
    
      Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
                 Address     000B.BE31.D3DA
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
                 Aging Time  20
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Fa0/1            Desg FWD 19        128.1    P2p
    Gi0/2            Root FWD 4         128.26   P2p
    Gi0/1            Desg FWD 4         128.25   P2p

Dan lakukan pada S2

    S2#show spanning-tree vlan 1
    VLAN0001
      Spanning tree enabled protocol ieee
      Root ID    Priority    32769
                 Address     0001.6448.C6E7
                 This bridge is the root
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
    
      Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
                 Address     0001.6448.C6E7
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
                 Aging Time  20
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Gi0/2            Desg FWD 4         128.26   P2p
    Fa0/1            Desg FWD 19        128.1    P2p
    Gi0/1            Desg FWD 4         128.25   P2p

dan S3

    S3#show spanning-tree vlan 1
    VLAN0001
      Spanning tree enabled protocol ieee
      Root ID    Priority    32769
                 Address     0001.6448.C6E7
                 Cost        4
                 Port        25(GigabitEthernet0/1)
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
    
      Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
                 Address     000C.CF45.7534
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
                 Aging Time  20
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Gi0/2            Altn BLK 4         128.26   P2p
    Gi0/1            Root FWD 4         128.25   P2p

Jika sudah tampil seperti itu kita coba pindahkan informasinya ke tabel. Sebagai berikut

| Switch | Port | Status (FWD, BLK...) | Root Bridge? |
| --- | --- | --- | --- |
| S1 | G0/1 | Forwarding | No |
|  | G0/2 | Forwarding | Yes |
| S2 | G0/1 | Forwarding | No |
|  | G0/2 | Forwarding | No |
| S3 | G0/1 | Forwarding | No |
|  | G0/2 | Blok | No |

Pada tabel kita hanya mencatat informasi dari trunk ports saja (Gigabit)

karena FastEthernet ialah sebuah `access port` yang konek dengan end devices alias hosts dan bukan bagian dari inter-switch trunk-based spanning tree.

Dan kita jabarkan satu persatu, 

**Pada S1 interface G0/2** jalur tersebut merupakan root bridge

**Pada S2 G0/1 dan G0/2** keduanya mempunyai Role **Designated** dan dilihat pada informasi Root ID bahwa router tersebut adalah root

**Pada S3**