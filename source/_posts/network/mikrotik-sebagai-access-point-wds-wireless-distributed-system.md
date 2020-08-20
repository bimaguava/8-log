---
draft: true
comments: true
toc: true
title: MikroTik sebagai Access Point WDS (Wireless Distributed System) dengan setelan
  roaming
date: 2020-08-19T20:18:00Z
updated: 
category:
- network
tags:
- mikrotik
keywords: []

---
# Contoh kasus

![](/images/untitled-document-copy.jpg)

Seperti gambar diatas 2 router mikrotik yang nantinya akan melakukan point to point, kalau [sebelumnya](https://8log.js.org/2020/08/19/network/mikrotik-sebagai-repeater/ "sebelumnya") menggunakan Access Point selain mikrotik pada contoh kali ini akan menggunakan mikrotik, sehingga nanti akan menggunakan mode yang bernama `station-bridge`.

**Akibatnya** Client bisa terkoneksi ke AP melalui AP manapun disana, tergantung jangkauan sinyal dari salah satu AP mana yang menjangkau client alias yang terdekat disisi client.

Ketika client berpindah lokasi dan terputus dengan salah satu access point, client akan secara otomastis berpindah ke access point lain yang menjangkau client tersebut.

# WDS VS Repeater

### AP Wireless Distributed System

Memiliki tujuan yang sama, yaitu untuk memperluas jangkauan jaringan

### AP Repeater

## Fitur MikroTik

**Wireless Repeater**

**WDS Slave**

# Referensi

* [MikroTik ID](http://www.mikrotik.co.id/artikel_lihat.php?id=47#:\~:text=Mode%20WDS-Slave,menggunakan%201%20card%20wireless%20card. "MikroTIk ID")