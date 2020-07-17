---
draft: true
comments: true
toc: true
title: MikroTik basic command line
date: 2020-07-13T17:00:00Z
updated: 2020-07-13T17:00:00Z
category: []
tags: []
keywords: []

---
1\. Memberi Nama Router

    system identity set name=RouterKu

2\. Melihat Interface yang terpasang

    /interface print

3\. Memberi Nama pada Interface Ethernet

    /interface ethernet set ether1 name=Public
    /interface Ethernet set ether2 name=Local 
    atau
    /interface set 0 name=Public
    /interface set 1 name=Local 
    atau
    / interface set 0 name=Public; set 1 name=Local

4\. Memberi IP Address pada interface Public dan Local

    /ip address add address=192.168.67.100/24 interface=Public
    /ip address add address=10.10.11.2/24 interface=Local

5\.Mengganti IP Address pada Interface Local

    /ip address remove 1
    /ip address add address=172.16.10.100/24 interface=Local

6\. Menambahkan DNS Resolver , Primary DNS dan Secondary DNS

    /ip dns static add name=dnsku.com address=172.16.10.100
    /ip dns set primary-dns=203.78.115.215 secondary-dns=203.78.115.222 allow-remote-request=yes

7\. Menambahkan default gateway

    / ip route add dst-address=0.0.0.0/0 gateway=192.168.67.2 Atau
    /ip route add gateway=192.168.67.2
    * Misal IP gateway yang digunakan adalah 192.168.67.2

8\. Menambahkan NAT Masquerade

    /ip firewall nat add chain=srcnat src-address=172.168.10.0/24 out-interface=Public action=masquerade

9\.Menambahkan DHCP Server

    - Buat IP Pool
    /ip pool add name = ippool1 ranges= 172.16.10.1-172.16.10.10
    
    -Setup DHCP Server
    /ip dhcp-server add interface=Local address=ippool1
    
    - Setup Netwok; Gateway, DNS Server,..
    /ip dhcp-server  network add address=172.16.10.0/24 gateway=172.16.10.100 s=dns-server=203.78.115.222
    

10\. Membuat Mark Connection yang nantinya di pakai untuk memilah Paket

    /ip firewall mangle add chain=forward src-address=172.16.10.1 action=mark-connection new-connection-mark=billing
    /ip firewall mangle add chain=forward src-address=172.16.10.2 action=mark-connection new-connection-mark=pc1
    /ip firewall mangle add chain=forward src-address=172.16.10.3 action=mark-connection new-connection-mark=pc2
    /ip firewall mangle add chain=forward src-address=172.16.10.4 action=mark-connection new-connection-mark=pc3

11\. Membuat mark packet untuk Queue, yang didapat dari mark connection

    /ip firewall mangle add chain=forward connection-mark=billing action=mark-packet new-packet-mark=billing
    /ip firewall mangle add chain=forward connection-mark=pc1 action=mark-packetnew-packet-mark=pc1
    /ip firewall mangle add chain=forward connection-mark=pc2 action=mark-packetnew-packet-mark=pc2
    /ip firewall mangle add chain=forward connection-mark=pc3 action=mark-packetnew-packet-mark=pc3

12\. Membuat Parent tertinggi Queue

    /queue tree add name=E-Net parent=ether2 max-limit=10000000

13\. Membuat Queue per terminal

    /queue tree add name=pcbil packet-mark=billing parent=E-Net limit-at=64000max-limit=250000
    /queue tree add name=pc1 packet-mark=pc1 parent=E-Net limit-at=64000 max-limit=250000
    /queue tree add name=pc2 packet-mark=pc2 parent=E-Net limit-at=64000 max-limit=250000
    /queue tree add name=pc3 packet-mark=pc3 parent=E-Net limit-at=64000 max-limit=250000

