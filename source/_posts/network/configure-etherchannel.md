---
draft: true
comments: true
toc: true
title: 'Cisco: Configure EtherChannel'
date: 2020-07-28T17:00:00.000+00:00
updated: 2020-07-28T17:00:00.000+00:00
category:
- network
tags:
- cisco
keywords: []

---
Waduh EtherChannel :)

![](/images/ccnaccnplinx-com-etherchannel-port-options00001.jpg)

Ether Channel ialah menggabungkan beberapa interface/link menjadi satu interface sehingga tidak adanya port yang di block, s

kenapa ada gabung2an seperti itu?

Karena dalam penggunaan FastEthernet maksimal kapasitas datanya 100Mbps, maka yang sering digunakan adalah menambah kabel untuk mengimbangi beban data.

Yang mana hal ini memungkinkan adanya pembagian beban trafik serta redundansi jika satu atau lebih link di dalam satu channel gagal.

dan juga load balancing..

> eh bukan... ternyata, itu berlaku untuk router, lupa. Mungkin nanti akan belajar lagi tentang bagaimana  ketika router mimiliki lebih dari satu link dengan nu berlaku untuk router, lupa. Mungkin nanti akan belajar lagi tentang bagaimailai AD yang sama maka router akan bisa menggunakan semua link itu dengan tujuan distribusi beban trafik pada dua atau lebih jalur/link itu yaitu trafik bisa lebih optimal.

nanti dah Kalok gak male..

## Istilah2

### port-channel

Gabungan beberapa interface atau bisa dikatakan channel group tadi akan menjadi interface baru

## Tipe Ether channel

### PAGP (Port Aggregation Control Protocol)

## Referensi

* [https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html](https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html "https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html")
* [https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/](https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/ "https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/")