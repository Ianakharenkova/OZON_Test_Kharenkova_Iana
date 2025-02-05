import json
import random


class NewValidInputs:
    def __init__(self):
        pass
    def gen_new_email(self):
        valid_inputs_json = '{"email": "","name": " Iana","password": "187654" }'

        valid_inputs = json.loads(valid_inputs_json)
        lst = ['l', 't', 'a', 'M', 'i', 'p', '1', '85']
        new_email_input = random.choices(lst, k=5)
        new_full_email = ''.join(new_email_input)
        lst = ['l', 't', 'a', 'M', 'i', 'p', 'n', 'b']
        new_name_input = random.choices(lst, k=5)
        new_name = ''.join(new_name_input)
        valid_inputs['email'] = new_full_email + "@mail.ru"
        valid_inputs['name'] = new_name
        new_valid = json.dumps(valid_inputs)

        return new_valid

t=NewValidInputs()
print(t.gen_new_email())