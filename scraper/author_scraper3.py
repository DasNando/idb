import urllib.request
import xml.etree.ElementTree as ET
import sys

print("{")
print("\t\"authors\": [")

#author_ids = [18541, 7113, 3503, 9494]
author_names = ['Eric Bronson', 'Guoqi XU', 'Dante Alighieri', 'Tracey West', 'Steven A. Riess', 'V. Flanagan', 'Niall Rudd', 'Terrence Ryan', 'Roberta Gellis', 'Jennie Klassel', 'Herbert L. Sussman', 'Katharina M. Wilson', 'Neville de Mestre', 'John Townsend', 'Kathryn Lomer', 'Mary Karr', 'Tess Gerritsen', 'Elaine L. Graham', 'Sandra G. Harding', 'Nelson Goodman', 'Anthony L. Gargano', 'David M. Kaplan', 'Asja Szafraniec', 'Bill Readings', 'Christine Rimmer', 'Carolyne Larrington', 'Beverly Barton', 'Bijoy H. Boruah', 'M.J Shallis', 'Markus N. A. Bockmuehl', 'Anja van de Stolpe', 'Martin E. Marty', 'Frank A. J. L. James', 'Darin Barney', 'Sheryl N. Hamilton', 'Andrew M. Lane', 'John Fizel', 'Jennifer Lawson', 'Sun Tzu', 'Thelma S. Horn', 'Nikki Giovanni', 'Christian Heath', 'Barrie Houlihan', 'Guillaume Apollinaire', 'Christina Dodd', 'Katherine Hall Page', 'Margaret Atwood', 'Wendell Odom', 'John Taylor', 'John Hollander', 'Patricia Waddell', 'Charles Bukowski', 'Suzanne E. Moshier', 'Barry B Luokkala', 'Samuel Taylor Coleridge', 'Nigel Wood', 'Robert Pepperell', 'Rowe, David', 'Meg Cabot', 'Bernadette Mayer', 'Nalini Singh', 'Benjamin Acosta-Hughes', 'Andrew Feenberg', 'Gaston Bachelard', 'Colleen Higgs', 'Marcia Sheehan Freeman', 'Rafaela Hillerbrand', 'John Ivy', 'Steven J. Overman', 'Robert Cormier', 'H. P. Lovecraft', 'Julia Kristeva', 'Julie Fison', 'Mary Gehr', 'Matt Lamy', 'Loren D. Estleman', 'Mark Brake', 'David Clay Large', 'Laurel R. Davis', 'Holt, Rinehart, and Winston, inc', 'Chip Walter', 'Darryl E. Brock', 'Iain Lindsey', 'Joe Orlando', 'Pierre Joris', 'Carolyn Keene', 'Uskali Mäki', 'John F. Haught', 'Hans Clevers', 'Timothy Mathews', 'Don McKay', 'Fred Leavitt', 'James M. Mensch', 'Roman Ingarden', 'David R. Maidment', 'Elizabeth Barrett Browning', 'Jude Deveraux', 'James Patterson', 'Rajeev Garg', 'Rae Armantrout', 'Stephen A. Mitchell', 'Domna Pastourmatzi', 'Aimée Thurlo', 'Tamara Siroone Ketabgian', 'Gary Raham', 'Ana Miragaya', 'Linda L. Griffin', 'M. Reason', 'Dirk Gringhuis', 'Leroy W. Dubeck', 'Hannah Leah Crummé', 'Gena Hale', 'Marisa Bortolussi', 'Arthur F. Marotti', 'Vassilis Lambropoulos', 'Thornton W. Burgess', 'B. Westphal', 'Lori Copeland', 'Julia Parks', 'Derek Walcott', 'Jennifer Greene', 'E. Siegel', 'Charlotte Mandell', 'William Irwin', 'Jorge Luis Borges', 'Judith Roof', 'Bennet Schaber', 'Philip Schultz', 'Antonio Gramsci', 'Robert Bly', 'Cheryl Howe', 'Scientific American Editors', 'Carrie Alexander', 'Sheri Whitefeather', 'Brian M. Stableford', 'Neil Roberts', 'Betty Neels', 'Martin Willis', 'Olive Senior', 'Carole Nelson Douglas', 'Pindar', 'Katharine M. Nohr', 'Méira Cook', 'Duška Radosavljevi?', 'Suzanne B. K. Scollon', 'Michael Adas', 'William H. Baarschers', 'Paul Beashel', 'Maurice Blanchot', 'Joseph A. Buttigieg', 'Franklin W. Dixon', 'J. V. Field', 'Ellen Schwartz', 'Paul J. Nahin', 'K. Johnson', 'Josephine Tey', 'John D. Barrow', 'John Sutherland', 'Denys Johnson-Davies', 'Ursula K. Le Guin', 'Jorge Iber', 'Philip Reeve', 'Dan Flockhart', 'Michael Wood', 'Lamartine Pereira da Costa', 'Will Bowers', 'Peter Dixon', 'Fiona Robertson', 'Andrea Barrett', 'Carl Mitcham', 'Kelly K. Owens', 'Linda Lael Miller', 'Patricia Waugh', 'C. B. Don', 'Sandra Brown', 'Neil Hook', 'Jeremy Stolow', 'Kenny Kemp', 'William Shatner', 'Stella Cameron', 'R.J Lambourne', 'Terry Eagleton', 'Jukka Mikkonen', 'Samantha Zacher', 'Emma Lazarus', 'Bernard Roelen', 'Charley Rosen', 'Brian Attebery', 'Steven W. Smith', 'Sara Bynoe', 'Laurent Gaudé', 'Michael Meyer', 'Herbert George Wells', 'Richard H. Weisberg', 'Stephen Hardy', 'Arthur Slade', 'Julie Garwood', 'Ted Kooser', 'David Thurlo', 'M. Wilson', 'Jennifer Michael Hecht', 'LaVyrle Spencer', 'Robert Portman', 'Dave Zirin', 'Dr. Charles N. Ford', 'Robert Scott Kretchmar', 'Michael Hulse', 'Marisabina Russo', 'D. Radosavljevic', 'Geoffrey Chaucer', 'Bernard James Mullin', 'William J. Bennett', 'Carly Phillips', 'Kirk J. Schneider', 'Holt, Rinehart and Winston Staff', 'Dr Matthew Wynn Sivils', 'Loren R. Graham', 'Northrop Frye', 'Per Sandin', 'Danielle Steel', 'Joseph Needham', 'Rodney D. Fort', 'William Anthony Sutton', 'Shane Neilson', 'Linore Rose Burkard', 'Judith McNaught', 'Stuart M. Kaminsky', 'Zoë Brigley', 'T. J. Binyon', 'Glen Macnow', 'Marc Rotenberg', 'Suzanne Enoch', 'Daisy Hicks Thomson', 'Sigmund Loland', 'Stephan Pastis', 'Emily Caddick Bourne', 'National Geographic Society (U.S.)', 'Peter May', 'Michael Novak', 'Leslie C. Kaplan', 'Verlyn Flieger', 'David Neal Miller', 'Richard Hantula', 'Maarten Van Bottenburg', 'Joseph Favorito', 'R. A. Brown', 'Jennifer Ackerman', 'M Shortland', 'Andy Sibson', 'Barry Mahon', 'Maria Esther Maciel', 'Stephanie Laurens', 'Paul Luff', 'Maya Angelou', 'Chunjuan Nancy Wei', 'Galway Kinnell', 'Roger Luckhurst', 'Najīb Maḥfūẓ', 'Sabine Roeser', 'Mark Stewart', 'James McClure', 'François Fortier', 'Timothy Liu', 'Matthew B.J. Delaney', 'Judith L. Oslin', 'Susan M. Tiberghien', 'Simone Murray', 'Patricia Cornwell', 'Celeste Bradley', 'Thomas J. Misa', 'Edward W. Said', 'Lenora Worth', 'Decourt Franck', 'Christine Mummery', 'D. Stanley Eitzen', 'Philip E. Agre', 'Rose Kerr', 'Thomas Michaud', 'Nicholas Nurston', 'Judith E. Boss', 'Emily Hallin', 'Don Norman', 'Michele Jaffe', "Kathleen O'Neal Gear", 'Rachel Zolf', 'Shona M. Thompson', 'Katie Fforde', 'Craig Bourne', 'Sally Gadsdon', 'George Michael Cohan', 'Rob Price', 'W. Michael Gear', 'Paisley Livingston', 'Tamara T. Allen', 'John Waller', 'W B Yeats', 'John V. Pickstone', 'Routledge', 'Thomas Hardy', 'Gary M. Miller', 'Carroll W. Pursell', 'Kathryn Thornton', 'Greg Iles', 'Jamie Beck', 'Elizabeth Lowell', 'Jan Parker', 'Bertrice Small', 'Cheryl St. John', 'Brian David Johnson', 'Jacob Fuchs', 'Martin Peterson', 'Ronald Scollon', 'Horace', 'Suman Gupta', 'Anne Carson', 'Andrew Jennings', 'Robert J. Rotella', 'Elfriede Jelinek', 'Lars Nielsen', 'Philip Brey', 'Lionel Giles', 'Vyv Simson', 'Evelyn Rogers', 'Samuel O. Regalado', 'Maeve Binchy', 'Uwe Kiencke', 'Kevin Powers', 'Mike Harris', 'Leslie Lafoy', 'Robert Fulford', 'Gertrude Chandler Warner', 'Lorraine Hansberry', 'Joseph A. Maguire', 'M. G. Kincaid', 'Isaac Asimov', 'Anne Lamott', 'Sun Zi', 'Epeli Hau?ofa']

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