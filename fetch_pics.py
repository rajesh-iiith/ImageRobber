import requests, urlparse 
from lxml import html  
import os, sys  
import urllib, re, cStringIO
from random import randint


myUrl = sys.argv[1]
toWhere = sys.argv[2]
min_image_size_in_KB = float(sys.argv[3])

if not os.path.exists(toWhere):
    os.makedirs(toWhere)

response = requests.get(myUrl)
parsed_body = html.fromstring(response.text)

# Get links of images
images = parsed_body.xpath('//img/@src')  
if not images:  
    sys.exit("Koi image nahin mila!!")

# Convert relative urls to absolute ones
images = [urlparse.urljoin(response.url, url) for url in images]  
print 'Found %s images' % len(images)
print '%s images are unique' % len(set(images))

image_id  = 0
for url in set(images):
	image_id = image_id + 1
	image_size = len(urllib.urlopen(url).read()) / float (1024)

	if (image_size >= min_image_size_in_KB):
		print "Downloading " + url
		location = toWhere+'/'+str(image_id)+'_'+url.split('/')[-1].split('?')[0]
		urllib.urlretrieve(url, location)
	else:
		print "Discarding " + url + " [size less than" + str(min_image_size_in_KB) + " KB]"
		