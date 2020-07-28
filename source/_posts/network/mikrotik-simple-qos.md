---
title: "MikroTik: Simple QOS"
toc: true
date: 2019-08-30 22:13:32
tags: mikrotik
categories: network
---

Dalam melimit kita bisa limit secara keseluruhan, yaitu jumlah max up dan down (ada di tab Total)  

Atau dengan menentukan max upload dan download dengan keinginan kita. Dan rule paling atas merupakan yang diprioritaskan oleh router.   

Dasarnya sangat simpel, kita hanya perlu buat queue baru, dan set targetnya 

* Per ip 
* Per subnet 
* Per interface 
* Beberapa ip 
* Atau mau dicampur dalam satu rule-nya 

Tapi, ini adalah pembagian secara total max limitnya. Jadi ini jumlahnya 

Bukan untuk masing-masing titiknya 

* Dari ip sekian sampai ip sekian 
* Dll 

Dan limitasi bandwith ini dilihat dari sudut pandang clientnya, kalau disetel up 5M down 5M  

Maka itulah yang ia dapatkan. Bukan dari sudut pandang routernya. 

## lainnya dalam simple queue
* Melimit berdasarkan hari 
* Burst 
* Packet Marks, melimit tcp port tertentu (ada di tab Advanced) 

## Tambahan
Untuk HTB Kurang optimal, lebih bagus menggunakan queue tree atau bisa juga dengan menambahkan opsi parent dan child di simple queue.  

Walaupun begitu, simple queue sangat powerfull juga, apalagi kalau menggunakan router yang multicore, CCR misalnya. Transmisi pendistribusian bandwith untuk core yang banyak akan sangat cepat, tapi kalau akhirnya memakai parent perhitungannya tentu akan berbeda karena akan mempengaruhi kecepatan dari pembagian bandwith yang dilakukan simple queue. 