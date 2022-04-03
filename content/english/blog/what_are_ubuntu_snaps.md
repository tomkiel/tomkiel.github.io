---
title: "What are Ubuntu Snaps?"
description: "Do you know what Snaps packages are? And do you know how they work on Linux?"
date: "Sat, 01 Jul 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- web development
image: "images/o_que_sao_ubuntu_snaps.jpeg"
---

One of the coolest things about GNU/Linux is the freedom of choice. It's something that doesn't exist on any other platform and that allows for greater control over what's happening. I don't see myself using another *OS*.  

The problem is related to the installation of programs and the lack of default. Today the files *.deb* and *.rpm* are predominant and adopted even by *Google* in the availability of its programs. Those who do not follow these standards had to turn around at 30 to be able to install the programs.


### The solution would be to adopt the .deb and .rpm files?


**Not exactly!**


Linux and its libraries are constantly being updated and not all distributions care about maintaining compatibility with older programs and what we see, most of the time, is a big puzzle when a program is not updated or is discontinued. Then, no installing that old program, but it would still work perfectly.


To solve this, many initiatives were designed, such as *Appimage*, *Fltapack* and *Snappy*. The difference is that here the packages are offered with their libraries and thus, they work independently of the system or system version. The idea is to have universal packages, which can be installed on all systems without changes or adaptations.


To improve the explanation, imagine the files as a *.zip* file. This file is our program. In .deb format we would only have the program itself inside this file and we would need more packages for it to work properly. Now imagine that all these packages were repackaged in another .zip and thus, generating only one file.  

Of course, this increases the size of the package, but at the same time it guarantees the program to work on any system and in any version.  

Nice, right?


### The Snap


Snap is the technology adopted by Canonical to be used in its ecosystem, such as *Ubuntu Desktop*, Servers and Internet of Things. As the implementation is open source, it didn't take long to be available in other distributions, such as *Gentoo*.  

*Ubuntu 16.04* comes with snappy by default and installing a program with it is simple, as seen in the installation of  [Hugo](# "How to install Hugo").


`$ sudo snap install hugo`


That's it, the software has just been installed and can be used normally. To install on other distributions we use the same command and therefore we will have the same software, ensuring compatibility.


Here's how to [install on Gentoo](# "How to install snaps on Gentoo"), following the same principle.

