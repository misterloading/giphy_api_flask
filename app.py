from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    if request.form["search"]:
        url = "https://api.giphy.com/v1/gifs/search?api_key=GmrOhlsTkFtVCMyuaN2ZhbNbKZUcN6ys&q=" + request.form["search"] + "&limit=16"
        giphy = requests.get(url)
        data_giphy = giphy.json()
        
        return render_template("index.html", data= data_giphy["data"])
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)