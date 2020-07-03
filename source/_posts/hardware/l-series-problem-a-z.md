---
title: 'L Series: Problem A-Z'
toc: true
date: 2019-12-04 15:01:08
tags: 
- epson
- repair
categories: hardware
---
# Case 1. No Power

Kondisi dimana printer mati total. Walaupun sebenarnya tidak **total**.

Tapi yang harus dipahami yaitu proses pengecekannya mulai dari mana yang baik.

Ini dilakukan supaya kita tidak bingung dan membuang banyak waktu untuk satu printer saja.

## 🧐 Sebab apa?
langsung kita tunjuk ialah:

### Mainboard
kita bisa lakukan adalah dengan mengecek resistor dan dioda pada mainboard dengan menggunakan tester dengan indikasi:

Tidak buzzer = good
Bunyi buzzer = putus

![Menyambung/jumper pada F1](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4i-D2eX2pG2Q9ZJwXG%2Flseries-problem-az-01.png?alt=media&token=88255869-a74d-4b6b-9a45-9bb984bf3c54)

Info lain: 

* apakah phnya juga sort? Sebetulnya ini tidak menyebabkan no power, hanya saja bisa mengarah kesana apabila dilakukan pengecekan

* ph yang sort dapat mengakibatkan mainboard short juga. yaitu pada bagian fusenya putus \(maka harus di jumper\) atau beberapa masalah pernah terjadi karena koil \(lilitan/spul\) pada ph terputus dan terbakar, sampai berefek balik pada IC pada mainboard.

### Power supply
Posisinya ada dibagian bawah badan printer. Kalau penyebabnya mati bisa karena korosi, elco ataupun diodanya mati.

### Panel depan 
Kebanyakan yang terjadi adalah tombol power pada panel perlu di repair karena sudah mulai renta. Bisa di repair dengan cairan WD.


# Case 2. General Error

General Error dapat diartikan masalah/error yang terjadi secara umum bisa karena apa saja.

Pada problem General Error maka kita akan mengecek keseluruhan masalah.

## 🧐 Sebab apa?

### 📌 Berkaitan dengan kerusakan kecil

Contoh indikasi masalah di mesin **L3110, L360**

* disk encoder baret, terkena gesekan oleh tulang besi printer

* head cable gosong, rusak/robek (bisa terjadi karena head bermasalah atau sort)

### 📌 System failure + Human eror

* PH sort (tidak bisa dipakai lagi)

Indikasinya bisa dilihat pada lampu indikator yang merah dan kuning, dua-duanya berkedip bersamaan

* Fuse mainboard putus (masih bisa di jumper) tergantung sebab masalahnya yang tidak berhubungan dengan part inti salah satunya print head

### 📌 Lain-lain

* Pemasangan part yang kurang presisi \(check all\)


# Case 3. Print Quality

## Indikasi

Problem ini merupakan masalah pada hasil cetak yang ditandai dengan:
* nozelnya bending ataupun tidak sempurna
* hasil test page, warna huruf bergaris
* hasil cetak gambar atau objek kurang maksimal walaupun dengan settingan kertas Epson mate
* huruf tercetak tebal sekali, kurang bagus dilihat. Atau sebaliknya, tipis sekali
* sasil cetak untuk tabel excel tidak lurus, atau kurang hurufnya kurang presisi
* dan lain sebagainya

## 🧐 Dilihat dari ...

### Nozel jelek

* **Pertama**, yang banyak terjadi adalah pada bagian adapter, tinta dalam adapter mulai kosong. Harus disedot menggunakan spet sampai adapter penuh terisi tinta

Tindakan salah ❌ :

Melakukan **Head Cleaning** \(pembersihan head biasa\), terus-menerus. Bahkan **Power Cleaning** \(setara 3x head cleaning\) tanpa mengetahui kadar kepenuhan tinta pada adapter. Dengan begitu hasil yang didapat adalah tinta di tengki anda terbuang sia-sia tanpa mendapatkan hasil nozel sempurna.



**Q**: _*"sudah disedot kok, keluar terus gelembung udara dari mulut adapter ?"*_s

