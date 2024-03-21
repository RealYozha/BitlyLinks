# Bit.ly link shortener
English: lines 6-36,
Русский: строки 39-69.


# English

## How to install
You should already have Python 3 and `pip` installed in order for the program to work.
Then use `pip` (or `pip3`, if there's a conflict with Python 2) to install dependencies:
```
pip install -r requirements.txt
```
We recommend using [virtualenv/venv](https://docs.python.org/3/library/venv.html) for the project to be isolated.
## Getting started
### Getting a token
To use the program, you must have a Bitly API token. You can get one [here](https://app.bitly.com/settings/api). Go to the link, click "Generate token" and copy the access token.
Then, in the folder with the program, find a file called `.env.copy` and rename it to `.env`. Open the file with a notepad and after "BITLY_TOKEN=" write your access token. Save the file.
### Usage
To start the program, use `python` (or `python3`, if there's a conflict with Python 2):
```
python master.py --link (bitly shortened link or any other url) --language english
```
Or use the short parameters:
```
python master.py -url (bitly shortened link or any other url) -lang en
```
When a `bitly` link is inserted, it returns the all-time clicks. When a normal link is inserted, it returns a shortened link by `bitly`.
## Library usage & thanks
### Used libraries
```
os, argparse, urllib, requests, dotenv
```
## License
This project was made for education purposes and not for commerical usage.
The `Hedgehog License 2.0 Private` license is used.


# Русский

### Как установить
Python 3 и `pip` уже должны быть установлены.
Затем используйте `pip` (или `pip3`, если есть конфликт с Python 2), чтобы установить зависимости:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.
## С чего начать
### Получение токена
Чтобы использовать программу, вам нужен токен API Bitly. Вы можете получить его [здесь](https://app.bitly.com/settings/api). Перейдите по ссылке, нажмите "Generate token" ("Создать токен") и скопируйте access token (токен доступа).
Далее, в папке с программой, найдите файл `.env.copy` и переименуйте его в `.env`. Откройте этот файл с помощью блокнота и после "BITLY_TOKEN=" напишите ранее полученный токен. Сохраните файл.
### Использование
Чтобы начать, используйте `python` (или `python3`, если есть конфликт с Python 2):
```
python master.py --link (сокращённая ссылка bitly или любая другая ссылка) --language russian
```
Или используйте более короткий вариант:
```
python master.py -url (сокращённая ссылка bitly или любая другая ссылка) -lang ru
```
Когда используется сокращённая ссылка `bitly`, программа выводит количество переходов за всё время. Когда обычная ссылка вставлена, программа выводит сокращённую ссылку `bitly`.
## Используемые библииотеки и "спасибо"
### Используемые библииотеки
```
os, argparse, urllib, requests, dotenv
```
## Лицензия
Этот проект был сделан в целях образования.
Используется лицензия `Hedgehog License 2.0 Private`.