import sqlite3
conn=sqlite3.connect('chatbot.db')
cursor=conn.cursor()
# 1. Create FAQ Table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS faq(
                   faq_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   question TEXT NOT NULL,
                   answer TEXT NOT NULL
               )
               ''')
# 2. Create Chat History Table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS chat_history(
                   chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   message TEXT,
                   response TEXT,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
               )
               ''')
# 3. Create Users Table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL,
                   role TEXT DEFAULT 'admin'
               )
               ''')
# Insert some dummy FAQ data for testing
cursor.execute("INSERT INTO faq (question, answer) VALUES ('Refund policy?', 'Refunds are available within 7 days.')")
cursor.execute("INSERT INTO faq (question, answer) VALUES ('Where is my order?', 'Please provide your order ID.')")
conn.commit()
conn.close()
print("Database and tables created successfully!")