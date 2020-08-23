---
draft: true
comments: true
toc: true
title: 'Cisco: OSPF intro'
date: 2020-08-22T16:48:00Z
updated: 
category:
- network
tags:
- cisco
keywords: []

---
# Preface

OSPF ialah sebuah [_Dynamic Routing Protocol_](https://www.ccnablog.com/dynamic-routing-protocols/) yang merupakan bagian dari `link state protocol`, yang dikenal dengan algoritma **shortest path first**-nya untuk menemukan jalur terbaik bagi router untuk sampai ke destinationnya yang sangat berguna untuk meminimalisir penggunaan bandwith terutama untuk network yang sudah sangat komplex.

Untuk lebih jelasnya silahkan baca dulu: [https://8log.js.org/2020/08/22/network/cisco-link-state-protocol/](https://8log.js.org/2020/08/22/network/cisco-link-state-protocol/ "https://8log.js.org/2020/08/22/network/cisco-link-state-protocol/")

# Serangkaian Paket yang dikirimkan OSPF

Dalam menemukan the best path-nya OSPF akan berurusan dengan sebuah paket-paket data yang dikirimkannya kepada ospf neighbor.

Apa saja? selengkapnya sebagai berikut.

## LSP (Link State Packet)

Ini adalah sebuah paket konvergensi yang dikirimkan router yang menjalankan routing ospf. Dan isi dari sebuah paket LSP ini sebagai berikut.

### 

## Hello Packet

# Proses pemilihan DR & BDR pada OSPF

# OSPF dalam Interior Gateway Protocol

Setelah selesai dengan definisi dan berbagai istilah dalam OSPF, kita musti tahu dimana posisi OSPF sebagai sebuah `routing protocol`.

**Untuk dapat dapat memahami dimana posisi OSPF perhatikan bagian merah-merah dibawah**

![](/images/070214_1740_dynamicrout2.png)

Bisa dilihat OSPF merupakan sebuah bagian dari `Interior Gateway Protocol` (IGP), yang mana IGP penyebutannya disandarkan kepada satu wilayah administratif yang disebut Autonomous System.

Autonomous System (AS) ini memiliki nomor layaknya Rukun Tetangga atau RT :v

![](/images/ic196634.gif)

Gambar itu bisa diasosiasikan seperti dalam suatu perkampungan dalam suatu RW wkwkwk.

Maka `Exterior Gateway Protocol` (EGP) layaknya sebuah RW yang mengorganisir beberapa RT didalamnya. Dalam hal ini posisi RT dicontohkan sebagai IGP.

Dan layaknya sebuah RT maka ia akan memiliki nomor. IGP juga sama, satu IGP hanya memiliki satu `AS number` sebagai identitas wilayahnya.

Selanjutnya, pada beberapa AS number atau beberapa RT pasti akan ada yang bertugas sebagai penghubung antara AS-AS number secara administratif maka ia disebut Exterior Gateway Protocol (EGP).

Oke..

lanjut..

# Tipe Area di OSPF