import os
import argparse
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
load_dotenv()


def create_bitlink(token: str, long_url: str):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"long_url": long_url}
    response = requests.post("https://api-ssl.bitly.com/v4/bitlinks",
                             headers=headers,
                             json=data)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(token: str, bitlink: str):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
        headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(token: str, link: str):
    parsed_link = urlparse(link)
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}/{parsed_link.path}",
        headers=headers)
    return response.ok


def main():
    print("Make sure to check the readme! | Обязательно проверьте readme!")
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', '--link', required=True, help='The link you want to use. | Ссылка, которую будете использовать.')
    parser.add_argument('-lang', '--language', help='Language. | Язык.', default='en')
    args = parser.parse_args()
    language = args.language
    bitly_token = os.environ['BITLY_TOKEN']
    if not bitly_token:
        if language == 'en':
            print("ERROR! You entered an incorrect token or you didn't enter the token.")
        elif language == 'ru':
            print("ОШИБКА! Вы ввели недействительный токен или вы не ввели токен.")
    input_url = args.link
    try:
        if is_bitlink(bitly_token, input_url):
            clicks = count_clicks(bitly_token, input_url)
            if language == 'en' or language == 'english':
                print(f"All-time clicks: {clicks}.")
            elif language == 'ru' or language == 'russian':
                print(f"Переходы за всё время: {clicks}.")
        else:
            bitlink = create_bitlink(bitly_token, input_url)
            if language == 'en' or language == 'english':
                print(f"Shortened link: {bitlink}.")
            elif language == 'ru' or language == 'russian':
                print(f"Сокращённая ссылка: {clicks}.")
    except requests.exceptions.HTTPError:
        if language == 'en' or language == 'english':
            print("ERROR! You entered an incorrect link.")
        elif language == 'ru' or language == 'russian':
            print("ОШИБКА! Вы ввели неправильную ссылку.")


if __name__ == '__main__':
    main()
