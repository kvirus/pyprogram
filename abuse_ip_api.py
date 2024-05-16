import requests

def check_domain(domain, api_key):
    url = f'https://api.abuseipdb.com/api/v2/check-domain'
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }
    params = {
        'domainName': domain
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return None

def main():
    # Введите свой API-ключ здесь
    api_key = 'ca19d6481ca9256b95a11b2de54d1edd2898f4cfd22c5c52dcf51348dde0a8e7d7dedf88c9c3a6d8'
    domain = '77.106.122.140'

    result = check_domain(domain, api_key)
    if result:
        print("Результат проверки:")
        print(result)

if __name__ == "__main__":
    main()