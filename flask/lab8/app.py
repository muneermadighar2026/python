from flask import Flask, render_template, request # Import request
import mysql.connector
app = Flask(__name__)
db = {
 "host": "localhost",
 "user": "root",
 "password": "redhat",
 "database": "test"
}

@app.route('/')
def form_page():
 return render_template('submit_name.html') # Serve the page with the form

@app.route('/login-page')                        # Serve the login page
def login_page():
 return render_template('login.html')

@app.route('/login', methods=['POST'])                        # Serve the login page
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    #connect to mysql
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    #check if the email and password match a record in the database
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    values = (email, password)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        return render_template('dahboard.html', firstname=result[1], lastname=result[2], email=result[3]) # return welcome page with dashboard
    else:
        return"invalid email or password" # return an error message

@app.route('/submit',methods=['POST'])      # This route handles the post request from the first form
def handle_submission_post():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')

    #connect to mysql
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    #Insert data into mysql
    query = "INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)"
    values = (firstname, lastname, email, password)
    cursor.execute(query,values)
    connection.commit()
    cursor.close()
    connection.close()
    return "Data submitted successfully" #return a success message

if __name__ == '__main__':
 app.run(debug=True)