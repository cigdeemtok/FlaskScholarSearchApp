import requests
from bs4 import BeautifulSoup


yayinID = ""
yayinAdi = ""
yazarlar = list()
tur = ""
yayimTarihi = ""
yayimciAdi = ""
keywords = list()
ozet = ""
referanslar = list()
#citied by
alintiSayisi = ""
doiNum = ""
urlAdresi = ""


searchedWord = 'text summarization'

count = len(searchedWord.split())

searchedWord = searchedWord.replace(" ","+")

print(f"searched word {searchedWord}")
print(f"word count {count}")

url ="https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={}&btnG=".format(searchedWord)

page = requests.get(url)
soup = BeautifulSoup(page.content, features = "html.parser")

print(soup.prettify())

body = soup.find("div", attrs={"id":"gs_res_ccl"})

top = body.find("div", attrs = {"id":"gs_res_ccl_top"})
if top:
    topCorrect = top.find("h2", attrs={"class":"gs_rt"})
    correctLink = topCorrect.a.get("href")
    correctWord = topCorrect.a.get_text()
    print(correctWord)
    print(correctLink)


articles = body.find_all("div",attrs={"class":"gs_r"})
print(articles)
for article in articles:
   #print(article)
    print("----------") 
    name = article.a.get_text()
    #print(name)
    
    #article id?
    id = article.get("data-cid")
    print(id)

    citedBy = article.find("div", attrs={"class":"gs_fl"} ).get_text().split()
    citedBy = citedBy[2:5]
    citedBy = ' '.join(citedBy)
    #print(citedBy)

    type = article.span.get_text()
    #print(type)
    #gives link types html book pdf etc

    #yazarlar
    authors = article.find("div", attrs = {"class":"gs_a"}).get_text()
    index = authors.find("-")
    authors = authors[: index].split(",")
    authors[-1] = authors[-1].replace("\xa0","")
    #print(authors)

    #search link
    link = article.a.get("href")
    #print(link)

    
    # if(link.endswith('pdf')):
    #     print('first page')
    #     print('link')
    # else:
    #     detailsPage = requests.get(link)
    #     details = BeautifulSoup(detailsPage.content, features='html.parser')
    #     pdfLinks = details.find_all('a')
    #     #print(pdfLinks)
    #     for aTags in pdfLinks:
    #         tagLink = aTags.a.get('href')
    #         if(tagLink.endswith('pdf')) and tagLink != None:
    #             print('url page')
    #             print(tagLink)
        

    # detailsPage = requests.get(link)
    # details = BeautifulSoup(detailsPage.content, features='html.parser')
    #print(details.get_text())
    # text = details.get_text()
    # abstractIndex = text.find('Abstract')
    # lastIndex = text.find('Keywords')
    # abstract = text[abstractIndex:lastIndex]
    # print(abstract)

    #pdf = details.find(class_ = re.compile('.*pdf.*',re.IGNORECASE) )



    # if(link.endswith('.pdf') == False):
    #     detailsPage = requests.get(link)
    #     details = BeautifulSoup(detailsPage.content,features="html.parser")
    #     f = open("demofile3.txt", "w")
    #     f.write(details.get_text())
    #     f.close()
    #     #print(details.get_text())



        # '''abstract = details.find('div',string=re.compile(r'\babstract\b',flags=re.I))
        #     if abstract:
        #     abstractText = abstract.get('p')
        #     print(abstractText)'''
        



    #articleDetail = details.find("article")
    #print(articleDetail)