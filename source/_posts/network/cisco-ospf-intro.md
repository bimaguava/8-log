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

Gambar itu bisa diasosiasikan seperti dalam suatu perkampungan dalam suatu RW (Rukun Warga)

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

![](/images/artboard-1.png)

Backbone Area(juga salah satu standard area) biasa disebut Area 0.

> Masing-masing biasanya maksimal berjumlah 50 router per-area mengingat memang OSPF mengkonsumsi CPU yang lumayan tinggi

Backbone/Area 0 bertindak sebagai penghubung bagi area lain agar bisa terkoneksi.

Maka semua area yang terhubung ke Area 0 akan bisa saling ping. Dalam kata lain apabila Area 2 dan Area 1 ingin bisa terhubung maka harus melalui Area Backbone terlebih dahulu. Dan tidak boleh terhubung selain ke area selain area 0.

Jadi apabila ada Area 3 seperti gambar ini

![](/images/artboard-12.png)

Maka, akan ada sebuah link tambahan, bernama **Virtual-Link** yang merupakan **fitur OSPF agar area selain area 0 seakan-akan terhubung langsung ke area 0/backbone area.**

Sedangkan di gambar terdapat router2 yang berbatasan dengan area luar backbone, yaitu ada ASBR dan ABR

> **ABR** ialah router OSPF di area A yang berbatasan dengan area lain

Sedangkan **ASBR**

> router yang berlokasi di perbatasan dengan selain OSPF, tapi ke `external route` (EIGRP, RIP, Static,dll)

## Stub Area

"Stub" disini berarti sebuah area yang tidak ada sambungannya lagi.

* tidak menerima `external route`, router hanya mengirim melalui default route (0.0.0.0)
* tapi masih menerima `summary route`

## Totally Stubby Area

Sedangkan Totally Stubby Area, sebuah area yang hanya ada pada perangkat cisco saja yang mana tidak menerima `external route` dan `summary route`

## Not-So-Stubby-Area (NSSA)

Prinsipnya sama dengan **Stub Area**, tapi dibalik stub ada sambungannya lagi berupa routing protocol lain.

## Totally Stubby NSSA

Prinsipnya sama dengan **NSSA**, hanya saja cuma untuk default route saja.

# Tipe LSA di OSPF

Sebagai pelengkap untuk membahas tipe2 area pada OSPF tadi kita akan membahas juga sebuah paket bernama LSA untuk membuat sebuah database OSPF.

Misal ketika ada perubahan topologi maka router dalam jaringan OSPF akan mengirimkan LSU yang didalamnya terdapat informasi LSA yang mana LSA terdiri dari beberapa tipe:

## **LSA Type 1** **(Router LSA)**

berisi router ID dari router2 yang menjalankan OSPF

![](/images/lsa-type-1.png)

## **LSA Type 2** **(Network LSA)**

berisi network2 yang dibawa oleh router2 OSPF itu

![](/images/lsa-type-2.png)

## **LSA Type 3 (Summary LSA)**

berisi `Summary Route` yang biasanya ada pada router yang menghubungkan 2 area atau lebih (ABR)

![](/images/lsa-type-3.png)

Tidak seperti LSA Type 1 & 2 untuk LSA Type 3 ini akan di-advertise keluar area

## **LSA Type 4 (Summary ASBR LSA)**

berisi `Summary Route` external diluar OSPF yang biasanya ada pada ASBR

![](/images/lsatype-4.png)

LSA ini digunakan untuk mengirimkan informasi mengenai ASBR ke area yang lain yang mana ASBR ini nanti yang akan mengadvertise `Eksternal Route` (LSA Type 5).

> LSA Type 4 ini tidak di advertise langsung dan digunakan oleh ASBR dalam 'local' areanya, namun oleh ABR di setiap area dalam satu AS (Autonomous System) yang sama.

## **LSA Type 5 (Autonomous System/AS External LSA):**

berisi rute2 external yang biasanya ada pada ASBR

![](/images/lsatype-5.png)

LSA tipe 5 ini merupakan paket yang di-generate oleh ASBR untuk mengirimkan Redistribute-Route Eksternal ke jaringan OSPF dalam suatu AS number.

Metode yang digunakan untuk melakukan redistribute nantinya ada 2 cara yaitu E1 (as-type 1) dan E2 (as-type2).

> Eksternal Route ini merupakan informasi routing diluar jaringan AS OSPF, bisa BGP, RIP, OSPF, atau Satic route.

## **LSA Type 6 (Multicast OSPF LSA/Group Membership LSA)**

Merupakan `Cisco Proprietary`, LSA ini berisi serangkaian paket agar setiap area mempunyai jalur sendiri untuk mengirim paket secara serentak (multicast)

## **LSA Type 7 (NSSA-External LSA)**

Tipe LSA ini digunakan oleh area OSPF yaitu NSSA (Not So Stubby Area) supaya ketika ada redistribute-route eksternal dan melewati area yang tidak support LSA Type 5 tetap dapat berjalan dengan baik.

![](/images/lsatype-7.png)

Misal, dibanyak kasus ketika ada redistribute-route eksternal dan melewati area STUB, dimana di area ini LSA type 5 tidak didukung, maka kita bisa menggantinya dengan area NSSA.

## Contoh LSA di Area OSPF

Nah sekarang ada beberapa contoh proses kerja LSA dalam beberapa Area OSPF, sekedar untuk contoh saja.

### Standard Areas

![](/images/ospf_standard_area.jpg)

Di gambar kita lihat ada Area 0 dan ada juga di Area Standard yang membawa LSA tipe 1 dan 2 yang sedang flooding antara router di areanya (di "local" areanya)

Tipe 3 dan 5 menggambarkan proses peng-advertising LSA ke `internal route` (tipe 3) dan `external route` (tipe 5) yang sedang flooding di area backbone (Area 0) dan Standard Area.

Tipe 4 khusus LSA ini die meng-inject kepada backbone yang mana berasal dari router ASBR (R3) yang berguna untuk memastikan semua router lain dapat menjangkau ASBR.

### Stub Areas

![](/images/ospf_stub_area.jpg)

Di gambar itu kita 

### Totally Stubby Areas

![](/images/ospf_total_stub_area.jpg)

### Not-so Stubby Areas (NSSA)

![](/images/ospf_nssa.jpg)

# Terakhir, Masalah OSPF dalam multi network

Nah jika sebelumnya sudah dibahas teori dengan sesingkat-singkatnya alias simpel. Sekarang kita akan membahas

# Referensi

* [https://packetlife.net/blog/2008/jun/24/ospf-area-types/](https://packetlife.net/blog/2008/jun/24/ospf-area-types/ "https://packetlife.net/blog/2008/jun/24/ospf-area-types/")
* [https://belajarcomputernetwork.com/2012/06/05/ospf-open-shortest-path-first/](https://belajarcomputernetwork.com/2012/06/05/ospf-open-shortest-path-first/ "https://belajarcomputernetwork.com/2012/06/05/ospf-open-shortest-path-first/")
* [https://www.ccnablog.com/dynamic-routing-protocols/](https://www.ccnablog.com/dynamic-routing-protocols/ "https://www.ccnablog.com/dynamic-routing-protocols/")
* \[Mikrotik ID\](http://www.mikrotik.co.id/artikel_lihat.php?id=319#:\~:text=LSA%20Type%205%20(OSPF%20AS,%2C%20OSPF%2C%20atau%20Satic%20route.)