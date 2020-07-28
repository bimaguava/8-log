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

![emergency screen](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4hyHXzI-JcxCCPv6Na%2Femergency-mode-escape-01.jpg?alt=media&token=fcf1d853-6cf6-410a-a0d9-15c986bc5cca)

Sebab apa?

Berdasarkan masalah yang terjadi pada kasus saya ialah input/output error dan error mounting partisi ntfs Sehingga menyebabkan nomor UUID partisi jadi berubah.

Coba lihat nomor id dari partisi secara manual

kita bisa lihat adanya ketidaksesuaian yang terjadi pada **/etc/fstab**

Gunakan command **blkid** untuk melihat UUID partisi yang sekarang

Perhatikan pada code yang di highlight

![blkid dan /etc/fstab](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4hz0j9YhBYZSFlcRyw%2Femergency-mode-escape-02.png?alt=media&token=e0a2afb4-7605-4f0c-9056-1da85428602f)


## Pemecahan Masalah
Baca instruksi yang diberikan oleh sistem dulu. Mungkin yang tampil di monitor kawan2 berbeda masalah.

Nanti kita harus masuk ke dalam mode execution dan menjalankan **fsck** untuk merepair.

### Masuk mode eksekusi

![execution mode](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4hz8KsK_b0jVmbEBwc%2Femergency-mode-escape-03.jpg?alt=media&token=4d550da6-b139-4a86-820b-91408d75d3d3)

Coba masukan perintahnya. supaya masuk ke dalam mode perintah atau eksekusi.

Tapi, dalam beberapa kasus inputan kita tidak ditanggapi sama sekali. Jadi mau tidak mau musti masuk dengan live cd atau usb bootable.

### Repair
Untuk menemukan lokasi partisi berada, bisa dengan **fdisk -l** seperti gambar dan karena berhubungan dengan file milik administrator (/etc) maka kita perlu menjalankannya dengan user root

![fdisk -l](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4hzFKIQgcXlBcyUzkS%2Femergency-mode-escape-04.png?alt=media&token=dd5e0de0-0f47-4b2b-b248-792fe9b7b7c8)

Setelah itu jalankan perintah fsck. Yang dibetulkan biasanya partisi root dan home. 

    # fsck.ext4 /dev/sda5
    # fsck.ext4 /dev/sda6

Terakhir jalankan

    # systemctl reboot

## Sumber
* [https://askubuntu.com...](https://askubuntu.com/questions/646414/welcome-to-emergency-mode-think-it-is-a-fsck-problem)