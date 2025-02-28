from flask import Flask,render_template
from mpmath import mp
def get_current():
    global chiffres
    with open("pi.txt","r") as f:
        chiffres = len(f.read())
        mp.dps = chiffres - 1
    f.close()
def update():
    mp.dps = mp.dps + 10
    with open("pi.txt","w") as r:
        r.write(str(mp.pi))
    r.close()
app = Flask(__name__)
get_current()
update()
@app.route("/")
def home():
    return render_template("index.html",pi=str(mp.pi))

if __name__ == "__main__":
    app.run(debug=False)
