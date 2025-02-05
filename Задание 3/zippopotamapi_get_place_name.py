import requests

class TestGetPlaceName:
    def __init__(self):
        pass

    def get_place_name_on_code(self):
        url="https://api.zippopotam.us/RU/440047"
        result = requests.get(url)
        if result.status_code == 200:
            print(f"Успешно, статус-код:", + result.status_code)
        else:
            print("Ошибка, статус-код:", + result.status_code)

        valid_place_name = "Пенза 47"
        response = result.json()
        check_in_response = response['places'][0]['place name']
        if valid_place_name in check_in_response :
            print("Код соответствует месту")
        else:
            print("Код не соответствует месту")



region_on_code = TestGetPlaceName()
region_on_code.get_place_name_on_code()