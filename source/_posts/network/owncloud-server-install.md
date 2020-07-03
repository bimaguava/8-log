---
title : "OwnCloud Server install"
date : "2019-03-01"
showDate: true
draft : false
categories : network
tags : owncloud
---

For reading: [manual_installation](https://doc.owncloud.org/server/10.1/admin_manual/installation/manual_installation.html) 

## Connect to server
Setup IP address for your server

    # vi /etc/network/interfaces
    
there is example config

    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).

    source /etc/network/interfaces.d/*

    # The loopback network interface
    auto lo
    iface lo inet loopback

    # The primary network interface
    auto eth0
    iface eth0 inet static
            address 192.168.0.128
            netmask 255.255.255.0
            gateway 192.168.0.1
            dns-nameservers 8.8.8.8 8.8.4.4

Tell your system to applied new config

    # /etc/init.d/networking restart

And access the server with remote using openssh

    # apt install openssh-server
    # /etc/init.d/ssh start
    # ssh root@ip_server

## Installing Web server
Such as apache2, php7.2 and additonal extensions,
mariadb-server, redis-server

    # apt install apt-transport-https lsb-release ca-certificates
    # wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
    # sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list'
    # apt-get update
    # apt-get install -y apache2 mariadb-server libapache2-mod-php7.2 \
    openssl php-imagick php7.2-common php7.2-curl php7.2-gd \
    php7.2-imap php7.2-intl php7.2-json php7.2-ldap php7.2-mbstring \
    php7.2-mysql php7.2-pgsql php-smbclient php-ssh2 \
    php7.2-sqlite3 php7.2-xml php7.2-zip

Aditional extensions

    # apt install -y php-apcu php-redis redis-server php7.2-ldap

on Debian 9 php7.0 is default. We're choose version 7.2

    # ad2dismod php7.0
    # ad2enmod php7.2

Start apache2 service

    # systemctl start apache2
    # systemctl enable apache2 #run every server boot

Start mariadb service

    # systemctl start MariaDB
    # systemctl enable mariadb

## Install OwnCloud server

    # -qO- https://download.owncloud.org/download/repositories/stable/Debian_9.0/Release.key | sudo apt-key add -
    # echo "deb https://packages.sury.org/php/ stretch main" | tee /etc/apt/sources.list.d/php.list
    # apt install apt-transport-https
    # apt update
    # apt install owncloud-files

## Create database admin

    # mysql --user=root mysql
    MariaDB [mysql]> CREATE USER 'dbadmin'@'localhost' IDENTIFIED BY '123';
    MariaDB [mysql]> GRANT ALL PRIVILEGES ON *.* TO 'dbadmin'@'localhost' WITH GRANT OPTION;
    MariaDB [mysql]> FLUSH PRIVILEGES;
    MariaDB [mysql]> exit

## Configure web server

    # vi /etc/apache2/sites-available/owncloud.conf

Add to this script to config file

    Alias /owncloud "/var/www/owncloud/"

    <Directory /var/www/owncloud/>
    Options +FollowSymlinks
    AllowOverride All

    <IfModule mod_dav.c>
    Dav off
    </IfModule>

    SetEnv HOME /var/www/owncloud
    SetEnv HTTP_HOME /var/www/owncloud

    </Directory>

Then create a links to **/etc/apache2/sites-enabled**:

    # ln -s /etc/apache2/sites-available/owncloud.conf /etc/apache2/sites-enabled/owncloud.conf

We need enable requiered module to runnig server 

    # a2enmod headers
    # a2enmod env
    # a2enmod dir
    # a2enmod mime
    # a2enmod unique_id

And please restart Apache one more

    # /etc/init.d/apache2 restart

After that, change owned group from ```/var/www/owncloud/``` to ```www-data```

    # chown -R www-data: /var/www/owncloud/

Finally, we can access OwnCloud server on http://your_ip_server/owncloud and
signup for OwnCloud. On database config we're choose mariadb. Then enter database administrator name "dbadmin" and password "123" into your OwnCloud Database.