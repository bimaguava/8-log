---
author: "Bima"
title: Change to Classical Naming Interface
date: 2018-10-01
showDate: true
toc: true
categories:
- linux
tags:
- repair
---

## Overview
My case is I'm not Familiar with this term on Ubuntu 16.04
![ugly naming](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4i0vuVdGvambPchX0c%2Fsetting-classical-naming-interface-01.png?alt=media&token=705ddf45-bf8f-4fdb-bfb2-b96ab4ebc990)

Formerly on Ubuntu 15.04
* Wireless network= wlan0, wlan1, wlan2, ..
* ethernet = ether1,2..

Now, I want to change ugly naming like wlp3s0, enp0s28, etc



## So what is this?
Wlan0 or Eth0 is **the classic naming scheme** for network interfaces applied by the kernel is to simply assign names beginning with "eth0", "eth1", ... to all interfaces as they are probed by the drivers.

Before Ubuntu 15.04 **the predictable network** interfaces naming not occur, why? [this is reason](https://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/)



## Risk of this method
According to the freedesktop.org page one of the reasons for switching to predictable naming is that classic naming convention can lead to software security risks in multi-interface systems when devices are added and removed at boot. 

## Method
The solution so tricky, I read from [this thread](https://askubuntu.com/questions/767786/changing-network-interfaces-name-ubuntu-16-04) and got right solution, maybe :v

### 1 - Add kernel boot parameter
Open terminal and edit grub file config

    $ sudo vi /etc/default/grub

add `net.ifnames=0 biosdevname=0` in this field `GRUB_CMDLINE_LINUX="..."` 

After your save change, run

```
$ sudo update-grub
$ reboot
```
and taraa you get change. 

Or not? using method 2

### 2 - Add persistent rules
And other way we will add new network rules.

script `/etc/udev/rules.d/70-persistent-net.rules` is rule system to find out interface assigned to the network device on your computer. So, open your terminal and run the following command

```
$ sudo vi /etc/udev/rules.d/70-persistent-net.rules
```

Add new network rules

```
# Network interfaces eth0
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="XX:XX:XX:XX:XX:XX", ATTR{dev_id}=="0x0", ATTR{type}=="1", NAME="eth0"

# Network interfaces wlan0
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="XX:XX:XX:XX:XX:XX", ATTR{dev_id}=="0x0", ATTR{type}=="1", AME="wlan0"
```

Simply, add your MAC address on `ATTR{address}=="..."` field

After rebooting you will get classical named on interface network like Wlan0 and Eth.

This is simple two line script as you need for.

If you dont know yet MAC Address located

(Line 1) enps0s25 Link encap:Ethernet HWaddr `f1:dc:f0:ac:91:90`

(Line 19) wlp3s0 Link encap:Ethernet HWaddr `10:0b:a9:0a:2b:10`

```
enps0s25 Link encap:Ethernet HWaddr f1:dc:f0:ac:91:90
inet addr:192.168.10.23 Bcast:192.168.10.255 Mask:255.255.255.0
UP BROADCAST MULTICAST MTU:1500 Metric:1
RX packets:0 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:0 (0.0 B) TX bytes:0 (0.0 B)
Interrupt:20 Memory:f2500000-f2520000

lo Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
inet6 addr: ::1/128 Scope:Host
UP LOOPBACK RUNNING MTU:65536 Metric:1
RX packets:7508 errors:0 dropped:0 overruns:0 frame:0
TX packets:7508 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:1707306 (1.7 MB) TX bytes:1707306 (1.7 MB)

wlp3s0 Link encap:Ethernet HWaddr 10:0b:a9:0a:2b:10
inet addr:192.168.0.10 Bcast:192.168.0.255 Mask:255.255.255.0
inet6 addr: fe80::899b:cd:a638:8f0f/64 Scope:Link
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets:117116 errors:0 dropped:0 overruns:0 frame:0
TX packets:66947 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:139014442 (139.0 MB) TX bytes:8581098 (8.5 MB)
```
