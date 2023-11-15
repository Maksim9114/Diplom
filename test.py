# Малыщик Максим, 10-я когорта — Финальный проект. Инженер по тестированию плюс

import sender

def test_get_order_number():
        response = sender.get_order_number()
        assert response.status_code == 200