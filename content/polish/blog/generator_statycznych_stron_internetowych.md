---
title: "generator statycznych stron internetowych"
description: "Dowiedz się, jak zainstalować i uruchomić projekt w menedżerze witryny Hugo. Łatwe generowanie statycznych stron internetowych."
date: "Sun, 02 Jul 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Artykuł
image: "images/gerador_de_site_estatico.jpeg"
---

 Gdy  *Google*  wydała Go na licencji BSD, to udostępniane społeczności skompilowany, produktywność ukierunkowana język programowania, który przypomina  *C*  i jest łatwa do nauczenia.. Najfajniejszą rzeczą w tym wszystkim jest to, że z Go, Hugo został stworzony, generator site, że efektywność i wydajność wartości. 


###  Hugo


 Hugo jest w zasadzie statyczna generator stronę internetową, która jest różna od CMS w PHP, gdzie kody są interpretowane w czasie rzeczywistym na serwerze, z Hugo, nasza strona jest generowana przez bloki lokalnie, a wynik, jest projekt już w html. Brzmi to mylące, ale to rzeczywiście proste.   

Istnieje wiele korzyści, a głównymi są wydajność i bezpieczeństwo. Ponieważ nasza strona jest czysty HTML, szanse na to cierpi znaczne ataków jest bardzo niska, a gdyby tak było, to jest bardzo łatwe do przeprowadzenia konserwacji, wystarczy wygenerować stronę ponownie. Prawdopodobnie problemy byłyby w środowisku hostingu, a nie w plikach.   

Poza tym, jak strona jest wszystko html, nie ma potrzeby do bazy danych lub nawet php. Projekt jest już obsługiwany ze wszystkich stron gotowych, bez potrzeby stosowania nowych zapytań. Czymś pozytywnym jest łatwość utrzymania strony internetowej w HTML. Wszelkie środowisko jest przygotowana do tego, w tym GitHub Pages, który jest do wykorzystania. 


###  Hugo vs WordPressie


 Po pierwsze, ważne jest, aby pamiętać, że Hugo nie jest CMS, a nawet nie posiada graficzny interfejs do zarządzania treścią. Jednak jest to stosunkowo proste w użyciu GitHub razem. Dzięki niemu, w uzupełnieniu do wersjonowania, możemy ułatwić publikację artykułów, za pomocą edytora prosty dla tekstu i wiersza polecenia do przedłożenia do zatwierdzenia.   

Wordpess ma więcej funkcji i jednocześnie potrzebuje więcej funkcji, oczywiście. Jest bardzo prosty udostępnić witrynę WordPress, tak długo, jak można utworzyć bazy danych i PHP działa serwer. Problem polega na wydajność, ponieważ wszystkie te usługi wymagają wiele od każdego serwera, a co za tym idzie, również wymagają serwerów z lepszych konfiguracjach.   

Będę nadal publikuje serię artykułów na temat optymalizacji WordPress i wykazać, że jest możliwe, aby mieć dobre wyniki z niego. Na razie, należy zwrócić uwagę na liczne zależności i braku prostoty. 


###  Obiekt


 Na początku migracji szablon przeznaczony dla WordPressa do stosowania w Hugo był prosty. Racjonalnie zrozumieć logikę działania, w ciągu kilku godzin strona była gotowa do odbioru treści. W „podziały” są łatwe do zrozumienia i wykorzystania katalogów pomaga.   

Dobrą rzeczą jest to, że organizacja może być bardzo dostosowane i nie są potrzebne żadne dodatkowe wtyczki. Replikować „post typy” naszego bloga, po prostu musieliśmy zorganizować kod w folderach i określić identyfikatory w pliku do publikacji. 


###  Trudności


 To nie wszystkie kwiaty, oczywiście.   

Zapomnij o dynamicznej zawartości, Ajax i formach. Statyczne strony internetowe nie wiem jak sobie z tym poradzić, a to trwa kreatywności, aby rozwiązać te problemy. Na styku tworzą używamy formspreee.io który pozwala 1000 zgłoszeń miesięcznie za darmo i dodaje warstwę zabezpieczeń z captcha i kontroli spamu. Co do reszty, niektóre adaptacje zostały wykonane.   

Niektóre błędy są jeszcze ustalone, a projekt można śledzić za pośrednictwem naszego repozytorium GitHub. 


 A do końca i nie włączyć ten tekst w książce, po prostu  [przeczytać ten artykuł](//blog,doseextra.com/comecando-com-o-hugo/ "First z Hugo")  o pierwszych krokach z Hugo. 

