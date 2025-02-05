import requests
from doregistr_inputs import NewValidInputs


class DoRegistration:
    def __init__(self):
        pass

    def success_doRegistration(self:NewValidInputs):
        url = "http://users.bugred.ru/tasks/rest/doregister"
        """self.gen_new_email() - json с уникальными значениями email и имени, чтобы точно пройти регистрацию"""
        registration_result = requests.post(url, self.gen_new_email())
        if registration_result.status_code == 200:
            print(f"Успешно, статус-код:", + registration_result.status_code)
        else:
            print("Ошибка, статус-код:", + registration_result.status_code)
        registration_response = registration_result.json()
        print(registration_response)
        if 'avatar' in registration_response:
            print(f"Решистрация успешно пройдена и присвоен аватар")



valid_inputs_json = NewValidInputs()
registration_success = DoRegistration
registration_success.success_doRegistration(valid_inputs_json)