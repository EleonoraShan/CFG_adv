import requests
from flask import Flask, render_template, request

app = Flask("MyApp")



@app.route("/<name>")
def hello_someone(name):
    return render_template("aboutpage.html", name=name.title())



@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["fnm"]
    print form_data["lnm"]
    print form_data["email"]
    #input=[form_data["fnm"],form_data["lnm"],form_data["email"]]
    m=open("mailing_list.txt", "a")
    m.write(form_data["fnm"])
    m.write(" ")
    m.write(form_data["lnm"])
    m.write(" ")
    m.write(form_data["email"])
    m.write("\n")

    m.close()
    #return "All ok!"
    return render_template("thankyou.html")









#$_POST['email']


#def send_simple_message():
#    return requests.post(
#        "https://api.mailgun.net/v3/sandbox7f65b143e7d5432fb278826b03c5fd83.mailgun.org/messages",
#        auth=("api", "44183171cf7f6a3fe49a3ca761e59cee-1df6ec32-e2806521"),
#        data={"from": "Excited User <mailgun@sandbox7f65b143e7d5432fb278826b03c5fd83.mailgun.org>",
#             #"to": ["ela.shantsila@hotmail.co.uk", "YOU@sandbox7f65b143e7d5432fb278826b03c5fd83.mailgun.org"],
#              "to": [form_data['email']],
#              "subject": "Hello",
#              "text": "Testing some Mailgun awesomness!"})

#send_simple_message()




app.run(debug=True)
