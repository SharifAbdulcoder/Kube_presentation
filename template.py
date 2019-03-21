from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/", methods={'GET'})
def index():
    user1 = {'name' : 'Abdul Sharif', 'username': 'abdugofir', 'email': 'abdugofir@gmail.com', 'password' : 'Redhat2019**&'}
    items = [{'text' : 'First'}, {'text' : 'Second'}, {'text': 'Third'}]
    return render_template("layout.html", abdul=True, username=user1['username'], python='Python', email=user1['email'], password=user1['password'], items=items)

if __name__ == "__main__":
    app.run(debug=True)
