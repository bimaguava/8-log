---
draft: true
comments: true
toc: true
title: 'Cisco: VLAN Configuration'
date: 2020-08-14T02:00:00Z
updated: 
category:
- network
tags:
- cisco
keywords: []

---
## Petunjunk

## Lab

Download: [https://drive.google.com/file/d/1RAV7lIylasbCADRXCa_gJw-CmdIR9nio/view](https://drive.google.com/file/d/1RAV7lIylasbCADRXCa_gJw-CmdIR9nio/view "https://drive.google.com/file/d/1RAV7lIylasbCADRXCa_gJw-CmdIR9nio/view")

![](/images/screenshot_2020-08-14_09-57-50.png)

VLAN sangat membantu dalam administrasi logical groups yang memungkinkan member dari grup (hosts e.g: pc, laptop) untuk dengan mudah dipindahkan, diubah, atau ditambahkan. 

Pada materi ini akan fokus pada 

* pembuatan,
* penamaan VLAN
* dan menetapkan `access ports` ke suatu VLAN

kalau belum tahu `access ports` saya akan kasih gambaran berikut, garis biru2 yang menuju ke pada hostsnya

![](/images/access_and_trunk_ports_explained-1024x461.jpg)

jadi disebut `access ports` karena merupakan sebuah port yang terhubung dengan host pada suatu vlan. 

Lanjut.

## Tabel Address

![](/images/screenshot_2020-08-14_09-58-42.png)

## 1. View the Default VLAN Configuration

### 1.A. Menampilkan default konfig Vlan 

ingat kalau ingin memasukkan perintah verification kita musti berada dulu di priviliged exec mode

    S1>enable 
    S1#show vlan brief 
    
    VLAN Name                             Status    Ports
    ---- -------------------------------- --------- -------------------------------
    1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                    Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                                    Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                                    Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                                    Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                    Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                                    Gig0/1, Gig0/2
    1002 fddi-default                     active    
    1003 token-ring-default               active    
    1004 fddinet-default                  active    
    1005 trnet-default                    active    

Disitu semua interface dari Fa0/1-24, Gig0/1-2 by default berada pada VLAN 1.

Dan juga kita menemukan VLAN yang lain yaitu VLAN 1002, 1003, 1004, dan 1005 yang mana kita tidak usah pikirkan dulu untuk saat ini. 

## 1.B. Cek konektivitas PC di jaringan yang sama