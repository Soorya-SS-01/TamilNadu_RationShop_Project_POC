from flask import Flask, request, jsonify, render_template
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText



app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="25610279",
    database="ration_db"
)

cursor = db.cursor(dictionary=True)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Get members
@app.route('/members', methods=['GET'])
def get_members():
    cursor.execute("SELECT * FROM members")
    return jsonify(cursor.fetchall())

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    message = data.get('message')

    sender_email = "rationdepartment1@gmail.com"
    sender_password = "nqll uhov unbc kkue"

    cursor.execute("SELECT email FROM members")
    members = cursor.fetchall()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        for member in members:
            if member['email']:   # skip empty emails
                msg = MIMEText(message, 'plain', 'utf-8')
                msg['Subject'] = "Ration Shop Notification / ரேஷன் கடை அறிவிப்பு"
                msg['From'] = sender_email
                msg['To'] = member['email']

                server.sendmail(sender_email, member['email'], msg.as_string())

        server.quit()

        return jsonify({"message": "Emails sent successfully"})

    except Exception as e:
        print("Email Error:", e)
        return jsonify({"error": str(e)}), 500

# Toggle collected
@app.route('/toggle-status/<int:id>', methods=['PUT'])
def toggle_status(id):
    cursor.execute("UPDATE members SET collected = NOT collected WHERE id=%s", (id,))
    db.commit()
    return jsonify({"message": "Updated"})

@app.route('/add-member', methods=['POST'])
def add_member():
    data = request.json
    name = data['name']
    phone = data['phone']
    email = data.get('email')

    cursor.execute(
        "INSERT INTO members (name, phone, email) VALUES (%s, %s, %s)",
        (name, phone, email)
    )
    db.commit()

    return jsonify({"message": "Added"})

# Delete member
@app.route('/delete-member/<int:id>', methods=['DELETE'])
def delete_member(id):
    cursor.execute("DELETE FROM members WHERE id=%s", (id,))
    db.commit()
    return jsonify({"message": "Deleted"})

@app.route('/send-reminder-email', methods=['POST'])
def send_reminder_email():
    data = request.json
    message = data.get('message')
    emails = data.get('emails')   # ✅ coming from frontend

    sender_email = "rationdepartment1@gmail.com"
    sender_password = "nqll uhov unbc kkue"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        for email in emails:
            if email:
                msg = MIMEText(message, 'plain', 'utf-8')
                msg['Subject'] = "Reminder - Ration Shop"
                msg['From'] = sender_email
                msg['To'] = email

                server.sendmail(sender_email, email, msg.as_string())

        server.quit()

        return jsonify({"message": "Reminder emails sent"})

    except Exception as e:
        print("Email Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    
