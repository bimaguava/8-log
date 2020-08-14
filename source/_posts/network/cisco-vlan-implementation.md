---
draft: true
comments: true
toc: true
title: 'Cisco: VLAN Implementation'
date: 2020-08-12T17:00:00Z
updated: 
category:
- network
tags:
- cisco
keywords: []

---
## Petunjuk Awal VLAN

Untuk teori silahkan baca di [sini]() karena sebelum membuat VLAN ada baiknya mengetahui kapan kita membutuhkan VLAN, dll.

Pada materi ini kita akan belajar bagaimana suatu VLAN bekerja, untuk yang ingin belajar konfigurasi VLAN silahkan ke [sini](8log.netlify.app/2020/07/26/network/cisco-vlan-configuration "sini")

## Lab

Download: [https://drive.google.com/file/d/1F78eUuw6BMl43hsats0RJw3C8HiwHRe1/view](https://drive.google.com/file/d/1F78eUuw6BMl43hsats0RJw3C8HiwHRe1/view "https://drive.google.com/file/d/1F78eUuw6BMl43hsats0RJw3C8HiwHRe1/view")

![](/images/screenshot_2020-08-13_23-40-48.png)

jadi, disini kita punya topologi yang memuat beberapa sub network (Lihat IP) yang mana ada 3 VLAN, VLAN 10, 20, dan 30.

Supaya mudah untuk pahami, tinggal melihat bagian host id dari IP misal 172.17.`10`.21 berarti nanti akan berada pada VLAN 10 seperti itu. Untuk lebih jelasnya silahkan merujuk ke tabel address.

## Tabel Address

![](/images/screenshot_2020-08-13_23-44-33.png)

## What we do?

* Pada bagian 1 kita akan mempelajari broadcast trafik pada topologi VLAN Implementation ini
* Pada bagian 2 kita akan mencoba mempelajari broadcast trafik yang dilakukan tanpa menggunakan VLAN

Intinya kita nanti akan memahami bagaimana suatu paket broadcast yang diforward switch saat pakai VLAN dan tidak memakai VLAN

## 1. Observe Broadcast Traffic in a VLAN Implementation

### 1.A. Ping dari PC1 ke PC6

Ping yang dilakukan ke network yang berbeda, yaitu **PC1: 172.17.10.21** ke **PC2: 172.17.30.26**

Mula-mula kita akan melihat dahulu suatu ARP request saat melintasi jaringan tersebut.

![img](https://i.imgur.com/mJDvWxV.gif)

dan hasilnya paket/pesan ICMP yang dikirim gagal yang artinya terjadi suatu masalah karena PC 1 berada pada VLAN yang berbeda dengan PC6 yang mana VLAN tidak mengizinkan device-nya berkomunikasi dengan VLAN yang berbeda/terpisah (secara logically)

Selain itu juga PC 1 berada pada sub network dan gateway yang berbeda yaitu **PC1: 172.17.10.21** ke **PC2: 172.17.30.26**

Untuk lebih paham dengan cuplikan tersebut, coba dianalisa

> _Kemana S1,S2,S3 mengirim paket setelah menerimanya?_

Tentunya ARP request yang dikirim dari switch merupakan sebuah pesan broadcast yang dikirim hanya ke sebuah host yang diizinkan saja, yakni adalah yang bersumber dari PC1 alias VLAN 10 saja.

Maka host2 yang berada pada VLAN 20, 30 tidak akan menerima broadcast tadi. Silahkan lihat kembali cuplikannya.

Karena pada dasarnya adalah switch akan **membawa paket kepada subnetwork yang sama.**

**Tidak mungkin switch meneruskan paket yang dikirim dari 172.17.10.21 ke 172.17.30.26** Karena bukan tujuannya alias berbeda network dan yang bertugas untuk hal itu ialah dinamakan router atau sebuah proses yang dinamakan routing dan tidak ada pembahasannya disini, melenceng.

### 1.B. Ping dari PC1 to PC4

Sekarang kita akan mengecek dari **PC1: 172.17.10.21** ke **PC4: 172.17.10.24**

Ia berada pada network yang sama yang mana berada pada VLAN 10, gateway yang sama yaitu 172.17.`10.1`

Simulasi saat pesan broadcast dikirim akan seperti ini

Kita lihat dicuplikan saat paket terkirim ke S1, dia mengirim kedua arah. Satu kearah PC7 satu kearah S3. Penjelasannya:

Saat S1 mengirim ke PC7 itu merupakan ARP request yang termasuk di dalam VLAN 10. Jadi jawabannya **switch akan memforward ke device mana saja yang berada pada VLAN 10**

Dan saat dimana S1 mengirim ke S3 itu merupakan sebuah kodratnya switch yang menerima paket dan meneruskannya kembali, jadi kita tahu bahwa penggunaan switch adalah meneruskan sebuah ARP request dari source ke destination dengan network yang sama.

Karena jalur ARP request sama dengan sumbernya maka paket akan berhasil diterima dari ujung ke ujung dan akan dikirim lagi ke PC1 yang ditandai dengan output packet reply from blablabla.. sehingga paket sukses diterima ~~dari JNE~~.

## 2. Observe Broadcast Traffic without VLANs

### 2.A. Menghapus konfig pada semua switch dan juga VLAN database

Sekarang kita akan menghapus startup-config terlabih dahulu

    S1>enable
    S1#erase startup-config 
    Erasing the nvram filesystem will remove all configuration files! Continue? [confirm]
    [OK]
    Erase of nvram: complete
    %SYS-7-NV_BLOCK_INIT: Initialized the geometry of nvram

Setelah menghapus startup-config kita masih akan bisa menemukan file dari VLAN database biasanya dengan nama **vlan.dat** yang berada pada `flash:/`

Coba lihat dengan command `show flash`

    S1#show flash: 
    Directory of flash:/
    
        1  -rw-     4414921          <no date>  c2960-lanbase-mz.122-25.FX.bin
        2  -rw-         796          <no date>  vlan.dat
    
    32514048 bytes total (28098331 bytes free)

Nah, sekarang kita akan menghapus file tersebut

    S1#delete vlan.dat
    Delete filename [vlan.dat]?
    Delete flash:/vlan.dat? [confirm]

Oke ...

et belum selesai.

### 2.B. Reload the switch

Sekarang kita perlu mereset pada `privileged exec mode` juga seperti tadi, dengan command `reload`

    S1#reload
    Proceed with reload? [confirm]
    C2960 Boot Loader (C2960-HBOOT-M) Version 12.2(25r)FX, RELEASE SOFTWARE (fc4)
    Cisco WS-C2960-24TT (RC32300) processor (revision C0) with 21039K bytes of memory.
    2960-24TT starting...
    Base ethernet MAC Address: 0030.A3C0.74BA
    Xmodem file system is available.
    Initializing Flash...
    flashfs[0]: 1 files, 0 directories
    flashfs[0]: 0 orphaned files, 0 orphaned directories
    flashfs[0]: Total bytes: 32514048
    flashfs[0]: Bytes used: 4414921
    flashfs[0]: Bytes available: 28099127
    flashfs[0]: flashfs fsck took 1 seconds.
    ...done Initializing Flash.
    
    Boot Sector Filesystem (bs:) installed, fsid: 3
    Parameter Block Filesystem (pb:) installed, fsid: 4
    
    
    Loading "flash:/c2960-lanbase-mz.122-25.FX.bin"...
    ########################################################################## [OK]

Sekarang coba lakukan pada S2 dan S3

* hapus konfigurasi switch
* hapus file vlan database
* reset switch

Kalau sudah nanti setelah di reload kita tunggu switchnya sedang proses booting atau biasanya dengan warna oren di packet tracer.

![](/images/screenshot_2020-08-14_09-01-28.png)

kalau mau cepat nyala hijau tinggal klik`Fast Forward Time` di toolbar bawah atau dengan keybind **\[Alt + D\]**

### 2.C. Klik Capture/Forward untuk mengirim ARP requests atau ping

[img](ssddddxxxxwdhttps://i.imgur.com/fdB5AWI.gif)

Perhatikan bahwa sekarang switch meneruskan ARP request keluar dari semua port, kecuali port tempat ARP request diterima.

Tindakan dari switch ini adalah mengapa VLAN dapat meningkatkan kinerja jaringan. Broadcast trafik yang ada dalam setiap VLAN. Ketika jendela Buffer Full muncul, klik tombol View Previous Events.