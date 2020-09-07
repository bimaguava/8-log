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

Seperti yang dibahas diawal, OSPF akan menyeleksi 3 hal, dan saat ini router memakai interface loopback yang telah disetel. Yang mana IP loopback tertinggi akan menjadi DR.

Sesuai output tersebut Router RC ialah sebuah Designated Router karena memiliki nilai Prioritas lebih tinggi. Sedangkan Router RB menjadi BDR.

Kedua, **Router RB**

    RB# show ip ospf neighbor
    Neighbor ID Pri State Dead Time Address Interface
    192.168.31.11 1 FULL/DROTHER 00:00:36 192.168.1.1 GigabitEthernet0/0
    192.168.31.33 2 FULL/DR 00:00:36 192.168.1.3 GigabitEthernet0/0

Kita melihat di sisi Router RB **..31.11** ialah **Router** **RA** dan **31.33** ialah **Router RC** yang statenya adalah sebagai **Designated Router**. Sedangkan Router RA merupakan hanya menjadi

Kemudian, `show ip ospf neighbor` di Router RC

    RC# show ip ospf neighbor
    Neighbor ID Pri State Dead Time Address Interface
    192.168.31.11 1 FULL/DROTHER 00:00:39 192.168.1.1 GigabitEthernet0/0
    192.168.31.22 1 FULL/BDR 00:00:38 192.168.1.2 GigabitEthernet0/0

Sehingga, kita tahu

* Router RC=**DR**
* Router RB=**BDR**
* Router RA=DROTHER (**Designated Router Other)**

## 1.B Mengaktifkan IP OSPF Adjacency debugging

Dengan ini kita bisa memonitor proses election DR dan BDR dengan sebuah debug command. Kita akan mengaktifkannya di Router RA dan RB. Sedangkan Router RC alias DR yang nanti kita akan coba untuk dipadamkan.

    RA# debug ip ospf adj
    OSPF adjacency events debugging is on
    
    RB# debug ip ospf adj
    OSPF adjacency events debugging is on

lanjut.

# 1.C Mendisable link G0/0 di RC

Kita akan belajar bagaimana sebuah proses election DR dan BDR, untuk mengetahui tersebut kita akan mencoba mendownkan si Designated Router

    RC(config)# int gigabitEthernet 0/0
    RC(config-if)# shutdown

![](/images/2020-07-09-sen-13-34-12.png)

Setelah sekitar 30 second (Setelah Dead timer expired), kita baru bisa melihat output debug, untuk mengetahui router mana yang dipilih sebagai DR dan router mana yang dipilih BDR setelah RC sebagai Designater Router dipadamkan

Untuk itu, lihat output debugging dari Router RB yang sudah kita aktifkan debugnnya

![](/images/2020-07-09-sen-13-48-18.png)

Jadi, setelah Router RC padam, kini yang menjadi Designated Router yaitu Router RB yang mana tadinya ia sebagai sebagai Backup.

Dan Router RA sebagai OSPF state/DROTHER sekarang berubah menjadi Backup Designated Router.

![](/images/2020-06-09_min_21-44-36.png)

Kurang lebih seperti itu proses sederhana yang terjadi apabila suatu link padam, maka router akan mengelek Router Backup (BDR) menjadi sebuah DR.

## 1.D Menyalahkan kembali link G0/0 RC

Kalau tadi kita sudah mengetahui apa yang terjadi bila suatu link padam. Sekarang link tersebut kita akan restore kembali.

> Sebelum itu, kita akan mencoba mengaktifkan event debuggingnya, karena ceritanya kita iseng ingin tahu proses debuggingnya events untuk suatu keperluan 

Perintahnya `debug ip ospf events`

    RA# debug ip ospf events
    OSPF adjacency events debugging is on
    
    RB# debug ip ospf events
    OSPF adjacency events debugging is on

Dengan keadaan Debugging events di RA dan RB aktif, sekarang kita coba restore link antara RC dan S1 alias gigabitEthernet 0/0

    RC(config)# int gigabitEthernet 0/0
    RC(config-if)# no shutdown

jika link sudah menyala (tandanya warna hijau), mari kita liat pesan debugging di RB

![](/images/2020-07-09_sen_14-50-47.png)

Nah, sekarang yang terjadi adalah ada perubahan roles lagi saat Router RC di restore atau dinyalahkan kembali.

Kenapa status DR dan BDR berubah lagi saat RC dinyalahkan?

> Karena seharusnya adalah **tidak berubah**

Alasan kenapa **tidak berubah?** hal ini semestinya terjadi dikarenakan OSPF tidak melakukan update DR BDR saat sudah ada yang aktif. Jika Designated Router sudah ada, maka OSPF process tidak perlu lagi mengganti Designated Routernya karena memang tidak perlu.

