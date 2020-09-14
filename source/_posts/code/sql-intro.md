---
title: SQL intro
toc: true
date: 2020-04-12 11:11:57
categories: 
- code
tags: 
- sql
---

Salah satu bahasa Query yang umum digunakan oleh data Scientist adalah SQL yang merupakan singkatan dari **Structure Query Language**.

SQL merupakan sebuah bahasa untuk berkomunikasi dengan data yang kita kenal dapat kita gunakan untuk menarik data dari sebuah database yang bertipe RDBMS. 


## Query

Query merupakan sebuah request atau permintaan akan informasi yang tersimpan di dalam database kita ibaratkan ketika memesan makanan di sebuah Kedai Kita bisa mengatakan **_"sambelnya sedikit aja ya"_**. Atau bahkan kita bisa meminta **_"makanan apa sih yang paling populer di kedai tersebut"_**.

## Mencari Data
Dalam **SQL** kita dapat menggunakan **SELECT** untuk mendapatkan satu data dari database.

    SELECT nama_kolom

Biasanya setiap database terdiri dari beberapa tabel. Karena inilah, kita harus menggunakan klausa **FROM** untuk memilih salah satu tabel tersebut. Dengan menggunakan **SELECT & FROM**, maka kita dapat secara spesifik memilih kolom tertentu dari tabel tertentu untuk diakses dan diolah.

    SELECT nama_kolom FROM nama_tabel;

Untuk "mengakhiri" statement **SQL**, berikan titik koma di akhir statement tersebut

## Mengambil Data dari beberapa kolom
Tentunya kita tidak semestinya mengakses beberapa kolom secara satu per satu. Jika Anda ingin mengambil data dari beberapa kolom, gunakan koma untuk memisahkan setiap nama kolom.

    SELECT nama, biaya

Jika Anda ingin mendapatkan data dari semua kolom dalam tabel, gunakan simbol *.

    SELECT * FROM nama_tabel

## RDBMS

RDMS merupakan singkatan dari relasional database management system. Dengan memakai syntax [[SQL]] dapat dipakai untuk memanipulasi data di ```RDBMS``` seperti 

*  CREATE atau menambah
*  READ atau membaca
*  UPDATE atau mengubah atau update dan
*  DELETE atau menghapus

Data dalam ```RDBMS``` disimpan sebagai sebuah table konsepnya mirip dengan tabel pada umumnya.