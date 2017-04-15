import urllib.request
import xml.etree.ElementTree as ET
import sys

print("{")
print("\t\"authors\": [")

#author_ids = [18541, 7113, 3503, 9494]
author_names = ['Christina Dodd', 'Simone Murray', 'Dante Alighieri', 'Robert Fulford', 'Carolyne Larrington', 'Maeve Binchy', 'Uskali Mäki', 'Philip Reeve', 'Guillaume Apollinaire', 'Beverly Barton', 'Herbert George Wells', 'Judith Roof', 'Richard H. Weisberg', 'Kirk J. Schneider', 'John Townsend', 'Suman Gupta', 'Markus N. A. Bockmuehl', 'Marisa Bortolussi', 'Ursula K. Le Guin', 'John V. Pickstone', 'John Ivy', 'Robert Cormier', 'Katherine Hall Page', 'François Fortier', 'R. A. Brown', 'Christine Mummery', 'Emma Lazarus', 'Pindar', 'Mike Harris', 'Susan M. Tiberghien', 'Roberta Gellis', 'Laurent Gaudé', 'Darin Barney', 'Ted Kooser', 'Julie Garwood', 'Nalini Singh', 'Emily Hallin', 'Don McKay', 'Jan Parker', 'Scientific American Editors', 'Martin Willis', 'James M. Mensch', 'Thomas J. Misa', 'Joseph Favorito', 'Brian M. Stableford', 'Roger Luckhurst', 'Stella Cameron', 'Dan Flockhart', 'Michael Adas', 'Rob Price', 'Fred Leavitt', 'Katharina M. Wilson', 'Katharine M. Nohr', 'Northrop Frye', 'Jorge Luis Borges', 'Terrence Ryan', 'Asja Szafraniec', 'Uwe Kiencke', 'Patricia Waugh', 'Jennifer Michael Hecht', 'Thelma S. Horn', 'Michael Wood', 'Rachel Zolf', 'Galway Kinnell', 'Timothy Liu', 'Don Norman', 'Kelly K. Owens', 'Katie Fforde', 'Franklin W. Dixon', 'Lori Copeland', 'Joseph A. Maguire', 'W B Yeats', 'Tracey West', 'John Sutherland', 'C. B. Don', 'Peter May', 'Glen Macnow', 'Betty Neels', 'Steven A. Riess', 'Derek Walcott', 'Barrie Houlihan', 'Jamie Beck', 'Robert Scott Kretchmar', 'Bertrice Small', 'Bill Readings', 'Loren D. Estleman', 'Jeremy Stolow', 'John D. Barrow', 'Marcia Sheehan Freeman', 'V. Flanagan', 'Benjamin Acosta-Hughes', 'Fiona Robertson', 'Jennifer Lawson', 'Aimée Thurlo', 'Matt Lamy', 'Maria Esther Maciel', 'Gertrude Chandler Warner', 'Dave Zirin', 'David M. Kaplan', 'Michael Meyer', 'Mark Brake', 'Herbert L. Sussman', 'Julia Parks', 'Jorge Iber', 'John Waller', 'Tess Gerritsen', 'Dr. Charles N. Ford', 'Philip Schultz', 'Shona M. Thompson', 'Joe Orlando', 'Craig Bourne', 'Rajeev Garg', 'Routledge', "Kathleen O'Neal Gear", 'Sally Gadsdon', 'Sigmund Loland', 'Olive Senior', 'Martin E. Marty', 'Julie Fison', 'Matthew B.J. Delaney', 'Thomas Michaud', 'Andrea Barrett', 'Pierre Joris', 'Danielle Steel', 'Patricia Cornwell', 'D. Radosavljevic', 'Elizabeth Barrett Browning', 'Carrie Alexander', 'Arthur Slade', 'Decourt Franck', 'Dr Matthew Wynn Sivils', 'B. Westphal', 'Denys Johnson-Davies', 'Domna Pastourmatzi', 'Josephine Tey', 'George Michael Cohan', 'Rowe, David', 'Paul Beashel', 'Gary Raham', 'Meg Cabot', 'Mark Stewart', 'LaVyrle Spencer', 'Jukka Mikkonen', 'Tamara Siroone Ketabgian', 'Elizabeth Lowell', 'Leroy W. Dubeck', 'Mary Karr', 'Rodney D. Fort', 'Sandra G. Harding', 'Robert Bly', 'D. Stanley Eitzen', 'Sandra Brown', 'Bernard James Mullin', 'Carly Phillips', 'Bijoy H. Boruah', 'Charles Bukowski', 'Lenora Worth', 'Christian Heath', 'Carole Nelson Douglas', 'William Shatner', 'Vassilis Lambropoulos', 'David R. Maidment', 'Eric Bronson', 'Guoqi XU', 'Philip E. Agre', 'Sheryl N. Hamilton', 'Robert Pepperell', 'Michael Novak', 'Suzanne Enoch', 'Thomas Hardy', 'Christine Rimmer', 'Margaret Atwood', 'John F. Haught', 'Holt, Rinehart and Winston Staff', 'Paisley Livingston', 'Gena Hale', 'Greg Iles', 'Brian David Johnson', 'M. Reason', 'Rae Armantrout', 'Anne Carson', 'Lamartine Pereira da Costa', 'Kevin Powers', 'Kenny Kemp', 'Carroll W. Pursell', 'Carl Mitcham', 'Terry Eagleton', 'Cheryl Howe', 'Leslie C. Kaplan', 'William H. Baarschers', 'M. Wilson', 'Barry B Luokkala', 'Geoffrey Chaucer', 'Verlyn Flieger', 'Sabine Roeser', 'Julia Kristeva', 'Elaine L. Graham', 'Zoë Brigley', 'Neville de Mestre', 'Shane Neilson', 'Linda Lael Miller', 'Steven W. Smith', 'Loren R. Graham', 'Patricia Waddell', 'Evelyn Rogers', 'Robert J. Rotella', 'Charley Rosen', 'Linore Rose Burkard', 'Wendell Odom', 'Stuart M. Kaminsky', 'Neil Roberts', 'Barry Mahon', 'Andrew M. Lane', 'Ronald Scollon', 'Antonio Gramsci', 'Nikki Giovanni', 'Chunjuan Nancy Wei', 'Tamara T. Allen', 'James McClure', 'Stephan Pastis', 'Samuel Taylor Coleridge', 'Arthur F. Marotti', 'Sara Bynoe', 'Sheri Whitefeather', 'Daisy Hicks Thomson', 'Maarten Van Bottenburg', 'Carolyn Keene', 'Laurel R. Davis', 'Horace', 'Ellen Schwartz', 'Nicholas Nurston', 'Judith McNaught', 'Isaac Asimov', 'Stephen A. Mitchell', 'Steven J. Overman', 'William J. Bennett', 'James Patterson', 'Elfriede Jelinek', 'National Geographic Society (U.S.)', 'Bernadette Mayer', 'Epeli Hau?ofa', 'Rose Kerr', 'M. G. Kincaid', 'R.J Lambourne', 'Samantha Zacher', 'J. V. Field', 'Jennie Klassel', 'Will Bowers', 'Paul J. Nahin', 'Edward W. Said', 'T. J. Binyon', 'Joseph Needham', 'Nelson Goodman', 'David Clay Large', 'Roman Ingarden', 'Maurice Blanchot', 'Kathryn Lomer', 'Vyv Simson', 'Michele Jaffe', 'Colleen Higgs']

