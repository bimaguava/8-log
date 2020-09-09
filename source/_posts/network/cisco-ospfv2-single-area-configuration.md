---
draft: true
comments: true
toc: true
title: 'Cisco: OSPFv2 Single. Area Configuration (point to point and broadcast multiaccess)'
date: 2020-09-08T13:06:00Z
updated: 
category:
- network
- ensa
tags:
- cisco
keywords: []

---
# **Objectives**

Kalau di materi [sebelumnya](https://8log.js.org/2020/08/16/network/cisco-ospfv2-single-area-point-to-point/), kita sudah mengimplementasikan OSPF single area dengan topologi point to point, sekarang kita akan mencoba menerapkannya ke jaringan `point to point and broadcast multiaccess`.

# **Overview**

Sekarang kita akan mencoba untuk mengkonfigurasi Routing Dynamic OSPF, untuk yang ingin tahu cara melihat dan menganalisis konfigurasi OSPF sebelumnya sudah dijelaskan di [sini](https://8log.js.org/2020/09/08/network/cisco-ospfv2-single-area-verify/).

# **Lab**

![](/images/2020-08-09_sel_07-21-22.png)

Pada materi kali ini akan sangat berguna sekali untuk melatih kemampuan kita dalam mengkonfigurasi router dengan OSPF dengan beberapa ketentuan yang disediakan sebagai berikut.

![](/images/2020-08-09_sel_20-08-28.png)

# **Tabel Address**

![](/images/2020-08-09_sel_07-23-29.png)

![](/images/2020-08-09_sel_07-23-44.png)

# **1. Mengemplementasikan OSPF di Router2 Headquarters**

Pertama-tama kita akan mengerjakan network di **Headquarters** yang berupa point to point.

Kita telah mengetahui di materi [kemarin]() bahwa di jaringan point to point tidak ada election DR/BDR, maka kita tidak perlu repot menyetel Router ID untuk router2 P2P ini.

![](/images/2020-09-09_rab_12-55-44.png)

Untuk itu mari kita langsung saja jalankan OSPF routing process di mulai pada router P2P-1 ini

    P2P-1(config)#router ospf 10

## 1.A. Mencari router yang directly connected dengan P2P-1

Kita akan mencari router interface yang directly connected alias terhubung secara langsung dengan Router P2P ini, langsung saja jalankan `do show ip route connected`

     C   10.0.0.0/30  is directly connected, Serial0/1/0
     C   10.0.0.8/30  is directly connected, Serial0/1/1
     C   10.0.0.12/30  is directly connected, Serial0/2/0

Tampak yang IP yang muncul yaitu berupa network2 yang terkoneksi langsung ke router P2P-1

Sedangkan kalau kita menggunakan command `do show ip route` saja

    Gateway of last resort is not set
    
         10.0.0.0/8 is variably subnetted, 6 subnets, 2 masks
    C       10.0.0.0/30 is directly connected, Serial0/1/0
    L       10.0.0.1/32 is directly connected, Serial0/1/0
    C       10.0.0.8/30 is directly connected, Serial0/1/1
    L       10.0.0.9/32 is directly connected, Serial0/1/1
    C       10.0.0.12/30 is directly connected, Serial0/2/0
    L       10.0.0.13/32 is directly connected, Serial0/2/0

Maka akan menampilkan juga interface2 milik router P2P-1 itu sendiri yang ada pada baris entri kode **L** alias **Local** yang kemudian meneruskan informasi ke network **C** Alias (directly) **Connected**, itu sekedar informasi.

Dari sini kita telah menemukan network2 yang directly connected, yaitu `10.0.0.0/30`, `10.0.0.8/30`, dan `10.0.0.12/30` yang juga sudah ada keterangannnya di topologi

![](/images/2020-09-09_rab_14-01-51.png)

## 1.B. Menyetel P2P-1 dengan Network statements dan inverse mask

Kita telah melakukan cara ini pada materi [sebelumnya](https://8log.js.org/2020/08/16/network/cisco-ospfv2-single-area-point-to-point/#2-B-Menyetel-R1-dengan-Network-statements-dan-Wilcard-Mask). Sekarang yang kita butuhkan adalah command

> Router(config-router)# **network** network-address wildcard-mask **area** area-id

Jadi kita mendaftarkan network2nya satu-persatu, lalu memasukkan wilcard mask (kalau lupa menghitung wilcard mask caranya di [materi yang lalu](https://8log.js.org/2020/08/16/network/cisco-ospfv2-single-area-point-to-point/#2-A-Cara-Mengkonversikan-subnet-ke-desimal) dan ingat karena single area berarti area 0.

    P2P-1(config-router)#network 10.0.0.0 0.0.0.3 area 0
    P2P-1(config-router)#network 10.0.0.8 0.0.0.3 area 0
    P2P-1(config-router)#network 10.0.0.12 0.0.0.3 area 0

Lanjut.

## 1.C. Mengatur interface cost pada Router OSPF P2P-1

Sekarang saatnya kita akan mengatur dahulu pada router OSPF ini sehingga pada interface GigabitEthernet dan FastEthernet disetel cost yang telah ditentukan, yaitu

* **GigabitEthernet=10**
* **FastEthernet=100**

perintahnya ialah `auto-cost reference-bandwidth <bandwidth>` \[ **Gbps** | **Mbps** \]

Sementara itu ...

_"apa itu OSPF cost?"_

_"kenapa ada OSPF cost?"_

_"kenapa digunakan?"_

_"dan apa itu reference-bandwith?"_

_"apa cost semacam ini hanya ada di OSPF saja?"_

Oke, cara belajar kita adalah **_learning by doing_** sembari ngoprek, sembari belajar :)

Sebelum itu kita harus tahu fungsi dari penerapan dari cost di OSPF ini yang tidak lain dan tidak bukan ialah untuk **metric** :) Yang merupakan suatu nilai yang digunakan untuk menuju ke destination.

![](/images/2020-09-09_rab_15-17-27.png)

Simpelnya metrik ini membantu router memilih rute terbaik dimana nilai metrik setiap routing protokol berbeda-beda.

Untuk OSPF sendiri untuk nilai metric nya menggunakan bandwith.

> Pada **Dynamic Routing Protocol lain** contoh seperti **RIP**, ia memakai `Hop` untuk metricnya dan **EIGRP** memakai `Bandwidth`, `Delay`, `Reliability`, dan `Load`

Sama seperti EIGRP, OSPF (juga) mendasarkan metriknya secara default pada `bandwidth link`, sehingga OSPF dinilai lebih baik dibanding RIP yang mengandalkan metrik `hop-count`.

Oke.

Lanjut.

Kalau seperti itu maka kita musti tahu berapa bandwith yang dipakai dahulu, karena logikanya sebuah paket akan lebih banyak overhead jika melewati medium yang kapasitas bandwithnya kecil.

Contoh saat melintas Serial link yang bandwithnya ialah 56Kbps maka paket OSPF akan lebih lama sampainya daripada melintasi Ethernet link yang bandwithnya 100Mbps.

Dan sekarang kita akan lihat bandwith dan cost ini **berbanding terbalik**, karena bandwith yang lebih tinggi seperti Ethernet link (100Mbps) akan mempunyai _cost yang lebih kecil_ dimana ini merupakan **rute terbaik**. Sedangkan bandwith yang lebih rendah seperti Serial link (56Kbps) akan memiliki _cost yang lebih tinggi_.

Sekedar info berikut default nilai cost pada beberapa interface

| Interface Type | bandwidth | Metric Calculation | Cost |
| :---: | :---: | :---: | --- |
| Ethernet Link | 10Mbps | 100000000/10000000 = 10 | 10 |
| FastEthernet Link | 100Mbps | 100000000/100000000 = 1 | 1 |
| Serial Link | 1544Kbps(default) | 100000000/1544000 = 64.76 | 64 |

### Konfigurasi interface cost menggunakan Auto Cost Reference Bandwith

Kalau mengikuti defaultnya, maka reference bandwith berjumlah 100 Mbps

    BimaRR# show ip ospf | include Reference
     Reference bandwidth unit is 100 mbps

Terlihat terlalu kecil.

Namun, menurut requirement diawal:

> **_Configure the OSPF routers so that the Gigabit Ethernet interface cost will be 10 and the Fast Ethernet cost will be 100._**

Kalau memilih reference bandwith 10000 Mbps

![](/images/2020-10-09_kam_00-06-57.png)

Berarti kita akan menyeting kabel yang kapasitas bandwithnya sekitar 100 Mbps untuk FastEthernet dan 1 Gbps (1000Mbps) untuk GigabitEthernet

Namun, jika kita memilih reference bandwith 1000 Mbps  
![](/images/2020-10-09_kam_00-03-17.png)

cocok untuk interfaces berkapasitas 10 Mbps untuk FastEthernet dan 100 Mbps untuk GigabitEthernet.

Dan melihat dari tabel berikut

### **Cost of common lines**

| Interface Type | bandwidth | Metric Calculation | Cost |
| :---: | :---: | :---: | --- |
| 56 Kbps line | 56Kbps | 100000000/56000 = 1785.71 | 1785 |
| 64 Kbps line | 64Kbps | 100000000/64000 = 1562.5 | 1562 |
| 128 Kbps line | 128Kbps | 100000000/128000 = 781.25 | 781 |
| 512 Kbps line | 512Kbps | 100000000/512000 = 195.31 | 195 |
| 1 Mbps line | 1Mbps | 100000000/1000000 = 100 | 100 |
| 10 Mbps line | 10Mbps | 100000000/10000000 = 10 | 10 |
| 100 Mbps line | 100Mbps | 100000000/100000000 = 1 | 1 |
| 1 Gbps line | 1Gbps | 100000000/100000000 0= 0.1 | 1 |
| 10 Gbps line | 10Gbps | 100000000/10000000000 = 0.01 | 1 |

mungkin konsumsi bandwith untuk nilai cost sesuai requirement tidak terlalu tinggi (FastEthernet 1 Mbps dan GigabitEthernet 10 Mbps), maka kita akan memilih `auto-cost bandwith-reference 1000`

    P2P-1(config-router)# auto-cost reference-bandwidth 1000
    % OSPF: Reference bandwidth is changed.
            Please ensure reference bandwidth is consistent across all routers.

Dan ada satu requirement lagi terkait OSPF cost ini, yaitu

> **_Configure the OSPF cost value of P2P-1 interface Serial0/1/1 to 50._**

Jadi selain mengubah `auto-cost reference-bandwith` yang mana OSPF akan mengkalkulasi sendiri kira-kira satu interface akan menggunakan bandwith berapa, kita juga akan menkonfigurasi berapa nilai cost yang akan digunakan OSPF untuk interface serial 0/1/1 pada router ini

    P2P-1(config)#int serial 0/1/1
    P2P-1(config-if)#ip ospf cost 50

Keknya panjang amat :)

<!------- CONTOH-------------------------------------------------------------------------------------------------

Selanjutnya apabila nanti ingin melihat cost dan bandwithnya kira-kira contohnya seperti ini.

Untuk melihat bandwith pakai perintah `show interfaces FastEthernet 0/0 | include BW`

    Router# show interfaces FastEthernet 0/0 | include BW
      MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec

Dan muncullah `100000 Kbit/sec`

Nanti dari sini OSPF akan menghitung costnya

> **Cost = Reference bandwidth (default 100 Mbps) / Interface bandwidth in bps.**
>
> atau **Cost = 10^8 / interface bandwidth in bps**

Cost = `100.000 kbps reference bandwidth / 100.000 interface bandwidth = 1`

Dan perintah verifikasi untuk menampilkan cost dengan `show ip ospf interface FastEthernet 0/0 | include Cost`

    Router# show ip ospf interface FastEthernet 0/0 | include Cost
      Process ID 1, Router ID 192.168.1.1, Network Type BROADCAST, Cost: 1

Nah, itulah hasil costnya, yaitu 1.

END CONTOH -------------------------------------------------------------------------------------------------->

(^_^)

## 1.D. Mengatur Hello dan Dead timer values antara P2P-1 dan BC-1

Setelah itu lanjut ke 

# **Referensi**

* [https://www.computernetworkingnotes.com/ccna-study-guide/ospf-metric-cost-calculation-formula-explained.html](https://www.computernetworkingnotes.com/ccna-study-guide/ospf-metric-cost-calculation-formula-explained.html "https://www.computernetworkingnotes.com/ccna-study-guide/ospf-metric-cost-calculation-formula-explained.html")
* [h](https://www.cisco.com/c/m/en_us/techdoc/dc/reference/cli/nxos/commands/ospf/auto-cost-ospf.html "https://www.cisco.com/c/m/en_us/techdoc/dc/reference/cli/nxos/commands/ospf/auto-cost-ospf.html")[https://networklessons.com/ospf/ospf-reference-bandwidth](https://networklessons.com/ospf/ospf-reference-bandwidth "https://networklessons.com/ospf/ospf-reference-bandwidth")