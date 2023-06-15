# python-challenge Sou Pilar

Autor da solução: Lucas da Silva de Oliveira (lucasoliveira783@gmail.com, https://www.linkedin.com/in/lucas-sil-oliveira)

## Apresentação do problema

Usando Python, escreva o código de uma API com as seguintes rotas:

[POST] /vowel_count -- conta vogais em palavras

Requisição: {"words": ["batman", "robin", "coringa"]}Resposta: {"batman": 2, "robin": 2, "coringa": 3}

[POST] /sort -- ordena palavras em um array, aceitando ordenação reversaRequisição: {"words": ["batman", "robin", "coringa"], "order": "asc"}Resposta: ["batman", "coringa", "robin"]

Requisição: {"words": ["batman", "robin", "coringa"], "order": "desc"}Resposta: ["robin", "coringa", "batman"]


## Tecnologias usadas
  * python3
  * Flask
  * coverage
  * docker
  * docker-compose
  * open api

Requisitos
============
  * [docker](https://www.docker.com/)
  * [docker-compose](https://docs.docker.com/compose/)

Como executar a aplicação localmente
============
### Execute os containers
```bash
$ make build up
```

Testes
=====

```bash
$ make test coverage
```

Cobertura de testes
=====
![image](https://github.com/Lucas-loliveira/python-challenge/assets/22778168/ce9e9a1c-bba6-45d8-982d-85aca6dd8426)



Documentação (OpenAPI)
=====
https://soupilar-python-challenge-3c29300bb2ba.herokuapp.com/api/docs


CI/CD
=====

  * CI: O CI nesse projeto foi feito utilizando o github actions, a pipeline é executada ao abrir um pull request e são executados os testes e flake8.
  * CD: O CD é feito diretamento no heroku, A plataforma observa todas as alteracões feitas na branch main e realiza o deploy automaticamente.


Futuras melhorias
=====
  * .env
