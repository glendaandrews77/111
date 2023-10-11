from flask import Flask # from the flask module import the Flask class

#OOPP -> Object Oriented Paradigm
app = Flask (__name__)  # create an instance of Flask (an object)
                        # variables that belong to a class
                        #are called (class) attributes.
                        #Functions that belong to a class
                        #are called "methods",
@app.get("/")           # Flask decorator
def index():            # View function
    me = {
        "first_name": "Glenda",
        "last_name": "GPL",
        "hobbies": "DIY stuff",
        "is_active": True
    }
    return me            # return statement (JSON)
