# To run locally: python3 setup.py
# Followed by: python3 app.py

# Note that the name of the database tables might be different on the server!
from flask import Flask, request, render_template
import sqlite3 
from config import SECRET_KEY 

app = Flask(__name__)
app.secret_key = SECRET_KEY 

def query_database(query):
    conn = sqlite3.connect('file:instance/ctfchallenge.db?mode=ro', uri=True)
    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()
    conn.close()
    
    return result

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/catfact', methods=['POST'])
def get_cat_fact():
    cat_fact_id = request.form.get('id', '')
    
    try:
        query = f"SELECT id, fact FROM facts WHERE id = '{cat_fact_id}'"
        fact = query_database(query)
    except Exception:
        fact = [(0, "Oops, an error occured!")]
    
    if fact:
        return render_template('index.html', fact=fact[0][1])
    else: 
        return render_template('index.html', fact="No cat facts for this ID :(")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)