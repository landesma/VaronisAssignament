from datetime import datetime, timedelta

from jwt import DecodeError
from sanic import Sanic
from sanic.response import json as sanic_json
import json
import jwt

JWT_SECRET = "secret"
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_MINUTES = 20

app = Sanic("My Hello, world app")


def login_required(func):
    def wrapper(request):
        if not request.token:
            return sanic_json({'message': 'Auth required'}, status=401)
        try:
            jwt.decode(request.token, JWT_SECRET, JWT_ALGORITHM)
            return func(request)
        except DecodeError:
            return sanic_json({'message': 'Auth failed'}, status=403)

    return wrapper


@app.route('/login')
async def login(request):
    post_data = request.args
    user_name = post_data["username"][0]
    password = post_data["password"][0]

    with open('users.json') as user_file:
        users = json.load(user_file)
        if not users.get(user_name) == password:
            return sanic_json({'message': 'Auth failed'}, status=403)

    payload = {
        'user_name': user_name,
        'exp': datetime.utcnow() + timedelta(minutes=JWT_EXP_DELTA_MINUTES)
    }
    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return sanic_json({'token': jwt_token})


@app.route("/normalize", methods=["POST", ])
@login_required
def normalize_data(request):
    body = {data["name"]: next(data[key] for key in data.keys() if key.endswith("Val")) for data in request.json}
    return sanic_json(body)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
