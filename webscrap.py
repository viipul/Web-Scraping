import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
myurl='https://www.imdb.com/title/tt0944947/quotes/?tab=qt&ref_=tt_trv_qu'
uclient=ureq(myurl)
page_html=uclient.read()
uclient.close()
page_soup=soup(page_html,'html.parser')
containers_odd=page_soup.findAll('div',{'class':'quote soda sodavote odd'})
containers_even=page_soup.findAll('div',{'class':'quote soda sodavote even'})
filename='quotes.csv'
f=open(filename,'w')
headers='Author,Quote\n'
f.write(headers)
#for odd index
for i in range(0,len(containers_odd)):
    con1 = containers_odd[i]
    if con1.p.a is not None and con1.p is not None:
        a=con1.p.a.text
        b=con1.p.text.strip()
        b=str(b)
        j=b.index(':')
        b=b[j+2:]
        b=b.replace(',', '|')
        b=b.replace('\n','/')
        f.write(a +','+b+'\n')
#for even index
for i in range(0,len(containers_even)):
    con1 = containers_even[i]
    if con1.p.a is not None and con1.p is not None:
        a=con1.p.a.text
        b=con1.p.text.strip()
        b=str(b)
        j=b.index(':')
        b=b[j+2:]
        b=b.replace(',', '|')
        b=b.replace('\n','/')
        f.write(a +','+b+'\n')

f.close()
print('File Saved')