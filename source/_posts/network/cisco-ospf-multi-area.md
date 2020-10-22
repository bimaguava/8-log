---
title: "Cisco: OFPF Multi Area"
draft: true
date : "2019-04-16"
categories : network
tags : cisco
---

Multi area on OSPF can help to pressing load of memory usage on router with minimum spec usually router nearby with computer client.

## Topology
![topology](https://res.cloudinary.com/bimagv/image/upload/v1603374760/2019-04/ospf-multi_bckwnr.png)

## Config

    R1(config)# router ospf 10
    R1(config-router)# network 10.10.1.0 0.0.0.3 area 0
    R1(config-router)# network 192.168.10.0 0.0.0.3 area 0
    R1(config-router)# exit

    R2(config)# router ospf 20
    R2(config-router)# network 10.10.1.0 0.0.0.3 area 0
    R2(config-router)# network 10.10.2.0 0.0.0.3 area 1
    R2(config-router)# network 10.10.3.0 0.0.0.3 area 2
    R2(config-router)# exit

    R3(config)# router ospf 30
    R3(config-router)# network 10.10.3.0 0.0.0.3 area 2
    R3(config-router)# network 192.168.30.0 0.0.0.255 area 2
    R3(config-router)# exit

    R4(config)# router ospf 40
    R4(config-router)# network 10.10.2.0 0.0.0.3 area 1
    R4(config-router)# network 192.168.20.0 0.0.0.255 area 1
    R4(config-router)# exit
