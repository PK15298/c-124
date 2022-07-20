# step 1 : IMPORT THE 'Flask' MODULE (CLASS)
from flask import Flask

# step 2 : to create an object called 'app' for the class Flask --> objectName = CLassname (__name__)
app = Flask(__name__)

# step 3: to define a route --> @objectName.route ("/routeName")
@app.route("/abc")

# step 4: to define the function for the route
def displayWord():
    return "Hello"

#step 5: run the code
if (__name__ == "__main__"):
    app.run(debug=True)