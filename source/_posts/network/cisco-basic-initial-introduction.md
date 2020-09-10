---
title: 'Cisco: Basic initial introduction'
draft: true
date: 2019-04-12
tags: cisco
category:
- network
- itn

---
## Router Mode

|modes|function|
|-----|------|
|setup mode|marked with notification message *"Continue with config dialog?"*|
|user exec mode|prompt: **Router>** Command allowed: ping and trace|
|priviliged mode|prompt: **Router#** Command allowed: ping, trace, show, copy, erase, dll|
|global config mode|prompt: **Router(config)#** Command wide configuration on router|
|interface mode|prompt and command spesificly understood interfaces on router|
|rommon mode|passwd recovery, telnet, etc|

## Verification command
|action|command|
|------|-------|
|show ip address|R1# show ip interface brief 
||Any mode# <with do> do show ip ...|
|show information command input|R1# show running-config use ‘enter’ and ‘space’ to show info|
|show other connect device|	R1# show cdp neighbor|
|show time|	R1# show clock|

## Cabling
|Cable|connection|
|-----|----------|
|straight-throught|router-switch|
||router-hub|
||pc-switch|
|cross-over|router-router|
||router-pc|
||switch-switch|
||switch-hub|
|console|config|
|serial|cloud-router|
 

## Basic config
masuk dari **user exec mode** ke **priviliged mode**

    Router> enable

masuk dari **priviliged mode** ke **global config mode**

    Router# conf terminal

memberi nama pada router atau perangkat

    Router(config)# hostname R1

membuat banner yang ditampilkan di awal login ke router

    Router(config)# banner motd #Admin Perpustakaan#

membuat password untuk priviliged mode (tidak terenkripsi, clear text based)

    R1(config)# security passwords min-length 6
    R1(config)# enable password 12345apaan 

membuat password untuk priviliged mode (terenkripsi, md5 hash)

    R1(config)# enable secret 12345apaan

atau kita bisa menghide passwd on **show run**. Dalam kata lain mengenkripsi clear text password

    R1(config)# service password-encryption

## IP address


    R1(config)# interface fa0/1
    R1(config-line)# description Connection to R2
    R1(config-line)# ip address 192.168.1.1 255.255.255.0

### mengaktifkan interfacenya
    R1(config-line)# no shutdown 
    R1(config-line)# exit

## Remote Access

**Console** 

- menggunakan kabel console
- tidak memerlukan settingan IP address pada sisi router maupun laptop

**Telnet**

- menggunakan kabel UTP
- memerlukan settingan IP address pada sisi komputer maupun laptop
- komunikasi telnet bersifat clear-text protocol, sehingga masih ada kekurangan dari sisi keamanan yaitu password dapat dengan mudah dilihat menggunakan packet sniffer

**SSH**

- menggunakan kabel UTP
- memerlukan settingan IP address
- komunikasi SSH bersifat encrypted protocol (enkripsi)

## Line console

    R1(config)# line console 0
    R1(config-line)# password 12345lupa

### automatic logout in 5 minute if no activity
    R1(config-line)# exectimeout 5 0

### activate password line console
    R1(config-line)# login
    R1(config-line)# exit

## Telnet

    R1(config)# username bima password 0 12345lupa 
    R1(config)# enable secret 12345engkripsi 

    router access only 1 machine. e.g: 5 machine (line vty 0 4)
    R1(config)# line vty 0

    R1(config-line)# login local
    R1(config-line)# transport input telnet
    R1(config-line)# exit
    root@localhost# telnet 192.168.1.1
 
## SSH

    R1(config)# ip domain-name cisco.com
    R1(config)# crypto key generate rsa

    R1(config)# line vty 0
    R1(config-line)# login local
    R1(config-line)# transport input ssh
    R1(config-line)# exit

    R1(config)# username bima password 0 12345lupa

    root@localhost# ssh -l bima 192.168.1.1

## Backup Config R1
Untuk proses backup, service yang digunakan menggunakan protokol  TFTP.

Sebelum proses backup dilakukan, pastikan konektivitas antara router R1 dan TFTP-Srv1 tidak ada masalah.

Untuk mengeceknya gunakan tes Ping. 

Setelah koneksi dari R1 ke TFTP-Srv1 sukses, langkah selanjutnya yaitu eksekusi command di R1. 

    R1# copy running-config tftp

    Address or name of remote host []? 192.168.1.11
    Destination filename [R1-confg]?
    Writing running-config....!!
    [OK - 828 bytes]

    828 bytes copied in 3.005 secs (275 bytes/sec)
 
## Backup IOS R1
Menampilkan lokasi penyimpanan Cisco IOS yang akan di backup

    R1# show flash

    System flash directory:
    File Length Name/status
    3 5571584 pt1000-i-mz.122-28.bin
    2 28282 sigdef-category.xml
    1 227537 sigdef-default.xml
    [5827403 bytes used, 58188981 available, 64016384 total]
    63488K bytes of processor board System flash (Read/Write)

Proses backup Cisco IOS R1 yang akan menyimpan konfigurasi router ke TFTP server

    R1# copy flash tftp

    Source filename []? pt1000-i-mz.122-28.bin
    Address or name of remote host []? 192.168.1.11
    Destination filename [pt1000-i-mz.122-28.bin]?
    Writing pt1000-i-mz.122-28.bin...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    [OK - 5571584 bytes]
    5571584 bytes copied in 0.29 secs (4402126 bytes/sec)

## Restore Config R1
kita bisa memakai file konfig yang ada di TFTP server
 
Perbedaan proses backup dan restore, kalo backup menyimpan konfigurasi router ke TFTP, sedangkan restore yaitu download konfigurasi dari TFTP ke router. 

Misalkan kita ingin mengconfig router dengan konfigurasi yang identik, maka kita bisa menggunakan konfigurasi yang sudah disimpan di TFTP.

Dengan mensetting koneksi TFTP dan router, maka kita bisa mendownload config di TFTP diarahkan ke router dan mengubah settingan yang berbeda kemudian disesuaikan dengan konfigurasi yang sudah direncanakan. 

Yang perlu diingat dari backup dan restore ini adalah source dan destination.

Kalau backup berarti sourcenya router dan destinationnya TFTP, sedangkan restore yang berfungsi sebagai sourcenya TFTP dan destinationnya router. 

    R1# copy tftp running-config

    Address or name of remote host []? 192.168.1.11
    Source filename []? R1-confg
    Destination filename [running-config]?
    Accessing tftp://192.168.1.11/R1-confg...
    Loading R1-confg from 192.168.1.11: !
    [OK - 828 bytes]
    828 bytes copied in 0.001 secs (828000 bytes/sec)
    
Untuk melihat hasil backup Cisco IOS dan R1 config bisa diakses melalui TFTP-Srv1 

## Etc..
|action|command|
|------|-------|
|save config to NVRAM|R1# do write|
|delete config|R1# erase startup-config then reload|