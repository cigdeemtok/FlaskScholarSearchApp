import requests
from bs4 import BeautifulSoup
import time
import random
from pymongo import MongoClient


def scrape_dergipark(searchedWord):
    rate = [i/10 for i in range(10)]

    client = MongoClient('localhost',27017)

    db = client.dergi_flask
    dbArticles = db.articles

    

    yayinID = ""
    yayinAdi = ""
    yazarlar = ""
    tur = ""
    yayimTarihi = ""
    yayimciAdi = ""
    keywords = ""
    ozet = ""
    #referanslar = list()
    #citied by
    alintiSayisi = ""
    doiNum = ""
    urlAdresi = ""
    pdfLink = ""


    #searchedWord = 'text summarization'
    

    count = len(searchedWord.split())

    searchedWord = searchedWord.replace(" ","+")

    print(f"searched word {searchedWord}")
    print(f"word count {count}")

    baseUrl = "https://dergipark.org.tr"

    url ="https://dergipark.org.tr/tr/search?q={}&section=articles".format(searchedWord)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, features = "html.parser")


    body = soup.find("div", attrs={"class":"article-cards"})


    articles = body.find_all("div",attrs={"class":"card-body"})
    # print(articles)
    for article in articles:
        #print(article)
        print("----------") 
        title = article.find("h5",attrs={"class":"card-title"})
        urlAdresi = title.a.get("href")
        print(urlAdresi)
        name = title.a.get_text()
        yayinAdi = ' '.join(name.split())
        print(yayinAdi)
        type = title.find("small", attrs={"class":"article-meta"})
        tur = type.get("span")
        print(tur)

        #makale detayına git
        

        detailsPage = requests.get(urlAdresi)
        details = BeautifulSoup(detailsPage.content, features="html.parser")

        #page content
        content = details.find("div", attrs={"id":"body-push-down"})

        #yayin adi
        yayimciAdi = content.find("h1",attrs={"id":"journal-title"}).get_text() if content else "None"
        print(yayimciAdi)

        # #pdf link
        pdf = content.find("a",attrs={"class":"pdf"}).get("href") if content else "None"
        pdfLink = baseUrl + pdf
        print(pdfLink)

        #authors
        authorsPart = content.find("p",attrs={"class":"article-authors"}).text.strip() if content else "No Author Information"
        yazarlar = ' '.join(authorsPart.split())
        print(yazarlar)

        # #doi number
        # doiNum = content.find("a",attrs={"class":"doi-link"}).text
        # print(doiNum)
    
        # #abstract
        abstractPart = content.find("div",attrs={"class":"article-abstract"})
        abstract = abstractPart.find("p") if abstractPart else "No Abstract Information"
        ozet = ','.join(abstract.text.strip().split('\n'))
        print(ozet)

        # #keywords
        keywords = content.find("div",attrs={"class":"article-keywords"}).text if keywords else "No Keywords"
        #keywords = keywordsPart.find_all("a")
        print(keywords)
        

        #references
        # referencePart = content.find("ul",attrs={"class":"fa-li"}).text
        # print(referencePart)
        # references = referencePart.find_all("li")
        # for reference in references:
        #     items = reference.text.strip()
        #     print(items)       

        #publication date
        articleInfo = content.find("span",attrs={"class":"article-subtitle"}).text if content else "No Article Information"
        cutIndex = articleInfo.find(",")
        yayimTarihi = articleInfo[:cutIndex]
        print(yayimTarihi)

        # #cited by 
        # alintiSayisi = content.find("div",attrs={"class":"ml-3"}).text
        # # citeNum = cited.get("span").text
        # print(alintiSayisi)

    

        dbArticles.insert_one({
        'searchedWord': searchedWord,
        'name':yayinAdi,
        'authors': yazarlar,
        'tur':tur ,
        'ozet' : ozet,
        'keywords':keywords,
        'yayimTarihi':yayimTarihi,
        'yayimciAdi':yayimciAdi,
        'alintiSayisi':'--',
        'doiNum':'--',
        'urlAdresi' : urlAdresi,
        'pdfLink' : pdfLink
        })



        time.sleep(random.choice(rate))
    return dbArticles.find({"searchedWord" : searchedWord})