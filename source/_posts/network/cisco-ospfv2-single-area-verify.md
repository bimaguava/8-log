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

Untuk menambahkan LAN baru ke **Branch Office**, kita disini hanya diberi akses untuk bekerja menggunakan R1 dan R2 saja, dengan username: **BranchAdmin**, dan password: **Branch1234.**

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

atau dengan memfilter opsi yang kita inginkan, yaitu `show ip route | include O`

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

Namun, pada field **state** menunjukkan OSPF belum memilih sebuah DR dan BDR, hal ini akan terjawab di akhir materi.

### Ketiga, tes ping dari PC1 ke ISP Network

    C:\>ping 64.100.54.5
    
    Pinging 64.100.54.5 with 32 bytes of data:
    
    Request timed out.
    Reply from 64.100.54.5: bytes=32 time=1ms TTL=253
    Reply from 64.100.54.5: bytes=32 time=1ms TTL=253
    Reply from 64.100.54.5: bytes=32 time=1ms TTL=253

Apabila ping tidak berhasil pastikan mereset process ID OSPF karena mungkin saja sebelumnya Router ID baru diset dan belum menunjukkan perubahan.

Dalam kasus tersebut maka ID itu tidak akan berubah sampai OSPF Process direset ulang terlebih dahulu dengan perintah `clear ip ospf process [pid]` atau bisa dengan mereload router.

## 2.A Verify OSPFv2 operation on R2

### Pertama, Mengetahui rute

Pertama-tama login terlebih dahulu ke router. Lalu, kita akan melihat ip route untuk meneliti rute-rutenya

    R2#show ip route
    Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
           i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
           * - candidate default, U - per-user static route, o - ODR
           P - periodic downloaded static route
    
    Gateway of last resort is 64.100.54.5 to network 0.0.0.0

Output:

         64.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C       64.100.54.4/30 is directly connected, GigabitEthernet0/1
    L       64.100.54.6/32 is directly connected, GigabitEthernet0/1
         172.16.0.0/16 is variably subnetted, 5 subnets, 3 masks
    O       172.16.1.0/24 [110/65] via 172.16.3.1, 00:30:42, Serial0/0/0
    C       172.16.2.0/24 is directly connected, GigabitEthernet0/0
    L       172.16.2.1/32 is directly connected, GigabitEthernet0/0
    C       172.16.3.0/30 is directly connected, Serial0/0/0
    L       172.16.3.2/32 is directly connected, Serial0/0/0
    O    192.168.1.0/24 [110/65] via 192.168.10.10, 00:30:42, Serial0/0/1
         192.168.10.0/24 is variably subnetted, 3 subnets, 2 masks
    O       192.168.10.4/30 [110/128] via 192.168.10.10, 00:30:42, Serial0/0/1
                            [110/128] via 172.16.3.1, 00:30:42, Serial0/0/0
    C       192.168.10.8/30 is directly connected, Serial0/0/1
    L       192.168.10.9/32 is directly connected, Serial0/0/1
    S*   0.0.0.0/0 [1/0] via 64.100.54.5

Dan Router R2 ini mendapatkan default Route ke ISP dengan routing protocol `Static default Route` yang kodenya __S*__.

Yang mana kita masih ingat tadi simbol __*__ ialah sebuah default route dan **S** merupakan sebuah protocol routing **Static**

Tentang Static default route:

* **Static default route** merupakan tipe routing static yang digunakan ketika destination network belum diketahui (internet).
* **Static default route** ini menggunakan destination network address 0.0.0.0 dan subnet mask 0.0.0.0 pada saat melakukan routing
* **Static default routing** ini juga dikenal sebagai `‘quad zero route’`
* Proses routing untuk **static default route** ini adalah nantinya router melakukan proses pencarian gateway yang akan digunakan oleh router untuk mengirimkan semua paket IP untuk network destination yang tidak diketahui di routing table, sehingga akan diforward ke route 0.0.0.0/0.

