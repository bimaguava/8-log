---
title: "Brute f Pt.5 ssh, vnc, etc"
date: 2020-03-05
categories : security
tags : bruteforce
---

Salah satu hal yang dilakukan saat mencoba mendapatkan akses dengan sistem layanan biasanya dengan melihat mereka dapat masuk ke salah satu layanan tersebut menggunakan kredensial default atau umum. 

Karena hardware atau perangkat IOT seperti router sering dibiarkan dengan kata sandi default dan membuatnya mudah untuk diserang.

## Instalasi

```
sudo apt install nmap hydra medusa ncrack
git clone https://github.com/GitHackTools/BruteDum
```

## Attack protokol

* FTP
* PostgrestSQL
* RDP
* Telnet
* SSH
* VNC

## Referensi

* https://null-byte.wonderhowto.com/how-to/brute-force-ssh-ftp-vnc-more-with-brutedum-0197449/
