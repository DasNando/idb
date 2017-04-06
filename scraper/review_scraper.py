import urllib.request
import xml.etree.ElementTree as ET

print("{")
print("\t\"reviews\": [")


test = urllib.request.urlopen("https://www.goodreads.com/review/show.xml?id=22&key=YCBYRWAFTg2cfUnmW8IWTg")
output = test.read().decode('utf-8')
xml_out = (str(output))

root = ET.fromstring(xml_out)

isbn = root.find('review').find('book').find('isbn').text
author = root.find('review').find('book').find('authors').find('author').find('name').text

review = root.find('review').find('body').text
review_c =review.replace('\n', '')
reviewer = root.find('review').find('user').find('display_name').text
source = root.find('review').find('url').text
rating = root.find('review').find('rating').text



print("\t\t{")
print("\t\t\t\"isbn\":", isbn, ",")
print("\t\t\t\"author\":", "\"" , author, "\"," )
print("\t\t\t\"review\":", "\"" ,review_c,  "\",")
print("\t\t\t\"reviewer\":", "\"", reviewer, "\",")
print("\t\t\t\"source\":", "\"", source, "\",")
print("\t\t\t\"rating\":", rating, ",")
print("\t\t}")



print("\t]")
print("}")