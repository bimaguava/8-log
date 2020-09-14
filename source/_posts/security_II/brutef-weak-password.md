---
title: "Brutef Weak Password"
date: 2020-03-04
categories : 
- security_II

tags : 
- bruteforce
- pentest-tools
---

VK , μTorrent , dan ClixSense semua mengalami pelanggaran data besar di beberapa titik di masa lalu. Basis data kata sandi yang bocor dari situs tersebut dan situs daring lainnya dapat digunakan untuk lebih memahami bagaimana kata sandi manusia dibuat dan meningkatkan keberhasilan peretas saat melakukan serangan brute-force.

contoh data kata sandi yang sudah di dump:

* https://haveibeenpwned.com/Passwords
* https://github.com/xajkep/wordlists

contoh top password dari kasus 1.4 Billion Plain-Text Credentials Leaked (2017)

* artikel: https://medium.com/4iqdelvedeep/1-4-billion-clear-text-credentials-discovered-in-a-single-database-3131d0a1ae14
* repositori: https://github.com/philipperemy/tensorflow-1.4-billion-password-analysis
* demonstrasi: https://youtu.be/TXf40iTMm0E

Tentunya dari sana kita bisa mempelajari bagaimana orang membuat password yang dapat kita gunakan untuk bahan wordlist.

Dari sana kita belajar bahwa daftar kata yang beratus GB dan komprehensif bukan satu hal yang utama. Karena kita nanti akan mengetahui bahwa daftar kata yang kecil, tepat sasaran, dan disetel dengan baik biasanya menyelesaikan pekerjaan dengan baik.

## Topik utama
Dilihat dari sudut pandang offensive

* pengolahan kata sandi yang sudah dikumpulkan diperlukan untuk penyusunan wordlist yang tepat sesuai dengan tempat dan kasusnya. Salah satu caran analisa kata sandi yang banyak tersebut dengan [pipal](https://github.com/digininja/pipal.git)

## Pipal

* penganalisis kata sandi pada website yang menyususn statistik daftar kata sandi
* mengidentifikasi angka paling umum yang ditambahkan pada kata sandi mulai panjang kata sampai kata sandi yang paling umum ditemukan

### Instalasi

	git clone https://github.com/digininja/pipal.git

### Menu

	ruby pipal.rb --h
	pipal 3.1 Robin Wood (robin@digi.ninja) (http://digi.ninja)

	Usage: pipal [OPTION] ... FILENAME
		--help, -h, -?: show help
		--top, -t X: show the top X results (default 10)
		--output, -o <filename>: output to file
		--gkey <Google Maps API key>: to allow zip code lookups (optional)
		--list-checkers: Show the available checkers and which are enabled
		--verbose, -v: Verbose

		FILENAME: The file to count

### Argumen

* list-checkers = modul yang digunakan untuk menyebutkan istilah keagamaan yang populer, eksplisit, warna kendaraan, dan banyak lagi. Semakin banyak modul yang digunakan maka akan semakin lama proses selesai
* top = menampilkan statistik paling umum (default 10)
* output = digunakan untuk menentukan file tempat analisis disimpan

### Penggunaan

secara basic Pipal akan menganalisis daftar kata sandi dan menampilkan banyak informasi berguna menggunakan modul basic.rb (Basic_Checker). Namun, untuk meningkatkan kemampuan analisis Pipal, salin modul yang diinginkan dari direktori **checkers_available** ke direktori **checkers_enabled**

Coba untuk menghubungkan modul berawalan "EN_" (Bahasa indonesia tidak tersedia)

ln -s /checkers_available/EN_* checkers_enabled

Cara penggunaanya simpel

ruby pipal.rb --top 500 --output output-file/yahoo.pipal data-file/password.list

Contoh hasil:

https://github.com/tokyoneon/1wordlist

## Pesan

pengolahan kata sandi pada masing-masing regional tentu akan berbeda. Maka artikel berikutnya akan langsung beranjak ke penyusunan wordlist yang berdasarkan semua hal yang berasal dari sumber yang terarah.