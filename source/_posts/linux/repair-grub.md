---
title : "Repair GRUB"
date : "2018-10-04"
showDate: true
toc: true
categories : linux
tags : repair
---

## Gambaran Masalah
Kesalahan kali ini berada di sisi user atau istilahnya *human error*. Karena komputer itu sifatnya diperintah, masalah yang banyak terjadi (sebagai user Linux) sebetulnya manusianya :v bukan sistemnya.

Uraian ini sebetulnya gak penting sih, semua akan tahu setelah mencoba sendiri :v

1. **Windows dan Linux**: install windows dulu jika tidak ada sistem operasi di komputer. Jangan Linux dulu. Karena Boot record Windows tidak bisa membuat menu dualboot seperti yang di lakukan Linux. Setelah itu baru buat usb bootable dan pilih opsi *Install Linux alongside Windows*

2. **Windows dan Windows yang lain**: buat partisi baru dengan resize partisi yang digunakan dalam Windows dan buat partisi baru untuk digunakan sebagai Windows yang lain. Boot ke installer Windows dan pilih partisi yang tadi dibuat

3. **Linux dan Linux yang lain**: karena pembuatan partisi baru harus di unmount terlebih dahulu, jadi untuk resize partisi bisa dilakukan saat installer linux yang lain dijalankan

4. **Mac OS X dan Windows**: untuk masuk bisa menjalankan installer Windows pengguna MAC hanya perlu menggunakan aplikasi bawaan, ```BootCamp```

5. **MAC OS X dan Linux**: wajib menggunakan boot manager dari luar seperti ```rEFInd```. Setelah itu baru menyediakan partisi, lalu masukkan file iso kedalam boot menu menggunakan ```hdiutil```

Kesimpulannya,

instalasi Windows sesudah Linux cara itu salah, kenapa?

karena tidak memungkinkan untuk sistem Windows mengelola Boot record sebagai tempat mount point yang dimiliki Linux (EXT4). Hasilnya jelas karena tidak ada menu untuk booting ke Linux jadi tidak bisa masuk.

Udah gitu 😄

## Pemecahan Masalah
Kita akan membuat merepair GRUB menu agar semua mount point bisa tampil, alih-alih menggunakan software Windows sejenis EasyBCD yang hanya tinggal "klik klik finish" 

### Repair
Kita harus masuk kedalam live cd sesuai distribusi masing2.

kalau sudah mount partisi **root** ke **/mnt** untuk bisa melakukan "change root". Maka /mnt dan subdirektorinya nanti digunakan sebagai tempat mount point sementara untuk file sistem kita. Kira-kira seperti itu fungsinya yang saya tahu

    $ sudo mount /dev/sdaX /mnt
    $ sudo mount --bind /dev /mnt/dev
    $ sudo mount --bind /proc /mnt/proc
    $ sudo mount --bind /sys /mnt/sys

sekarang status root kita pindahkan ke /mnt. Setelah itu dilanjut install & update grubnya

    $ sudo chroot /mnt
    # grub-install /dev/sda && Update GRUB

sudah selesai tinggal exit dari 'change root' bisa dengan Ctrl-D.

Jangan lupa, sebelum rampung lepaskan semua pernak-pernik yang dijadikan tempat mounting sementara tadi

    $ sudo umount /mnt/dev
    $ sudo umount /mnt/proc
    $ sudo umount /mnt/sys
    $ sudo umount /mnt

huh beress.

## Sumber
* [https://howtoubuntu.org...](https://howtoubuntu.org/how-to-repair-restore-reinstall-grub-2-with-a-ubuntu-live-cd)
