---
draft: true
comments: true
toc: true
title: 'Cisco: Configure EtherChannel'
date: 2020-08-08T15:52:00Z
updated: 
category:
- network
tags:
- cisco
keywords: []

---
## Petunjuk mengkonfig EtherChannel

blabla

## Lab

![](/images/screenshot-from-2020-08-09-13-48-41.png)

Sebuah topologi dengan 3 switch telah berhubungan, dan disini kita punya sebuah case yaitu ada redundant uplink. Dan pada yang oren2 itu ialah [STP](https://8log.netlify.app/2020/08/08/network/cisco-spanning-tree-protocol-stp/ "STP"), yang mana itu tidak digunakan karena untuk mencegah looping terjadi karena broadcast yang terjadi sangat banyak.

Pada lab ini kita akan mengonfigurasi Port Aggregation Protocol (PAgP), protokol Cisco EtherChannel, dan Link Aggregation Control Protocol (LACP), versi standar terbuka IEEE 802.3ad dari EtherChannel.

## Istilah

* **Port Channel**, yaitu gabungan beberapa interface itu atau channel group tadi akan melahirkan sebuah ~~keturunan~~ interface baru

## Tabel Address

![](/images/screenshot-from-2020-08-09-13-49-38.png)

## 1. Configure Basic Switch Settings