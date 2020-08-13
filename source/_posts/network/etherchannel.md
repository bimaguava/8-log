---
draft: true
comments: true
toc: true
title: 'Cisco: EtherChannel'
date: 2020-07-28T17:00:00.000+00:00
updated: 
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

_Dalam menghubungkan sebuah switch satu dengan yang lain kita mengenal `trunk,`_

Trunk-trunk pada EtherChannel berada pada status forwarding semua atau blocking semua, karena STP memperlakukan semua trunk pada EtherChannel sebagai 1 trunk.

Saat EtherChannel berada pada status forwarding, maka switch akan melakukan load-balance/membagi rata trafik pada semua trunk, sehingga bandwidth yang tersedia jadi lebih banyak.

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

## Cara men-Channel

* **Manual (Tanpa protokol dan negoisasi)**
* **PAGP (Port Aggregation Control Protocol)**, merupakan Cisco propietary yang memiliki fitur `auto-negotiate` yang membuat EtherChannel secara otomatis ketika PAGP diset.

  Berikut mode PAGP:

  ![](/images/pagp.png)
* **LACP (Link Aggregation Control Protocol)**, yakni merupakan protokol open standard yaitu IEEE dan digunakan untuk bertemu dengan switch merk lain.

  Berikut mode LACP:

  ![](/images/lacp.png)

## Etherchannel Guidelines and Restrictions

EtherChannel has some specific guidelines that must be followed in order to avoid configuration problems.

1) All Ethernet interfaces support EtherChannel up to a maximum of eight interfaces with no requirement that the interfaces be on the same interface module.

2) All interfaces within an EtherChannel must operate at the same speed and duplex.

3) EtherChannel links can function as either single VLAN access ports or as trunk links between switches.

4) All interfaces in a Layer 2 EtherChannel must be members of the same VLAN or be configured as trunks.

5) If configured as trunk links, Layer 2 EtherChannel must have the same native VLAN and have the same VLANs allowed on both switches connected to the trunk.

6) When configuring EtherChannel links, all interfaces should be shutdown prior to beginning the EtherChannel configuration. When configuration is complete, the links can be re-enabled.

7) After configuring the EtherChannel, verify that all interfaces are in the up/up state.

8) It is possible to configure an EtherChannel as static, or for it to use either PAgP or LACP to negotiate the EtherChannel connection. The determination of how an EtherChannel is setup is the value of the **channel-group** _number_ **mode** command. Valid values are:

**active** LACP is enabled unconditionally

**passive** LACP is enabled only if another LACP-capable device is connected.

**desirable** PAgP is enabled unconditionally

**auto** PAgP is enabled only if another PAgP-capable device is connected.

**on** EtherChannel is enabled, but without either LACP or PAgP.

9) LAN ports can form an EtherChannel using PAgP if the modes are compatible. Compatible PAgP modes are:

**desirable => desirable**

**desirable => auto**

If both interfaces are in **auto** mode, an Etherchannel cannot form.

10) LAN ports can form an EtherChannel using LACP if the modes are compatible. Compatible LACP modes are:

**active => active**

**active => passive**

If both interfaces are in **passive** mode, an EtherChannel cannot form using LACP.

11) Channel-group numbers are local to the individual switch. Although this activity uses the same Channel-group number on either end of the EtherChannel connection, it is not a requirement. Channel-group 1 (interface po1) on one switch can form an EtherChannel with Channel-group 5 (interface po5) on another switch.

## Referensi

* [https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html](https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html "https://www.cisco.com/c/en/us/support/docs/lan-switching/etherchannel/12023-4.html")
* [https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/](https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/ "https://belajarcomputernetwork.com/2012/12/13/etherchannel-2/")
* [https://www.youtube.com/watch?v=H9wFWP6KPCY](https://www.youtube.com/watch?v=H9wFWP6KPCY "https://www.youtube.com/watch?v=H9wFWP6KPCY")
* CCNA SRWE