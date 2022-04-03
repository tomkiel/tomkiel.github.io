---
title: "Czym są snap Ubuntu?"
description: "Czy wiesz, czym są pakiety Snaps? A czy wiesz, jak działają w systemie Linux?"
date: "Sat, 01 Jul 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- rozwój sieci
image: "images/o_que_sao_ubuntu_snaps.jpeg"
---

Jedną z najfajniejszych rzeczy w GNU/Linuksie jest wolność wyboru. To coś, co nie istnieje na żadnej innej platformie i pozwala na większą kontrolę nad tym, co się dzieje. Nie widzę siebie używającego innego *OS*.  

Problem związany jest z instalacją programów i brakiem domyślnych. Obecnie pliki *.deb* i *.rpm* są dominujące i stosowane nawet przez *Google* w zakresie dostępności swoich programów. Ci, którzy nie przestrzegają tych standardów, musieli odwrócić się w wieku 30 lat, aby móc zainstalować programy.


### Rozwiązaniem byłoby zaadoptowanie plików .deb i .rpm?


**Niezupełnie!**


Linux i jego biblioteki są stale aktualizowane i nie wszystkie dystrybucje dbają o utrzymanie zgodności ze starszymi programami, a to, co widzimy, przez większość czasu jest wielką zagadką, gdy program nie jest aktualizowany lub jest wycofywany. Wtedy nie trzeba instalować tego starego programu, ale nadal będzie działał idealnie.


Aby rozwiązać ten problem, opracowano wiele inicjatyw, takich jak *Appimage*, *Fltapack* i *Snappy*. Różnica polega na tym, że tutaj pakiety oferowane są ze swoimi bibliotekami, dzięki czemu działają niezależnie od systemu lub wersji systemu. Ideą jest posiadanie uniwersalnych pakietów, które można zainstalować na wszystkich systemach bez zmian lub adaptacji.


Aby ulepszyć wyjaśnienie, wyobraź sobie pliki jako plik *.zip*. Ten plik to nasz program. W formacie .deb mielibyśmy tylko sam program w tym pliku i potrzebowalibyśmy więcej pakietów, aby działał poprawnie. Teraz wyobraź sobie, że wszystkie te pakiety zostały przepakowane do innego .zip, a tym samym wygenerowały tylko jeden plik.  

Oczywiście zwiększa to rozmiar pakietu, ale jednocześnie gwarantuje działanie programu na dowolnym systemie i w dowolnej wersji.  

Fajnie, prawda?


### Pstryknięcie


Snap to technologia przyjęta przez firmę Canonical do wykorzystania w jej ekosystemie, takim jak *Ubuntu Desktop*, serwery i Internet rzeczy. Ponieważ implementacja jest open source, nie trzeba było długo czekać na jej dostępność w innych dystrybucjach, takich jak *Gentoo*.  

*Ubuntu 16.04* jest domyślnie wyposażony w Snappy, a instalacja programu za jego pomocą jest prosta, co widać na przykładzie instalacji [Hugo](# "Jak zainstalować Hugo") .


`$ sudo przystawki zainstaluj hugo`


To wszystko, oprogramowanie zostało właśnie zainstalowane i może być normalnie używane. Aby zainstalować na innych dystrybucjach, używamy tego samego polecenia i dlatego będziemy mieć to samo oprogramowanie, zapewniając kompatybilność.


Oto jak [zainstalować w Gentoo](# "Jak zainstalować snapy w Gentoo"), zgodnie z tą samą zasadą.

