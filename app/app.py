import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def show_fibonacci():
    nextNumber = 1
    previous = 0
    limit = 50
    found = 0
    answer = "0, "
    while(found < limit):
        temp = nextNumber
        nextNumber = nextNumber + previous
        previous = temp
        found = found + 1
        answer += str(nextNumber) + ", "

    return answer

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)