# AC_02_Automacao_Testes_Software
    
Atividade Contínua 02

Exercício 01
Seja o código da classe Blog abaixo que realiza chamadas a uma API aberta, útil para testes,
que devolve posts para um determinado blog.
```sh
# blog.py
import requests
class Blog:
def posts(self):
endereco = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(endereco)
return response.json()
def post_by_user_id(self, userId: str):
e = f"https://jsonplaceholder.typicode.com/posts/{userId}"
response = requests.get(e)
return response.json()
```


Perceba que a classe Blog acessa a API jsonplaceholder, que é um serviço API fake para
testes. Para os testes de unidade, utilize objetos mock que simule o objeto da classe Blog.
Crie testes para os métodos posts e post_by_user_id. Como sugestão para o
desenvolvimento deste exercício, crie uma fixture que devolve uma lista de posts, no mesmo
formato que o serviço API devolve, como apresenta o exemplo abaixo:

```sh
post = [{'userId' : 1,
'Id' : 1,
'title' : 'Titulo teste 1',
'body' : 'Conteudo do blog 1'},
{'userId' : 2,
'Id' : 2,
'title' : 'Titulo teste 2',
'body' : 'Teste de conteudo do blog 2'}]
```

<p align="center">
	<img alt="Repository language count" src="https://img.shields.io/github/languages/count/Matheus-Nazario/AC_01_Automacao_Testes_Software">
	<a href="https://www.linkedin.com/in/matheus-naz%C3%A1rio-676411b3/">
		<img alt="Made by Matheus Nazário" src="https://img.shields.io/badge/Made%20By-Matheus%20Naz%C3%A1rio-green">
	</a>
	<a href="https://github.com/Matheus-Nazario/AC_01_Automacao_Testes_Software/commits/master">
		<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Matheus-Nazario/AC_01_Automacao_Testes_Software?color=blue">
	</a>
	<img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen?color=blue">
</p>

<p align="center">
	<a href="https://www.python.org/">
	  <img alt="Python" src="https://img.shields.io/static/v1?color=red&label=Dev&message=Python&style=for-the-badge&logo=Python">
	</a>
</p>

# ⛏  Tech & Dependências

### Pré-requisitos

* Python 3.10.11
* pytest 7.4.0

<hr>

## Clonando o serviço

```sh
git clone https://github.com/Matheus-Nazario/AC_01_Automacao_Testes_Software.git
 
```

# Executando o serviço

Na pasta raiz do projeto executar o comando:

```sh
pip3 install -r requirements.txt
```

```sh
python3 -m unittest test.testBlog
```

<hr>