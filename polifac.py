from bs4 import BeautifulSoup
import urllib.request
fac = urllib.request.urlopen('http://politics.virginia.edu/faculty')
fachtml = fac.read() 
soup = BeautifulSoup(fachtml)
tds = soup.find_all('td')
list1 = []
list2 = []
s = ['views-field', 'views-field-field-position']
for td in tds: 
	if td['class'] == s:
		heads = td.find_all('h4')
		for head in heads:
			link = head.find('a') 
			actualLink = 'http://politics.virginia.edu/' + link.get('href')
			name = link.contents[0]
			t = (actualLink, name)
			list1.append(t)
			biopage = urllib.request.urlopen(actualLink)
			biohtml = biopage.read()
			biosoup = BeautifulSoup(biohtml)
			divs = biosoup.find_all('div')
			bio = ""
			match = "body"
			for div in divs:
				try:
					if div['id'] == match: 
						p = div.find('p')
						bio = p.renderContents()
						t2 = (name, bio)
						list2.append(t2)
				except: 
					continue		
print(list1)
print(list2)