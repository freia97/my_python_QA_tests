import requests

class TestFirAPI:
    def test_first_api(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = 'Vitalii'
        data = {'name' : name}
        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong response code"
        response_dict = response.json()
        assert "answer" in response_dict, "There is no field"
        expected_response_text = f"Hello, {name}"
        actual_responce_text = response_dict["answer"]
        assert actual_responce_text == expected_response_text