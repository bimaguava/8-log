---
draft: true
comments: true
toc: true
title: 'Cisco: VLAN introduction'
date: 2020-07-26T17:00:00.000+00:00
updated: 2020-07-26T17:00:00.000+00:00
category:
- network
- itn
tags:
- cisco
keywords: []

---
**secara default, switch membagi collision domain dan router membagi broadcast domain**

tapi sekarang di switch PUN bisa menciptakan broadcast domain sendiri. Caranya dengan menggunakan/membuat VLAN.

## Collision Domain

ini merupakan sistem Ethernet tunggal dimana komponen-komponennya (kabel, hub, repeaters, dan station interface) merupakan bagian dari signal time domain yang sama.

![](/images/screenshot-from-2020-07-27-15-43-12.png)

## Broadcast Domain

Sesuai artinya "broadcast", yaitu menyebarkan paket ARP di dalam suatu jaringan dengan segmen yang sama (yang diluar segmen tidak akan dapat request ARP atau mendengarkan sinyal/ping dari segmen lain), switch akan meneruskan trafik broadcast melalui interfacenya ke suatu segmen network sebagaimana yang dilakukan router, Switch pun bisa melakukan BD yaitu dengan pakai Virtual LAN (VLAN).

Selain switch berikut beberapa perangkat terkait

![](/images/screenshot-from-2020-07-27-16-12-13.png)

Dengan memakai VLAN ini dampaknya switch dapat bisa tahu device mana yang berada pada satu segmen, karena dapat mengirim request ARP ke semua device dalam segmen network tertentu.

**_Q: "Apakah host dalam suatu vlan dapat berkomunikasi dengan vlan yang berbeda lainnya? host vlan 10 ingin ngobrol dengan vlan 20_**

**_A: Tidak bisa, untuk bisa berkomunikasi dengan VLAN yang berbeda maka akan membutuhkan sebuah Router ditengah2_**

## Memahami VLAN

VLAN pada switch itu ialah sebuah port virtual yang mana penggabungan/pengelompokan dari beberapa port.

![](/images/screenshot-from-2020-07-27-16-22-02.png)

Efeknya VLAN ini

* Faktor keamanan terjaga daripada orang-orang yang suka colok kabel sembarangan, karena tidak langsung konek.
* perkerjaan lebih terorganisir
* resiko broadcast storm, jika memang VLAN yang dibuat sangat2 besar.

## Gambaran konfig
| Fungsi                                             | Command                       |
|----------------------------------------------------|-------------------------------|
| port nomor satu dikasi buat VLAN 10                     | interface fa0/1               |
|                                                         | switchport access vlan10      |
| untuk mengasosiasikan port nomor 1 sampai 5 ke VLAN 10  | interface range f0/2-5        |
|                                                         | switchport access vlan 10     |
| untuk mengasosiasikan port yang tidak berurutan ke VLAN 10    | interface fa0/1, fa0/3, fa0/5 |
|                                                         | switchport access vlan 10     |
| menampilkan interface vlan                              | show vlan brief               |