import urllib.request
import xml.etree.ElementTree as ET

print("{")
print("\t\"reviews\": [")

review_ids = [776888734, 22, 1827306723, 375155603, 1111947229, 1830471201, 39699485, 1332603757, 338642336, 1408520676, 694052294, 712375019, 822821285, 702682359, 834652058, 308546240, 1507819577, 13656519, 1603408174, 501928931, 11636196, 1513680552, 402694522, 1808650773, 1746706763, 176044725, 1391258120, 1433760337, 391698065, 259150059, 530238442, 877819904, 373631009, 488945235, 1522138714, 432717247, 750487022, 444771373, 1804661298, 1340200511, 22086209, 12312790]
length = len(review_ids)

for re_id in review_ids:

	url = "https://www.goodreads.com/review/show.xml?id=" + str(re_id) +"&key=YCBYRWAFTg2cfUnmW8IWTg"

	test = urllib.request.urlopen(str(url))
	output = test.read().decode('utf-8')
	xml_out = (str(output))

	root = ET.fromstring(xml_out)

	isbn = root.find('review').find('book').find('isbn').text
	author = root.find('review').find('book').find('authors').find('author').find('name').text
	title = root.find('review').find('book').find('title').text

	review = root.find('review').find('body').text
	
	if review != None :
		review = review.replace('\"', '\\\"')
		review =review.replace('\n', '')

	reviewer = root.find('review').find('user').find('display_name').text
	source = root.find('review').find('url').text
	rating = root.find('review').find('rating').text



	print("\t\t{")
	print("\t\t\t\"isbn\":", "\"" , isbn, "\"," )
	print("\t\t\t\"title\":", "\"" , title, "\"," )
	print("\t\t\t\"author\":", "\"" , author, "\"," )
	print("\t\t\t\"review\":", "\"" ,review,  "\",")
	print("\t\t\t\"reviewer\":", "\"", reviewer, "\",")
	print("\t\t\t\"source\":", "\"", source, "\",")
	print("\t\t\t\"rating\":", "\"" , rating, "\"" )
	

	if length > 1 :
		print("\t\t},")
		length-= 1
	else :
		print("\t\t}")	



print("\t]")
print("}")