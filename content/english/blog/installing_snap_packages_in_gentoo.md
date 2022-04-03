---
title: "Installing snap packages in Gentoo"
description: "In today's article we are going to install the Hugo static site generator on the Gentoo GNU/Linux meta distribution."
date: "Fri, 07 Jul 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Articles
image: "images/instalando_pacotes_snap_no_gentoo.jpeg"
---

This is a super quick tip and it's for everyone using the meta distribution [Gentoo](//www.gentoo.org/ "Get to know Gentoo GNU/Linux"), because Today we are going to see how to install Canonical's snap package manager and install our first program through it.  

Don't know what a snap is? [Click here](//blog.doseextra.com/o-que-sao-ubuntu-snaps/ "What is snap?") and find out.


### Terminal


First we go to the terminal to make the first configurations.


With it open, let's add the snappy repository, creating the following file with the nano editor:


`$ sudo nano -w /etc/portage/repos.conf/gentoo-snappy.conf`


In the file, add the following information:  

`[gentoo-snappy]`  

`location = /usr/local/portage/gentoo-snappy`  

`sync-type = git`  

`sync-uri = https://github.com/zyga/gentoo-snappy.git`  

`priority = 50`  

`auto-sync = yes`


Save changes by pressing Ctrl and *“O”(Ctrl + O)* and then *Enter*.  

With the file saved, let's type the following:  

`$ sudo emaint sync --repo gentoo-snappy`


Wait for the action to finish, which shouldn't take long, and install the main package:  

`$ sudo emerge -av app-emulation/snapd`


And then enable program startup:


`$ sudo systemctl enable --now snapd.service`


Done! The package manager is installed and ready to use.  

To test, let's install Hugo, typing the following command:  

`$ sudo snap install hugo`


If everything went correctly, you can call Hugo with the command `hugo` in the terminal.


That's it for today, don't miss our tips by liking our page on [Facebook](//facebook.com/doseextra "Follow us on Facebook") or following us on [Twitter](//twitter.com/sitedoseextra "Follow us on Twitter").

