from flask import Flask,render_template,request,redirect
from flask_mail import Mail,Message

app=Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'parisath213@gmail.com'
app.config['MAIL_PASSWORD'] = 'zguuhclbjkxheeup'
app.config['MAIL_USE_TLS'] = True

mail = Mail(app)

@app.route("/",methods=["GET","POST"])
def send():
    if request.method=="POST":
        get_mail=request.form.get("mailid")
        get_info=request.form.get("receive")
        message=request.form.get("message")
        msg=Message('subject',sender=get_mail,recipients=[get_info])
        msg.body=message
        mail.send(msg)
        return "mail send....!"
    return render_template("mail.html")
if __name__=="__main__":
    app.run(debug=True)


