import urllib
import urllib.request

def search_for(x):
	string = "https://www.goodreads.com/search.xml?key=YCBYRWAFTg2cfUnmW8IWTg&id=" + urllib.parse.quote(x, safe='')
	return string

authors = ['Anne Lamott', 'Thornton W. Burgess', 'Jennifer Ackerman', 'Maya Angelou', 'H. P. Lovecraft', 'Scott Doorley', 'Gaston Bachelard', 'Daniel Keyes']

f = open('author_data.xml', 'w')

for author in authors:
	test_data = urllib.request.urlopen(search_for(author))
	output = test_data.read().decode('utf-8')
	f.write(output)
	f.write('\n')

print('success')
f.close()
