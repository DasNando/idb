import urllib
import urllib.request

def search_for(x):
	string = "https://en.wikipedia.org/w/api.php?action=query&titles=" + urllib.parse.quote(x, safe='') + "&prop=revisions&rvprop=content&format=json"
	#string = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + urllib.parse.quote(x, safe='') + "&format=json"
	return string

test_data = urllib.request.urlopen(search_for('Anne Lamott'))
output = test_data.read().decode('utf-8')
formatted_output = str(output).replace('\\n', '\n')

f = open('author_test.json', 'w')
f.write(output)
f.close()

f = open('author_test.txt', 'w')
f.write(formatted_output)
f.close()
