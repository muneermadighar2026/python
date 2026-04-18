from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
@app.route('/api/time')
def current_time_api():
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S") # Format the time as a string
# For an API, returning JSON is often preferred:
    response_data = {"current_timestamp": now.isoformat(),"readable_time": time_string,"timezone_info": str(now.astimezone().tzinfo)}
    return response_data # Flask automatically converts dict to JSON
if __name__ == '__main__':
    app.run(debug=True)