length = len(author_names)

for author in author_names:

	url1 = 'https://www.goodreads.com/api/author_url/' + urllib.parse.quote(author, safe='') + '?key=YCBYRWAFTg2cfUnmW8IWTg'

	xml = urllib.request.urlopen(url1)
	output = xml.read().decode('utf-8')
	xml_str = str(output)

	try:
		a_id = ET.fromstring(xml_str).find('author').attrib['id']
	except:
		length -= 1
		continue
	sys.stderr.write('scraped author id: ' + str(a_id) + '\n')


	url = "https://www.goodreads.com/author/show/" + str(a_id) + "?format=xml&key=YCBYRWAFTg2cfUnmW8IWTg"

	test = urllib.request.urlopen(str(url))
	output = test.read().decode('utf-8')
	xml_out = (str(output))

	root = ET.fromstring(xml_out)

	name = root.find('author').find('name').text
	image_url = root.find('author').find('large_image_url').text
	image_url2 = image_url.replace('\n', '')

	about = root.find('author').find('about').text
	if about != None :
		about = about.replace('\"', '\\\"')
		about = about.replace('\n', '')

	works_count = root.find('author').find('works_count').text
	gender = root.find('author').find('gender').text
	hometown = root.find('author').find('hometown').text
	birthdate = root.find('author').find('born_at').text
	#if type(birthdate) == 'NoneType':
	#	birthdate = " "
	deathdate = root.find('author').find('died_at').text




	print("\t\t{")
	print("\t\t\t\"name\":", "\"" , name, "\"," )
	print("\t\t\t\"image_url\":", "\"" , image_url2, "\"," )
	print("\t\t\t\"about\":", "\"" , about,  "\",")
	print("\t\t\t\"works_count\":", works_count, ",")
	print("\t\t\t\"gender\":", "\"", gender, "\",")
	print("\t\t\t\"hometown\":", "\"", hometown, "\",")
	print("\t\t\t\"birthdate\":", "\"", birthdate, "\",")
	print("\t\t\t\"deathdate\":", "\"", deathdate, "\"")
	
	if length > 1 :
		print("\t\t},")
		length -= 1
	else :
		print("\t\t}")	



print("\t]")
print("}")