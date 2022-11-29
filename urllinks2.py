
import urllib.request
import bs4 
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

aux_count=0

url = input("Enter - ")
count=int(input("Enter count- "))
pos=int(input("Enter position-"))
link=url
while aux_count<=count:
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    tags=soup("a")
    print(link)
    for tag in tags:
        index=tags.index(tag)
        if index==(pos-1):
            link=tag.get("href",None)
    aux_count+=1

