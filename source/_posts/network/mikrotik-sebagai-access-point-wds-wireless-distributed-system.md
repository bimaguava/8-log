---
draft: true
comments: true
toc: true
title: MikroTik sebagai Access Point WDS (Wireless Distributed System)
date: 2020-08-19T20:18:00Z
updated: 
category:
- network
tags:
- mikrotik
keywords: []

---
# Contoh kasus

![](/images/screenshot-from-2020-08-20-15-19-52.png)

Seperti gambar diatas ada lebih dari satu AP yang nantinya akan memancarkan wireless dengan SSID yang sama.

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