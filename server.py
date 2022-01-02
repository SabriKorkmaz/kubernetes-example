import os

from flask import Flask

app = Flask(__name__)


app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)



@app.route("/")
def main():
    return "Api initialized"


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5555)
