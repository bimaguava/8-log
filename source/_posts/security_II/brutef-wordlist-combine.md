---
title: "Brutef Wordlist Combine"
date: 2020-03-04
categories : 
- security_II

tags : 
- bruteforce
- pentest-tools
---

Seperti yang kita tahu menggunakan teknik tebakan adalah suatu cara yang sangat tradisional untuk mencoba masuk kedalam sistem. 

Maka dari itu perlu tindakan komprehensif dalam melakukannya. Salah satu cara efektif dalam menjalankan teknik ini adalah memperhatikan daftar kata dan membuat sendiri kustom password. 

Hal itu dapat mengurangi lama proses bruteforce. Salah satu solusinya ialah **wordlister**

## wordlister

* digunakan untuk membuat kustom kombinasi kapitalisasi, permutasi, leetspeak yang digunakan untuk cracking password

## Instalasi

    wget https://raw.githubusercontent.com/4n4nk3/Wordlister/master/wordlister.py

## Penggunaan

Untuk menggunakan Wordlister, pertama-tama kita perlu file input yang berisi daftar kata sandi yang ingin kita buat permutasi dan potong-potong.

### Argumen 

* input = nama file teks yang berisi kata sandi
* perm = jumlah permutasi yang akan digabungkan pada baris yang sama
* min = panjang minimum kata sandi yang dihasilkan
* maks = panjang maksimum kata sandi yang dihasilkan

    python3 wordlister.py --input list.txt --perm 2 --min 6 --max 32

### Argumen opsional

* leet = akan mengubah huruf apa saja menjadi angka menggunakan leetspeak
* cap = Opsi kapitalisasi huruf kapital huruf pertama dari setiap kata sandi
* up = akan mengubah setiap huruf dalam kata menjadi huruf besar
* append = jika ingin menambahkan kata pada sisi belakang yang diberikan ke semua kata sandi
* prepend = jika ingin menambahkan kata pada sisi depan yang diberikan ke semua kata sandi

contoh:

    python3 wordlister.py --input list.txt --perm 2 --min 6 --max 32 --leet --cap --append 1969
    Iloveyou
    Iloveyou1969
    1l0v3y0u
    1l0v3y0u1969
    iloveyou
    Password
    Password1969
    iloveyou1969
    P455w0rd
    P455w0rd1969
    password

Atau mengarahkannya ke file text agar lebih efektif


    python3 wordlister.py --input list.txt --perm 2 --min 6 --max 32 --leet --cap --append 1969 > mywordlist.txt

## Pesan

Penyusunan wordlist semacam ini memiliki kekurangan, yaitu menggunakan cara yang belum efektif dalam melibatkan informasi tentang victim. Perlu otomatisasi dalam hal tersebut yang akan ada pada artikel berikutnya.

## Sumber
* https://null-byte.wonderhowto.com/how-to/use-wordlister-create-custom-password-combinations-for-cracking-0206006/