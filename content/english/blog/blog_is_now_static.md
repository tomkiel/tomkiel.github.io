---
title: "Blog is now static"
description: "We migrated from WordPress! Now the blog is generated with Hugo and GitHub!"
date: "Fri, 30 Jun 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Articles
image: "images/o_blog_agora_e_estatico.png"
---

I have always advocated WordPress and the use of a user-friendly CMS, as not everyone is knowledgeable enough to venture into more complex alternatives. I myself use WordPress on several important projects and I still believe that it is one of the most complete tools today, but…


### Performance


It's not news to anyone that WordPress is a little monster in terms of resource consumption, especially when poorly configured. To get the CMS working, we need an Apache or Ngnix server, PHP and MySQL. All this running together can be a hosting company's nightmare. We currently rely on Digital Ocean servers for our sites and for some clients. Even with much better settings than the vast majority of Brazilian accommodations, it is not difficult to generate a bottleneck, as long as the appropriate settings are not made. A VPS of US$10.00 is not recommended to have all services together.  

Most of the settings I've made concern the use of caching, script automation and the use of CDNs. The website that is accessed in your browser is a “snapshot” of the original website, I mean it is a static version of the content and not something in real time. The site is already all HTML, isn't it?


### Changes


After a lot of study on improving our services, we found that it is not possible to simply spend more money, it is necessary to optimize what we already have. Therefore, we decided, among other things, to migrate one of the servers to FreeBSD and perform performance settings on it. All our servers are Linux and I will explain the reasons for the change in another post. n Taking advantage of what happened, I decided to study ways to improve our sites and also, at the same time, to study something entirely new. One of the first options was to use Hugo to generate static pages locally, reducing the need for a database, for example.


### Hugo


I met [Hugo](//gohugo.io) through the portal [Tablesses](//tableless.com.br/site -tableless-static/), which also made the change to the site, ditching WordPress and the need for multiple servers to maintain the structure. Based on the testimony of [Diego Eis](//tableless.com.br/author/diego-eis/), I was tempted to learn more about this such as Hugo.  

It is not a CMS, it doesn't need MySQL, PHP and it doesn't have some “features” like a graphical editor and user login. In fact, it is designed to be used locally, in conjunction with any text editor. For these reasons, it seemed quite strange to me at first…I was surprised at how easy and simple it was. Hugo is written in GO and its syntax is practically spoken English, it's so simple. Within a week, I had a website fully migrated to the platform.  

In the future I want to write articles and tutorials for use, I also want to demonstrate the migration of sites to the platform.


### More Open Source


If before, maintaining a WordPress site on GitHub was practically impossible, with Hugo it is not. Our projects are migrating there and will be available for use and study. It is very easy to maintain a website there…


### Now-our-blog is open


You can help us and become an author as it is now much easier to submit an article. Just know how to use GitHub minimally and be willing to share knowledge. ![🙂](https://sworg/images/core/emoji/12.0.0-1/72x72/1f642.png)  

Without the use of CMS, no login is required and all content management is done through the GitHub repository by *pull requests*.


### For the future


We are increasingly focused on creating relevant content and with that, we plan articles and tutorials for the next few days, including more articles on website development, WordPress and Hugo.



> Creating and sharing content is what drives us!
> 
> 

