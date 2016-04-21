from bs4 import BeautifulSoup
import re
import requests

#url = raw_input("Enter a website to extract the URL's from: ")
p=open("symptom.txt","r").read()
s=str(p).split("\n")
#print "s",s,"\n"

#print soup
#print '-----------------------'

#Gloss extraction ;) :p 


out = open("symptoms_synonyms.txt","w")
for i in s:
    #lst = str(i).split('\t')
    #r = str(lst[0]).strip()
    #print "lst",lst[0],r,"\n"
    lst = re.sub('_','',i)
    tgt = []
    m = []
    try:
	print "url :",lst
	r  = requests.get("http://www.synonym.com/synonyms/"+lst)
	data = r.text
	soup = BeautifulSoup(data)
	#print soup.body.p
#    if i >= 1:
    #print i,"#########"
    #k=str(i).strip()
#k=k.replace(" ","_")
    

	for k in soup.body.findAll('ul','synonyms'):
   	    k = k.findAll('li')
	    #print "k ",k
	    target = re.sub("<[^>]*>",'',str(k) )
	    #target = re.sub(' ','',target)
	    #print "target ",target
	    '''
		i = str(i).strip()
		i = str(i).split('<li>')
		i = str(i).split('</li>')
		i = str(i).split('</a>')
		i = str(i).split('>')
	    '''	
		#print target
	    tgt.append(target)
	#for t in tgt:
#	for s in t:
       		#print "t ",str(t).replace("\n","")
		#m.append(str(t)) 
    	#print "m--", m
#	i = i.strip()
	out.write(str(i).strip())        
	out.write("\t")
	#out.write(str(lst[1]))
	#out.write("\t")
	#tgt = str(tgt)
	#for z in range(len(tgt)):
        #	out.write(str(tgt[z]))
	out.write(str(tgt))
	out.write("\n")

#	print "tgt",tgt
    except:
	print lst[0],"has no data"
	out.write(str(i).strip())        
	out.write("\t")
	out.write("{}")        
	continue
    
   
out.close()
	#print i
#print uls
#for ul in uls:
#	for syn in ul.findAll('li'):
	#	print syn

#		print '____________________---------------_________________'

	#	print syn.findAll('a')

#print((soup.get_text())

print '#############################'
#for link in soup.findAll('a'):
#	if link in uls:
#		print(link.get('href'))
'''
firstH3 = soup.find('h3') # Start here
uls = []
for nextSibling in firstH3.findNextSiblings():
    if nextSibling.name == 'h2':
        break
    if nextSibling.name == 'ul':
        uls.append(nextSibling)
'''
#uls = (soup.findAll('ul','synonyms'))
#uls.split('<li>')
#uls.split('</li>')
#print '++++++++++++++++++++++'
