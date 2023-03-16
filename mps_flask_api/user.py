from datetime import datetime
from random import randint
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


amount = 3
resp = {
    "01": dict(
        id="01",
        nome="Thiago",
        idade=19,
        nasicmento="2004-01-22",
        timestamp=get_timestamp(),
    ),
    "02": dict(
        id="02",
        nome="Deb",
        idade=20,
        nasicmento="2002-04-29",
        timestamp=get_timestamp(),
    ),
    "03": dict(
        id="03",
        nome="Luana",
        idade=20,
        nasicmento="2002-10-22",
        timestamp=get_timestamp(),
    ),
}


def read_all():
    return resp


def create(user: dict):
    user_id = user.get("user_id", "")
    user_name = user.get("user_name", "")
    if user_id and user_name not in resp:
        global amount
        amount += 1

        new_user = dict(
            id=user["user_id"],
            nome=user["user_name"],
            idade=randint(10, 50),
            nasicmento=f"{2023 - randint(10, 50)}-{randint(1, 12)}-{randint(1, 31)}",
            timestamp=get_timestamp(),
        )

        resp[user["user_id"]] = new_user

        return new_user, 201
    else:
        abort(406, f"user with {user_name} already exists")


def read_one(user_id):
    if user_id in resp:
        return resp.get(user_id, "")
    else:
        abort(404, f"Person with ID {user_id} not found")


def update(user_id, user):
    if user_id in resp:
        resp[user_id]["nome"] = user.get("user_name", resp[user_id]["nome"])
        resp[user_id]["timestamp"] = get_timestamp()
        return resp[user_id]
    else:
        abort(404, f"Person with ID {user_id} not found")


def delete(user_id):
    if user_id in resp:
        del resp[user_id]
        return make_response(f"{user_id} successfully deleted", 200)
    else:
        abort(404, f"Person with ID {user_id} not found")