Sumber: [https://misskecupbung.wordpress.com/2018/12/08/cisco-static-default-route/](https://misskecupbung.wordpress.com/2018/12/08/cisco-static-default-route/ "https://misskecupbung.wordpress.com/2018/12/08/cisco-static-default-route/")

### Kedua, Mengetahui Network type OSPF

Kita lihat bagian interface G0/0

![](/images/2020-08-09_sel_17-11-42.png)

coba lihat dengan perintah

    R2# show ip ospf interface g0/0
    
    GigabitEthernet0/0 is up, line protocol is up
      Internet address is 172.16.2.1/24, Area 0
      Process ID 10, Router ID 2.2.2.2, Network Type BROADCAST, Cost: 1
      Transmit Delay is 1 sec, State DR, Priority 1
      Designated Router (ID) 2.2.2.2, Interface address 172.16.2.1
      No backup designated router on this network
      Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
        No Hellos (Passive interface)
      Index 1/1, flood queue length 0
      Next 0x0(0)/0x0(0)
      Last flood scan length is 1, maximum is 1
      Last flood scan time is 0 msec, maximum is 0 msec
      Neighbor Count is 0, Adjacent neighbor count is 0
      Suppress hello for 0 neighbor(s)

Dan dari pesan itu kita tahu informasi network typenya: **Process ID 10, Router ID 2.2.2.2, Network Type BROADCAST**

Kenapa Broadcast?

Dan dari pesan itu kita tahu bahwa tidak ada paket hello yang dikirimkan ke interface ini karena ini dikonfigurasi sebagai passive interface: **No Hellos (Passive interface)**

Kenapa dia passive interface? alasannya mungkin karena memang interfaces ini mengarah ke LAN jadi link ini tidak perlu berpartisipasi dalam OSPF process.

Maka dari itu untuk menghemat cost dari OSPF yang selalu mengirim paket ke semua interface. jadi interface yang ke LAN ini di passive-kan untuk mencegah proses OSPF mengirim paket trafik yang tidak perlu ke interface LAN. Cukup di OSPF neighbor adjacency saja.

### Ketiga, tes ping dari PC2 ke R3 S0/0/1

    C:\>ping 192.168.10.10
    
    Pinging 192.168.10.10 with 32 bytes of data:
    
    Reply from 192.168.10.10: bytes=32 time=2ms TTL=254
    Reply from 192.168.10.10: bytes=32 time=1ms TTL=254
    Reply from 192.168.10.10: bytes=32 time=1ms TTL=254
    Reply from 192.168.10.10: bytes=32 time=1ms TTL=254
    
    Ping statistics for 192.168.10.10:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 1ms, Maximum = 2ms, Average = 1ms

dan terkoneksi dengan baik, cuma cek.

## 3.C Verify OSPFv2 operation on R3

### Pertama, Melihat IP protocols

Sekarang kita mau memverifikasi bahwa konfigurasi OSPF sedang diproses berjalan baik. Untuk itu kita perlu mengetahui bahwa routing dari R3, dia me-route ke mana saja. Coba menggunakan perintah `show ip protocols`

    R3# show ip protocols 
    
    Routing Protocol is "ospf 10"
      Outgoing update filter list for all interfaces is not set 
      Incoming update filter list for all interfaces is not set 
      Router ID 3.3.3.3
      Number of areas in this router is 1. 1 normal 0 stub 0 nssa
      Maximum path: 4
      Routing for Networks:
        192.168.1.0 0.0.0.255 area 0
        192.168.10.4 0.0.0.3 area 0
        192.168.10.8 0.0.0.3 area 0
      Routing Information Sources:  
        Gateway         Distance      Last Update 
        1.1.1.1              110      00:00:51
        2.2.2.2              110      00:00:50
        3.3.3.3              110      00:00:51
      Distance: (default is 110)

Dan terlihat R3 telah me route 3 network, 192.168.1.0 0.0.0.255 area 0, 192.168.10.4 0.0.0.3 area 0, 192.168.10.8 0.0.0.3 area 0 ini merupakan network OSPF yang konfigurasinya ada di ketiga router (R1,R2,R3).

### Ketiga, Neighbor priority

Sekarang apa neighbor priority yang ditampilkan pada OSPF Neighbor router, selain menggunakan `show ip ospf neighbor` kita juga bisa mendapatkan perintah yang lebih detail dengan `show ip ospf neighbor detail`

    R3# show ip ospf neighbor 
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    1.1.1.1           0   FULL/  -        00:00:36    192.168.10.5    Serial0/0/0
    2.2.2.2           0   FULL/  -        00:00:39    192.168.10.9    Serial0/0/1

Disana Nilai prioritynya nol untuk `192.168.10.5` dan `192.168.10.9` yang kita sudah tahu router dengan prioritas tertinggi menjadi Designated Router. Jika prioritasnya sama, maka router dengan ID router tertinggi menjadi DR, yaitu router neighbor dengan ID 2.2.2.2.

Dan kita belum melihat adanya DR dan BDR yang terpilih.

### Keempat, tes ping dari PC3 ke ISP Network

    C:\>ping 64.100.54.5
    
    Pinging 64.100.54.5 with 32 bytes of data:
    
    Request timed out.
    Reply from 64.100.54.5: bytes=32 time=1ms TTL=253
    Reply from 64.100.54.5: bytes=32 time=1ms TTL=253
    Reply from 64.100.54.5: bytes=32 time=1ms TTL=253
    
    Ping statistics for 64.100.54.5:
        Packets: Sent = 4, Received = 3, Lost = 1 (25% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 1ms, Maximum = 1ms, Average = 1ms

dan terkoneksi dengan baik, cuma ngecek.

oke.

kanjut.

## **2. Add the new Branch Office LAN to the OSPFv2 network**

Setelah kita mengecek sembari belajar perintah verifikasi, sekarang saatnya menambahkan LAN Branch Office ke jaringan OSPF kita.

Sebelum itu kita lihat show run Router R4 (Branch Office) dengan memfilter beberapa output saja yang kita inginkan

    R4# show run | begin router ospf
    router ospf 10
     router-id 4.4.4.4
     log-adjacency-changes
     passive-interface GigabitEthernet0/0/1
     network 192.168.1.0 0.0.0.255 area 0
     network 192.168.11.0 0.0.0.255 area 0
    !

Terlihat di interface G0/0/1 (yang mengarah le LAN-nya) yang merupakan passive interface sehingga tidak akan menerima paket update OSPF dan ternyata kita lihat sudah ada pre-configure OSPF Network di R4 ini.

Yaitu, 2 network berikut

![](/images/2020-08-09_sel_19-18-45.png)

Jadi sekarang kita mengkoneksikan Router R4 ke switch S3 dengan menggunakan kabel Straight.

Maka, setelah dihubungkan R3 akan langsung menjadikan R4 sebagai Neighbor adjacency sebagaimana terlihat di log R3

    13:01:35: %OSPF-5-ADJCHG: Process 10, Nbr 4.4.4.4 on GigabitEthernet0/0 from LOADING to FULL, Loading Done

Sudah sampai sini kita pastinya ingin melihat suatu perubahan pada jaringan OSPF kita tadi yang tadinya point to point, maka dengan menambah link ke LAN Branch Office maka akan cukup untuk memenuhi satu syarat agar OSPF bisa otomatis mengelek DR/BDR yaitu tipe networknya **broadcast network**.

Dengan itu maka suatu DR BDR election process akan terjadi disitu.

![](/images/2020-08-09_sel_19-37-32.png)

Sumber: [https://www.freeccnaworkbook.com/workbooks/ccna/configuring-ospf-network-types](https://www.freeccnaworkbook.com/workbooks/ccna/configuring-ospf-network-types "https://www.freeccnaworkbook.com/workbooks/ccna/configuring-ospf-network-types")

Kita cek lagi pada ospf2 neighbor kita

Mulai dari R3

    R3# show ip ospf neighbor 
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    1.1.1.1           0   FULL/  -        00:00:38    192.168.10.5    Serial0/0/0
    2.2.2.2           0   FULL/  -        00:00:30    192.168.10.9    Serial0/0/1
    4.4.4.4           1   FULL/BDR        00:00:34    192.168.1.2     GigabitEthernet0/0

Router R1 (1.1.1.1), Router R2 (2.2.2.2) tidak dipilih sebagai DR/BDR karena OSPF memilih berdasarkan Router ID (dalam kasus ini) yang tertinggi, yaitu pada Router R3 dan R4

    R4# show ip ospf neighbor 
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    3.3.3.3           1   FULL/DR         00:00:33    192.168.1.1     GigabitEthernet0/0/0

R3 sebagai DR dan R4 sebagai BDR. Padahal posisi R4 dengan router ID 4.4.4.4 seharusnya dipilih sebagai sebuah Designated Router.

Kenapa hal ini terjadi?

R1 dan R2 ialah point to point network yang mana disana tidak ada OSPF election DR/BDR.

Sedangkan R3 dan R4 berada pada multiaccess network. Namun saat  terjadi proses election, yang dipilih ialah si R3 dengan Router ID 3.3.3.3. Mungkin ada sesuatu yang terjadi tapi belum ku ketahui (^_^)

![](/images/memecenter_1411257255873_287.jpg)

# **Referensi**

* [https://misskecupbung.wordpress.com/2018/12/08/cisco-static-default-route/](https://misskecupbung.wordpress.com/2018/12/08/cisco-static-default-route/ "https://misskecupbung.wordpress.com/2018/12/08/cisco-static-default-route/")
* [https://flylib.com/books/en/3.73.1.41/1/](https://flylib.com/books/en/3.73.1.41/1/ "https://flylib.com/books/en/3.73.1.41/1/")