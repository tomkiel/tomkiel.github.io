---
title: "Produkcja wideo w systemie Linux – część 3"
description: "Po serii artykułów na temat produkcji wideo w systemie Linux, dzisiaj porozmawiamy o niesławnych i problematycznych kodekach &#8221;! Kodeki i ProRes w systemie Linux."
date: "Wed, 07 Jun 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Artykuł
image: "images/producao_de_videos_no_linux_–_parte_3.jpeg"
draft: true
---

>>>>>> (ang.). Jeśli stracisz poprzednie artykuły, sprawdzamy następujące powiązki: 

.

Today, temat ten jest o wiele bardziej techniczny i bardzo mało adresowany na stronach internetowych dla naszego ukochanego GNU/Linux. Jeśli podążasz za innymi artykułami, wiesz, że platforma *Open Source* ma bardzo dobry zakres oprogramowania redagowania, kompozycji i korekcji koloru. n


###  Wiemy, że programy nie są naszym zaniepokojeniem, ale co o kodekach?

>
>. *codecs* u "*decoders*" są odpowiedzialne za translację konkretnego pliku multimedialnego, czy jest to wideo, u audio image, w czytelnych informacjach w oprogramowaniu odtwarzania wizualnego. W uproszczeniu operacja jest podobna do pracy tłumacza czasu rzeczywistego, który słucha angielskiego mówca i gdy rozmowa się odbywa się w Portugalii. Wobec tego wszyscy w bluzili mogą wiedzieć, co brytyjski wywiad odpowiada prezenterowi. łatwe? (pol.).
>>>>>> (ang.). Teraz wyobraża sobie, że konferansjer nie mówi wystarczająco dobrze, u gorszy, stara się powstrzymać naszego tłumacza. Na pewno wynik będzie zupełnie inny niż oczekiwano, a być może jego umiejętności są kwestionowane. Jest mniej tego, co się dzieje z pewnym oprogramowaniem.
>. W przypadku reprodukcji treści, w przypadku *Ubuntu*, znajduje się pakiet 

 (ang.).
### Licences of course (ang.). Znaczna część kosztów oprogramowania musi zapłacić *royalties* oo z technologii trzecich i mediów. Posiada również rozwój i dystrybucję, ale w zależności od strategii rynku może być wchłonięta w sprzedaży sprzętu. Ponieważ firma musi unikać problemów prawnych, wolne wersje często mają ograniczenia.
>>> >>>>>>>>>>>>>>>>>>>> (ang.). Nie przeszkodzi to oo z narzędzia, wymaga jedynie kilku adekumentów na zakup całkowitej licencji. W przypadku  [BlackMagic](https:/www.blackmagicdesign.com/br) jego rozwiązania są zaskakująco kompletne i przechodzące problemy kodowe są bardzo proste.
 Video Production in linux and FFmpg (ang.).
Yes, rozwiązanie jest bardzo proste i przynosi jej tylko dodatnie punkty. Pozwólcie lepiej wyjaśnić!
Kod h.264 jest bardzo zły i bardzo zwarty. Jest ona dla strony internetowej, ponieważ ratuje wiele megas i jest to bardzo ważne dla *streamming*. Jednak dla edytacji kanałów wideo oznacza, że wiele informacji zostało utraconych. Jest to bardzo duży problem, kiedy ogarnianie wymagań, które tylko obsługują ten format, ponieważ niektóre informacje są utracone. n Połączenie dawinci i czarnej magii nie powstają tego formatu w wersji linux. Możliwe i przyszłe wersje są rozwiązane, ale nie ma komentarza na stronie..
ffmpg and conversion to cudowne [em](https:/pt.wikipedia.org/wiki/Apple_ProRes) Nawet w godzinach x, już przerobiłem wideoklipy do proresu, modlił się dla tego konkretnego oprogramowania. Z konwersją plik staje się gigantyczny i pozwala na edytację, aby pracować z wieloma większymi kolorami.
"A bad video will always be bad" (ang.).
Nie ma cudów, filmy nie zyskują informacji, które nie istnieją w pliku. Jeśli wideo jest w niskiej jakości i w złych warunkach oświetlenia, nie będzie miał takich samych korzyści jak formaty *RAW i stał się kolejnym filmem [>>>>>> (ang.). Dodatkowym punktem wyjścia jest konwersja wideo do sekwencji obrazów w png w celu ekstrakcji tego konkretnego obrazu!](http:/globo.com/Cultura/noticia/2016/09-filmes-dequento-in-tarantino-quecis-precissasopen. Co się dzieje, gdy dekompresuje wideo, damy bardziej możliwości edytacji oprogramowania do pracy z kolorowaniem i poprawkami. Jest łatwo zrozumieć różnice z wykorzystaniem.
#4 Nie jest zbyt łatwo rozwiązywać tego!</h4>.
* pakiet ffmpeg jest prawdziwym szwajcarskim knivem i pozwala nam na liczne możliwości. Jest bardzo popularny, a niektóre z nich są rodzimymi pakietami. W przypadku ffmpeg można przekształcić na prory i więcej. *
Proszę modlitwy Ubuntu: </p>
Do instalacji:n<strong>sudo apt-get instaluje ffmpeg</strong></p>.
<p>Converting for ProRes:<br />>> (ang.).
– ARQUIVO_ORIGINAL (ang.). W:v prores - Profil:v 3 -c:a pcm_s16le _s16le _ (ang.).
<p>Remembering that -profile może być 0='proxy', 1='lt', 2='standard', 3='hq', odpowiadający „perfilowi” konwersji.
>. Ostateczny plik zostanie wygenerowany w tym samym folderze i będzie gotowy do pracy. <imgsrc=)*.
**ffmpeg -i video (ang.). mp4 image: 18d148ad3441823a8fee22738b7dc7e707336e18b24c8c31273dc9aff94ae9b3}d.png</strongerstwo.**

