---
draft: true
comments: true
toc: true
title: 'Cisco: OSPFv2 Single Area (Verify)'
date: 2020-09-08T00:40:00Z
updated: 
category:
- network
- ensa
tags:
- cisco
keywords: []

---
# **Objectives**

Pada materi ini kita akan belajar menggunakan perintah verifikasi pada jaringan OSPFv2 ini seperti:

* Mengidentifikasi dan verify status `OSPF Neighbor`
* Mengetahui bagaimana suatu rute dipilih dan digunakan dalam sebuah jaringan
* Mengetahui bagaimana `Neighbor state` ditentukan
* Melihat konfigurasi OSPF process ID
* Dan juga nanti kita akan menambahkan sebuah LAN ke sebuah OSPF network

# **Lab**

![](/images/2020-08-09_sel_07-49-05.png)

Pada area berwarna hijau nanti disana kita menambahkan sebuah jaringan wireless baru yang mana itu ialah LAN **Branch Office**.

Cuma kita akan belajar memverifikasi saja bagaimana OSPF yang sudah diterapkan disitu, setelah itu nanti kita baru akan mencoba menyambungkan LAN baru ke **Branch Office.**

Untuk menambahkan LAN baru ke **Branch Office**, kita disini hanya diberi akses untuk bekerja menggunakan R1 dan R2 saja, dengan username: **BranchAdmin**, dan password: **Branch1234**

# **Tabel Address**

![](/images/2020-08-09_sel_07-49-38.png)

# 1. Verify the existing OSPFv2 network operation

Command verifikasi atau pengecekan yang nanti digunakan ialah:

* **show ip interface brief**
* **show ip route**
* **show ip route ospf**
* **show ip ospf neighbor**
* **show ip protocols**
* **show ip ospf**
* **show ip ospf interface**

## 1.A Mengecek rute OSPF 

Kalau baru membuka Paket Tracer biasanya kita akan menunggu proses STP, apabila lampu indikator hijau sudah muncul maka kita bisa melanjutkan.

Pertama-tama kita akan login ke R1, lalu kita akan mencoba melihat status interface2 yang terkoneksi dengan perintah `show ip route`

    R1# show ip route 
    Gateway of last resort is 172.16.3.2 to network 0.0.0.0
    
         172.16.0.0/16 is variably subnetted, 5 subnets, 3 masks
    C       172.16.1.0/24 is directly connected, GigabitEthernet0/0
    L       172.16.1.1/32 is directly connected, GigabitEthernet0/0
    O       172.16.2.0/24 [110/65] via 172.16.3.2, 01:17:06, Serial0/0/0
    C       172.16.3.0/30 is directly connected, Serial0/0/0
    L       172.16.3.1/32 is directly connected, Serial0/0/0
    O    192.168.1.0/24 [110/65] via 192.168.10.6, 01:17:06, Serial0/0/1
         192.168.10.0/24 is variably subnetted, 3 subnets, 2 masks
    C       192.168.10.4/30 is directly connected, Serial0/0/1
    L       192.168.10.5/32 is directly connected, Serial0/0/1
    O       192.168.10.8/30 [110/128] via 172.16.3.2, 01:17:06, Serial0/0/0
                            [110/128] via 192.168.10.6, 01:17:06, Serial0/0/1
    O*E2 0.0.0.0/0 [110/1] via 172.16.3.2, 01:17:06, Serial0/0/0