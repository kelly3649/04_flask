import hashlib

from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

app.secret_key = '\xb6\x16\xea"\xffA\x93(I\x8am)\x18>\xc2\x06\x07\x02\x9c\xb8\xbb\xbbxw\x98\xc1q\r\x04&\x97\xa7'


@app.route("/")
def login():
    return render_template("home.html", extra= "")

@app.route("/jacobo")
def js():
    return redirect("/")

@app.route("/reg", methods=['POST'])
def register():
    return render_template("reg.html")

@app.route("/confirm", methods=['POST'])
def confirm():
    print "THE INPUT: username/password"
    print "\n\n\n"
    name = request.form["username"]
    pswd = request.form["password"]
    print "****************"
    print name + "/" + pswd 
    users = open('data/users.csv','r')
    userL = users.read()
    userL = userL.split("\n") 
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
        users = open("data/users.csv", "a")
        users.write("" + name + "\n")
        users.close()
        pCodes = open("data/pCodes.csv","a")
        pCodes.write("" + pswd + "\n")
        pCodes.close()
        return render_template("home.html", extra="Account creation is a success!")
    else:
        return render_template("sOrF.html", sOrF = status)

@app.route("/auth", methods=['POST'])
def authenticate():
    print "THE INPUT: username/password"
    print "\n\n\n"
    name = request.form["username"]
    pswd = request.form["password"]
    print name + "/" + pswd
    #name = app.secret_key
    users = open('data/users.csv','r')
    userL = users.read()
    userL = userL.split("\n")
    pCodes = open('data/pCodes.csv','r')
    pCodesL = pCodes.read()
    pCodesL = pCodesL.split("\n")
    print pCodesL[1]
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
        session[name] = pswd
        session["TorF"] = True 
        status = "success"
    print "*************" + session["Jerry"]
    if session["TorF"]==True:
        return render_template("welcome.html")
    else:
        return render_template("sOrF.html", sOrF=status)

@app.route("/logout", methods=["POST"])
def logout():
    session["TorF"] = False
    return render_template("home.html", extra="")
    

if __name__=="__main__":
    app.debug = True
    app.run()
 
