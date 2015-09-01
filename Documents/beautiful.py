from bs4 import BeautifulSoup
import urllib


userinput=raw_input("Input URL: ")
r = urllib.urlopen(userinput).read()
soup = BeautifulSoup(r)

#if lazada
if "lazada" in userinput:
	print "This is Lazada"
	letters = soup.find_all("span", class_="price")
	result = str(letters[1])
	print result[result.find("RP"):result.find("/")-1]	
#if bilna
elif "bilna" in userinput:
	print "This is Bilna"
	letters = soup.find_all("span", class_="price")
	result = str(letters[0])
	print result[result.find("Rp"):result.find("/")-1]	
#if blibli 
elif "blibli" in userinput:
	print "this is blibli"
elif "ebay" in userinput:
	print "This is Ebay"
	letters = soup.find_all("span", class_="notranslate")
	result = str(letters[0])
	print result[result.find("US"):result.find("/")-1]	
else:
	print "unknown"
