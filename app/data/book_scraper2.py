import urllib.request
import xml.etree.ElementTree as ET
import time

print("{")
print("\t\"books\": [")

#isbn = ["0307424987", "0486121631", "1101980842", "030747772X", "1609772709", "0307424987", "0698170431", "0679755330", "1599869772"]
#length = len(isbn)

subjects = ['technology', 'sports', 'literature', 'poetry', 'romance', 'mystery', 'science+fiction']
length = len(subjects)

for i in subjects:
	time.sleep(1)

	url = "https://www.googleapis.com/books/v1/volumes?q=subject:"+ str(i) + "&maxResults=40&langRestrict=en&key=AIzaSyBIbqz2Qb-Afi-v1iXP3QRdM8wQmQMdFG4"

	test = urllib.request.urlopen(str(url))
	output = test.read().decode('utf-8')
	if length > 1 :
		print(str(output), end = ',\n')
		length-=1
	else :
		print(str(output))




print("\t]")
print("}")