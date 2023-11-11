import sender
import data

def test_get_order_number():
        response = sender.get_order_number()
        assert response.status_code == 200