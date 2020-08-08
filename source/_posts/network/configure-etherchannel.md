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

## Ether Channel 

![](/images/ccnaccnplinx-com-etherchannel-port-options00001.jpg)

Ialah menggabungkan beberapa interface/link menjadi satu interface.

**Karena** dalam penggunaan FastEthernet maksimal kapasitas datanya 100Mbps, maka yang sering digunakan adalah menambah kabel untuk mengimbangi beban data.

Yang mana hal ini memungkinkan adanya pembagian beban trafik serta redundansi jika satu atau lebih link di dalam satu channel gagal.

> Jika disederhanakan maksud dari Etherchannel itu seperti load balancing, tapi dilakukan di switch yang seharusnya dilakukan di router

s

## Istilah2

### port-channel

Gabungan beberapa interface atau bisa dikatakan channel group tadi akan menjadi interface baru

## Tipe Ether channel

### PAGP (Port Aggregation Control Protocol)

## Referensi

* [https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html](https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html "https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html")
* [https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/](https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/ "https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/")