**A**: _*"Kemungkinan terdapat perputaran udara di dalam. Jadi harus di sedot habis dulu tinta di tengkinya, kemudian isi tinta lagi. Kalau masih dapat masalah yang sama, mungkin bisa ganti adapternya karena sudah jelek. Opsi lain adalah ganti ink system."*_s

* **Kedua**, jika cara pertama ternyata kurang maksimal, anda me-refurbish, membersihkan head dengan cairan pembersih head.

Cairan tidak boleh mengenai bagian sensitif print head. Jika salah melakukan hal init bisa sort maka phnya tidak bisa digunakan kembali karena akan merusak part yang lain seperti mainboard.

### Hasil blank

* Selang mampet, sebab jika selang mampet atau kadang terjepit printer bisa tidak mengeluarkan tinta. 

    Maka periksa selang dari head menuju tengki terjepit atau ada masalah juga cek selang bagian ink system, apakah ada yang terjepit. 

    Biasanya saat pemasangan ink system baru karena mungkin terburu-buru atau kurang teliti selang bagian bawah ink system terjepit dengan frame printer.

* Fuse pada mainboardnya putus, musti di jumper

    Hal ini bisa disebabkan karena PH si printernya telah sort. Pada kondisi ini PH tidak bisa digunakan lagi. Tapi mainboardnya masih bisa di repair (kalau tidak ikutan sort)

    Hasil pun cuma tinta amburadul yang keluar 

![hasil print ph yang sort](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4i083eYYmZOR5RI1Od%2Flseries-problem-az-02.png?alt=media&token=4c017833-6e56-46a5-80dd-66d505b79b74)

Kalau itu merupakan indikasi head yang sort dan kemungkinan yang kedua adalah kabel head sudah rusak.

### Print via ADF bergaris

**Q**: _"Print ADF bergaris?"_

![bercak garis](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4i0Fz59nw9Nd6Z7Khb%2Flseries-problem-az-03.png?alt=media&token=2e3580f3-5278-4a10-adce-33f51b4ba234)

**A**: _"bersihkan tulang bagian \(abu-abu\) dalam scanner"_

## Finishing problem

dalam menyelesaikan Print Quality:

1. Cari titik masalahnya, untuk masalah PQ masih bisa dengan mudah untuk dianalisa
2. Menyelesaikan masalah dengan rapih, apabila mengganti head baru, jangan lupa **input ID head** di Adjustment Portal
3. Kalau masalah sudah teratasi selesaikan dengan mereset inkpad conter **Waste Inkpad Counter**
4. Cek tempat pembuangan atau inkpad, kalau sudah penuh diganti


# Case 4. Paper Jam

## Repair berdasarkan jenis dan tipe

Hal yang harus diketahui dalam penganalisaan masalah paper jam adalah melihat dari sudut pandang mana kita merepair.

Secara umum, paper jam masalahnya adalah sama

* kertas yang tidak keluar
* keluar tapi stop ditengah
* Kertas keluar tapi hanya lewat \(ngelost\)

Tapi dalam penerapannya pasti akan berbeda, sesuai jenis printernya. Dibedakan menjadi:

* Tipe L360, L3110, dll \(standar\)
* Tipe L1300 \(mid end/tipe panjang\)
* Tipe L1455 \(mid end\)

Jenis diatas memiliki fitur dan mesin yang proses berjalannya tidak sama. Karena spare part yang dipakai pun ada sedikit perbedaan.

Maka disarankan untuk dapat melihat list sparepart pada dealer Epson atau spi.

### Tipe standar: keluarga L360, L3110, dll

#### kertas tidak keluar

Secara menebak-nebak, kita sudah bisa menyimpulkan apabila kertas tidak keluar pasti ada yang bermasalah dengan bagian rollernya.

Kemungkinannya:

1. **Ada benda yang tersangkut**
    seperti sisa kertas sobek, struk belanja, kacang atau bekas makanan, pulpen/pensil :v

2. **spring jatuh**
    Salah satu spring yang ada pada printer jatuh atau terlepas karena seuatu hal. Karena springnya lepas jadi si roller tidak bergerak sebagaimana mesti si spur gear dan gear2 lain bergerak

