from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

#get webpage content to text
source = requests.get('https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/').text

soup = BeautifulSoup(source, 'lxml')

#Flask configuration
app = Flask(__name__)
@app.route('/')
def index():
    #main details
    head = soup.find('title').get_text() #article title
    content = soup.find('article').get_text()

    #adittional details
    img = soup.find("meta",  property="og:image")['content']
    site_name = soup.find("meta",  property="og:site_name")['content']
    updated_date = soup.find("meta",  property="article:published_time")['content']
    description = soup.find("meta",  property="og:description")['content']
    #save values in dictionary
    hi = [1,2]

    #send variables to index.hmtl
    return render_template('index.html',**locals())

app.run(debug=True)