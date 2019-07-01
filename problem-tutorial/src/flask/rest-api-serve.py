from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'user_id': 1, 'user_name': ''}
]


@app.route('/users/<user_id>')
def get_user(user_id):
    print("get the user:", user_id)
    return jsonify(users)


if __name__ == '__main__':
    app.run(port=8081)