3. **Karet roller sudah cekung**
    Kalau ini adalah faktor lama pemakaian. Karena rollernya cekung jadi saat roller berputar tidak mengenai kertas, sehingga kertas masih diam ditempat.

    Cara repairnya tinggal buka karet rollernya, tambahkan double tip atau semacamnya untuk mempadatkan area karet roller tanpa menggantinya dengan yang baru.

4. **Cek part bagian bawah printer, namanya lupa :v. Ada sebuah shaf roller, tapi kecil :v.**

    Pada bagian itu cek karet rollernya, masih cembung tidak dan besi atau kawat pengaitnya apakah ada kawat besi \(pengunci\) yang menonjol, biasanya di potong. 
    
    Paling mudah bisa di cek dengan memutar rollernya, kalau bisa berputar kebelakang sudah pasti part itu bermasalah

#### keluar, stop ditengah

* **Pertama**, kalau proses keluarnya kertas seperti terhambat sesuatu, berarti itu adanya benda yang menahan proses keluarnya kertas

* **Kedua**, kalau proses keluarnya kertas sempurna, tapi secara tiba-tiba berhenti dengan tidak wajar. 

    Kemungkinan yang bermasalah adalah mainboardnya karena proses print bekerja, membaca perintah dari user \(kita\), dan disambungkan berupa perintah eksekusi dengan task sekian printer mulai print. 
    
    Disitu yang bertindak sebagai otak dari eksekusi adalah mainboard. Jika keluaran bermasalah seperti ini dengan tidak wajar, sudah bisa dipastikan mainboard mengalami masalah.

#### keluar, hanya lewat

Kalau masalah ini adalah berkaitan dengan perputaran gear pada printer, bukan pada tawuran :v. Yang masih terpikir oleh ingatan saya adalah spur gear, geriginya banyak yang ompong @L3110.

#### finishing problem

Secara keseluruhan, semua penganalisaan adalah tentang ketelitian seorang teknisi. Satu langkah terlewat atau kurang teliti bisa membuat bingung dan frustasi. Sampai-sampai mengganti part yang tidak perlu diganti.

Pada Paper Jam, bisa juga disebabkan oleh masalah yang berkaitan dengan sistem, seperti setelan kertas contohnya.

### Tipe mid end: keluarga L1300

**Q**: _"L1300 kertas ngelost?"_

**A**: _"Dapat terjadi karena roller sudah mulai cekung, buka karet roller dan menambahkan beberapa lilitan double tip._

![karet roller L1300](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4i0Mdh8joDpX3TJLKC%2Flseries-problem-az-04.png?alt=media&token=5471c19d-1090-4745-8e24-6eb3b2b8ba78)

_Lalu, settingan roller besi terlalu renggang, bisa menurunkan posisi baut besi roller agar mendapatkan perputaran roller yang lebih presisi_

![setelan baut L1300](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4i0Wk-nmnoZN-CkMYP%2Flseries-problem-az-05.png?alt=media&token=7201b342-5a5c-4b3b-97eb-fdb111667dea)

_Atau secara sistem karena setelan kertas belum di setel ke kertas yang di load misal A3. Namun yang harus dicatat adalah problem PJ yang berhubungan dengan L1300 ada kalanya ASFnya diganti."_


# Case 5. Full Counter

Saat dimana perhitungan kadar tinta secara software atau secara sistem.

## 🧐 Tandanya?

![tanda full counter](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4i0i5kx_wGWn4EFkdi%2Flseries-problem-az-06.png?alt=media&token=71ac3841-8a0d-486d-84b4-d3661d2d8f2e)
Lampu indikator dengan simbol segitiga merah menyala terus menerus (tanpa berkedip)

## Solusinya
Direset atau **Waste ink pad counter**. Tentunya dengan menggunakan Adjustment Portal, atau software resetter lainnya.


# Case 6. Intermitten power

tripping ditandai dengan berkedipnya kedua led dengan cepat. Solusinya lakukan initial setting atau repair part yang rusak pada mainboard.