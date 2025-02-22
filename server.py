from flask import Flask

app = Flask(__name__)

#Debug is enabled in order for the changes made to the file to be reflected on the webpage without needing to restart the server.
if __name__ == "__main__":
    app.run(debug=True)
