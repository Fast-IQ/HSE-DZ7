from requests import get

def get_weather(city, api_key):
    query = (f'https://api.openweathermap.org/data/2.5/weather'
             f'?q={city}'
             f'&appid={api_key}'
             f'&units=metric'
            f'&lang=ru')
    
    response = get(query)

    data = response.json()
    
    if data['cod'] != 200:
            print(f"Ошибка: {data['message']}")
            return
        
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    
    print(f'Текущая температура в {city}: {temperature}°C')
    print(f'Описание погоды: {description.capitalize()}')

if __name__ == "__main__":
    api_key = 'fd9df40302629e90212c7b454a7715a3'
    city = input('Введите название города: ')
    get_weather(city, api_key)