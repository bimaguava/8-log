---
title: "Cisco OFPF Multi Area"
draft: true
date : "2019-04-16"
categories : network
tags : cisco
---

Multi area on OSPF can help to pressing load of memory usage on router with minimum spec usually router nearby with computer client.

## Topology
![topology](https://gblobscdn.gitbook.com/assets%2F-M4i1FkyJ96YEscBnmfS%2F-M4icPZWcnOSs2jE7Vt9%2F-M4iekmBsiZhubcXo9s4%2Fospf-multi.png?alt=media&token=4078756d-5df8-4856-97ee-380bb63464b1)

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