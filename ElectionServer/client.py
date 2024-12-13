from pprint import pprint
import requests


election_srv = requests.get('http://127.0.0.1:8000/api/election/get_election/?id=1')
response = election_srv.json()['response']

choices = response['choices']
election_data = response['election']

choices_choice = {i['id']:i['name'] for i in choices}
election = {
    'id': election_data['id'],
    'name': election_data['name']
}
txt = [f'{i['id']}. {i['name']}' for i in choices]

print(f'Голосование "{election['name']}"')

name = input('Введит свой id: ')
while True:
    choice = int(input(f'''
Введите id ответа
{"\n".join(txt)}: '''))
    if choices_choice.get(choice):
        break
    print('Такого числа не существует!\n')


data = {
    'id_card': name,
    'election': election['id'],
    'choice': choice
}

resp = requests.post('http://127.0.0.1:8000/api/user/post_user_election/', data=data)
print(resp.text)