---
title: "Blog jest teraz statyczny"
description: "Przeprowadziliśmy migrację z WordPressa! Teraz blog jest generowany za pomocą Hugo i GitHub!"
date: "Fri, 30 Jun 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Artykuł
image: "images/o_blog_agora_e_estatico.png"
---

Zawsze opowiadałem się za WordPressem i korzystaniem z przyjaznego dla użytkownika systemu CMS, ponieważ nie każdy ma wystarczającą wiedzę, aby zapuszczać się w bardziej złożone alternatywy. Sam używam WordPressa w kilku ważnych projektach i nadal uważam, że jest to jedno z najbardziej kompletnych narzędzi w dzisiejszych czasach, ale…


### Wydajność


Nikomu nie jest wiadomo, że WordPress jest małym potworem pod względem zużycia zasobów, zwłaszcza gdy jest źle skonfigurowany. Aby CMS działał, potrzebujemy serwera Apache lub Ngnix, PHP i MySQL. Wszystko to razem może być koszmarem dla firmy hostingowej. Obecnie polegamy na serwerach Digital Ocean dla naszych witryn i niektórych klientów. Nawet przy znacznie lepszych ustawieniach niż większość brazylijskich obiektów noclegowych, nie jest trudno wygenerować wąskie gardło, o ile nie zostaną wprowadzone odpowiednie ustawienia. Nie zaleca się korzystania z VPS w wysokości 10,00 USD, aby mieć wszystkie usługi razem.  

Większość wprowadzonych przeze mnie ustawień dotyczy korzystania z pamięci podręcznej, automatyzacji skryptów i korzystania z sieci CDN. Witryna, do której uzyskujesz dostęp w Twojej przeglądarce, jest „migawką” oryginalnej witryny, mam na myśli statyczną wersję treści, a nie coś w czasie rzeczywistym. Witryna zawiera już cały kod HTML, prawda?


### Zmiany


Po wielu badaniach nad ulepszaniem naszych usług stwierdziliśmy, że nie można po prostu wydać więcej pieniędzy, konieczne jest zoptymalizowanie tego, co już mamy. Dlatego zdecydowaliśmy się m.in. na migrację jednego z serwerów do FreeBSD i wykonanie na nim ustawień wydajności. Wszystkie nasze serwery to Linux i powody tej zmiany wyjaśnię w innym poście.n Korzystając z tego, co się stało, postanowiłem przestudiować sposoby na ulepszenie naszych stron i jednocześnie przestudiować coś zupełnie nowego. Jedną z pierwszych opcji było użycie Hugo do lokalnego generowania stron statycznych, zmniejszając na przykład potrzebę bazy danych.


### Hugo


Poznałem [Hugo](//gohugo.io) przez portal [Stoły](//tableless.com.br/site -tableless-static/), które również wprowadziły zmiany w witrynie, porzucając WordPress i potrzebę utrzymania struktury wielu serwerów. W oparciu o zeznania [Diego Eisa](//tableless.com.br/author/diego-eis/) miałem ochotę dowiedzieć się więcej o tym takim jak Hugo.  

Nie jest to CMS, nie wymaga MySQL, PHP i nie posiada pewnych „funkcji”, takich jak edytor graficzny i logowanie użytkownika. W rzeczywistości jest przeznaczony do użytku lokalnego, w połączeniu z dowolnym edytorem tekstu. Z tych powodów na początku wydawało mi się to dość dziwne… Byłem zaskoczony, jak łatwe i proste to było. Hugo jest napisany w GO, a jego składnia to praktycznie mówiony angielski, to takie proste. W ciągu tygodnia moja strona internetowa została w pełni zmigrowana na platformę.  

W przyszłości chcę pisać artykuły i tutoriale do użytku, chcę też zademonstrować migrację witryn na platformę.


### Więcej otwartego oprogramowania


Jeśli wcześniej utrzymanie witryny WordPress na GitHub było praktycznie niemożliwe, z Hugo tak nie jest. Nasze projekty migrują tam i będą dostępne do użytku i nauki. Utrzymanie tam witryny internetowej jest bardzo łatwe…


### Teraz-nasz-blog jest otwarty


Możesz nam pomóc i zostać autorem, ponieważ teraz znacznie łatwiej jest przesłać artykuł. Wystarczy wiedzieć, jak minimalnie korzystać z GitHub i dzielić się wiedzą. ![🙂](https://sworg/images/core/emoji/12.0.0-1/72x72/1f642.png)  

Bez użycia CMS logowanie nie jest wymagane, a całe zarządzanie treścią odbywa się za pośrednictwem repozytorium GitHub przez *żądania ściągania*.


### Na przyszłość


Jesteśmy coraz bardziej skoncentrowani na tworzeniu odpowiednich treści, dlatego planujemy artykuły i samouczki na kilka następnych dni, w tym więcej artykułów na temat tworzenia stron internetowych, WordPressa i Hugo.



> Tworzenie i udostępnianie treści jest tym, co nas napędza!
> 
> 

