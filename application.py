import subprocess
from flask import Flask, render_template, request

#importing another python file 
#which containes user defined downloader function 
from download import downloader

#setting a default folder as a destination
DOWNLOADS_FOLDER = './downloads'

#initiating flask
app = Flask(__name__)

#base route that containes main page
@app.route('/')
def index():
    #renders index file which extends layout file
    return render_template('index.html')

#url submission route
@app.route('/download', methods=["POST"])
def download():
    url = request.form.get('download_link')
    file_location = downloader(url,DOWNLOADS_FOLDER)
    if not url:
        return render_template('failure.html')
    else:
        return file_location

if __name__ == "__main__":
    app.run(debug=True)
