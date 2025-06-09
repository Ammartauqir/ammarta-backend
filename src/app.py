from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from flask_mail import Mail, Message
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)


# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')

mail = Mail(app)

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        # Create email message
        msg = Message(
            subject=f'AmmarTa Contact Form: {subject}',
            sender=app.config['MAIL_USERNAME'],
            recipients=['ammar.tauqir2@gmail.com']
        )

        # Email body
        msg.html = f'''
            <h2>New Contact Form Submission</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Subject:</strong> {subject}</p>
            <p><strong>Message:</strong></p>
            <p>{message}</p>
        '''

        # Send email
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'}), 200

    except Exception as e:
        print(f'Error sending email: {str(e)}')
        return jsonify({'message': 'Failed to send email'}), 500

@app.route("/api/info")
def get_info():
    return jsonify({"message": "Hello, World! from Flask backend"})

if __name__ == "__main__":
    app.run(debug=True)

