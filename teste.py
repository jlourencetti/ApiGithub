import unittest
import requests


def get_username(username):
    resposta = requests.get(f'https://api.github.com/users/{username}')
    if resposta.status_code == 200:
        return resposta.json()


usuario = get_username('jlourencetti')
print(usuario)


class User:
    def __init__(self, user):
        self.user = user

    def get_parameter(self):
        resposta = requests.get(f'https://api.github.com/users/{self.user}')
        if resposta.status_code == 200:
            data = resposta.json()

        parameters = ['login', 'id', 'avatar_url', 'html_url']
        requisicao = {}
        for x in parameters:
            requisicao[x] = data[x]
        return(requisicao)


# usuario = User('jlourencetti')
# print(usuario.get_parameter())


class TestMethods(unittest.TestCase):

    def test_this_test_words(self):
        self.assertTrue(True)

    def test_username_parameters(self):
        parameters = ['login', 'id', 'avatar_url', 'html_url']
        response = get_username('jlourencetti')
        for param in parameters:
            self.assertTrue(param in response.keys())

    def test_user_object(self):
        parameters = ['login', 'id', 'avatar_url', 'html_url']
        check = get_username('jlourencetti')
        for param in parameters:        
            self.assertFalse(param in check.keys())


if __name__ == "__main__":
    unittest.main()
