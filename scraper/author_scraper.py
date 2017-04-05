import urllib.request

def search_for(x):
	string = "https://en.wikipedia.org/w/api.php?action=query&titles=" + x + "&prop=revisions&rvprop=content&format=json"
	return string.replace(' ', '_')

test_data = urllib.request.urlopen(search_for('Anne Lamott'))
output = test_data.read().decode('utf-8')
output.replace(r'\n', '\n')

print(output)