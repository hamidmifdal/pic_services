from flask import Flask , render_template
r = render_template
app = Flask(__name__)

@app.route('/')
def main():
    return r('dist/index.html')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)