from flask import Flask, render_template, redirect, url_for, request
from email.message import EmailMessage
import ssl
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']

        if name == "jaii" and password == "2305":
            return redirect(url_for('show_attendance'))
        else:
            return "Invalid username or password"

@app.route('/attendance')
def show_attendance():
    return render_template('attendence.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        email_sender = "kishoree2375@gmail.com"
        email_password = "rvsy meio kasm hjdf" 
        
        section_emails = {
            "AI&DS-A": "jaiisrinivasan2305@gmail.com",
            "AI&DS-B": "jaiisrinivasan2305@gmail.com",
            "ECE-A": "ece_a@example.com",
            "ECE-B": "ece_b@example.com",
            "CSE-A": "cse_a@example.com",
            "CSE-B": "cse_b@example.com",
            "IT": "jaiisrinivasan2305@gmail.com",
            "CSBS": "jaiisrinivasan2305@gmail.com",
            "MECH": "jaiisrinivasan2305@gmail.com",
        }

        attendance_data = {
            "AI&DS-A": request.form.get('aia', ''),
            "AI&DS-B": request.form.get('aib', ''),
            "ECE-A": request.form.get('eca', ''),
            "ECE-B": request.form.get('ecb', ''),
            "CSE-A": request.form.get('csa', ''),
            "CSE-B": request.form.get('csb', ''),
            "IT": request.form.get('it', ''),
            "CSBS": request.form.get('cb', ''),
            "MECH": request.form.get('me', ''),
        }

        for section, attendance in attendance_data.items():
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = section_emails.get(section, '') 
            em['Subject'] = f"Attendance for {section}"
            body = f"Attendance for {section}:\n\n{attendance}\n"
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.send_message(em)

        return "Emails sent successfully!"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
