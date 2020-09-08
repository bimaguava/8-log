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

### Pertama, ospf route

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

Hal yang pertama adalah di kolom kiri terdapat simbol2 yang arti nya ada di keterangan Codes. Yang mana berbagai macam entri ada C, L, dll

Contohnya **O*E2**

* **O** - OSPF (routing protokol yang digunakan ialah OSPF)
* __*__ - candidate default (merupakan default route)
* **E2** - OSPF external type 2

Untuk OSPF external ada 2 tipe, E1 dan E2

> E1 akan memperhitungkan `external metric` dan juga `internal metric`

Sedangkan

> E2 hanya memperhitungkan `external metric`, dimana setiap routing protocol yang akan terhubung entah itu RIP, OSPF, EIGRP, Static, dll akan memiliki external metric saat diredistribute (`redistribute connected subnets`) ke OSPF

Lalu timbul pertanyaan bagaimana cara menghitung nilai metric tersebut?

Masih fokus bagian ini

    O*E2 0.0.0.0/0 [110/1] via 172.16.3.2, 01:17:06, Serial0/0/0

Yang mana merupakan rute menuju titik dimana sebuah destination, yaitu 0.0.0.0/0 alias internet (ISP Network) dengan menggunakan **Routing protokol OSPF** serta **OSPF external type 2**.

Kemudian menggunakan **default route** yang diterima R1 via interface 172.16.3.2 (serial0/0/0) alias Router R2 dimana R1 menerima sebuah default route.

![](https://i.imgur.com/RZ07Fpk.png)

Lalu, dari code `[110/1]`, 110 menunjukkan **administrative distance** OSPF sedangkan 20 menunjukkan **nilai metric** yang digunakan R1 menuju network tersebut yang sebagai jumlah hop dan agregate host.

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

Dan disini kita memiliki OSPF yang AD nya bernilai 110

**Berikut tabel nilai metric**

![](/images/selection_078.png)

Dan juga sebuah default route yang mana external route (E2) dari 'default route' (yang tadi kodenya __*__ **- candidate default**)  adalah 1.

Itu sekedar pengetahuan, oke.

simpelnya kita sebetulnya bisa memfilter output dari **show ip route** untuk menunjukkan hanya rute yang berhubungan dengan OSPF saja yang akan ditampilkan alias entri O saja. Dengan cara `show ip route ospf`

    R1# show ip route ospf 
         172.16.0.0/16 is variably subnetted, 5 subnets, 3 masks
    O       172.16.2.0 [110/65] via 172.16.3.2, 03:12:41, Serial0/0/0
    O    192.168.1.0 [110/65] via 192.168.10.6, 03:12:41, Serial0/0/1
         192.168.10.0/24 is variably subnetted, 3 subnets, 2 masks
    O       192.168.10.8 [110/128] via 172.16.3.2, 03:12:41, Serial0/0/0
                         [110/128] via 192.168.10.6, 03:12:41, Serial0/0/1
    O*E2 0.0.0.0/0 [110/1] via 172.16.3.2, 03:12:41, Serial0/0/0

atau dengan opsi lain, yaitu `show ip route | include O`

    R1# show ip route | include O       
    O       172.16.2.0/24 [110/65] via 172.16.3.2, 03:17:17, Serial0/0/0
    O    192.168.1.0/24 [110/65] via 192.168.10.6, 03:17:17, Serial0/0/1
    O       192.168.10.8/30 [110/128] via 172.16.3.2, 03:17:17, Serial0/0/0
    O*E2 0.0.0.0/0 [110/1] via 172.16.3.2, 03:17:17, Serial0/0/0

Maka yang muncul adalah rute-rute OSPF saja.

### Kedua, OSPF Neighbor

Sekarang kita akan melihat OSPF neighbor atau router2 tetangga (OSPF)

    R1# show ip ospf neighbor 
    
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    2.2.2.2           0   FULL/  -        00:00:31    172.16.3.2      Serial0/0/0
    3.3.3.3           0   FULL/  -        00:00:31    192.168.10.6    Serial0/0/1

Dari situ kita mengetahui router mana yang merupakan adjacency (berdekatan) dengan R1, yaitu Router R2 (S0/0/0 `172.16.3.2`), dan R3 (S0/0/1 `192.168.10.6`).

Dan kita lihat Neighbor ID alias _"Router ID nya Neighbor"_ yang biasanya didapatkan dari Router ID, atau kalau tidak ada Loopback ID, kemudian IP Address. Tujuannya nanti akan dipakai sebagai pemilihan sebuah DR dan BDR, untuk materi tersebut silahkan lihat [disini](https://8log.js.org/2020/08/24/network/cisco-ospfv2-determine-the-dr-and-bdr/).

### Ketiga, tes ping dari PC1 ke ISP Network

    C:\>ping 64.100.54.5
    
    Pinging 64.100.54.5 with 32 bytes of data:
    
    Request timed out.
    Reply from 64.100.54.5: bytes=32 time=1ms TTL=253
    Reply from 64.100.54.5: bytes=32 time=1ms TTL=253
    Reply from 64.100.54.5: bytes=32 time=1ms TTL=253

Apabila ping tidak berhasil pastikan mereset process ID OSPF karena mungkin saja sebelumnya Router ID baru diset dan belum menunjukkan perubahan. 

Dalam kasus tersebut maka ID itu tidak akan berubah sampai OSPF Process direset ulang terlebih dahulu dengan perintah `clear ip ospf process [pid]` atau bisa dengan mereload router.

# **Referensi**

* [http://www.mikrotik.co.id/artikel_lihat.php?id=321](http://www.mikrotik.co.id/artikel_lihat.php?id=321 "http://www.mikrotik.co.id/artikel_lihat.php?id=321")
* [https://flylib.com/books/en/3.73.1.41/1/](https://flylib.com/books/en/3.73.1.41/1/ "https://flylib.com/books/en/3.73.1.41/1/")