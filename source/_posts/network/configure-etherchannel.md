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

## Ether Channel itu...

![](/images/ccnaccnplinx-com-etherchannel-port-options00001.jpg)

Ialah menggabungkan beberapa interface/link menjadi satu interface. Maka di EtherChannel kita buat ada 2 kabel tapi seakan2 jadi satu kabel.

Dan gabungan beberapa interface itu atau channel group tadi akan melahirkan sebuah ~~keturunan~~ interface baru yang dinamakan `port-channel`

### _"Apa cuma bisa 2 kabel?"_

Penggabungan kabel bisa dibuat 2, 4 sampai 8 kabel tergantung kebutuhan.

Jadi, 2 kabel tersebut digunakan apabila data trafik yang keluar melebihi dari kapasitas maksimal dari sebuah kabel.

**Karena** dalam penggunaan FastEthernet maksimal kapasitas datanya 100Mbps, maka yang sering digunakan adalah menambah kabel untuk mengimbangi beban data.

Atau mungkin sebaiknya bisa juga menggunakan GigabitEthernet (1000Mbps/1Gbps)

## Manfaat lain

Kalau tadi adalah tentang bagaimana kita bisa mengupgrade resource trafik,

di dunia **_"Perbandwith-an"_** ini memungkinkan adanya pembagian beban trafik serta redundansi jika satu atau lebih link di dalam satu channel gagal. 

Silahkan baca: [Spanning tree](https://8log.netlify.app/2020/08/08/network/cisco-spanning-tree-protocol-stp/ "Spanning tree"), BPDUGuard

> Secara sederhana Etherchannel itu seperti load balancing, tapi dilakukan di switch yang seharusnya dilakukan di router

## Tipe Ether channel

### PAGP (Port Aggregation Control Protocol)

## Referensi

* [https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html](https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html "https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html")
* [https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/](https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/ "https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/")