from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Nome, data, descrição.
amount = 3
events = {
    "01": dict(
        id="01",
        nome="aniv do Thiago",
        data="2023-01-22",
        descricao="parabens",
        user_id="01",
        timestamp=get_timestamp(),
    ),
    "02": dict(
        id="02",
        nome="aniv do Ronaldo",
        data="2023-03-18",
        descricao="parabens ronaldo!!",
        user_id="01",
        timestamp=get_timestamp(),
    ),
    "03": dict(
        id="03",
        nome="MPS",
        data="2023-03-16",
        descricao="Entrega desse trabalho",
        user_id="01",
        timestamp=get_timestamp(),
    ),
}


def read_all():
    return events


def create(event: dict):
    event_id = event.get("event_id", "")
    event_name = event.get("event_name", "")
    event_date = event.get("event_date", "")
    event_desc = event.get("event_desc", "")
    user_id = event.get("user_id", "")
    if event_id and event_id not in events:
        global amount
        amount += 1

        new_event = dict(
            id=event_id,
            nome=event_name,
            data=event_date,
            descricao=event_desc,
            user_id=user_id,
            timestamp=get_timestamp(),
        )

        events[event_id] = new_event

        return new_event, 201
    else:
        abort(406, f"event with {event_name} already exists")


def read_one(event_id):
    if event_id in events:
        return events.get(event_id, "")
    else:
        abort(404, f"Person with ID {event_id} not found")


def update(event_id: str, event: dict):
    if event_id in events:
        events[event_id]["nome"] = event.get("event_name", events[event_id]["nome"])
        events[event_id]["data"] = event.get("event_date", events[event_id]["data"])
        events[event_id]["descricao"] = event.get(
            "event_desc", events[event_id]["descricao"]
        )
        events[event_id]["timestamp"] = get_timestamp()
        return events[event_id]
    else:
        abort(404, f"Person with ID {event_id} not found")


def delete(event_id):
    if event_id in events:
        del events[event_id]
        return make_response(f"{event_id} successfully deleted", 200)
    else:
        abort(404, f"Person with ID {delete} not found")
