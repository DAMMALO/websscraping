import urllib.request, urllib.parse, urllib.error
import json
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
    
info = json.loads(data)
print('count:', len(info["comments"]))

count=0
for item in info["comments"]:
    count+=item["count"]
print(count)
