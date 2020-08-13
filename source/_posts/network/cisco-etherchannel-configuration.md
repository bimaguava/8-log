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

### 1.A. Verification Command

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

### 1.B. Semua port untuk EtherChannels ubah ke static trunk ports

Nah, sebelum menyetel EtherChannel, sesuai guidelinenya yaitu _Port yang digunakan untuk EtherChannel harus di VLAN yang sama, **atau** dijadikan Trunk._

> _Bagaimana jika port dikonfigurasi bukan dengan static, tapi dengan **DTP (Dynamic Trunking Protocol)** ?_

kalau dengan DTP akibatnya kita tidak bisa menyetel ke mode trunk, dan link nya tidak bisa membentuk trunk yang mana tetap menjadi `access ports` **alias** port yang biasa terhubung dengan host di suatu vlan.

Kita akan menyeting `static trunk port` yang terhubung switch satu dengan switch lain

ke S3 dulu

![](/images/screenshot-from-2020-08-09-16-27-04.png)

    S3(config)# int range fastEthernet 0/21-24

meng _on_-kan mode trunk

    S3(config-if-range)# switchport mode trunk

dan menyetop switch dari mengirim DTP message dengan switchport nonegotiate

    S3(config-if-range)# switchport nonegotiate

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

    S2(config)# int range fastEthernet 0/23-24, gigabitethernet 0/1-2
    S2(config-if-range)# switchport mode trunk
    S2(config-if-range)# switchport nonegotiate

lalu, pada S1

![](/images/screenshot-from-2020-08-09-16-37-21.png)

    S1(config)# int range fastEthernet 0/21-22, gigabitEthernet 0/1-2
    S1(config-if-range)# switchport mode trunk
    S1(config-if-range)# switchport nonegotiate

## 2. Configure EtherChannel with Cisco PAgP

**NOTE:** Saat mengonfigurasi EtherChannels, disarankan untuk mematikan `physical port` tadi

Jika tidak, `EtherChannel Misconfig Guard` dapat menempatkan port ini ke dalam `error disabled state`. Kalau seperti itu maka `physical port` dan `port channel` dapat diaktifkan kembali setelah EtherChannel dikonfigurasi.

### 2.A. Configure Port Channel 1

EtherChannel yang sudah dibuat untuk lab ini menggabungkan port F0/21 dan F0/22 **antara S1 dan S3** yang dikonfig dengan static trunk ports.

Gunakan perintah `show interfaces trunk` untuk memastikan bahwa Anda memiliki link trunk aktif untuk kedua link tersebut, dan native VLAN pada kedua link tersebut sama.

    Switch(config-if-range)# do show int tr
    Port        Mode         Encapsulation  Status        Native vlan
    Fa0/21      on           802.1q         trunking      1
    Fa0/22      on           802.1q         trunking      1
    Fa0/23      on           802.1q         trunking      1
    Fa0/24      on           802.1q         trunking      1
    
    <output omitted>

**Pada S1 dan S3**, tambahkan port **F0/21 dan F0/22** ke Port Channel 1 dengan perintah `channel-group 1 mode desirable`

Opsi mode `desirable` memungkinkan switch untuk secara aktif negotiate untuk membentuk link PAgP.

**NOTE**: _jangan lupa_, interface harus **dimatikan** sebelum ditambahkan ke `channel group`

    S1(config)# int range fastEthernet 0/21-22
    S1(config-if-range)# shutdown
    S1(config-if-range)# channel-group 1 mode desirable

dan nyalahkan kembali interfacenya

    S1(config-if-range)#no shutdown

![](/images/screenshot_2020-08-12_17-02-20.png)

Nah, sekarang lakukan ke S3

    S3(config)# int range fastEthernet 0/21-22
    S3(config-if-range)# shutdown
    S3(config-if-range)# channel-group 1 mode desirable 
    S3(config-if-range)# no shutdown

Konfigurasikan `logical interfaces` untuk menjadi trunk dengan terlebih dahulu memasukkan perintah `interface port-channel [number]` dan kemudian perintah `switch mode trunk`

