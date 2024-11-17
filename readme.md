# Analizator Wyników - API w Dockerze

## Jak sklonować repozytorium:

Aby sklonować repozytorium, użyj polecenia:
```sh
gh repo clone PJATK-ASI-2024/Lab-4_s24448
cd Lab-4_s24448
```

## Jak uruchomić aplikację lokalnie:

1. Zainstaluj zależności:
```sh
pip install -r requirements.txt
```

2. Uruchom aplikację:
```sh
python flask_api.py
```
   
Aplikacja będzie dostępna pod adresem `http://127.0.0.1:25565`.

## Jak uruchomić aplikację z Dockerem:

1. Zbuduj obraz:
```sh
docker build -t lab4 .
```


2. Uruchom kontener:
```sh
docker run -p 25565:25565 Lab4
```


Aplikacja będzie dostępna pod adresem `http://localhost:25565`.

## Jak pobrać i uruchomić obraz z Docker Hub:

1. Pobierz obraz z Docker Hub:

```sh
docker pull tpawlak0322/lab4:1.0
```

2. Uruchom kontener:
```sh
docker run -p 25565:25565 lab4
```

Aplikacja będzie dostępna pod adresem `http://localhost:25565`.

## Korzystanie z aplikacji

Nalezy wysłać POST request z danymi a w odpowiedzi dostaniemy wynik
```sh
curl -X POST -H "Content-Type: application/json" -d @{nazwa_pliku}.json http://localhost:25565/predict
```

{nazwa_pliku} - nazwa pliku z danymi

np

```json
[
    {   
        "rownames": 0,
        "gender": "male",
        "ethnicity": "other",
        "fcollege": "yes",
        "mcollege": "no",
        "home": "yes",
        "urban": "yes",
        "unemp": 6.2,
        "wage": 8.09,
        "distance": 0.2,
        "tuition": 0.88915,
        "education": 12,
        "income": "high",
        "region": "other"
    }
]
```

Aplikacja zwróci przewidywany wnik score.

np.
{
  "prediction": [
    -0.3989633734711598
  ]
}