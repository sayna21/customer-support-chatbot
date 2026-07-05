from flask import Flask, render_template, request, jsonify, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import nltk
from nltk.tokenize import word_tokenize
app=Flask(__name__)
app.secret_key='super_secret_key_for_this_internship_project'
def get_db_connection():
    conn= sqlite3.connect('chatbot.db')
    conn.row_factory=sqlite3.Row
    return conn
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message").lower()

    tokens = word_tokenize(user_message)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    bot_response = None
    
    all_faqs = cursor.execute('SELECT question, answer FROM faq').fetchall()
    for faq in all_faqs:
        question = faq['question'].lower()
        
        if any(word in question for word in tokens if len(word) > 2):
            bot_response = faq['answer']
            break

    if not bot_response:
        cursor.execute("SELECT answer FROM faq WHERE question LIKE ?", ('%' + user_message + '%',))
        result = cursor.fetchone()
        if result:
            bot_response = result['answer']

    if not bot_response:
        bot_response = "I'm sorry, I don't have an answer for that. Connecting you to a support agent..."
        
    # Chat History table
    cursor.execute("INSERT INTO chat_history (user_id, message, response) VALUES (?, ?, ?)", (1, user_message, bot_response))
    conn.commit()
    conn.close()
    
    return jsonify({"response": bot_response})
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        conn=get_db_connection()
        user=conn.execute('SELECT * FROM users WHERE email=?', (email,)).fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['user_id']=user['user_id']
            session['role']=user['role']
            return redirect('/admin')
        return "Invalid credentials!"
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
    
# --- ADMIN DASHBOARD ROUTES ---
@app.route('/admin')
def admin():
    if 'user_id' not in session:
        return redirect('/login')
    conn=get_db_connection()
    faqs=conn.execute('SELECT * FROM faq').fetchall()
    logs=conn.execute('SELECT * FROM chat_history ORDER BY timestamp DESC').fetchall()
    total_chats = conn.execute('SELECT COUNT(*) FROM chat_history').fetchone()[0]
    most_asked=conn.execute('SELECT message, COUNT(message) as count FROM chat_history GROUP BY message ORDER BY count DESC LIMIT 3').fetchall()
    failed=conn.execute("SELECT COUNT(*) FROM chat_history WHERE response LIKE 'I%m sorry%'").fetchone()[0]
    success_rate=round(((total_chats - failed)/total_chats)*100,1)if total_chats>0 else 0
    conn.close()
    return render_template('admin.html', faqs=faqs, logs=logs, total_chats=total_chats, most_asked=most_asked, success_rate=success_rate)

@app.route('/add_faq', methods=['POST'])
def add_faq():
    question=request.form['question']
    answer=request.form['answer']
    conn=get_db_connection()
    conn.execute('INSERT INTO faq (question, answer) VALUES(?, ?)', (question, answer))
    conn.commit()
    conn.close()
    return redirect('/admin')
@app.route('/delete_faq/<int:id>')
def delete_faq(id):
    conn=get_db_connection()
    conn.execute('DELETE FROM faq WHERE faq_id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/admin')
@app.route('/edit_faq/<int:id>')
def edit_faq(id):
    conn=get_db_connection()
    faq=conn.execute('SELECT * FROM faq WHERE faq_id=?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', faq=faq)
@app.route('/update_faq/<int:id>', methods=['POST'])
def update_faq(id):
    question=request.form['question']
    answer=request.form['answer']
    conn=get_db_connection()
    conn.execute('UPDATE faq SET question=?, answer=? WHERE faq_id=?', (question, answer, id))
    conn.commit()
    conn.close()
    return redirect('/admin')
        
if __name__=='__main__':
    app.run(debug=True)