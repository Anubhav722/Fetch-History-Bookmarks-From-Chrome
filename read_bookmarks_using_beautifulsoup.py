from bs4 import BeautifulSoup

filename = "output.html"
file = open(filename, 'r')

soup = BeautifulSoup(file.read())

for link in soup.find_all('a'):
    print(link.text)
    print(link['href'])
    print("\n")

