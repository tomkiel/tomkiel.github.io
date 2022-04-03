---
title: "Instalando e configurando o gerador de sites Hugo"
description: "Saiba como instalar e começar um projeto no gerenciador de sites Hugo. Gere sites estáticos facilmente."
type: "post"
date: "Sat, 01 Jul 2017 03:00:00 +0000"
author: "Regis Tomkiel"
categories: 
- artigos
image: "images/instalando_e_configurando_o_gerador_de_sites_hugo.jpeg"
---

O objetivo desse artigo é demonstrar os primeiros passos na criação de um site no Hugo, portanto, não espere nada muito avançado, pois o foco é para quem nunca viu ele funcionando.


### Instalação


Iremos abordar a instalação em sistemas GNU/Linux, mais precisamente, usando pacotes Snaps no Gentoo Linux. É um método muito fácil e que ajuda a manter o Hugo sempre atualizado e funcionando sem qualquer configuração adicional.  

Para saber como instalar snaps no Gentoo, [acesse aqui](# "como instalar snaps no Gentoo").  

**Bom, vamos ao processo!**


#### 1° – Acessando o terminal


Para realizar a instalação, abra o aplicativo de terminal, neste caso estou usando o Gnome Shell e o programa padrão, o gnome-terminal ou simplesmente “terminal”.![Instalando o Hugo com o Snap](https://i.imgur.com/LqOQRat.jpg "Como instalar o gerador de sites Hugo")


Com ele aberto, digite o seguinte comando:  

`sudo snap install hugo`


Aguarde o término da instalação e verifique a versão do Hugo:  

`hugo version`  

![Verificando a versão do Hugo](https://i.imgur.com/ItqSO0z.jpg "Versão do gerador de sites Hugo")


Com a instalação bem sucedida, é hora de começar o site.


#### 2° – Criando seu primeiro site


Crie uma pasta chamada Sites na home:  

`mkdir $HOME/Sites`


Acesse a pasta:  

`cd $HOME/Sites`


Crie o primeiro projeto:`hugo new site meu-primeiro-projeto`  

![Criando o primeiro projeto](https://i.imgur.com/jdBAkgr.jpg "Criando o primeiro projeto com o Hugo")


Abra a pasta `$HOME/Sites` em seu editor de texto preferido, como o [Gedit](https://wiki.gnome.org/Apps/Gedit "Editor de texto do Gnome") ou [Atom](https://atom.io/ "Editor de textos Atom"), por exemplo. Eu utilizei o [nano](https://www.nano-editor.org/ "Editor GNU/Nano").


Neste primeiro momento, vamos realizar só as configurações necessárias para o site ser minimamente acessado. Portanto, o próximo passo é procurar e baixar um *template* para nosso projeto. Acesse [este link](# "baixar o tema crap") ou utilize o git.  

`git clone https:https://github.com/thomasheller/crab.git`  

![Baixando um tema para o Hugo](https://i.imgur.com/qDkwG3S.jpg "Baixando um tema simples para o projeto")


Para o tema funcionar, mova a pasta “crab” para o diretório `$HOME/Sites/meu-primeiro-projeto/themes/`, assim:  

`$ mv crap $HOME/Sites/meu-primeiro-projeto/themes/`  

![Movendo o tema para a pasta correta](https://i.imgur.com/PyIh8wg.jpg "Movendo o tema para a pasta correta no projeto")


Para testar o site, acesse a pasta raiz de seu projeto:  

n`$ cd $HOME/Sites/meu-primeiro-projeto`


Com o editor de texto, abra o arquivo config.toml e digite a seguinte linha:  

`theme = “crab”`  

![Editando o arquivo de configurações](https://i.imgur.com/HRQJler.jpg "Editando o arquivo de configurações config.toml")


Novamente no terminal, digite:  

`$ hugo server`  

![Iniciando o servidor de desenvolvimento](https://i.imgur.com/22nJDK0.jpg "Iniciando nosso servidor com a prévia do site")


Abra o navegador e acesse o endereço <http:https://localhost:1313> e seu site vai estar funcionando e nem precisa de Apache instalado na máquina.


![Acessar o site pelo navegador](https://i.imgur.com/4Sopw63.jpg "Acessando o site no navegador")


#### 3° – Personalizando e configurando


Agora, com seu editor de código preferido, abra o arquivo *config.toml*. É nele que as principais configurações serão feitas, como a definição da URL base do site, definição do tema escolhido, título, dentre muitas outras.  

Para começar é importante ler a documentação do Hugo e seguir a sequência de artigos do blog. O próximo será sobre as principais configurações do site, não perca.

