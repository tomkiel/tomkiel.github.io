---
title: "static website generator"
description: "Learn how to install and start a project in the Hugo site manager. Easily generate static websites."
date: "Sun, 02 Jul 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Articles
image: "images/gerador_de_site_estatico.jpeg"
---

When *Google* released Go under the BSD license, it made available to the community a compiled, productivity-focused programming language that resembles *C* and is easy to learn. . The coolest thing about all of this is that with Go, Hugo was created, a site generator that values ​​efficiency and performance.


### The Hugo


Hugo is basically a static website generator, that is, different from a CMS in php, where the codes are interpreted in real time on the server, with Hugo, our website is generated through blocks locally and the result, is the project already in html. It sounds confusing, but it's actually simple.  

There are numerous advantages and the main ones are performance and safety. As our site is pure HTML, the chances of it suffering significant attacks is very low and if they did, it is very easy to perform maintenance, just generate the site again. Probably the problems would be in the hosting environment and not in the files.  

Also, as the site is all html, there is no need for a database or even php. The project is already hosted with all pages ready, without the need for new queries. Something positive is the ease of hosting a website in html. Any environment is prepared for this, including GitHub Pages, which is free to use.


### Hugo vs WordPress


Firstly, it is important to remember that Hugo is not a CMS and does not even have a graphical interface for managing content. However, it is relatively simple to use GitHub together. With it, in addition to versioning, we can facilitate the inclusion of articles, using a simple editor for the text and a command line to submit for approval.  

Wordpess has more features and at the same time, needs more features, of course. It is very simple to host a WordPress site, as long as you can create a database and the server runs php. The problem is in performance, as all these services demand a lot from any server and, consequently, also require servers with better configurations.  

I will still publish a series of articles on WordPress optimization and demonstrate that it is possible to have good results with it. For now, pay attention to the numerous dependencies and lack of simplicity.


### Facility


Initially, migrating a template designed for WordPress for use in Hugo was simple. Reasonably understanding the logic of operation, in a few hours the site was ready to receive content. The “divisions” are easy to understand and the use of directories helps.  

The good thing is that the organization can be very customized and no additional plugins are needed. To replicate the “post types” of our blog, we just had to organize the code in folders and define IDs in the file for publication.


### Difficulties


It's not all flowers, of course.  

Forget about dynamic content, Ajax and forms. Static websites don't know how to deal with this and it takes creativity to solve these problems. For the contact form we are using formspreee.io which allows 1000 monthly submissions for free and adds a layer of security with captcha and spam control. For the rest, some adaptations were made.  

Some bugs are still being fixed and the project can be followed through our GitHub repository.


And to finish and not turn this text into a book, just [read this article](//blog,doseextra.com/comecando-com-o-hugo/ "First steps with Hugo")  about the first steps with Hugo.

