import mechanize
import urllib2
import cookielib 
import requests
from PIL import Image
from bs4 import BeautifulSoup
import re, time, random
import subprocess, os, re, hashlib, sys

URL='https://www.irctc.co.in/eticketing/captchaImage'

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
	print 'Usage: python <script_name> <number_of_captchas>'
	exit(0)

__DIR__ = './solved/'
if not os.path.exists(__DIR__):
    os.makedirs(__DIR__)

# Here are the image properties
white = [(255,255,255,255), (255,255,255)]
black = [(0,0,0,0),(0,0,0)]
IMAGE = {}
IMAGE['RAW_FILE'] = __DIR__ + 'temp.png'
IMAGE['SOLVER_FILE'] = __DIR__ + '.captcha.png'
IMAGE['OUTPUT_FILE'] = __DIR__ + '.out' # Final output will be in out.txt file 

LOG_FILE = 'irctc.log'


def resetBrowser(br):

	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0')]
	br.set_cookiejar(cookieJar)
	br.set_handle_redirect(False)
	br.set_handle_robots(False)
	br.set_handle_referer(True)
	br.set_handle_refresh(False)
	br.set_handle_gzip(False)
	br.set_handle_equiv(True)

def tesseractOutput():
	temp = subprocess.Popen(["tesseract", IMAGE['SOLVER_FILE'], IMAGE['OUTPUT_FILE']], stdout=subprocess.PIPE).communicate()[0][:-1]
	with open(IMAGE['OUTPUT_FILE'] + '.txt', 'r+') as f:
		result = str(f.read())
		return result
	return None

def gocrOutput():
	result = subprocess.Popen(["gocr", IMAGE['SOLVER_FILE']], stdout=subprocess.PIPE).communicate()[0][:-1]
	return str(result)

def prepareResult(result):
	result = str(re.sub('[^A-Za-z0-9]+', '', str(result))).upper() 
	resultWithHash = result + '_' +  str(hashlib.md5(open(IMAGE['RAW_FILE'], 'rb').read()).hexdigest())
	return (result, resultWithHash)

def imageResetting(i):
	pixels = i.load() 
	width, height = i.size
	for x in range(width):
		for y in range(height):
			if pixels[x, y] in black:
				pixels[x, y] = white[1]
	i.save(IMAGE['SOLVER_FILE'])

total = int(sys.argv[1])
cookieJar = cookielib.LWPCookieJar()
br = mechanize.Browser()
resetBrowser(br)

for counter in xrange(1,total+1):
	br.open(URL)

	with open(IMAGE['RAW_FILE'], "w+") as f:
		f.write(br.response().read())

	i = Image.open(IMAGE['RAW_FILE'])
	imageResetting(i)

	result = tesseractOutput()

	if result == None:
		print "Some error occured in " + str(counter) + "/" + str(total)
		continue
	else:
		print "Done " + str(counter) + "/" + str(total)

	result,resultWithHash = prepareResult(result)
	
	if len(result) != 5:
		with open(LOG_FILE, 'a') as f:
			f.write("Wrong captcha decoded for " + resultWithHash + "\n")
	else:
		with open(LOG_FILE, 'a') as f:
			f.write(resultWithHash + "\n")
		os.system('mv ' + IMAGE['RAW_FILE'] + ' ' + __DIR__ + str(resultWithHash) + '.png')
		os.system('mv ' + IMAGE['SOLVER_FILE'] + ' ' + __DIR__ + '.' + str(result) + '.png')