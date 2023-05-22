import requests as requests


city="Khimki,RU"
appid="66b2d3910b1e92a1ffda85f651c55313"

res=requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'q':city,'units':'metric','lang':'ru','APPID':appid})

data=res.json()

print("Город",city)
print("Погодные условия",data['weather'][0]['description'])
print("Температура",data['main']['temp'])
print("Минимальная температу",data['main']['temp_min'])
print("Максимальная температура",data['main']['temp_max'])
print("Видимость",data['visibility'])
print("Скорость ветра",data['wind']['speed'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

data = res.json()

print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'],"> \r\nВидимость <", i['visibility'],"> \r\nCкорость ветра <",i['wind']['speed'],">")
    print("____________________________")
