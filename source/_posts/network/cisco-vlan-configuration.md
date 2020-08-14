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

kalau belum tahu `access ports` saya akan kasih gambaran

![](/images/access_and_trunk_ports_explained-1024x461.jpg)

jadi disebut `access ports` karena merupakan sebuah port yang terhubung dengan host pada suatu vlan.

## Tabel Address

![](/images/screenshot_2020-08-14_09-58-42.png)

## 1. View the Default VLAN Configuration

### 1.A. Menampilkan default konfig Vlan 