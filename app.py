from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

SUPPORT_EMAIL = "help.nexture@gmail.com"

def send_email(name, email, message):
    body = f"""
New client inquiry from Nexture website

Name: {name}
Email: {email}

Message:
{message}
"""
    msg = MIMEText(body)
    msg["Subject"] = "New Client Inquiry - Nexture"
    msg["From"] = SUPPORT_EMAIL
    msg["To"] = SUPPORT_EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SUPPORT_EMAIL, "YOUR_GMAIL_APP_PASSWORD")
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("Email error:", e)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/why")
def why():
    return render_template("why.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    success = False
    if request.method == "POST":
        send_email(
            request.form["name"],
            request.form["email"],
            request.form["message"]
        )
        success = True
    return render_template("contact.html", success=success)

if __name__ == "__main__":
    app.run(debug=True)
