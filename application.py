from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=["POST"])
def download():
    url = request.form.get('download_link')
    if not url:
        return render_template('failure.html')
    else:
        return f'Requested URL {url}'


if __name__ == "__main__":
    app.run(debug=True)
