---
draft: true
comments: true
toc: true
title: MikroTik membridgekan beberapa port
date: 2020-07-13T17:00:00Z
updated: 2020-07-13T17:00:00Z
category:
- network
tags: []
keywords: []

---
Sering kali setiap ingin colok kabel baru kita direpotkan untuk menambahkan konfigurasi pada mulai dari mengaktifkan interface ether sekian, sekian.

![](/images/2020-07-14_1.jpg)

Karena Router ia masing-masing port merupakan independen **tidak bisa colok ether sekian ke komputer langsung konek.** Yang saya inginkan adalah bukan port yang independen seperti itu. Maka saya membutuhkan bridge.

Efeknya menggunakan bridge ini (dalam contoh ini **Bridge-WAN** dan **Bridge-LAN**) adalah jelas lebih ke manajemen untuk bagi yang suka saja.

## Bridge-WAN

Untuk Bridge WAN misal kita inginkan pada beberapa port nanti tinggal tambahkan saja pada tab ports untuk ether yang baru ke bridge wan. Nah itu juga untuk meminimalisir  jika ada rule-rule lain yang musti merubah semuanya.

Contoh pertama bikin dulu Bridge-WAN di **Bridge>Bridge**

![](/images/screenshot_2020-07-14_2.png)

Kalau sudah, sekarang tinggal buka **Bridge>Tab Ports** lalu pilih ether1 dan pastinya disetel ke brige-wan. Jika ingin menambahkan ehter yang lain tinggal tambah lagi.

Maka saat memasukkan IP-nya nanti bukan lagi memilih ether1 tapi Bridge-WAN

(disini kebutuhan saya menggunakan DHCP)

![](/images/screenshot_2020-07-14_3.png)

## Bridge-LAN

LAN-nya juga ingin di bridge karena mungkin gak mau repot jikalau port 2 nya rusak, ingin pindah ke port lain maka rule atau konfigurasi yang sudah dibikin juga harus diganti terlebih dahulu. Caranya seperti tadi.

## Contoh

![](/images/screenshot_2020-07-14_5.png "Contoh")