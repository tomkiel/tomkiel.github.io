---
title: "Installing and configuring the Hugo website generator"
description: "Learn how to install and start a project in the Hugo site manager. Easily generate static websites."
date: "Sat, 01 Jul 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Articles
image: "images/instalando_e_configurando_o_gerador_de_sites_hugo.jpeg"
---

The purpose of this article is to demonstrate the first steps in creating a website in Hugo, so don't expect anything too advanced, as the focus is for those who have never seen it working.


### Installation


We will cover installing on GNU/Linux systems, more precisely, using Snaps packages on Gentoo Linux. It's a very easy method that helps to keep Hugo always up to date and working without any additional configuration.  

To learn how to install snaps in Gentoo, [click here](# "how to install snaps in Gentoo").  

**Okay, let's get to the process!**


#### 1° – Accessing the terminal


To install, open the terminal application, in this case I'm using the Gnome Shell and the default program, gnome-terminal or simply “terminal”.![Installing Hugo with Snap](https://i.imgur.com/LqOQRat.jpg "How to install the Hugo site generator")


With it open, type the following command:  

`sudo snap install hugo`


Wait for the installation to finish and check the Hugo version:  

`hugo version`  

![Checking Hugo version](https://i.imgur.com/ItqSO0z.jpg "Hugo site generator version")


With successful installation, it's time to start the site.


#### 2° – Creating your first site


Create a folder called Sites in the home:  

`mkdir $HOME/Sites`


Go to the folder:  

`cd $HOME/Sites`


Create the first project:`hugo new site my-first-project`  

![Creating the first project](https://i.imgur.com/jdBAkgr.jpg "Creating the first project with Hugo")


Open the `$HOME/Sites` folder in your preferred text editor, such as [Gedit](https://wiki.gnome.org/ Apps/Gedit "Gnome Text Editor") or [Atom](https://atom.io/ "Atom Text Editor"), for example. I used the [nano](https://www.nano-editor.org/ "GNU/Nano Editor").


In this first moment, we will only perform the necessary settings for the site to be minimally accessed. So the next step is to look for and download a *template* for our project. Go to [this link](# "download crap theme") or use git.  

`git clone https:https://github.com/thomasheller/crab.git`  

![Downloading a theme for Hugo](https://i.imgur.com/qDkwG3S.jpg "Downloading a simple theme for the project")


For the theme to work, move the “crab” folder to the `$HOME/Sites/my-first-project/themes/` directory, like this:  

`$ mv crap $HOME/Sites/my-first-project/themes/`  

![Moving the theme to the correct folder](https://i.imgur.com/PyIh8wg.jpg "Moving the theme to the correct folder in the project")


To test the site, access your project's root folder:  

n`$ cd $HOME/Sites/my-first-project`


With the text editor, open the config.toml file and type the following line:  

`theme = "crab"`  

![Editing the settings file](https://i.imgur.com/HRQJler.jpg "Editing the config.toml settings file")


Again in the terminal, type:  

`$ hugo server`  

![Starting the development server](https://i.imgur.com/22nJDK0.jpg "Starting our server with the site preview")


Open your browser and access the address <http:https://localhost:1313> and your site will be working and you don't even need Apache installed on the machine.


![Accessing the site in the browser](https://i.imgur.com/4Sopw63.jpg "Accessing the site in the browser")


#### 3° – Customizing and configuring


Now, with your code editor of choice, open the *config.toml* file. It is there that the main settings will be made, such as the definition of the base URL of the site, definition of the chosen theme, title, among many others.  

To get started, it's important to read Hugo's documentation and follow the sequence of blog articles. The next one will be about the main site settings, don't miss it.

