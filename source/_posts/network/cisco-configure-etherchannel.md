---
draft: true
comments: true
toc: true
title: 'Cisco: Configure EtherChannel'
date: 2020-08-08T15:52:00Z
updated: 
category:
- network
tags:
- cisco
keywords: []

---
## Petunjuk mengkonfig EtherChannel

* EtherChannel tidak akan kebentuk kalau ada SPAN (Switched Port Analyzer) di salah satu port, SPAN ini fitur yang bisa diaktifin di Cisco switch untuk melihat frame yang keluar masuk di port itu (berguna untuk network monitoring juga)
* Speed dan Duplex harus sama
* Port yang digunakan untuk EtherChannel harus di VLAN yang sama, **atau** dijadikan Trunk
* EtherChannel bisa di Switch Layer 3 atau di Layer 2

## Lab

Download: [https://drive.google.com/file/d/1Jvzgnsv6lhFTVRGyQU2X0zNKREKpg6xn/view](https://drive.google.com/file/d/1Jvzgnsv6lhFTVRGyQU2X0zNKREKpg6xn/view "https://drive.google.com/file/d/1Jvzgnsv6lhFTVRGyQU2X0zNKREKpg6xn/view")

![](/images/screenshot-from-2020-08-09-13-48-41.png)

Sebuah topologi dengan 3 switch telah berhubungan, dan disini kita punya sebuah case yaitu ada redundant uplink. Dan pada yang oren2 itu ialah [STP](https://8log.netlify.app/2020/08/08/network/cisco-spanning-tree-protocol-stp/ "STP"), yang mana itu tidak digunakan karena untuk mencegah looping terjadi karena broadcast yang terjadi sangat banyak.

Pada lab ini kita akan mengonfigurasi **Port Aggregation Protocol (PAgP)**, **Link Aggregation Control Protocol (LACP)**, **versi standar terbuka IEEE 802.3ad** dari EtherChannel.

## Istilah

* **Port Channel**, yaitu gabungan beberapa interface itu atau **channel group** tadi akan melahirkan sebuah ~~keturunan~~ interface baru

## Tabel Address

![](/images/screenshot-from-2020-08-09-13-49-38.png)

## 1. Configure Basic Switch Settings

### Verification Command

Pastikan semua port terhubung **(connected)** dengan benar, cek dengan

    S2# show interfaces | include Ethernet
    
    ...
    FastEthernet0/23 is up, line protocol is up (connected)
    FastEthernet0/24 is up, line protocol is up (connected)
    GigabitEthernet0/1 is up, line protocol is up (connected)
    GigabitEthernet0/2 is up, line protocol is up (connected)

dan atau dengan `interface status` yang juga menampilkan `speed` dan `duplex` yang mana keduanya harus sama.

    S2# show interface status
    
    Port      Name               Status       Vlan       Duplex  Speed Type
    ...
    Fa0/23                       connected    1          auto    auto  10/100BaseTX
    Fa0/24                       connected    1          auto    auto  10/100BaseTX
    Gig0/1                       connected    1          auto    auto  10/100BaseTX
    Gig0/2                       connected    1          auto    auto  10/100BaseTX

Sekarang kita coba menampilkan `interfaces trunk`

    S2# show interfaces trunk

dan ternyata belum ada (di semua switch)

## Konfigurasikan semua port yang diperlukan untuk EtherChannels sebagai static trunk ports

_Bagaimana jika port dikonfigurasi dengan **DTP (Dynamic Trunking Protocol)**_ 