---
draft: true
comments: true
toc: true
title: 'Cisco: OSPFv2 Single Area Configuration (point to point and broadcast multiaccess)'
date: 2020-09-08T13:06:00Z
updated: 
category:
- network
- ensa
tags:
- cisco
keywords: []

---
# **Objectives**

Kalau di materi [sebelumnya](https://8log.js.org/2020/08/16/network/cisco-ospfv2-single-area-point-to-point/), kita sudah mengimplementasikan OSPF single area dengan topologi point to point, sekarang kita akan mencoba menerapkannya ke jaringan `point to point and broadcast multiaccess`.

# **Overview**

Sekarang kita akan mencoba untuk mengkonfigurasi Routing Dynamic OSPF, untuk yang ingin tahu cara melihat dan menganalisis konfigurasi OSPF sebelumnya sudah dijelaskan di [sini](https://8log.js.org/2020/09/08/network/cisco-ospfv2-single-area-verify/).

# **Lab**

![](/images/2020-08-09_sel_07-21-22.png)

Pada materi kali ini akan sangat berguna sekali untuk melatih kemampuan kita dalam mengkonfigurasi router dengan OSPF dengan beberapa ketentuan yang disediakan sebagai berikut.

![](/images/2020-08-09_sel_20-08-28.png)

# **Tabel Address**

![](/images/2020-08-09_sel_07-23-29.png)

![](/images/2020-08-09_sel_07-23-44.png)

# **1. Mengemplementasikan OSPF di Router2 Headquarters**

Pertama-tama kita akan mengerjakan network di **Headquarters** yang berupa point to point.

Kita telah mengetahui di materi [kemarin]() bahwa di jaringan point to point tidak ada election DR/BDR, maka kita tidak perlu repot menyetel Router ID untuk router2 P2P ini.

![](/images/2020-09-09_rab_12-55-44.png)

Untuk itu mari kita langsung saja jalankan OSPF routing process di mulai pada router P2P-1 ini

    P2P-1(config)#router ospf 10

## 1.A. Mencari router yang directly connected dengan P2P-1

Kita akan mencari router interface yang directly connected alias terhubung secara langsung dengan Router P2P ini, langsung saja jalankan `do show ip route connected`

     C   10.0.0.0/30  is directly connected, Serial0/1/0
     C   10.0.0.8/30  is directly connected, Serial0/1/1
     C   10.0.0.12/30  is directly connected, Serial0/2/0

Tampak yang IP yang muncul yaitu berupa network2 yang terkoneksi langsung ke router P2P-1

Sedangkan kalau kita menggunakan command `do show ip route` saja

    Gateway of last resort is not set
    
         10.0.0.0/8 is variably subnetted, 6 subnets, 2 masks
    C       10.0.0.0/30 is directly connected, Serial0/1/0
    L       10.0.0.1/32 is directly connected, Serial0/1/0
    C       10.0.0.8/30 is directly connected, Serial0/1/1
    L       10.0.0.9/32 is directly connected, Serial0/1/1
    C       10.0.0.12/30 is directly connected, Serial0/2/0
    L       10.0.0.13/32 is directly connected, Serial0/2/0

Maka akan menampilkan juga interface2 milik router P2P-1 itu sendiri yang ada pada baris entri kode **L** alias **Local** yang kemudian meneruskan informasi ke network **C** Alias (directly) **Connected**, itu sekedar informasi.

Dari sini kita telah menemukan network2 yang directly connected, yaitu `10.0.0.0/30`, `10.0.0.8/30`, dan `10.0.0.12/30` yang juga sudah ada keterangannnya di topologi

![](/images/2020-09-09_rab_14-01-51.png)

## 1.B. Menyetel P2P-1 dengan Network statements dan inverse mask

Kita telah melakukan cara ini pada materi [sebelumnya](https://8log.js.org/2020/08/16/network/cisco-ospfv2-single-area-point-to-point/#2-B-Menyetel-R1-dengan-Network-statements-dan-Wilcard-Mask). Sekarang yang kita butuhkan adalah command

> Router(config-router)# **network** network-address wildcard-mask **area** area-id

Jadi kita mendaftarkan network2nya satu-persatu, lalu memasukkan wilcard mask (kalau lupa menghitung wilcard mask caranya di [materi yang lalu](https://8log.js.org/2020/08/16/network/cisco-ospfv2-single-area-point-to-point/#2-A-Cara-Mengkonversikan-subnet-ke-desimal) dan ingat karena single area berarti area 0.

    P2P-1(config-router)#network 10.0.0.0 0.0.0.3 area 0
    P2P-1(config-router)#network 10.0.0.8 0.0.0.3 area 0
    P2P-1(config-router)#network 10.0.0.12 0.0.0.3 area 0

Lanjut.

## 1.C. Mengatur interface cost pada Router OSPF P2P-1

Sekarang saatnya kita akan mengatur dahulu pada router OSPF ini sehingga pada interface GigabitEthernet dan FastEthernet disetel cost yang telah ditentukan, yaitu

* **GigabitEthernet=10**
* **FastEthernet=100**

perintahnya ialah `auto-cost reference-bandwidth <bandwidth>` \[ **Gbps** | **Mbps** \]

Sementara itu ...

_"apa itu OSPF cost?"_

_"kenapa ada OSPF cost?"_

_"kenapa digunakan?"_

_"dan apa itu reference-bandwith?"_

_"apa cost semacam ini hanya ada di OSPF saja?"_

Oke, cara belajar kita adalah **_learning by doing_** sembari ngoprek, sembari belajar :)

Sebelum itu kita harus tahu fungsi dari penerapan dari cost di OSPF ini yang tidak lain dan tidak bukan ialah untuk **metric** :) Yang merupakan suatu nilai yang digunakan untuk menuju ke destination.

![](/images/2020-09-09_rab_15-17-27.png)

Simpelnya metrik ini membantu router memilih rute terbaik dimana nilai metrik setiap routing protokol berbeda-beda.

Untuk OSPF sendiri untuk nilai metric nya menggunakan bandwith atau dalam kata lain cost (hampir mirip)

| --- | --- |
| Bandwidth | OSPF Cost |
| 100 Gbps | 1 |
| 40 Gbps | 1 |
| 10 Gbps | 1 |
| 1 Gbps | 1 |
| 100 Mbps | 1 |
| 10 Mbps | 10 |
| 1.544 Mbps | 64 |
| 768 Kbps | 133 |
| 384 Kbps | 266 |
| 128 Kbps | 781 |

> Pada **Dynamic Routing Protocol lain** contoh seperti **RIP**, ia memakai `Hop` untuk metric dan **EIGRP** memakai `Bandwidth`, `Delay`, `Reliability`, dan `Load`

Sama seperti EIGRP, OSPF mendasarkan metriknya secara default pada `bandwidth link`, sehingga OSPF dinilai lebih baik daripada RIP mengandalkan metrik `hop-count`.

    P2P-1(config-router)#auto-cost reference-bandwidth 1000
    % OSPF: Reference bandwidth is changed.
            Please ensure reference bandwidth is consistent across all routers.

## 1.D Mengatur cost value pada P2P-1 interface serial 0/1/1

Selain `auto-cost reference-bandwith` kita juga akan menyetel cost yang digunakan OSPF untuk interface serial 0/1/1 pada router ini

    P2P-1(config)#int serial 0/1/1
    P2P-1(config-if)#ip ospf cost 50