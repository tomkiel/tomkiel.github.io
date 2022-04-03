---
title: "Video Production on Linux – Part 3"
description: "Following our series of articles on Video Production on Linux, today we are going to talk about the infamous and problematic &#8220;codecs&#8221;! Codecs and ProRes on Linux."
date: "Wed, 07 Jun 2017 03:00:00 +0000"
type: "post"
author: "Regis Tomkiel"
categories: 
- Articles
image: "images/producao_de_videos_no_linux_–_parte_3.jpeg"
draft: true
---

 If you have lost the previous articles, check the following links:



Today the subject is much more technical and very little addressed on the websites listing programs for our beloved GNU/Linux. If you have followed the other articles, you know that the platform *Open Source* has a very good range of editing software, composition and color correction. n


###  We know that programs are not our concern, but what about Codecs?


> The *codecs* u "*decoders*" are responsible for translating a certain multimedia file, whether it is video, u audio image, in readable information in a u visualization playback software. simplifying, the operation is similar to the work of a real-time translator, who listens to the English speaker and as the conversation goes on, overlap in Portuguese. so everyone in the brazilian can know what that British interviewee is responding to the presenter. easy, no?
 Now imagine that the announcer does not speak clearly enough, u worse, tries to hinder our translator. certainly the result will be quite different than expected and perhaps the skills of the professional are questioned as well. is more u less that happens with some software. >
> For content reproduction, in the case of the *Ubuntu*, just install the package 


### 
Licences of course! much of the cost of a software so is to pay the *royalties* oo of third-party technologies and media decoders. also has the development and distribution, but that, depending on the market strategy, can be absorbed in the sale of hardware, for example. as the company needs to avoid legal problems, free versions often have some restrictions. >
 This does not prevent the oo of the tool, only require some adequations u the purchase of the complete license. in the case of [BlackMagic](https://www.blackmagicdesign.com/br), its solutions are surprisingly complete and bypassing codec problems is very easy. >
 Video production in linux and FFmpg
Yes, the solution is very simple and brings with it only positive points. Let me explain better!
the h.264 codec is very bad and extremely compacted. it is great for the web as it saves many megas and this is very important for *streamming* u video channels, however, for editing it means that many information has been lost. this is a very big problem when oaring the dslr that only support this format, because some information is lost. n The davinci and blackmagic fusion do not matter these formats in the linux version. maybe and future versions this is solved, but there is no comment on.
ffmpg and conversion to the wonderful [em](https://pt.wikipedia.org/wiki/Apple_ProRes) Even in times of the x, I already converted the dslr videos to prores, praying a specific software for that. with conversion the file becomes giant and allows, when editing, to work with a range of larger colors. >

Of course there are no miracles, videos do not gain information that does not exist in the file. if the video is in a low quality and in bad lighting conditions, it will not have the same benefits of formats *RAW and become the next movie of the  [An extra tip is to convert the video to a sequence of images in png great to extract that specific picture!](http://gq.globo.com/Cultura/noticia/2016/09/20-filmes-de-quentin-tarantino-que-voce-precisa-assisopen. What happens is that when decompressing the video, we give the editing software more possibilities to work with coloring and corrections. it is easy to understand the differences with use. >
#4 >No linux is very easy to solve this!</h4>
* The ffmpeg package is a true Swiss knive and allows us numerous possibilities. it is very popular and there will certainly be native packages in its distribution. with the ffmpeg we can convert to prores and more. *
supposing you are praying Ubuntu:</p>
* To install:n<strong>sudo apt-get install ffmpeg</strong></p>
<p>Converting for ProRes:<br />
-i ARQUIVO_ORIGINAL. avi -c:v prores -profile:v 3 -c:a pcm_s16le _
<p>Remembering that -profile can be 0=‘proxy’, 1=‘lt’, 2=‘standard’, 3=‘hq’, corresponding to the “perfil” of conversion. >
> The final file will be generated in the same folder and will be ready to be imported and worked. <img src=)*
**ffmpeg -i video. mp4 image{18d148ad3441823a8fee22738b7dc7e707336e18b24c8c31273dc9aff94ae9b3}d.png</strong**

