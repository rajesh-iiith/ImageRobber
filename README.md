# ImageRobber
Robs all the images from a web page, leaving the useless ones.

usage: fetch_pics.py [-h] [-d DESTINATION] [-u URLOFPAGE] [-m MINSIZE]

Description of your program

optional arguments:
  -h, --help            show this help message and exit
  -d DESTINATION, --destination DESTINATION
                        directory where images will be stored
  -u URLOFPAGE, --urlofpage URLOFPAGE
                        URL to the web page
  -m MINSIZE, --minsize MINSIZE
                        Minimum size of image in KB



python fetch_pics.py -u https://in.udacity.com/ -d udacity -m 10

This will create a directory called udacity in your current directory, and fetch all the images (of size >=10KB) from https://in.udacity.com/ into this.
