---
title: "Cisco OSPF Single Area + DR BDR"
draft: true
date : "2019-04-14"
categories : network
tags : cisco
---

Just input entry route such as **network address** with **wilcard mask** and choose area. And then configure DR & BDR

## Topology
![topology](https://gblobscdn.gitbook.com/assets%2F-M4i1FkyJ96YEscBnmfS%2F-M4icPZWcnOSs2jE7Vt9%2F-M4ieoxl1sQHB4Bwj25r%2Fospf-single.png?alt=media&token=f6d811fd-344a-4aa5-ac4b-8eef0696b0cc)

## Config

    router ospf <process ID>
    network <address> <wildcard mask> area <area ID>

**Process ID** is identity of router. Process ID configuring not same with other.

**Area ID**. In single area just using 1 various of OSPF area, 0. OSPF network area distributed in 2 area. Backbone and non backbone. Code area for backbone have 0 value. For execption area (nonbackbone) must not same with backbone area. e.g: 88 or 44.

    R1(config)# router ospf 10
    R1(config-router)# network 10.10.1.0 0.0.0.3 area 0
    R1(config-router)# network 10.10.3.0 0.0.0.3 area 0
    R1(config-router)# network 192.168.2.0 0.0.0.255 area 0
    R1(config-router)# exit

    R2(config)# router ospf 20
    R2(config-router)# network 10.10.2.0 0.0.0.3 area 0
    R2(config-router)# network 10.10.3.0 0.0.0.3 area 0
    R2(config-router)# network 192.168.3.0 0.0.0.225 area 0
    R2(config-router)# exit

    R3(config)# router ospf 30
    R3(config-router)# network 10.10.1.0 0.0.0.3 area 0
    R3(config-router)# network 10.10.2.0 0.0.0.3 area 0
    R3(config-router)# network 192.168.1.0 0.0.0.255 area 0
    R3(config-router)# exit

On 1 process ID, by default OSPF using highest IP address on active interface as Router ID. So, we can manually set 1 IP address as Router ID with additional config. Router ID need to add if you want allocate load of LSA to some router as DR & BDR.

## DR & BDR

**LSA** (Link-State Advertisement) using in OSPF router to send broadcast routing information to all router on 1 area. It causes on bandwith usage. For press consumption, usually administrator choosing one of router interface to be DR and BDR.

**DR** (Designated Router) identic with router with strong spesification. Because, DR will be handle LSA broadcasting which before do by all routers.

**BDR** (Backup Designated Router) backuper if DR down.

To configure DR & BDR we have change Router ID. Thereis method

1. interface loopback
2. router-id command
3. interface priority command

To configure interface loopback just add ip address to router.

### pros

using address from physical interface for router-id is not propose. If administrator put down cable or shutdown with command. It can be changing value of router-id. That annoying.

    R1(config)# interface loopback0
    R1(config-if)# ip address 10.1.1.1 255.255.255.255
    R1(config-if)# no shutdown
    R1(config-if)# end
    R1# show ip ospf database

    R2(config)# interface loopback0
    R2(config-if)# ip address 10.1.1.2 255.255.255.255
    R2(config-if)# no shutdown
    R2(config-if)# end
    R2# show ip ospf database

    R3(config# interface loopback0
    R3(config-if)# ip address 10.1.1.3 255.255.255.255
    R3(config-if)# no shutdown
    R3(config-if)# exit
    R3# show ip ospf database