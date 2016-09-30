import random
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("button.html")

@app.route("/reg", methods=['POST'])
def register():
    return render_template("reg.html")
    
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
    ##print request.args['KELLY']
    status = "failure"
    if request.form['username'] == "JERRY":
        status = "success"
        
    return render_template("sOrF.html", sOrF=status)
    

if __name__=="__main__":
    app.debug = True
    app.run()
