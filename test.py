# Малыщик Максим, 10-я когорта — Финальный проект. Инженер по тестированию плюс

import sender
import data

def test_get_order_number():

    order_response = sender.new_order(data.order_body)
    track_number = order_response.json()["track"]
    response = sender.get_order_number(track_number)
    assert response.status_code == 200