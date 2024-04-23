from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

def creatingTable():
    conn = sqlite3.connect('to_do_list.db')
    conn.execute('CREATE TABLE IF NOT EXISTS TO_DO_LIST(task_no INTEGER , task TEXT)')

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_task' , methods = ['POST'])
def add_task():
    creatingTable()
    conn = sqlite3.connect('to_do_list.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO TO_DO_LIST(task_no , task ) VALUES (?, ?)', (request.form['task_no'], request.form['task']))
    conn.commit()
    conn.close()
    return 'Task added successfully'

@app.route('/update_task' , methods = ['POST'])
def update_task():
    conn = sqlite3.connect('to_do_list.db')
    cur = conn.cursor()
    cur.execute('UPDATE TO_DO_LIST SET task =? WHERE task_no = ?' ,( request.form['task'],request.form['task_no']))
    conn.commit()            
    conn.close()
    return 'Task updated successfully'

@app.route('/delete_task' , methods = ['POST'])
def delete_task():
    conn = sqlite3.connect('to_do_list.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM TO_DO_LIST WHERE task_no = ?', (request.form['task_no'],))
    conn.commit()
    conn.close()
    return 'Task deleted successfully'

@app.route('/show_list' , methods = ['GET'])
def show_list():
    conn = sqlite3.connect('to_do_list.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM TO_DO_LIST ')
    tasks = cur.fetchall()
    conn.close()
    return render_template('show_list.html', tasks=tasks)

app.run(debug=True)
