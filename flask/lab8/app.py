from flask import Flask, render_template, request # Import request
# import mysql.connector

app = Flask(__name__)

# db = {
#     "host": "localhost",
#     "user": "root",
#     "password": "redhat",
#     "database": "test"
# }

@app.route('/')
def form_page():
 return render_template('login.html') # Serve the page with the form

@app.route('/register')
def register_page():
 return render_template('register.html') # Serve the page with the form


@app.route('/login-page')
def login_page():
 return render_template('login.html') # Serve the login page
 
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == "john@example.com" and password == "123456":
        result = ("John", "Doe", "john@example.com")  # Simulate a successful login with hardcoded user data
    else:
        result = None  # Simulate a failed login attempt


    # # connect to mysql
    # connection = mysql.connector.connect(**db)
    # cursor = connection.cursor()
    # # check if the email and password match a record in the database
    # query = "SELECT * FROM users WHERE email = %s AND password = %s"
    # values = (email, password)
    # cursor.execute(query, values)
    # result = cursor.fetchone()
   
    # cursor.close()
    # connection.close()

    if result:
        return render_template('dashboard.html', firstname=result[0], lastname=result[1], email=result[2])  # Render a welcome page with the user's first name
    else:
        error_message = "Invalid email or password. Please try again."
        return render_template('login.html', error=error_message)  # Re-render the login    
        

# @app.route('/submit',methods=['POST'])  # This route handles the post request from the first form
# def handle_submission_post():
#     firstname = request.form.get('firstname')
#     lastname = request.form.get('lastname')
#     email = request.form.get('email')
#     password = request.form.get('password')

#     # connect to mysql
#     connection = mysql.connector.connect(**db)
#     cursor = connection.cursor()
#     # insert data into mysql
#     query = "INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)"
#     values = (firstname, lastname, email, password)
#     cursor.execute(query, values)
#     connection.commit()
#     cursor.close()
#     connection.close()
#     success_message = "Data submitted successfully! You can now log in with your email and password."
#     return render_template('submit_name.html', success=success_message)  # Re-render the form page with a success message


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)