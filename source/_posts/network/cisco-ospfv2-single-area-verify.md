---
draft: true
comments: true
toc: true
title: 'Cisco: OSPFv2 Single Area (Verify)'
date: 2020-09-08T00:40:00Z
updated: 
category:
- network
- ensa
tags:
- cisco
keywords: []

---
# **Objectives**

Pada materi ini kita akan belajar menggunakan perintah verifikasi pada jaringan OSPFv2 ini seperti:

* Mengidentifikasi dan verify status `OSPF Neighbor`
* Mengetahui bagaimana suatu rute dipilih dan digunakan dalam sebuah jaringan
* Mengetahui bagaimana `Neighbor state` ditentukan
* Melihat konfigurasi OSPF process ID
* Dan juga nanti kita akan menambahkan sebuah LAN ke sebuah OSPF network

# **Lab**

![](/images/2020-08-09_sel_07-49-05.png)

Pada area berwarna hijau nanti disana kita menambahkan sebuah jaringan wireless baru yang mana itu ialah LAN **Branch Office**.

Cuma kita akan belajar memverifikasi saja bagaimana OSPF yang sudah diterapkan disitu, setelah itu nanti kita baru akan mencoba menyambungkan LAN baru ke **Branch Office.**

Untuk menambahkan LAN baru ke **Branch Office**, kita disini hanya diberi akses untuk bekerja menggunakan R1 dan R2 saja, dengan username: **BranchAdmin**, dan password: **Branch1234**

# **Tabel Address**

![](/images/2020-08-09_sel_07-49-38.png)

# 1. Verify the existing OSPFv2 network operation

Command verifikasi atau pengecekan yang nanti digunakan ialah:

* **show ip interface brief**
* **show ip route**
* **show ip route ospf**
* **show ip ospf neighbor**
* **show ip protocols**
* **show ip ospf**
* **show ip ospf interface**

## 1.A Mengecek rute OSPF 

Kalau baru membuka Paket Tracer biasanya kita akan menunggu proses STP, apabila lampu indikator hijau sudah muncul maka kita bisa melanjutkan.

Pertama-tama kita akan login ke R1, lalu kita akan mencoba melihat status interface2 yang terkoneksi dengan perintah `show ip route`

    R1# show ip route 
    Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
           i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
           * - candidate default, U - per-user static route, o - ODR
           P - periodic downloaded static route

output:

    Gateway of last resort is 172.16.3.2 to network 0.0.0.0
    
         172.16.0.0/16 is variably subnetted, 5 subnets, 3 masks
    C       172.16.1.0/24 is directly connected, GigabitEthernet0/0
    L       172.16.1.1/32 is directly connected, GigabitEthernet0/0
    O       172.16.2.0/24 [110/65] via 172.16.3.2, 01:17:06, Serial0/0/0
    C       172.16.3.0/30 is directly connected, Serial0/0/0
    L       172.16.3.1/32 is directly connected, Serial0/0/0
    O    192.168.1.0/24 [110/65] via 192.168.10.6, 01:17:06, Serial0/0/1
         192.168.10.0/24 is variably subnetted, 3 subnets, 2 masks
    C       192.168.10.4/30 is directly connected, Serial0/0/1
    L       192.168.10.5/32 is directly connected, Serial0/0/1
    O       192.168.10.8/30 [110/128] via 172.16.3.2, 01:17:06, Serial0/0/0
                            [110/128] via 192.168.10.6, 01:17:06, Serial0/0/1
    O*E2 0.0.0.0/0 [110/1] via 172.16.3.2, 01:17:06, Serial0/0/0

Hal yang pertama adalah di kolom kiri terdapat simbol2 yang arti nya ada di keterangan Codes.

Contohnya **O*E2** 

* **O** - OSPF (routing protokol yang digunakan ialah OSPF)


* __*__ - candidate default (merupakan default route)


* **E2** - OSPF external type 2

Untuk OSPF external ada 2 tipe, E1 dan E2

> E1 akan memperhitungkan `external metric` dan juga `internal metric`

Sedangkan

> E2 hanya memperhitungkan `external metric`, dimana setiap routing protocol yang akan terhubung entah itu RIP, OSPF, EIGRP, Static, dll akan memiliki external metric saat diredistribute ke OSPF

Lalu timbul pertanyaan bagaimana cara menghitung nilai metric tersebut?

Masih fokus bagian ini

    O*E2 0.0.0.0/0 [110/1] via 172.16.3.2, 01:17:06, Serial0/0/0

Yang mana merupakan rute menuju titik dimana sebuah destination, yaitu 0.0.0.0/0 alias internet (ISP Network) dengan menggunakan **Routing protokol OSPF** dan menggunakan **default route** yang diterima R1 serta **OSPF external type 2** via interface 172.16.3.2 (serial0/0/0)

![](https://i.imgur.com/RZ07Fpk.png)

Lalu, dari code `[110/1]`, 110 menunjukkan **administrative distance** OSPF sedangkan 20 menunjukkan **nilai metric** yang digunakan R1 menuju network tersebut. 

**Berikut tabel Administrative distance**

| Route Source | Default Distance Value |
| --- | --- |
| Connected interface | 0 |
| Static route | 1 |
| EnhanceInterior Gateway Routing Protocol (EIGRP) summary route | 5 |
| Externa Border Gateway Protocol (BGP) | 20 |
| Internal EIGRP | 90 |
| IGRP | 100 |
| OSPF | 110 |
| Intermediate System-to-Intermediate System (IS-IS) | 115 |
| Routing Information Protocol (RIP) | 120 |
| Exterior Gateway Protocol (EGP) | 140 |
| On Demand Routing (ODR) | 160 |
| External EIGRP | 170 |
| Internal BGP | 200 |
| Unknown | 255 |

**Berikut tabel nilai metric**

![](/images/selection_078.png)

# **Referensi**

* [http://www.mikrotik.co.id/artikel_lihat.php?id=321](http://www.mikrotik.co.id/artikel_lihat.php?id=321 "http://www.mikrotik.co.id/artikel_lihat.php?id=321")
* 