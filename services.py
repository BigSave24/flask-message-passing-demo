from enum import Status

def retrieve_item(item_id):
    """
    This is a stubbed method of retrieving a resource. It doesn't actually do anything.
    """
    return {
        "id": item_id,
        "brand_name": "Clean Breathing",
        "name": "Air Purifier",
        "weight": 12.3,
    }


def create_item(item_id, request_body):
    """
    This is a stubbed method of creating a resource. It doesn't actually do anything.
    """
    return {
        "id": item_id,
        "body": request_body,
    }

def create_order(body):
    # do stuff to process the data
    return body

def retrieve_orders():
    """
    This is a stubbed method for retrieving multiple orders. IT doesn't actually do anything.
    """
    return [
        {
            "order_id": 1,
            "created_by": "justin",
            "status": Status.Completed.value,
            "created_at": "2020-09-28T08:56:44",
            "equipment": [
                "KEYBOARD"
            ]
        },
        {
            "order_id": 2,
            "created_by": "tom",
            "status": Status.Queued.value,
            "created_at": "2020-09-28T09:56:44",
            "equipment": [
                "MOUSE",
                "WEBCAM"
            ]
        }
    ]
