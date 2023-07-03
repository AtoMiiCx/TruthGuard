TruthGuard - Fake News Detection Web App
TruthGuard is a web application designed to verify the authenticity of news articles provided via a URL. The application utilizes machine learning algorithms to analyze the content of the article and determine if it is fake or true. In addition to detecting fake content, the application also checks for bad grammar and other signs of unreliable sources.

Table of Contents
Introduction
Features
Technologies Used
Setup
Usage
API Endpoints
Contributing
License
Introduction
Fake news has become a prevalent issue in today's information age. TruthGuard aims to combat misinformation by providing users with a tool to assess the credibility of news articles. The application uses a combination of machine learning algorithms and curated databases of fake and true articles to make informed predictions about the reliability of the content.

Features
Verify the authenticity of news articles by providing a URL.
Utilize machine learning algorithms to perform fact-checking and content analysis.
Detect fake content, bad grammar, and signs of unreliable sources.
Provide detailed results, including the prediction (fake or true), detected language, website status, and more.
Technologies Used
Vue.js: Frontend framework for building the user interface.
Flask: Backend framework for creating the RESTful API.
Firebase Firestore: Cloud-based NoSQL database for storing article and source information.
Machine Learning Algorithms: Trained models for fake news detection and content analysis.
Axios: JavaScript library for making API requests from the Vue.js app.
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/TruthGuard.git
cd TruthGuard
Install the required dependencies for both the frontend and backend:

Frontend:

bash
Copy code
cd frontend
npm install
Backend:

bash
Copy code
cd backend
pip install -r requirements.txt
Set up your Firebase Firestore database and obtain the necessary credentials.

Configure the backend Flask app with your Firebase credentials in app.py.

Usage
Run the backend Flask app:

bash
Copy code
cd backend
python app.py
Run the frontend Vue.js app:

arduino
Copy code
cd frontend
npm run serve
Access the TruthGuard web application by visiting http://localhost:8080 in your web browser.

API Endpoints
POST /verify: Endpoint to verify the authenticity of a news article using a URL. Provide the URL as a JSON object in the request body. The response will contain detailed information about the article's trueness, detected language, website status, etc.
Contributing
Contributions to TruthGuard are welcome! If you find any bugs or have ideas for new features, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
