import hashlib
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("button.html", extra= "")

@app.route("/reg", methods=['POST'])
def register():
    return render_template("reg.html")

@app.route("/confirm", methods=['POST'])
def confirm():
    print "THE INPUT: username/password"
    print "\n\n\n"
    print request.form["username"] + "/" + request.form["password"]
    users = open('users.csv','r')
    userL = users.read()
    userL = userL.split("\n")
    name = request.form["username"]
    pswd = request.form["password"]
    hashObj = hashlib.sha1()
    hashObj.update(pswd)
    pswd = hashObj.hexdigest()
    status = "success"
    for x in userL:
        print x + "\n"
        if x == name:
            status = "failure. Username is already registered!"
            #add()
    users.close()
    if status == "success":
        users = open("users.csv", "a")
        users.write("" + name + "\n")
        users.close()
        pCodes = open("pCodes.csv","a")
        pCodes.write("" + pswd + "\n")
        pCodes.close()
        return render_template("button.html", extra="Account creation is a success!")
    else:
        return render_template("sOrF.html", sOrF = status)

@app.route("/auth", methods=['POST'])
def authenticate():
    print "THE INPUT: username/password"
    print "\n\n\n"
    print request.form["username"] + "/" + request.form["password"]
    users = open('users.csv','r')
    userL = users.read()
    userL = userL.split("\n")
    pCodes = open('pCodes.csv','r')
    pCodesL = pCodes.read()
    pCodesL = pCodesL.split("\n")
    print pCodesL[1]
    name = request.form["username"]
    pswd = request.form["password"]
    pos = 0
    realPos = -1
    for x in userL:
        if x == name:
            realPos = pos
        pos+=1
    status = "failure,"
    if realPos < 0:
        status += " username is not registered!"
    else:
        status += " Wrong password!!!"
    hashObj = hashlib.sha1()
    hashObj.update(pswd)
    pswd = hashObj.hexdigest()
    if pswd == pCodesL[realPos]:
        status = "success"
        
    return render_template("sOrF.html", sOrF=status)


if __name__=="__main__":
    app.debug = True
    app.run()