**Tambahkan konfigurasi ini ke kedua switch (S1 dan S3)**

    S1(config)# int port-channel 1
    S1(config-if)# switchport mode trunk 
    
    S3(config)# int port-channel 1
    S3(config-if)# switchport mode trunk 

### 2.B. Verify status Port Channel 1

Keluarkan perintah `show etherchannel summary` pada S1 dan S3 untuk memverifikasi bahwa EtherChannel berjalan pada kedua switch.

Perintah ini menampilkan jenis EtherChannel, port yang digunakan, dan status port.

Outputnya harus sama seperti ini:

port yang menggunakan PAgP yaitu port yang berhubungan dengan S1 dan S3 atau **port F0/21 dan F0/22.**

    S3# show etherchannel summary 
    ...
    Number of channel-groups in use: 1
    Number of aggregators:           1
    
    Group  Port-channel  Protocol    Ports
    ------+-------------+-----------+----------------------------------------------
    
    1      Po1(SU)           PAgP   Fa0/21(P) Fa0/22(P

Output S1 juga sama

    S1# show etherchannel summ
    ...
    Number of channel-groups in use: 1
    Number of aggregators:           1
    
    Group  Port-channel  Protocol    Ports
    ------+-------------+-----------+----------------------------------------------
    
    1      Po1(SU)           PAgP   Fa0/21(P) Fa0/22(P) 

atau alternatifnya dengan `show interface trunk`

Output pada S3

    S3#show interfaces trunk
    Port        Mode         Encapsulation  Status        Native vlan
    Po1         on           802.1q         trunking      1
    Fa0/23      on           802.1q         trunking      1
    Fa0/24      on           802.1q         trunking      1
    ...

dan S1

    S1# show interface trunk
    Port        Mode         Encapsulation  Status        Native vlan
    Po1         on           802.1q         trunking      1
    Gig0/1      on           802.1q         trunking      1
    Gig0/2      on           802.1q         trunking      1
    ...

Dan selesai lah dengan Port Channel 1 dengan PGaP, berikutnya kita akan mengkonfig Port Channel 2 dan 3 dengan LACP

## 3. Configure 802.3ad LACP Etherchannel

### 3.A. Configure Port Channel 2

> 802.3ad adalah versi open source dari EtherChannel yang dilirlis IEEE tahun 2000

Seperti command sebelumnya, kita akan **konfigurasikan link antara S1 dan S2**, menggunakan **port G0/1 dan G0/2**, sebagai LACP EtherChannel.

Kita harus menggunakan nomor `port channel` yang berbeda yang ada pada S1, karena kita sudah menggunakannya pada langkah sebelumnya.

Untuk mengkonfigurasi `port channel 2` sebagai LACP, gunakan perintah `channel-group 2 mode active`

> mode active menunjukkan bahwa switch melakukan negotiate link itu sebagai LACP, bukan PAgP

Berikut konfig S1

    S1(config)# int range gigabitEthernet 0/1-2
    S1(config-if-range)# shutdown
    
    S1(config-if-range)# channel-group 2 mode active
    S1(config-if-range)# no shutdown
    
    S1(config-if-range)# int port-channel 2
    S1(config-if)# switchport mode trunk 

dan S2

    S2(config)# int range gigabitEthernet 0/1-2
    S2(config-if-range)# shutdown
    
    S2(config-if-range)# channel-group 2 mode active
    S2(config-if-range)# no shutdown
    
    S2(config-if-range)# int port-channel 2
    S2(config-if)# switchport mode trunk 

### 3.B. Verify Port Channel 2 Status

Pada S1 kita cek `interface trunk`

    S1# show int tr
    Port        Mode         Encapsulation  Status        Native vlan
    Po1         on           802.1q         trunking      1
    Po2         on           802.1q         trunking      1
    
    Port        Vlans allowed on trunk
    Po1         1-1005
    Po2         1-1005
    
    Port        Vlans allowed and active in management domain
    Po1         1
    Po2         1
    
    Port        Vlans in spanning tree forwarding state and not pruned
    Po1         1
    Po2         1

Maka `port channel` yang telah dibuat akan muncul, Po2

Lalu, coba kita cek `etherchannel summary`

    S1# show etherchannel summary 
    Flags:  D - down        P - in port-channel
            I - stand-alone s - suspended
            H - Hot-standby (LACP only)
            R - Layer3      S - Layer2
            U - in use      f - failed to allocate aggregator
            u - unsuitable for bundling
            w - waiting to be aggregated
            d - default port
    
    
    Number of channel-groups in use: 2
    Number of aggregators:           2
    
    Group  Port-channel  Protocol    Ports
    ------+-------------+-----------+----------------------------------------------
    
    1      Po1(SU)           PAgP   Fa0/21(P) Fa0/22(P) 
    2      Po2(SU)           LACP   Gig0/1(P) Gig0/2(P) 

Status Po2-nya SU, yaitu S=`layer 2` dan U=`in use` yang menggunakan protocol LACP dan Ports Gig0/1 dan Gig0/2 dengan keterangan P atau `in port-channel` yang mana logical interface bukan physical interface.

Lalu, Lakukan juga pengecekan pada S2 dan pastikan menampilkan data dari Port Channel 2 yang telah dibuat tadi.

## 4. Configure a Redundant EtherChannel link

### 4.A. Configure Port Channel 3

Pada S2 kita tambahkan ke Port Channel 3 dengan mode passive.

Opsi passive ini menunjukkan kita ingin menggunakan LACP jika perangkat LACP lain terdeteksi atau perangkat lain memakai mode active.

Dan jangan lupa juga port channel 3 ini static trunk seperti semua port channel sebelumnya

    S2(config)# interface range f0/23 - 24
    S2(config-if-range)# shutdown
    
    S2(config-if-range)# channel-group 3 mode passive
    S2(config-if-range)# no shutdown
    
    S2(config-if-range)# interface port-channel 3
    S2(config-if)# switchport mode trunk

dan di sisi S3 kita akan menggunakan mode active, sehingga konfigurasi pada port channel ini passive/active yang menunjukkan bahwa salah satu perangkat bisa dijadikan passive dimana dia akan mengaktifkan LACP jika mendeteksi perangkat LACP active.

    S3(config)# interface range f0/23 - 24
    S3(config-if-range)# shutdown
    
    S3(config-if-range)# channel-group 3 mode active
    S3(config-if-range)# no shutdown
    
    S3(config-if-range)# interface port-channel 3
    S3(config-if)# switchport mode trunk

### 4.B. Verify Port Channel 3 status

Sekarang adalah saatnya pembuktian bahwa konfigurasi EtherChannel yang dilakukan telah betul

    S2# show etherchannel sum
    
    Number of channel-groups in use: 3
    Number of aggregators:           3
    
    Group  Port-channel  Protocol    Ports
    ------+-------------+-----------+----------------------------------------------
    
    1      Po1(SD)           -      
    2      Po2(SU)           LACP   Gig0/1(P) Gig0/2(P) 
    3      Po3(SU)           LACP   Fa0/23(P) Fa0/24(P) 

Nah, pastikan Port Channel yang digunakan S2 seperti ini

Dan di sisi S3 akan seperti ini

    S3# show etherchannel sum
    
    Number of channel-groups in use: 2
    Number of aggregators:           2
    
    Group  Port-channel  Protocol    Ports
    ------+-------------+-----------+----------------------------------------------
    
    1      Po1(SU)           PAgP   Fa0/21(P) Fa0/22(P) 
    3      Po3(SU)           LACP   Fa0/23(P) Fa0/24(P) 

Dan lakukan pembuktian untuk konfigurasi pada static trunk juga dengan command `show interface trunk`

Jika sudah, kita akan mengecek spanning tree. Karena membuat EtherChannel tidak akan mencegah Spanning Tree (STP) untuk mendeteksi switching loops.

Dilihat pada S3

    S3#show spanning-tree active
    VLAN0001
      Spanning tree enabled protocol ieee
      Root ID    Priority    32769
                 Address     0001.436E.8494
                 This bridge is the root
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
    
      Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
                 Address     0001.436E.8494
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
                 Aging Time  20
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Po3              Desg FWD 9         128.28   Shr
    Po1              Desg FWD 9         128.27   Shr

Po3 dan Po1 merupakan logical interface pada spanning tree yang mana ada keterangan **the bridge is the root berarti bahwa switch ini merupakan sebuah root**.

Nah jika kita lihat topologi S3 ini adalah root maka **yang berwarna oren (Port Channel 2) merupakan Alternative**

![](/images/screenshot_2020-08-13_21-14-14.png)

    S1#show spanning-tree active 
    VLAN0001
      Spanning tree enabled protocol ieee
      Root ID    Priority    32769
                 Address     0001.436E.8494
                 Cost        9
                 Port        27(Port-channel1)
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
    
      Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
                 Address     000A.F313.2395
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
                 Aging Time  20
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Po1              Root FWD 9         128.27   Shr
    Po2              Altn BLK 3         128.28   Shr

Role Po2 **Alternative dan statusnya di BLOK (BLK)**

Hal ini karena Port Channel 2 tidak bertindak operative karena STP menempatkan beberapa port untuk di blok dan yang diblok oleh STP ini ialah Gigabit 0/1 dan 0/2 nya S1. 

Yang mana STP ini berkaitan dengan pencegahan terjadinya switching loop yang diakibatkan oleh switch yang saling reply broadcast sampai terjadi looping.

Untuk penjelasan tentang STP silahkan ke [sini](https://8log.netlify.app/2020/08/08/network/cisco-spanning-tree-protocol-stp/ "sini")

> _Lalu, apakah bisa misal kita ingin menjadikan Po2 ini sebagai root?_

Ya, menggantinya dengan dengan mengkonfigurasi S1 menjadi primary root untuk VLAN 1 atau default VLAN. Sebagai berikut

    S1(config)# spanning-tree vlan 1 root primary

atau bisa dengan cara mengeset prioirity ID nya, seperti ini

    S1(config)# spanning-tree vlan 1 root priority 24576

Coba kita lihat S1 setelah diset root primary nya berpindah dari S3 ke S1, dengan output pada S1 **This bridge is the root**

    S1(config)#do show spanning-tree
    VLAN0001
      Spanning tree enabled protocol ieee
      Root ID    Priority    24577
                 Address     000A.F313.2395
                 This bridge is the root
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
    
      Bridge ID  Priority    24577  (priority 24576 sys-id-ext 1)
                 Address     000A.F313.2395
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
                 Aging Time  20
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Po1              Desg FWD 9         128.27   Shr
    Po2              Desg LSN 3         128.28   Shr

Itu akan menjadikan S1 sebagai sebuah root bagi S3, dan status BLOK oleh STP akan pindah ke Fa0/23 dan 24 (Port Channel 3)

![](/images/screenshot_2020-08-13_21-27-00.png)

Maka berikut tampilan dari output S3

    S3# show spanning-tree active
    VLAN0001
      Spanning tree enabled protocol ieee
      Root ID    Priority    24577
                 Address     000A.F313.2395
                 Cost        9
                 Port        27(Port-channel1)
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
    
      Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
                 Address     0001.436E.8494
                 Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
                 Aging Time  20
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Po3              Altn BLK 9         128.28   Shr
    Po1              Root FWD 9         128.27   Shr

Dari output itu kita akan mendapatkan pada Port Channel 3 yang statusnya di BLOK (oleh STP)

## Referensi

* [https://geek-university.com/ccna/access-and-trunk-ports-explained/](https://geek-university.com/ccna/access-and-trunk-ports-explained/ "https://geek-university.com/ccna/access-and-trunk-ports-explained/")
* CCNA SRWE