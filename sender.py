import configuration
import requests
import data

def new_order(order_body):
               return requests.post(configuration.URL_SERVICE + configuration.new_order,
                         json=order_body,
                         )


def get_order_number():
    response = new_order(data.order_body)
    track_number = str(response.json()["track"])
    return requests.get(configuration.URL_SERVICE + configuration.order_track+track_number
                         )