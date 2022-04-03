---
title: "GitHub for Beginners"
description: "Learn how to use and configure GitHub easily with a detailed guide."
date: "Mon, 09 Oct 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- web development
image: "images/github_para_iniciantes.jpeg"
---

> The easy way to start with GitHub
 All developers have already needed to organize their source code. is an important part of the development process and without the organization, imagine the madness at correcting a ***bug*** u the simple analysis of changes? without a clear versioning policy, a lot of work may have been thrown out and hours wasted development. *
is not something everyone likes to do, but documentation and version control is indispensable for a good project, even more when we deal with collaboration environments, distinct teams u location. In these scenarios, a simple project can become a true **< in Greek>tragedy** and end up in disaster. organization is fundamental. *
If the more conservatives still use “own” means, there are currently tools focused on the arduous task of facilitating our life. the main tool, is the [git](https://github.com " Meet github"), developed by the kernel creator [Linux](http://linux.org "Site Linux.org") title="GitHub from linus torvalds" href="https://github.com/torvald the tool is simplified and widely adopted, including in the development of the operating system [Windows 10](http://www.diolinux. com.br/2017/05/microsoft-migra-codigo-windows-git.html " Microsoft migrates source code from windows to git")


#### Git is not only GitHub


Bom, I believe that many know that [github)]( is not the only repository option, but is the most known and widespread. many open source projects are hosted and versioned on the platform. in the case of open source projects, the service works free of charge, allowing the addition of expecific functions in the paid mode. for most oraries, the free version is more than enough. *
github uses git for repositories handling and version control. but this oo is not exclusive to github and the git independent of the platform, being used even, for the most adventurous, locally and offline u with any other desired medium. Therefore, learning the basic oo of github will work as an introduction to git in general. >
#### Starting


> The first thing to do, it is obviously to create an orario in the github accessing [this link.)](after that, we are able to venture into the multitude of code projects, documentation, location and what else creativity allows. As an example, using a GNU/Linux environment, we will install git in fedora 26 and clone a repository with editable GIMP file formats. >
**Installing**  

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
< > < > < > < > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > < > > > > > < > > > > > > > > > > > > > > > > > > > < > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > Cloning our first project  

`git clone "https://github.com/tchelinuxorg/resources-grafico.git`


 After that, we have the **< in>graphic resources** folder with all the files and codes in the repository. >
![](//i.imgur.com/tTDjqHQ.jpg "List of cloned files from the repository ") Setting up our git
 Now that we already have the local files, we can edit and who knows how to submit our first commit, right? Yes, but before we need to set up some details. *
the first is our .gitconfig, which must contain at least the orary and email of our account. to add this information just type the following:


< > < > < > < > < > < > < > < > < > < > < > < > > < > < > < > < > < > < > < > < > < > < > < > < > < > < > < > < > < > < > > > < > > > > < > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > The orary of GitHub:  

`git config -global user. name your directory HERE`


< > < > < > < > < > < > < > < > < > < > < > < > > < > < > < > < > < > < > < > < > < > < > < > < > < > < > < > < > < > < > > > < > > > > < > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > The email registered:n`git config -global user.email your E-MAIL HERE`


* These changes are recorded in the /home/SEUUSUARIO/.gitconfig directory and can be viewed with the command:  

`cat ~/.gitconfig`


####  Creating a project fork


Well, we already know how to clone, but how to submit the changes made?  

When it comes to open projects, there are at least two options for the submission of changes. the simplest is through forks and the other is being part of the repository team. *
in this first article, we will see how to create a fork using the GitHub website interface:


== sync, corrected by elderman == " Performing a fork on github" src="//i.imgur.com/Zq8JzoD. jpg alt"= "/ When we create a fork, we are copying the state of development of a project in a new repository, under our orary. and with ready fork, we need to perform the clone again, now in a new folder:  

"https://github. with/yourself/graphic resources.git


 Now we have full freedom of project changes in our repository. knowing this, we'll go to the next step and make our first commit.


> Our first commit
 We say we make some changes to the README file. md, u we added a new file. to inform git our change, we need to enter the command ***add*** of the following form:  

`git add -A`


 Once complete, we need to commit, informing our changes as follows:  

`git commit -m "change of the README file. md and new file addition"`


* To finish and send the files to the server, just finish with the following command:  

`git push`
* Your GitHub orary and password will be requested.
> The pull request
 Now that we fix the README file. md, we wish to inform the developer of this correction. for this, we use the feature called “Pull Request”. that means that we ask the repository administrator to change a file from the initial project, and it is up to him to accept u not our submission. *
to perform our pull request, we will again use the GitHub web interface:


== sync, corrected by elderman == " Performing a "src="//i.imgur.com/czz6ZKx. jpg alt"= / Final conclusions
* This is only the beginning and many other options are available for the use of github. in the next article we will address the concept of ***branch***. >
> For today, be sure to keep up with our channel at the [YouTube](https://www.youtube.com/channel/UC5Zz7kecrmtYZSKCS79_-Wg?view_as=subscriber "Canal "). <img src="https://s.w.org/images/core/emoji/12.0.0-1/72x72/1f609.png" alt="😉 class="wp-smiley" style="height: 1 in; max-height: 1 in;" /<p

