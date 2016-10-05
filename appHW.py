import hashlib
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("button.html")

@app.route("/reg", methods=['POST'])
def register():
    return render_template("reg.html")

@app.route("/confirm", methods=['POST'])
def confirm():
    print "THE INPUT: username/password"
    print "\n\n\n"
    print request.form["username"] + "/" + request.form["password"]
    name = request.form["username"]
    pswd = request.form["password"]
    users = open('users.csv','r')
    users = users.read()
    users = users.split()
    status = "success"
    for x in users:
        print x + "\n"
        if x == name:
            status = "failure. Username is already registered!"
            #add()
    return render_template("sOrF.html", sOrF=status)

@app.route("/auth", methods=['POST'])
def authenticate():
    print "\n\n\n"
    print ":::DIAG::: this Flask obj"
    print app
    print "request"
    print request
    print "headers"
    print request.headers
    print "methods"
    print request.method
    print "argss"
    status = "failure"
    if request.form['username'] == "JERRY":
        status = "success"
        
    return render_template("sOrF.html", sOrF=status)


if __name__=="__main__":
    app.debug = True
    app.run()
