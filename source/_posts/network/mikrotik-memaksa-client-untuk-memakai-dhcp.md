---
title: MikroTik Memaksa Client Untuk Memakai DHCP
toc: true
date: 2019-08-30 21:51:19
tags: mikrotik
categories: network
---

Kadang kita ingin membatasi penggunaan ip misal untuk 10.10.10.2 s/d 10.10.10.5 untuk kepentingan keamanan. Jadi apabila user ingin memakai statik dalam rentang ip diatas atau diatasnya dari host 20-254, maka tidak akan tersambung ke router. 

Caranya hanya dengan mengaktifkan 'Add ARP for leases'  

    IP>DHCP Server>Nama DHCP Server 

Dan pada interface yang bersangkutan ```Interfaces>Ethernet>ether berapa>``` Menu ARP dijadikan reply-only