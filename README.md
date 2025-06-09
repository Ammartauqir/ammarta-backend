# Portfolio Backend

This is the backend server for the portfolio website, handling contact form submissions and email notifications.

## Setup Instructions

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Gmail credentials:
```
EMAIL_USER=your.email@gmail.com
EMAIL_PASS=your_app_specific_password
```

4. For Gmail setup:
   - Enable 2-factor authentication in your Google Account
   - Generate an "App Password":
     1. Go to Google Account → Security
     2. Under "2-Step Verification", click on "App passwords"
     3. Select "Mail" and your device
     4. Copy the generated password
   - Use this App Password in the `.env` file

5. Run the server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### Contact Form
- **URL**: `/api/contact`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "name": "Sender Name",
    "email": "sender@email.com",
    "subject": "Message Subject",
    "message": "Message Content"
  }
  ```

### Health Check
- **URL**: `/api/info`
- **Method**: `GET`
- **Response**: `{"message": "Backend is working!"}`

## Features
- Contact form email handling
- CORS support for frontend communication
- Environment variable configuration
- Error handling and logging
- HTML email formatting# Portfolio Backend

This is the backend server for the portfolio website, handling contact form submissions and email notifications.

## Setup Instructions

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Gmail credentials:
```
EMAIL_USER=your.email@gmail.com
EMAIL_PASS=your_app_specific_password
```

4. For Gmail setup:
   - Enable 2-factor authentication in your Google Account
   - Generate an "App Password":
     1. Go to Google Account → Security
     2. Under "2-Step Verification", click on "App passwords"
     3. Select "Mail" and your device
     4. Copy the generated password
   - Use this App Password in the `.env` file

5. Run the server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### Contact Form
- **URL**: `/api/contact`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "name": "Sender Name",
    "email": "sender@email.com",
    "subject": "Message Subject",
    "message": "Message Content"
  }
  ```

### Health Check
- **URL**: `/api/info`
- **Method**: `GET`
- **Response**: `{"message": "Backend is working!"}`

## Features
- Contact form email handling
- CORS support for frontend communication
- Environment variable configuration
- Error handling and logging
- HTML email formatting