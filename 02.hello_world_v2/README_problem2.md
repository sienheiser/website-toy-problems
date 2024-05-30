In this problem we make the website print "Hello World" again. 
The difference is how we structure the application. Try making the 
flask application run with the following directory structure

.
├── README.md
├── app
│   ├── __init__.py
│   ├── hello_world.py
│   └── templates
│       └── hello_world.html
└── main.py


main.py will only have the following code

"""from app import app

if __name__ == "__main__":
   app.run(debug=True)"""


