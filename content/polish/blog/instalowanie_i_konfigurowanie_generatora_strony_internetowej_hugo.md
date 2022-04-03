---
title: "Instalowanie i konfigurowanie generatora strony internetowej Hugo"
description: "Dowiedz się, jak zainstalować i uruchomić projekt w menedżerze witryny Hugo. Łatwe generowanie statycznych stron internetowych."
date: "Sat, 01 Jul 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Artykuł
image: "images/instalando_e_configurando_o_gerador_de_sites_hugo.jpeg"
---

Celem tego artykułu jest zademonstrowanie pierwszych kroków w tworzeniu strony internetowej w Hugo, więc nie oczekuj niczego zbyt zaawansowanego, ponieważ skupiamy się na tych, którzy nigdy nie widzieli, jak działa.


### Instalacja


Omówimy instalację na systemach GNU/Linux, a dokładniej przy użyciu pakietów Snaps w Gentoo Linux. Jest to bardzo prosta metoda, dzięki której Hugo jest zawsze aktualny i działa bez dodatkowej konfiguracji.  

Aby dowiedzieć się, jak zainstalować przystawki w Gentoo, [kliknij tutaj](# "jak zainstalować przystawki w Gentoo").  

**OK, przejdźmy do procesu!**


#### 1° – Dostęp do terminala


Aby zainstalować, otwórz aplikację terminala, w tym przypadku używam powłoki Gnome i domyślnego programu, gnome-terminal lub po prostu „terminal”.![Instalowanie Hugo za pomocą Snap](https://i.imgur.com/LqOQRat.jpg "Jak zainstalować generator witryn Hugo")


Po otwarciu wpisz następujące polecenie:  

`sudo snap install hugo`


Poczekaj na zakończenie instalacji i sprawdź wersję Hugo:  

`wersja Hugo`  

![Sprawdzanie wersji Hugo](https://i.imgur.com/ItqSO0z.jpg "Wersja generatora witryny Hugo")


Po pomyślnej instalacji nadszedł czas, aby uruchomić witrynę.


#### 2° – Tworzenie pierwszej witryny


Utwórz folder o nazwie Witryny w domu:  

`mkdir $HOME/Sites`


Przejdź do folderu:  

`cd $HOME/Sites`


Utwórz pierwszy projekt:`hugo nowa witryna mój-pierwszy-projekt`  

![Tworzenie pierwszego projektu](https://i.imgur.com/jdBAkgr.jpg "Tworzenie pierwszego projektu z Hugo")


Otwórz folder `$HOME/Sites` w preferowanym edytorze tekstu, takim jak [Gedit](https://wiki.gnome.org/ Apps/Gedit Na przykład  "Gnome Text Editor") lub [Atom](https://atom.io/ "Atom Text Editor"). Użyłem [nano](https://www.nano-editor.org/ "GNU/Nano Editor").


W pierwszej chwili wprowadzimy tylko niezbędne ustawienia, aby dostęp do witryny był minimalny. Następnym krokiem jest więc wyszukanie i pobranie *szablonu* dla naszego projektu. Przejdź do [ten link](# "download crap theme") lub użyj git.  

`git klon https:https://github.com/thomasheller/crab.git`  

![Pobieranie motywu dla Hugo](https://i.imgur.com/qDkwG3S.jpg "Pobieranie prostego motywu dla projektu")


Aby motyw działał, przenieś folder „krab” do katalogu `$HOME/Sites/my-first-project/themes/` w następujący sposób:  

`$ mv bzdura $HOME/Sites/mój-pierwszy-projekt/motywy/`  

![Przenoszenie motywu do właściwego folderu](https://i.imgur.com/PyIh8wg.jpg "Przenoszenie motywu do odpowiedniego folderu w projekcie")


Aby przetestować witrynę, przejdź do folderu głównego projektu:  

n`$ cd $HOME/Sites/mój-pierwszy-projekt`


Za pomocą edytora tekstu otwórz plik config.toml i wpisz następujący wiersz:  

`theme = "krab"`  

![Edycja pliku ustawień](https://i.imgur.com/HRQJler.jpg "Edycja pliku ustawień config.toml")


Ponownie w terminalu wpisz:  

`serwer $ hugo`  

![Uruchamianie serwera programistycznego](https://i.imgur.com/22nJDK0.jpg "Uruchamianie naszego serwera z podglądem strony")


Otwórz przeglądarkę i uzyskaj dostęp do adresu [http://localhost:1313](http://localhost:1313), a Twoja witryna będzie działać, a Ty nie nawet potrzebujesz zainstalowanego Apache na komputerze.


![Dostęp do witryny w przeglądarce](https://i.imgur.com/4Sopw63.jpg "Dostęp do witryny w przeglądarce")


#### 3° – Dostosowywanie i konfiguracja


Teraz, korzystając z wybranego edytora kodu, otwórz plik *config.toml*. To tam zostaną wprowadzone główne ustawienia, takie jak definicja podstawowego adresu URL witryny, definicja wybranego motywu, tytuł i wiele innych.  

Aby rozpocząć, ważne jest, aby przeczytać dokumentację Hugo i postępować zgodnie z sekwencją artykułów na blogu. Następny będzie dotyczył głównych ustawień witryny, nie przegap tego.