14\. Firewall Basic

    / ip firewall filter add chain=forward connection-state=invalid action=drop comment=”drop invalid connections”
    
    add chain=virus protocol=tcp dst-port=135-139 action=drop comment=”Drop Blaster Worm”
    add chain=virus protocol=udp dst-port=135-139 action=drop comment=”Drop Messenger Worm”
    add chain=virus protocol=tcp dst- port=445 action=drop comment=”Drop Blaster Worm”
    add chain=virus protocol=udp dst- port=445 action=drop comment=”Drop Blaster Worm”
    add chain=virus protocol=tcp dst- port=593 action=drop comment=”________”
    add chain=virus protocol=tcp dst-port=1024-1030 action=drop comment=”________”
    add chain=virus protocol=tcp dst- port=1080 action=drop comment=”Drop MyDoom”
    add chain=virus protocol=tcp dst- port=1214 action=drop comment=”________”
    add chain=virus protocol=tcp dst- port=1363 action=drop comment=”ndm requester”
    add chain=virus protocol=tcp dst-port=1364 action=drop comment=”ndm server”
    add chain=virus protocol=tcp dst- port=1368 action=drop comment=”screen cast”
    add chain=virus protocol=tcp dst- port=1373 action=drop comment=”hromgrafx”
    add chain=virus protocol=tcp dst- port=1377 action=drop comment=”cichlid”
    add chain=virus protocol=tcp dst-port=1433-1434 action=drop comment=”Worm”
    add chain=virus protocol=tcp dst- port=2745 action=drop comment=”Bagle Virus”
    add chain=virus protocol=tcp dst- port=2283 action=drop comment=”Drop Dumaru.Y”
    add chain=virus protocol=tcp dst-port=2535 action=drop comment=”Drop Beagle”
    add chain=virus protocol=tcp dst- port=2745 action=drop comment=”Drop Beagle.C-K”
    add chain=virus protocol=tcp dst-port=3127-3128 action=drop comment=”Drop MyDoom”
    add chain=virus protocol=tcp dst-port=3410 action=drop comment=”Drop Backdoor OptixPro”
    add chain=virus protocol=tcp dst-port=4444 action=drop comment=”Worm”
    add chain=virus protocol=udp dst-port=4444 action=drop comment=”Worm”
    add chain=virus protocol=tcp dst-port=5554 action=drop comment=”Drop Sasser”
    add chain=virus protocol=tcp dst-port=8866 action=drop comment=”Drop Beagle.B”
    add chain=virus protocol=tcp dst-port=9898 action=drop comment=”Drop Dabber.A-B”
    add chain=virus protocol=tcp dst-port=10000 action=drop comment=”Drop Dumaru.Y”
    add chain=virus protocol=tcp dst-port=10080 action=drop comment=”Drop MyDoom.B”
    add chain=virus protocol=tcp dst-port=12345 action=drop comment=”Drop NetBus”
    add chain=virus protocol=tcp dst-port=17300 action=drop comment=”Drop Kuang2″
    add chain=virus protocol=tcp dst-port=27374 action=drop comment=”Drop SubSeven”
    add chain=virus protocol=tcp dst-port=65506 action=drop comment=”Drop PhatBot, Agobot,Gaobot”
    add chain=forward action=accept protocol=tcp dst-port=80 comment=”Allow HTTP”
    add chain=forward action=accept protocol=tcp dst-port=25 comment=”Allow SMTP”
     add chain=forward protocol=tcp comment=”allow TCP”
    add chain=forward protocol=icmp comment=”allow ping”
    add chain=forward protocol=udp comment=”allow udp”
    add chain=forward action=drop comment=”drop everything else”
    add chain=input src-address-list=”port scanners” action=drop comment=”dropping portscanners” disabled=no
     
    / ip firewall filter add chain=virus protocol= udp dst-port=135 action=drop comment=”Confiker” disabled=no
    
    / ip firewall filter add chain=virus protocol= udp dst-port=137 action=drop comment=”Confiker” disabled=no
    
    / ip firewall filter add chain=virus protocol= udp dst-port=138 action=drop comment=”Confiker” disabled=no
    
    / ip firewall filter add chain=virus protocol= udp dst-port=445 action=drop comment=”Confiker” disabled=no
    
    / ip firewall filter add chain=virus protocol= tcp dst-port=135 action=drop comment=”Confiker” disabled=no
    
    / ip firewall filter add chain=virus protocol= tcp dst-port=139 action=drop comment=”Confiker” disabled=no
    
    / ip firewall filter add chain=virus protocol= tcp dst-port=5933 action=drop comment=”Confiker” disabled=no
    
    / ip firewall filter add chain=virus protocol= tcp dst-port=445 action=drop comment=”Confiker” disabled=no
    
    / ip firewall filter add chain=virus protocol= tcp dst-port=4691 action=drop comment=”Confiker” disabled=no

15\. Set jam Otomatis

    system ntp client set primary-ntp=0.pool.ntp.org secondary-ntp=3.pool.ntp.org enabled=yes
    

16\. Membackup System configuration

    /system backup save name="Backup-versi1"

17\. Restore System configuration

    /system backup load name="Backup-versi1"