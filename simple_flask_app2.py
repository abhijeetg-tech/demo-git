from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/greet", methods=["POST"])
def greet():

    data = request.json
    #I will do some processing or transformation on the data
    name = data.get("name", "user")
    age = data.get("age", 15)
    
    res = f"Hello, {name}! you are {age} years old."
    return jsonify({"message": res})

if __name__ == "__main__":
    app.run(debug=True)
