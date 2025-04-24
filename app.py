from flask import Flask

app = Flask(__name__) # create an instance of the Flask class

@app.route('/')  # decorator to tell Flask what URL should call the function
def main(): # function to run when the route is accessed

    print('Hello, World!')
    return 'Hello, World!'




if __name__ == '__main__': # run the app
    app.run() # run the app on the local development server
