---
title: "Gerador de site estático"
description: "Saiba como instalar e começar um projeto no gerenciador de sites Hugo. Gere sites estáticos facilmente."
type: "post"
date: "Sun, 02 Jul 2017 03:00:00 +0000"
author: "Regis Tomkiel"
categories: 
- artigos
image: "images/gerador_de_site_estatico.jpeg"
---

Quando a *Google* lançou a Go sob a licença BSD, disponibilizou para a comunidade uma linguagem de programação compilada focada em produtividade, que se assemelha a *C* e possui fácil aprendizado. O que é mais legal disso tudo, é que com a Go, foi criado o Hugo, um gerador de sites que preza pela eficiência e desempenho.


### O Hugo


O Hugo é basicamente um gerador de site estático, ou seja, diferente de um CMS em php, onde os códigos são interpretados em tempo real no servidor, com o Hugo, nosso site é gerado através de blocos localmente e o resultado, é o projeto já em html. Parece confuso, mas na verdade é simples.  

São inúmeras vantagens e as principais tangem desempenho e segurança. Como nosso site é HTML puro, as chances de le sofrer ataques expressivos é muito baixa e caso acontecessem, é muito fácil realizar a manutenção, bastando gerar o site novamente. Provavelmente os problemas estaria no ambiente de hospedagem e não nos arquivos.  

Também, como o site é todo html, não é necessário banco de dados e nem mesmo php. O projeto já está hospedado com todas as páginas prontas, sem necessidades de novas consultas. Algo positivo é a facilidade em hospedar um site em html. Qualquer ambiente está preparado para tal, inclusive o GitHub Pages, que tem uso gratuito.


### Hugo vs WordPress


Primeiramente é importante lembrar que o Hugo não é um CMS e nem mesmo possuí uma interface gráfica para gerenciamento de conteúdo. Todavia, é relativamente simples utilizar o GitHub em conjunto. Com ele, além do versionamento, podemos facilitar a inclusão de artigos, usando um editor simples para o texto e uma linha de comando para submeter para aprovação.  

O Wordpess possuí mais recursos e ao mesmo tempo, necessitam de mais recursos, é claro. É muito simples hospedar um site WordPress, desde que seja possível criar um banco de dados e o servidor rode php. O problema está no desempenho, já que todos esses serviços exigem bastante de qualquer servidor e por consequência, também exigem servidores com melhores configurações.  

Ainda vou publicar uma série de artigos sobre otimização do WordPress e demonstrar que é possível ter bons resultados com ele. Por hora, atento-me às dependências numerosas e falta de simplicidade.


### Facilidade


Inicialmente, migrar um template projetado para o WordPress para a utilização no Hugo foi simples. Entendendo razoavelmente a lógica de funcionamento, em poucas horas o site estava pronto para receber conteúdo. As “divisões” são de fácil entendimento e o uso de diretórios ajuda.  

O bom, é que a organização pode ser muito personalizada e não são necessários plugins adicionais. Para replicar os “posts types” do nosso blog, bastou organizar o código em pastas e definir IDs no arquivo para publicação.


### Dificuldades


Nem tudo são flores, é claro.  

Esqueça conteúdo dinâmico, Ajax e formulários. Sites estáticos não sabem lidar com isso e é preciso recorrer à criatividade para solucionar esses problemas. Para o formulário de contatos, estamos usando o formspreee.io que permite 1000 envios mensais gratuitamente e adiciona uma camada de segurança com captcha e controle de spam. Para o resto, foram feitas algumas adaptações pontuais.  

Alguns bugs ainda estão sendo corrigidos e o projeto pode ser acompanhado por nosso repositório no GitHub.


E para finalizar e não transformar este texto num livro, basta [ler este artigo](//blog,doseextra.com/comecando-com-o-hugo/ "Primeiros passos com o Hugo") sobre os primeiros passos com o Hugo.

