# API GetUserSteam

Um backend API REST escrito em python, utilizando Flask

## Etiquetas

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Steamfront](https://img.shields.io/badge/steamfront-%200.1.0-green)](https://pypi.org/project/steamfront/)
[![Python](https://img.shields.io/badge/Python-%203.10.5-green)](https://www.python.org/downloads/release/python-3105/)
[![Flask](https://img.shields.io/badge/Flask-2.2.2-green)](https://flask.palletsprojects.com/en/2.2.x/)
[![Flask-cors](https://img.shields.io/badge/Flask--Cors-3.0.10-green)](https://pypi.org/project/Flask-Cors/)

## GitHub

https://github.com/jvictor-br/apiGetUserSteam

## Stack utilizada

**Front-end:** HTML, CSS

**Back-end:** Python, Flask

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`API_KEY` = Chave API fornecida pela Steam em https://steamcommunity.com/dev/apikey

Documentação da API da Steam Utilizada: https://steamcommunity.com/dev

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/jvictor-br/apiGetUserSteam
```

Entre no diretório do projeto

```bash
  cd my-project
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Inicie o servidor

```bash
  python ./back.py
```

## Uso/Exemplos

### Iniciar:

Dentro do diretório usar comando, `python ./back.py`

### Uso:

Obter usuario: Fazer request GET na rota `0.0.0.0/user`, usando id64 do perfil que deseja buscar

### Exemplo:

GET `0.0.0.0/user`

Headers `id:76561198813506766`

Resposta:

```JSON
{
    "steamid": "76561198813506766",
    "communityvisibilitystate": 3,
    "profilestate": 1,
    "personaname": "Victor_BR",
    "commentpermission": 1,
    "profileurl": "https://steamcommunity.com/id/VictorOficial/",
    "avatar": "https://avatars.akamai.steamstatic.com/d3eb39d70f297a4191bea908797cd7972a77ad86.jpg",
    "avatarmedium": "https://avatars.akamai.steamstatic.com/d3eb39d70f297a4191bea908797cd7972a77ad86_medium.jpg",
    "avatarfull": "https://avatars.akamai.steamstatic.com/d3eb39d70f297a4191bea908797cd7972a77ad86_full.jpg",
    "avatarhash": "d3eb39d70f297a4191bea908797cd7972a77ad86",
    "lastlogoff": 1678678667,
    "personastate": 1,
    "realname": "Victor",
    "primaryclanid": "103582791429523258",
    "timecreated": 1518313257,
    "personastateflags": 0,
    "loccountrycode": "BR",
    "locstatecode": "27",
    "total": 70,
    "games": [
        {
            "appid": 620,
            "playtime_forever": 0,
            "playtime_windows_forever": 0,
            "playtime_mac_forever": 0,
            "playtime_linux_forever": 0,
            "rtime_last_played": 0
        },{"..."}
    ]
}
```

## Screenshots

#### Screenshot do Request acima

![App Screenshot](https://i.imgur.com/cjyfwTU.png)

## Aprendizados

- Utilização de API externa
- Backend em Flask

## Relacionados

Segue alguns projetos relacionados

[SteamMatchWEB](https://github.com/jvictor-br/SteamMatchWEB)
