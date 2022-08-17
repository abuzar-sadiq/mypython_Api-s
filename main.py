from flask import Flask , render_template , request
import pandas as pd

app = Flask(__name__,static_folder="../templates")
Registrants={}
SPORTS=["cricket","Football","tennis","badminton"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register" , methods = ["POST"])
def register():
    name=request.form.get("name")
    sports=request.form.get("sports")
    if not name or sports not in SPORTS:
        return render_template("failure.html")
    Registrants[name] = sports

    entries = {'Name': Registrants.keys(), 'Sports': Registrants.values()}
    entry = pd.DataFrame(entries)
    # Enter your csv file path to store data in your machine
    entry.to_csv('C:\\Users\\HP\\Desktop\\home100.csv', index=False)
    return render_template("success.html")

@app.route("/registrants")
def registrants():

    return render_template("registrants.html", registrants=Registrants)


if __name__ == "__main__":
   app.run(debug=True)

