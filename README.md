# FlaskScholarSearchApp

This is a school project that I coded with Flask. This project's purpose is to scrape article informations from a source and displaying those in a website that I created. For scraping I used Python and creating the website I used Flask. I used MongoDB for saving scraped data to database. I used Html and Css for frontend part of the app. 

This website has 2 routes. First one is Home page. This page has a search bar initially and when you search a article of your interest, scraping function starts to run and get all related articles. Articles are saved in database and listed in home page after scraping is done. They have informations like title, authors, summary of article, publisher of article and publishing year. This article information container alsa has a PDF link that is scraped from source and it is clickable. This way whem users click that pdf link, they can reach the article. Title of the article is also clickable and send us to the search route and let us display the clicked article's details. We fetch ID of the saved articles from database and display it in search route like that.

We fetch data with web scraping. I used BeautifulSoup for web scraping. As you can see there are two files for scraping data. They have different sources. One has a website called Dergipark as source and other has Google Scholar. In Google Scolar, I faced some limitations when scraping data. So I used Dergipark as my source in the Flask app. But I still wanted to add other file here to show how to scrape data from there as well.

You can clone the repository and after installing required libraries by running this command : 
```
flask --app main run
```

There are some images from the app: 
<p float="left">
  <img src="https://github.com/cigdeemtok/FlaskScholarSearchApp/blob/main/images/scholar_flask_homepage.png" width="75%" /><br>
  <img src="https://github.com/cigdeemtok/FlaskScholarSearchApp/blob/main/images/scholar_flask_details.png" width="75%" />
</p>

This is the database structure: 
<p float="left">
  <img src="https://github.com/cigdeemtok/FlaskScholarSearchApp/blob/main/images/scholar_flask_database.png" width="75%" />
</p>

I hope you find this project helpful. Any feedback is appreciated.
