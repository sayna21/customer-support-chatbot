import sqlite3
from werkzeug.security import generate_password_hash
conn=sqlite3.connect('chatbot.db')
hashed_password=generate_password_hash("admin123")
conn.execute("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)", ("Head Admin", "admin@test.com", hashed_password, "admin"))
conn.commit()
conn.close()
print("Admin user created! Login with: admin@test.com / admin123")