---
title: "Instalowanie pakietów snap w Gentoo"
description: "W dzisiejszym artykule zamierzamy zainstalować generator stron statycznych Hugo w meta-dystrybucji Gentoo GNU/Linux."
date: "Fri, 07 Jul 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Artykuł
image: "images/instalando_pacotes_snap_no_gentoo.jpeg"
draft: true
---

To bardzo szybka wskazówka dla wszystkich użytkowników metadystrybucji [Gentoo](//www.gentoo.org/ "Poznaj Gentoo GNU/Linux"), ponieważ Dzisiaj zobaczymy, jak zainstalować menedżera pakietów snap firmy Canonical i za jego pośrednictwem zainstalować nasz pierwszy program.  

Nie wiesz, co to jest przystawka? [Kliknij tutaj](//blog.doseextra.com/o-que-sao-ubuntu-snaps/ "Co to jest przystawka?") i dowiedz się.


### Terminal


Najpierw przechodzimy do terminala, aby dokonać pierwszych konfiguracji.


Po otwarciu dodajmy repozytorium Snappy, tworząc następujący plik za pomocą edytora nano:


`$ sudo nano -w /etc/portage/repos.conf/gentoo-snappy.conf`


W pliku dodaj następujące informacje:  

`[gentoo-snappy]`  

`lokalizacja = /usr/local/portage/gentoo-snappy`  

`sync-type = git`  

`sync-uri = https://github.com/zyga/gentoo-snappy.git`  

`priorytet = 50`  

`automatyczna synchronizacja = tak`


Zapisz zmiany, naciskając Ctrl i *„O” (Ctrl + O)*, a następnie *Enter*.  

Po zapisaniu pliku wpiszmy:  

`$ sudo emaint sync --repo gentoo-snappy`


Poczekaj na zakończenie akcji, co nie powinno zająć dużo czasu, i zainstaluj główny pakiet:  

`$ sudo emerge -av app-emulation/snapd`


A następnie włącz uruchamianie programu:


`$ sudo systemctl enable --now snapd.service`


Gotowe! Menedżer pakietów jest zainstalowany i gotowy do użycia.  

Aby przetestować, zainstalujmy Hugo, wpisując następujące polecenie:  

`$ sudo snap install hugo`


Jeśli wszystko poszło poprawnie, możesz zadzwonić do Hugo za pomocą polecenia `hugo` w terminalu.


To wszystko na dziś, nie przegap naszych wskazówek, polubienie naszej strony na [Facebook](//facebook.com/doseextra "Obserwuj nas na Facebooku") lub śledząc nas na [Twitter](//twitter.com/sitedoseextra "„Obserwuj").

