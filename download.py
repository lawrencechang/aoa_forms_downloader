#

def run():
  print("Welcome to Lawrence's Apartment Owners Association forms downloader!")

  from bs4 import BeautifulSoup
  import urllib.request
  import urllib.parse
  import re
  import os

  page_url = "https://www.aoausa.com/"
  url = "https://www.aoausa.com/forms.list.html"
  document_extensions = ["pdf", "docx"]
  links = []
  output_dir = "downloaded_files/"

  html_page = urllib.request.urlopen(url)
  soup = BeautifulSoup(html_page, features="html.parser")

  for document_extension in document_extensions:
    for link in soup.findAll('a', attrs={'href': re.compile(document_extension)}):
      links.append(link.get('href'))
  print("Got " + str(len(links)) + " links!")

  count = 0
  # Use to limit number of downloads.
  max_count = 5
  for link in links:    
    sanitzied_url = urllib.parse.quote(page_url + link, safe=":/")
    print("Sanitized url is: " + sanitzied_url)

    output_path = output_dir + link
    if not os.path.isdir(output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
    urllib.request.urlretrieve(sanitzied_url, output_path)

    count += 1
    if count == max_count:
      break;

  return links
  

if __name__ == "__main__":
  links = run()
