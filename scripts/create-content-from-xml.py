from unicodedata import category
import requests
import xmltodict
from os import listdir, path
import re
from markdownify import markdownify, ATX
from textwrap import dedent
from lxml import html
from glob import glob
from googletrans import Translator
from deep_translator import GoogleTranslator, LibreTranslator

translator = Translator()

app_url = "https://blog.doseextra.com/feed/"

html_tags = re.compile("<.*?>")


def string_parser(string):
    return (
        string.lower()
        .replace(" ", "_")
        .replace("ç", "c")
        .replace("á", "a")
        .replace("ã", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ñ", "n")
        .replace("ü", "u")
        .replace(".", "_")
        .replace("-", "")
        .replace("/", "_")
        .replace("!", "")
        .replace("?", "")
        .replace("(", "")
        .replace(")", "")
        .replace("[", "")
        .replace("]", "")
        .replace("{", "")
        .replace("}", "")
        .replace("=", "_igual")
        .replace("+", "")
        .replace("*", "")
        .replace("&", "e")
        .replace("#", "_cerquilha")
        .replace("$", "")
        .replace("%", "_por_cento")
        .replace("'", "")
        .replace(",", "_e")
        .replace(":", "")
    )


def parse_description(string):
    description = re.sub(html_tags, "", string)
    return (
        description.replace("\n", " ")
        .replace("<p>", "")
        .replace("</p>", "")
        .replace("<br />", "")
        .strip()
    )


def parse_content_to_markdown(string):
    return markdownify(string)


def get_post_thumbnail_from_url(url, title):
    if not glob("../themes/tomkiel/assets/images/" + title + "*"):
        post_request = requests.get(url, verify=False)
        html_content = html.fromstring(post_request.content)
        img_src = html_content.xpath(
            '//*[@id="content"]/div/div[1]/div/div/img/@src')
        img_request = requests.get(img_src[0], verify=False)

        if img_request.ok:
            file_type = img_request.headers['Content-type'].split("/")[1]

            with open("../themes/tomkiel/assets/images/" + title + "." + file_type, "wb") as file:
              print("Writing image: " + title + "." + file_type)
              file.write(img_request.content)
              file.close()
              return title + "." + file_type
    else:
        print(title + " image exists!")


def write_portuguese(item, image_file):
    blog_file = string_parser(item["title"]) + ".md"
    if path.isfile("../content/portuguese/blog/" + blog_file):
      print("File already exists: " + blog_file)
    else:
      with open("../content/portuguese/blog/" + blog_file, "w") as f:
          print("Writing file: " + blog_file)
          content = dedent(
              "---\n"
              + 'title: "'
              + item["title"]
              + '"\n'
              + 'description: "'
              + parse_description(item["description"])
              + '"\n'
              + 'type: "post"\n'
              + 'date: "'
              + item["pubDate"]
              + '"\n'
              + 'author: "'
              + item["dc:creator"]
              + '"\n'
              + 'categories: '
              + '\n- '
              + item['category'][0].lower()
              + '\n'
              + 'image: "images/'
              + image_file
              + '"\n'
              + "---\n"
              + "\n"
              + parse_content_to_markdown(item["content:encoded"])
          )
          print(content)
          f.write(content)
          f.close()
          print("File created:" + blog_file)

def write_english(item, image_file):
    title = GoogleTranslator(source='pt', target='en').translate(item["title"])
    blog_file = string_parser(title) + ".md"
    description = GoogleTranslator(source='pt', target='en').translate(parse_description(item["description"]))
    category = LibreTranslator(source='pt', target='en', base_url = 'http://127.0.0.1:5000/').translate(item["category"][0])
  
    if len(item["content:encoded"]) < 5000:
      content = GoogleTranslator(source='pt', target='en').translate(item["content:encoded"]) or "Nothings"
    else:
      content = LibreTranslator(source='pt', target='en', base_url = 'http://127.0.0.1:5000/').translate(item["content:encoded"]) or "Nothings"

    if path.isfile("../content/english/blog/" + blog_file):
      print("File already exists: " + blog_file)
    else:
      with open("../content/english/blog/" + blog_file, "w") as f:
          file_content = dedent(
              "---\n"
              + 'title: "'
              + title
              + '"\n'
              + 'description: "'
              + description
              + '"\n'
              + 'date: "'
              + item["pubDate"]
              + '"\n'
              + 'type: "post"\n'
              + 'author: "'
              + item["dc:creator"]
              + '"\n'
              + 'categories: '
              + '\n- '
              + category
              + '\n'
              + 'image: "images/'
              + image_file
              + '"\n'
              + "---\n"
              + "\n"
              + parse_content_to_markdown(content)
          )
          f.write(file_content)
          f.close()
    
def write_polish(item, image_file):
    title = GoogleTranslator(source='pt', target='pl').translate(item["title"])
    blog_file = string_parser(title) + ".md"
    description = GoogleTranslator(source='pt', target='pl').translate(parse_description(item["description"]))
    category = LibreTranslator(source='pt', target='pl', base_url = 'http://127.0.0.1:5000/').translate(item["category"][0])
    if len(item["content:encoded"]) < 5000:
      content = GoogleTranslator(source='pt', target='pl').translate(item["content:encoded"]) or "Nothings"
    else:
      content = LibreTranslator(source='pt', target='pl', base_url = 'http://127.0.0.1:5000/').translate(item["content:encoded"]) or "Nothings"

    if path.isfile("../content/polish/blog/" + blog_file):
      print("File already exists: " + blog_file)
    else:
      with open("../content/polish/blog/" + blog_file, "w") as f:
          file_content = dedent(
              "---\n"
              + 'title: "'
              + title
              + '"\n'
              + 'description: "'
              + description
              + '"\n'
              + 'date: "'
              + item["pubDate"]
              + '"\n'
              + 'type: "post"\n'
              + 'author: "'
              + item["dc:creator"]
              + '"\n'
              + 'categories: '
              + '\n- '
              + category
              + '\n'
              + 'image: "images/'
              + image_file
              + '"\n'
              + "---\n"
              + "\n"
              + parse_content_to_markdown(content)
          )
          f.write(file_content)
          f.close()

index = 1
while True:
    try:
        feed_url = app_url + "?paged=" + str(index)
        response = requests.get(feed_url, verify=False)
        parsed_content = xmltodict.parse(response.content)
        blog_content = parsed_content["rss"]["channel"]["item"]
        index += 1

        for item in blog_content:
            image_file = get_post_thumbnail_from_url(item["link"], string_parser(item["title"]))
            write_portuguese(item, image_file)
            write_english(item, image_file)
            write_polish(item, image_file)

    except Exception as err:
        print(err)
        print("End of the content")
        break
