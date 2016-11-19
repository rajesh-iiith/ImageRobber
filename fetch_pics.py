import requests, urlparse 
from lxml import html  
import os, sys  
import urllib, re, cStringIO
from random import randint
import argparse

current_dir = os.path.dirname(os.path.abspath(__file__))

def parse_inputs():
	parser = argparse.ArgumentParser(description='Description of your program')
	parser.add_argument('-d','--destination', help='directory where images will be stored', default = os.path.join(current_dir,"input"))
	parser.add_argument('-u','--urlofpage', help='URL to the web page', default = "empty")
	parser.add_argument('-m','--minsize', help='Minimum size of image in KB', default = '0')

	args = vars(parser.parse_args())

	myUrl = args['urlofpage']
	toWhere = args['destination']
	min_image_size_in_KB = float (args['minsize'] )


	return myUrl, toWhere, min_image_size_in_KB	

myUrl, toWhere, min_image_size_in_KB = parse_inputs()

if myUrl == 'empty':
		print "Enter URL of the web page"
		sys.exit(1)

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

	print image_size, min_image_size_in_KB
	if (image_size >= min_image_size_in_KB):
		print "Downloading " + url
		location = toWhere+'/'+str(image_id)+'_'+url.split('/')[-1].split('?')[0]
		urllib.urlretrieve(url, location)
	else:
		print "Discarding " + url + " [size less than" + str(min_image_size_in_KB) + " KB]"	