Sama yang terjadi dengan BDR, OSPF process tidak akan memilih device yang baru untuk memilih BDR juga.

> **Permasalahannya...** ialah karena kita tadi mengaktifkan `events debugging` pada Router RA dan RB, sehingga menyebabkan OSPF process menangkap perubahan update, hasilnya DR dan BDR pun berubah (lihat lagi gambar screenshot! diatas OSPF mengelek DR dan BDR baru, dibagian `13:04:10 OSPF: Elect BDR blablabla..`)

**Note**: Karena perintah OSPF tidak mengembalikan RB sebagai DR dan RA sebagai BDR, kita tinggal matikan debugging pada RA dan RB.

Perintahnya `undebug all` untuk mematikan event debugging yang sebelumnya kita aktifkan untuk iseng2. Nah, setelah itu coba lagi matikan link gigabitEthernet 0/0 dan nyalahkan lagi

Betulkah seperti itu yang terjadi? Mari kita coba...

**Pertama**, Matikan debug di RA dan RB

    RA# undebug all
    All possible debugging has been turned off
    
    RB# undebug all
    All possible debugging has been turned off

**Kedua**, Matikan link RC ke S1

    RC(config)# int gigabitEthernet 0/0
    RC(config-if)# shutdown

**Ketiga**, Lalu, nyalahkan lagi (^_^)

    RC(config-if)# no shutdown

**Keempat**, Tunggu sebentar sampai linknya ijo, kemudian jalankan

    RC(config-if)# do show ip ospf neighbor

![](/images/2020-07-09_sen_16-02-08.png)

Dan berikut log debugnya

![](/images/2020-07-09_sen_16-10-04.png)

Kita lihat tidak ada proses pengelekan (election) DR BDR baru.

Yang artinya **Router RB** tetap jadi **Designated Router** 

dan **Router RA** tetap jadi **Backup Designated Router**

Oke.

Materi di lanjut.

## 1.E Mendisable link G0/0 RB

Percobaan pertama adalah mendisable link di Router RC, kita sekaran akan masuk ke percobaan kedua yaitu mendisable link di Router RB

    RB(config)# int gigabitEthernet 0/0
    RB(config-if)# shutdown

![](/images/2020-07-09_sen_16-17-37.png)

Selanjutnya, kita tinggal melihat apa yang terjadi pada output debugging yang berada di RA

![](/images/2020-07-09_sen_16-24-20.png)

Maka, **Router RA** yang awalnya merupakan BDR sekarang menjadi **Designated Router**

dan **Router** **RC** yang tadinya sebuah OSPF state/DROTHER menjadi **Backup Designated Router**

Kira-kira seperti itu simpelnya.

Sebelum menuju Part 2, silahkan nyalahkan kembali link RC yang dimatikan tadi. Untuk hasilnya sudah pasti DR BDR-nya **tidak berubah.**

Dan jangan lupa kalau sudah tidak ingin lihat debuggingnya dimatikan saja

    RA# undebug all
    All possible debugging has been turned off
    
    RB# undebug all
    All possible debugging has been turned off

Oke.

Materi dilanjut ke Part 2.

# **2. Modify OSPF Priority and Force Elections**

Sekarang kita akan belajar bagaimana cara memilih paksa DR dan BDR berdasarkan nilai priority-nya, semakin besar nilainya makan akan diseleksi sebagai sebuah DR. Kurang lebih seperti itu.

## 2.A Menyetel OSPF priority pada setiap router

Caranya gunakan perintah `ip ospf priority <value>` untuk mengkonfigurasi port GigabitEthernet 0/0 pada setiap router dengan **OSPF priorities interfaces** berikut:

* **RA**: 200


* ·**RB**: 100


* ·**RC**: 1 (default priority)

Confignya akan seperti ini

    RA(config)# interface g0/0
    RA(config-if)# ip ospf priority 200

    RB(config)# interface g0/0
    RB(config-if)# ip ospf priority 100

    RC(config)# interface g0/0
    RC(config-if)# ip ospf priority 1

## 2.B Memilih paksa (election process) dengan mereset OSPF process pada router

Setelah menyetel priority pada masing-masing router, untuk apply changes dengan perintah `clear ip ospf process`

    RA# clear ip ospf process
    Reset All OSPF processess? [no] yes
    
    RB# clear ip ospf process
    Reset All OSPF processess? [no] yes
    
    RC# clear ip ospf process
    Reset All OSPF processess? [no] yes

Setelah ini kita akan mendapatkan hasilnya dari force election ini, yakni 

* **RA**: 200 menjadi **Designated Router**


* ·**RB**: 100 menjadi **Backup Designated Router**


* ·**RC**: 1 (default priority)