import urllib.request
import xml.etree.ElementTree as ET

print("{")
print("\t\"authors\": [")

author_ids = [18541, 7113, 3503, 9494]

for a_id in author_ids:

	url = "https://www.goodreads.com/author/show/" + str(a_id) + "?format=xml&key=YCBYRWAFTg2cfUnmW8IWTg"

	test = urllib.request.urlopen(str(url))
	output = test.read().decode('utf-8')
	xml_out = (str(output))

	root = ET.fromstring(xml_out)

	name = root.find('author').find('name').text
	image_url = root.find('author').find('large_image_url').text
	image_url2 = image_url.replace('\n', '')

	about2 = root.find('author').find('about').text
    #about2 = about.replace('\n', '')

	works_count = root.find('author').find('works_count').text
	gender = root.find('author').find('gender').text
	hometown = root.find('author').find('hometown').text
	birthdate = root.find('author').find('born_at').text
	#if type(birthdate) == 'NoneType':
	#	birthdate = " "
	deathdate = root.find('author').find('died_at').text
	#if type(deathdate) == 'NoneType':
	#	deathdate = " "



	print("\t\t{")
	print("\t\t\t\"name\":", "\"" , name, "\"," )
	print("\t\t\t\"image_url\":", "\"" , image_url2, "\"," )
	print("\t\t\t\"about\":", "\"" , about2,  "\",")
	print("\t\t\t\"works_count\":", works_count, ",")
	print("\t\t\t\"gender\":", "\"", gender, "\",")
	print("\t\t\t\"hometown\":", "\"", hometown, "\",")
	print("\t\t\t\"birthdate\":", "\"", birthdate, "\",")
	print("\t\t\t\"deathdate\":", "\"", deathdate, "\",")
	print("\t\t}")



print("\t]")
print("}")