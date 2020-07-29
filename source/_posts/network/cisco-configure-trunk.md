---
draft: true
comments: true
toc: true
title: 'Cisco: Configure trunk'
date: 2020-07-29T17:00:00.000+00:00
updated: 2020-07-29T17:00:00.000+00:00
category:
- network
tags:
- cisco
keywords: []

---
**Simpelnya trunk itu diperlukan untuk meneruskan informasi VLAN antar switch.**

Fungsi Trunk itu tidak lain dan tidak bukan adalah menghubungkan 2 switch agar kedua VLAN di masing masing SWITCH dapat terhubung.

`ini bukan di switch manageble doang sih, di routerboard kalo diterapkan vlan juga nanti akan memerlukan setelan trunk untuk bisa terhubung antar VLANnya`

## Gambaran konfig

### switch mode trunk

Untuk mengaktifkan trunk pada suatu interface yang terhubung ke switch lain

### switchport native vlan \[nomor\]

Native VLAN ini suatu aturan data frame yang memungkinkan switch yang tidak mendukung 802.1Q agar bisa melintaskan traffic VLAN ke switch atau perangkat lain.

### switchport trunk allowed vlan \[nomor vlan – nomor vlan\]

kita bisa mem-filter vlan mana saja yang bisa lewat di jalur trunk itu

## Lab

download: [https://drive.google.com/file/d/1FRAww1bpBoFtxtQ0XSzHbdVwToVZHvEU/view](https://drive.google.com/file/d/1FRAww1bpBoFtxtQ0XSzHbdVwToVZHvEU/view "https://drive.google.com/file/d/1FRAww1bpBoFtxtQ0XSzHbdVwToVZHvEU/view")

![](/images/screenshot_2020-07-29_10-48-19.png)

## Tabel Address

![](/images/screenshot_2020-07-29_10-55-12.png)

## Instruksi (sekaligus pembahasan wkwkwk)

## 1. Mengecek status VLAN

Lihat tabel address, PC1 dan PC 4 terhubung dengan VLAN 10, coba kita cek ping apakah nyambung?

    C:\>ping 172.17.10.24
    
    Pinging 172.17.10.24 with 32 bytes of data:
    
    Request timed out.
    Request timed out.
    Request timed out.
    Request timed out.

Nah, belum bisa. karena...

teorinya ialah VLAN defaultnya hanya di nomor 1 (VLAN 1), jika ingin menghubungkan dengan ke switch lain dengan **selain VLAN 1** maka kita butuh Trunk

Lalu, cek VLAN pada S2 dan S3

    show vlan brief

dan status keduanya betul (sudah sama)

    10   Faculty/Staff                    active    Fa0/11
    20   Students                         active    Fa0/18
    30   Guest(Default)                   active    Fa0/6
    88   Management                       active    
    99   Native                           active    

coba kita lihat di S1, Nah **G0/1** dan **G0/2** sebagai penghubung di tengah-tengah berada pada native VLAN atau di VLAN 1 (by default). 

![](/images/screenshot_2020-07-29_12-05-40.png)

untuk bisa nyambung kita setel trunknya dulu

    S1(config)#int range g0/1-2
    S1(config-if-range)#switchport mode trunk 

Setelah itu kita perlu merubah Native VLAN ke VLAN 99 sesuai tabel

    S1(config-if-range)#switchport trunk native vlan 99
    %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1 (99), with S2 GigabitEthernet0/1 (1).
    %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/2 (99), with S3 GigabitEthernet0/2 (1).

dah. coba di ping PC1 ke PC 4

    C:\>ping 172.17.10.24
    
    Pinging 172.17.10.24 with 32 bytes of data:
    
    Reply from 172.17.10.24: bytes=32 time=1ms TTL=128
    Reply from 172.17.10.24: bytes=32 time<1ms TTL=128
    Reply from 172.17.10.24: bytes=32 time<1ms TTL=128

nah udah bisa.

Sedangkan pesan "Native VLAN mismatch ..." itu muncul karena

## Referensi

[https://www.webiptek.com/2019/10/native-vlan-cisco.html](https://www.webiptek.com/2019/10/native-vlan-cisco.html "https://www.webiptek.com/2019/10/native-vlan-cisco.html")