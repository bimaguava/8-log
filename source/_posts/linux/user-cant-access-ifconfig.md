---
title : "User Can't Access ifconfig"
date : "2018-10-17"
showDate: true
toc : true
categories : linux
tags : repair
---

It's very annoying for user should do **sudo ifconfig** every time

## Overview
**Elementary OS Loki** is Ubuntu Xenial based with pantheon desktop and Loki not have **net-tools** to run arp, route, iptunnel and of course ifconfig.

I need install net-tools

    $ sudo apt install net-tools

Then run **ifconfig** command (as user) and it still not working

![ifconfig not work](https://gblobscdn.gitbook.com/assets%2F-M4hrSq2FgEwSBYhHwyl%2F-M4hsuqa5BQ4gBgwIn2d%2F-M4hze9NReB7VgoW2Vse%2Fhow-user-able-to-access-ifconfig-01.png?alt=media&token=bf611f34-8692-422c-9981-3054e8ac9910)

But you can do with sudo su or root account. This tutorial will show how to run app located on **/sbin** like **ifconfig** as normal user

## Goal
The goal of case is user can access ifconfig (without run sudo or su)

## How
We can try to setting up PATH to access **/sbin/ifconfig** or use alternative way

### Set $PATH
There are several ways what I want it. 

First think is I have to try assign special access for user to execute /sbin directory. 

Generally, checking the content of PATH (user) to ensure system failure. The default output for command **echo $PATH** is

    PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"

Source: [https://askubuntu.com...](https://askubuntu.com/questions/422605/why-is-usr-local-games-after-usr-games-in-the-default-path)


just add that path to **/etc/environment** to fix. this a Ubuntu system-wide configuration file, contains variables specifying the basic environment for all processes. 

    $ sudo vi /etc/environment

Then, execute these path

    $ source /etc/environment

### Alternative
If you dont like opening access to sbin directory, try alternative

1. Another tool to show network interfaces like ifconfig. Thereis ```ip addr```
2. Use Change mode ```chmod 4755 /sbin/ifconfig```. In same time you can do ifconfig until you close terminal

Thats all.