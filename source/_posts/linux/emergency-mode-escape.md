---
title : "Linux problem: Stuck in emergency mode"
date : "2018-10-03"
showDate: true
draft : false
toc: true
categories : linux
tags : 
- repair
---

## Titik masalah
Inti masalah ini, yaitu tidak bisa boot kembali ke hardisk karena itu tidak bisa masuk ke dalam sistem operasi seperti biasanya.

![emergency screen](https://res.cloudinary.com/bimagv/image/upload/v1603375351/2018-10/03%20linux%20problem%20stuck%20in%20emergency%20mode/emergency-mode-escape-01_lhsykp.jpg)

Sebab apa?

Berdasarkan masalah yang terjadi pada kasus saya ialah input/output error dan error mounting partisi ntfs Sehingga menyebabkan nomor UUID partisi jadi berubah.

Coba lihat nomor id dari partisi secara manual

kita bisa lihat adanya ketidaksesuaian yang terjadi pada **/etc/fstab**

Gunakan command **blkid** untuk melihat UUID partisi yang sekarang

Perhatikan pada code yang di highlight

![blkid dan /etc/fstab](https://res.cloudinary.com/bimagv/image/upload/v1603375355/2018-10/03%20linux%20problem%20stuck%20in%20emergency%20mode/emergency-mode-escape-02_p0ffxa.png)


## Pemecahan Masalah
Baca instruksi yang diberikan oleh sistem dulu. Mungkin yang tampil di monitor kawan2 berbeda masalah.

Nanti kita harus masuk ke dalam mode execution dan menjalankan **fsck** untuk merepair.

### Masuk mode eksekusi

![execution mode](https://res.cloudinary.com/bimagv/image/upload/v1603375347/2018-10/03%20linux%20problem%20stuck%20in%20emergency%20mode/emergency-mode-escape-03_oiqqlv.jpg)

Coba masukan perintahnya. supaya masuk ke dalam mode perintah atau eksekusi.

Tapi, dalam beberapa kasus inputan kita tidak ditanggapi sama sekali. Jadi mau tidak mau musti masuk dengan live cd atau usb bootable.

### Repair
Untuk menemukan lokasi partisi berada, bisa dengan **fdisk -l** seperti gambar dan karena berhubungan dengan file milik administrator (/etc) maka kita perlu menjalankannya dengan user root

![fdisk -l](https://res.cloudinary.com/bimagv/image/upload/v1603375345/2018-10/03%20linux%20problem%20stuck%20in%20emergency%20mode/emergency-mode-escape-04_dfodc4.png)

Setelah itu jalankan perintah fsck. Yang dibetulkan biasanya partisi root dan home. 

    # fsck.ext4 /dev/sda5
    # fsck.ext4 /dev/sda6

Terakhir jalankan

    # systemctl reboot

## Sumber
* [https://askubuntu.com...](https://askubuntu.com/questions/646414/welcome-to-emergency-mode-think-it-is-a-fsck-problem)
