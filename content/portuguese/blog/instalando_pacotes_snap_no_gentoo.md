---
title: "Instalando pacotes snap no Gentoo"
description: "No artigo de hoje vamos instalar o gerador de sites estáticos Hugo na meta distribuição Gentoo GNU/Linux."
type: "post"
date: "Fri, 07 Jul 2017 03:00:00 +0000"
author: "Regis Tomkiel"
categories: 
- artigos
image: "images/instalando_pacotes_snap_no_gentoo.jpeg"
---

Esta é uma dica super rápida e é para todos que utilizam a meta distribuição [Gentoo](//www.gentoo.org/ "Conheça o Gentoo GNU/Linux"), pois hoje vamos ver como instalar o gerenciador de pacotes snap da Canonical e de quebra, instalar nosso primeiro programa por ele.  

Não sabe o que é o snap? [Clique aqui](//blog.doseextra.com/o-que-sao-ubuntu-snaps/ "O que é snap?") e conheça.


### Terminal

Primeiramente vamos ao terminal para realizarmos as primeiras configurações.

 1. Com ele aberto, vamos adicionar o repositório do snappy, criando o seguinte arquivo com o editor nano:  

{{<code class="language-bash">}}$ sudo nano -w /etc/portage/repos.conf/gentoo-snappy.conf {{</code>}}

 2. No arquivo, adicione as seguintes informações:  

{{<code class="language-textile">}}
[gentoo-snappy]  
location = /usr/local/portage/gentoo-snappy
sync-type = git
sync-uri = https://github.com/zyga/gentoo-snappy.git  
priority = 50
auto-sync = yes

{{</code>}}


 3. Salve as alterações pressionando as teclas **Ctrl** e **O** **(Ctrl + O)** e depois *Enter*.  Com o arquivo salvo, vamos digitar o seguinte:  

{{<code class="language-bash">}}$ sudo emaint sync --repo gentoo-snappy{{</code>}}

 4. Aguarde o término da ação, que não deve demorar muito e instale o pacote principal:  

{{<code class="language-bash">}}$ sudo emerge -av app-emulation/snapd {{</code>}}


 5. E depois habilite a inicialização do programa:  

{{<code class="language-bash">}}$ sudo systemctl enable --now snapd.service {{</code>}}

Pronto! O gerenciador de pacotes está instalado e pronto para ser utilizado.  

 6. Para testarmos, vamos instalar o Hugo, digitando o seguinte comando:  

{{<code class="language-bash">}}$ sudo snap install hugo {{</code>}}


Se tudo ocorreu corretamente, você poderá chamar o Hugo com o comando ***hugo*** no terminal.  

{{<code class="language-bash">}}$ hugo {{</code>}}

Por hoje é isso, não perca nossas dicas curtindo nossa paǵina no [Facebook](//facebook.com/doseextra "Nos siga no Facebook") ou seguindo no [Twitter](//twitter.com/sitedoseextra "Nos siga no Twitter").

