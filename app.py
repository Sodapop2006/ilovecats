from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def cats():
    url = "https://api.thecatapi.com/v1/images/search"
    r = requests.get(url)
    json = r.json()
    url = json[0]["url"]

    return "<img src = '" + url + "'></img>"

# --------------------------------------------------

# import requests

# url = "https://api.thecatapi.com/v1/images/search"
# r = requests.get(url)
# json = r.json()
# url = json[0]["url"]
# print(url)
# <img scr="cat.com/catPic.jpg"></img>