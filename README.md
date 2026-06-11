#AI-Powered Customer Support Chatbot

#Project Overview
The AI-Powered Customer Support Chatbot is a professional full-stack web application designed to automate business-to-customer interactions.
It utilizes Natural Language Processing (NLP) to provide instantaneous responses to frequently asked questions, reducing operational costs and improving customer experience.
The system includes a secure management portal for real-time monitoring and knowledge base updates.

#Core Features
Real-time Conversational UI: A sleek, user-friendly chat interface with a custom black theme.
NLP Intent Recognition: Uses smart keyword matching to understand and respond to user queries accurately.
Secure Admin Dashboard: A protected panel for monitoring chat logs and system performance.
FAQ Management: Full administrative control to add, edit, or delete chatbot responses.
Analytics & Reporting: Provides insights into total interactions, popular questions, and success rates.
Human Escalation: Automatically identifies unresolved queries and suggests human agent intervention.
Mobile Responsive: Optimized for various devices, including mobile-friendly layouts tested for consistency.

#Technology Stack
Frontend: HTML5, CSS3 (Custom Styling), JavaScript

Backend: Python Flask

Database: SQLite

NLP Engine: NLTK (Natural Language Toolkit)

#Project Structure
CUSTOMER_SUPPORT_CHATBOT/
├── app.py                 # Core application logic and API routes 
├── database_setup.py      # Database initialization script 
├── create_admin.py        # Secure admin account generation script
├── chatbot.db             # SQLite database storage 
├── static/
│   └── style.css          # Global styling (Black Theme)
└── templates/             # HTML UI components
    ├── index.html         # User chat interface
    ├── admin.html         # Analytics dashboard
    ├── login.html         # Admin authentication
    └── edit.html          # FAQ editor module

#Setup and Installation
1.Clone the Repository: Ensure Python 3.x is installed on your system.

2.Install Dependencies

3.Initialize the Database: Run the setup script to create the required tables (users, faq, chat_history)

4.Create Admin User: Run the utility script to set up your secure credentials

5.Run the Application

6.Access Links:
Chat Interface: http://127.0.0.1:5000/
Admin Dashboard: http://127.0.0.1:5000/admin

#Demo Credentials
To test the secure Admin Dashboard and Analytics features, use the following sample credentials:
Email: admin@test.com
Password: admin123

## Author
**[Sayna Kumari]**