
import urllib.request
# import bs4 
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = bs4.BeautifulSoup(html, "html.parser")

# sumita=0
# count=0
# # Retrieve all of the anchor tags
# tags = soup('span')
# for tag in tags:

#     sumita+=int(tag.contents[0])
#     count+=1
#     print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)

# print("count: ", count)
# print(sumita)
print(dir(urllib.request))