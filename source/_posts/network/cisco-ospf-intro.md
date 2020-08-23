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

Sebagai protokol link state OSPF merupakan bentukan dari sebuah metode TCP/IP yang akan sangat bergantung pada IP, akibatnya apabila dalam implementasi ingin berganti versi IP misal dari IPv4 ke IPv6, maka akan ganti OSPF pula dengan OSPF IPv6.

# Link State Packet (LSP): Paket yang dikirimkan OSPF

Dalam menemukan the best path-nya OSPF akan berurusan dengan sebuah paket-paket data yang dikirimkannya kepada `ospf neighbor`.

`LSP` Ini adalah sebuah paket konvergensi yang dikirimkan router yang menjalankan routing ospf.

**Dan isi dari sebuah paket LSP ini ada:**

* Hello packet
* Database Description (DBD) **tidak dibahas**
* Link State Request (LSR) **tidak dibahas**
* Link State Update (LSU) **tidak dibahas**
* Link State Acknowledgement (LSAck) **tidak dibahas**

Karena saya lagi pusing, jadi cuma bahas yang menurut saya penting gampang saja.

oke.

lanjut.

## Hello packet

Sebuah paket yang digunakan untuk:

* Men-discover `ospf neighbor`
* Dan juga meng-advertise router yang ingin dijadikan `ospf neighbor`
* Lalu, dalam Hello Packet juga mengirimkan `router ID` ini dikonfigurasi yang mana merupakan sebuah identitas dari sebuah router.

  > **jika router-id tidak dikonfigurasi**, maka router memilih alamat IP tertinggi dari salah satu interface loopback-nya alias interface bayangan
* Selain itu Hello Pakcet ini juga akan memilih sebuah `Designated Router` (DR) alias router dengan spek tinggi dan `Backup Designated Router` (BDR) alias sebuah backup jika DR-nya down. Prosesnya nanti akan dijelaskan.

> Ingat, DR dan BDR akan diperlukan hanya pada `network Multi Access`, untuk `network Non-Broadcast` tidak perlu

Kan Hello Packet ini yang akan menentukan 2 router yang nanti bisa menjadi tetangganya (neighbor adjacency) atau tidak, **maka harus memenuhi syarat** Hello packet terlebih dahulu, yaitu ...

dengan memastikan dalam 10 detik (pada network multi access) atau 30 detik (pada `Non-Broadcast Multiple-Access`/NBMA) router tersebut musti menerima paket hello yang telah dikirim untuk bisa dianggap sebagai neighbor adjacency.

_Dalam proses tersebut dikenal dengan istilah **Hello interval** dan **Dead interval**_

> yang bertugas menentukan seberapa sering kita mengirim paket halo ialah **Hello Interval**

Sedangkan,

> yang menentukan berapa lama kita harus menunggu paket hello sebelum kita menyatakan tetangga mati ialah **Dead Interval**

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

# Tipe Network di OSPF

Dalam OSPF ada 5 tipe network, yaitu

* **Point-to-point**
* **Point-to-multipoint**
* **Broadcast Multi Access**
* **Virtual links**
* **Non-broadcast Multiaccess (NBMA)**

Tapi untuk sekarang kita hanya perlu mengetahui `point-to-point` dan `broadcast-multiaccess` saja.

Untuk yang belum tahu perbedaan point-to-point dan multi Access, berikut contoh simpelnya

![](/images/unnamed.png)

Dilihat dari gambar setiap physical dalam topologi point-to-point linknya hanya untuk single destination saja

![](/images/download.png)

Sedangkan physical link dalam topologi Multi Access dapat berkomunikasi ke lebih dari satu destination, alias dalam 1 router bisa diakses dari beberapa router.

**Lalu, Apa yang dimaksud dengan broadcast dan non-broadcast?**

Contoh proses **broadcast**

![](/images/broadcast-1.jpg)

Dikatakan broadcast karena di gambar fitur switch memang menyediakan fungsi broadcast yang menyebabkan semua router (R2,R3,R4) menerima paket yang dikirim dari R1.

Contoh **non-broadcast** 

![](/images/non-broadcast.jpg)

Sedangkan pada gambar ini merupakan switch frame relay, kita tahu di switch frame relay tidak ada fitur broadcast. Makanya di gambar tanda hijaunya (paket) cuma menuju satu router (R2)

**Tipe2 network** yang koneksi OSPFnya melalui switch frame relay itu seperti Point-to-Multipoint, Broadcast Multiaccess, dan NBMA. 

# Tipe Area di OSPF

## **Standard Area/Normal Area**

area lain selain area 0

## **Backbone Area**

biasa disebut Area 0, semua area yang terhubung ke Area 0 akan bisa saling ping, Backbone juga salah satu standard area

* **Stub Area**

  Normal area yang tidak ada “sambungan”nya lagi
* **Totally Stubby Area**
* **Not-So-Stubby-Area (NSSA)**
* **Totally Stubby NSSA**

# Terakhir, Masalah OSPF dalam multi network

Nah jika sebelumnya sudah dibahas teori dengan sesingkat-singkatnya alias simpel. Sekarang kita akan membahas 

# Referensi

* [https://www.ccnablog.com/ospf-part-iv/](https://www.ccnablog.com/ospf-part-iv/ "https://www.ccnablog.com/ospf-part-iv/")
* [https://belajarcomputernetwork.com/2012/06/05/ospf-open-shortest-path-first/](https://belajarcomputernetwork.com/2012/06/05/ospf-open-shortest-path-first/ "https://belajarcomputernetwork.com/2012/06/05/ospf-open-shortest-path-first/")
* [https://www.ccnablog.com/dynamic-routing-protocols/](https://www.ccnablog.com/dynamic-routing-protocols/ "https://www.ccnablog.com/dynamic-routing-protocols/")
* [https://packetlife.net/blog/2008/jun/19/ospf-network-types/](https://packetlife.net/blog/2008/jun/19/ospf-network-types/ "https://packetlife.net/blog/2008/jun/19/ospf-network-types/")