import configuration
import requests

def new_order(order_body):
               return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER,
                         json=order_body,
                         )


def get_order_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK+str(track_number))

