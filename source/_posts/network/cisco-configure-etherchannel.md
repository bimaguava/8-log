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

Sebuah topologi dengan 3 switch telah berhubungan, dan disini kita punya sebuah case yaitu ada redundant uplink.

Dan pada yang oren2 itu ialah [STP](https://8log.netlify.app/2020/08/08/network/cisco-spanning-tree-protocol-stp/ "STP"), yang mana STP itu tidak menggunakan salah satu port karena untuk mencegah looping yang terjadi karena broadcast yang terjadi sangat banyak.

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

### Semua port untuk EtherChannels ubah ke static trunk ports

Nah, sebelum menyetel EtherChannel, sesuai guidelinenya yaitu _Port yang digunakan untuk EtherChannel harus di VLAN yang sama, **atau** dijadikan Trunk._

> _Bagaimana jika port dikonfigurasi bukan dengan static, tapi dengan **DTP (Dynamic Trunking Protocol)** ?_

kalau dengan DTP akibatnya kita tidak bisa menyetel ke mode trunk, dan link nya tidak bisa membentuk trunk yang mana tetap menjadi `access ports` **alias** port yang biasa terhubung dengan host di suatu vlan.

Kita akan menyeting `static trunk port` yang terhubung switch satu dengan switch lain

ke S3 dulu

![](/images/screenshot-from-2020-08-09-16-27-04.png)

    S3(config)#int range fastEthernet 0/21-24

meng _on_-kan mode trunk

    S3(config-if-range)#switchport mode trunk

dan menyetop switch dari mengirim DTP message dengan switchport nonegotiate

    S3(config-if-range)#switchport nonegotiate

kalau sudah coba kita lihat di tabel interface trunk

    S3(config-if-range)# do show int trunk
    
    Port        Mode         Encapsulation  Status        Native vlan
    Fa0/21      on           802.1q         trunking      1
    Fa0/22      on           802.1q         trunking      1
    Fa0/23      on           802.1q         trunking      1
    Fa0/24      on           802.1q         trunking      1
    ...

pada S2

![](/images/screenshot-from-2020-08-09-16-36-57.png)

    S2(config)#int range fastEthernet 0/23-24, gigabitethernet 0/1-2
    S2(config-if-range)#switchport mode trunk
    S2(config-if-range)#switchport nonegotiate

lalu, pada S1

![](/images/screenshot-from-2020-08-09-16-37-21.png)

    S1(config)#int range fastEthernet 0/21-22, gigabitEthernet 0/1-2
    S1(config-if-range)#switchport mode trunk
    S1(config-if-range)#switchport nonegotiate

## 2. Configure EtherChannel with Cisco PAgP

**NOTE:** Saat mengonfigurasi EtherChannels, disarankan untuk mematikan `physical port` tadi

Jika tidak, `EtherChannel Misconfig Guard` dapat menempatkan port ini ke dalam `error disabled state`. Kalau seperti itu maka `physical port` dan `port channel` dapat diaktifkan kembali setelah EtherChannel dikonfigurasi.

### Configure Port Channel 1

EtherChannel yang sudah dibuat untuk lab ini menggabungkan port F0/21 dan F0/22 **antara S1 dan S3** yang dikonfig dengan static trunk ports.

Gunakan perintah `show interfaces trunk` untuk memastikan bahwa Anda memiliki link trunk aktif untuk kedua link tersebut, dan native VLAN pada kedua link tersebut sama.

    S1# show interfaces trunk
    
    Port Mode Encapsulation Status Native vlan
    F0/21 on 802.1q trunking 1
    F0/22 on 802.1q trunking 1
    G0/1 on 802.1q trunking 1
    G0/2 on 802.1q trunking 1
    
    <output omitted>

**Pada S1 dan S3**, tambahkan port F0/21 dan F0/22 ke Port Channel 1 dengan perintah `channel-group 1 mode desirable` 

Opsi mode `desirable` memungkinkan switch untuk secara aktif negotiate untuk membentuk link PAgP. 

**NOTE**: _jangan lupa_, interface harus **dimatikan** sebelum ditambahkan ke `channel group`

    S1(config)#int range fastEthernet 0/21-22
    S1(config-if-range)#shutdown
    S1(config-if-range)#channel-group 1 mode desirable

dan nyalahkan kembali interfacenya

    S1(config-if-range)#no shutdown

![](/images/screenshot_2020-08-12_17-02-20.png)

Nah, sekarang lakukan ke S3

    S3(config)#int range fastEthernet 0/21-24
    S3(config-if-range)#shutdown
    S3(config-if-range)#channel-group 1 mode desirable 
    S3(config-if-range)#no shutdown

## Referensi

* [https://geek-university.com/ccna/access-and-trunk-ports-explained/](https://geek-university.com/ccna/access-and-trunk-ports-explained/ "https://geek-university.com/ccna/access-and-trunk-ports-explained/")