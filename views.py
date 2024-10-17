from flask import Blueprint, render_template,request, redirect, url_for
from .dergipark_scraping import scrape_dergipark
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

views = Blueprint('views', __name__)


client = MongoClient('localhost',27017)

db = client.dergi_flask
articles = db.articles


@views.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        searchedWord = request.form['searchedWord']
        allResults = scrape_dergipark(searchedWord=searchedWord)
        return render_template("home.html",articles=allResults)
    return render_template("home.html")
    

@views.route('/search/<article_id>',methods = ['POST', 'GET'])
def search(article_id):
    article = articles.find_one({'_id': ObjectId(article_id)})
    return render_template("search.html",article=article)