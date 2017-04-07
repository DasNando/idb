import urllib.request
import json
from bs4 import BeautifulSoup

print("{")
print("\t\"publishers\": [")

pubs = ["Harper Collins", "Simon & Schuster", "Random House"]
length = len(pubs)

for i in pubs:

	url = "https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=revisions&titles=" + urllib.parse.quote(i, safe='') + "&redirects=1&rvprop=content&rvparse=1"

	test = urllib.request.urlopen(str(url))
	output = test.read().decode('utf-8')

	t = json.loads(output)
	html = t['query']['pages'][0]['revisions'][0]['content']
	soup = BeautifulSoup(html, 'html.parser')

	


    #Fields
	name = soup.caption.text
	about = soup.p.text
	about = about.replace('\"', '\\"')
	about = about.replace('\n', '')

	#Iterate thru table
	table = soup.table.extract()


	founding_date = " "
	hq = " "
	country = " "
	founders = " "

	z = table.th
	while z != None :
		if z.text == "Founded" :
			founding_date = z.find_next('td').text
			founding_date = founding_date.replace('\n', '')

		if z.text == "Headquarters location" :

			hq = z.find_next('td').text
			hq = hq.replace('\n', '')
			
		if z.text == "Country of origin" :
			country = z.find_next('td').text
			country = country.replace('\n', '')

		if z.text == "Founders" :
			founders = z.find_next('td').text
			country = country.replace('\n', '')


		table.th.decompose()
		z = table.th

	print("\t\t{")
	print("\t\t\t\"name\":", "\"" , name, "\"," )
	print("\t\t\t\"about\":", "\"" , about, "\"," )
	print("\t\t\t\"founders\":", "\"" , founders, "\"," )
	print("\t\t\t\"founding_date\":", "\"" ,founding_date,  "\",")
	print("\t\t\t\"country\":", "\"", country, "\",")
	print("\t\t\t\"hq\":", "\"" , hq, "\"" )
	

	if length > 1 :
		print("\t\t},")
		length-= 1
	else :
		print("\t\t}")	
		

print("\t]")
print("}")