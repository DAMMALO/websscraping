import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter url- ')

parms= dict()
parms['address'] = address
url=urllib.parse.urlencode(parms)
print('Retrieving', address)
uh= urllib.request.urlopen(address, context=ctx)

data= uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree= ET.fromstring(data)
    
res=0
couts = tree.findall('.//count')
for i in couts:
    res+=int(i.text)
print("resultado: ", res)    