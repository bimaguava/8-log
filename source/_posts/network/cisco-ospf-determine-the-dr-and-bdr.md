---
draft: true
comments: true
toc: true
title: 'Cisco: OSPF Determine the DR and BDR'
date: 2020-08-24T18:00:00.000+00:00
updated: 
category:
- network
- ensa
tags:
- cisco
keywords: []

---
# **Overview**

Di materi ini akan membahas tentang dasar-dasar dari bagaimana untuk dapat bekerja menggunakan sebuah Designated Router (DR) dan Backup Designated Router (BDR) pada OSPF.

Yang mana kalau sudah membaca pada [OSPF intro](https://8log.js.org/2020/08/22/network/cisco-ospf-intro/) kita tahu bahwa ada 3 hal dalam proses seleksi DR dan BDR, yaitu:

* Dengan memilih Router ID yang tertinggi
* Kalau tidak ada router ID, maka dilihat dari IP loopbacknya
* Dan kalau tidak ada IP loopback, maka IP Interfacenya

Selain itu, juga kita sudah mengetahui bahwa untuk mengkonfigurasi OSPF ada 3 cara, yaitu:

* dengan memasukkan network2 dan wilcard mask _e.g:_ `network 10.1.1.0 0 0.0.0.3 area 0`
* dengan memasukkan IP address dari interfaces dan zero quad mask _e.g:_ `network 10.1.1.2 0.0.0.0 area 0`
* atau dengan menyetel langsung di interfacesnya 

Sekarang kita akan mengembangkan materi kita untuk lebih memahami untuk dapat bekerja dengan OSPF sebagai protokol routing yang termasuk di Interior Gateway Protokcol (IGP).

# **Lab**

![](/images/2020-06-09-min-21-44-36.png)

Jadi skenarionya, kita akan belajar apa yang dilakukan dari DR dan BDR dan melihat perubahan apa yang terjadi dalam jaringan saat hal ini diimplementasikan. 

Kemudian akan mengubah prioritas untuk mengontrol tugas dari sebuah DR dan mencoba untuk mengelek sebuah DR sesuai yang kita inginkan.

Sehingga, pada akhirnya kita akan memverifikasi bahwa sebuah router yang kita pilih berhasil menjadi sebagai DR dan juga sebagai BDR.

# **Tabel Address**

![](/images/2020-07-09-sen-00-53-03.png)

# **1. Examine DR and BDR Changing Roles**

## 1.A Melihat status(state) OSPF Neighbor

Disini kita mempunyai topologi yang sudah di setel dengan OSPF, sekarang kita ingin melihat status DR-BDR dari OSPF neighbor menggunakan perintah `show ip ospf neighbor` di setiap router.

Jika router menampilkan **FULL/DROTHER**, artinya router tersebut bukan DR atau BDR.

Pertama, **Router RA** dahulu

    RA# show ip ospf neighbor
    Neighbor ID Pri State Dead Time Address Interface
    192.168.31.33 2 FULL/DR 00:00:35 192.168.1.3 GigabitEthernet0/0
    192.168.31.22 1 FULL/BDR 00:00:35 192.168.1.2 GigabitEthernet0/0

outpunya menampilkan 2 interface, yaitu **192.168.31.33 (Router RC)** dan **192.168.31.22 (Router RB)**.

Seperti yang dibahas diawal, OSPF akan menyeleksi 3 hal, dan saat ini router memakai interface loopback yang telah disetel. Yang mana IP loopback tertinggi akan menjadi DR, sesuai output tersebut Router RC ialah sebuah Designated Router karena memiliki nilai Prioritas lebih tinggi. Sedangkan Router RB menjadi BDR.

Kedua, **Router RB**

    RB# show ip ospf neighbor
    Neighbor ID Pri State Dead Time Address Interface
    192.168.31.11 1 FULL/DROTHER 00:00:36 192.168.1.1 GigabitEthernet0/0
    192.168.31.33 2 FULL/DR 00:00:36 192.168.1.3 GigabitEthernet0/0

**..31.11** ialah **Router** **RA** dan 31.33 ialah **Router RC**.

    RC# show ip ospf neighbor
    Neighbor ID Pri State Dead Time Address Interface
    192.168.31.11 1 FULL/DROTHER 00:00:39 192.168.1.1 GigabitEthernet0/0
    192.168.31.22 1 FULL/BDR 00:00:38 192.168.1.2 GigabitEthernet0/0

# **2. Modify OSPF Priority and Force Elections**