# To run locally: python3 setup.py
# Followed by: python3 app.py

# Note that the name and schema of the database tables might be different on the server!
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

@app.route('/catbreed', methods=['POST'])
def get_cat_fact():
    cat_breed = request.form.get('breed', '')
    
    if "sleep" in cat_breed.lower():
        return render_template('index.html', message="Obviously there's no Sleep cat breed, duh!")
    
    try:
        query = f"SELECT id, breed FROM cat_breeds WHERE breed = '{cat_breed}'"
        query_result = query_database(query)    
    except Exception:
        query_result = []
    
    if query_result:
        return render_template('index.html', message="Cat breed exists!")
    else: 
        return render_template('index.html', message="Cat breed does not exist :(")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8889, debug=True)