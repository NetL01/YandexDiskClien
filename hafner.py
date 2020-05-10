import sys
import yadisk
import os

print('''
Это приложение работает через код подтверждения.
Для начала работы перейдите по ссылке:
https://oauth.yandex.ru/authorize?response_type=code&client_id=94885fad3a5e407b8cda5af348597aae
После - отправьте сюда свой токен доступа
''')

def load():
    path = input('Введите путь файла в вашей системе: ')
    if os.exists(path):
        print('Выбран файл: ', path.split('/')[-1])
    else:
        print('По вашему пути ничего не было найдено')
        print('Повторите попытку')
        load()
        

y = yadisk.YaDisk("94885fad3a5e407b8cda5af348597aae", "59d96c74713947b9bad0f691dffb5699")
url = y.get_code_url()
print("Переходим по URL: %s" % url)
code = input("Введите код подтверждения: ")
try:
    response = y.get_token(code)
except yadisk.exceptions.BadRequestError:
    print("Неверный токен")
    sys.exit(1)

y.token = response.access_token

if y.check_token():
    print("Токен получен!")
else:
    print("Упс... Токен куда-то пропал(")    

print('Все основные операции, как и заливка, выполняются на специально отведённое место у вас на диске')
print('На данный момент можно выполнить следующие операции:')
print('Заливка файла на диск(команда !load')

print('Скачивание файла с диска (команда !upload)')

print(y.get_last_uploaded)
        



# print('Files:               ', y.get_files())
# print('Публичные ресурсы:             ', y.get_public_resources())
# print('DiskInfo:            ', y.get_disk_info())
# print('LISTDIR                      ', list(y.listdir('/')))
# print('MKDIR                 ', y.mkdir("/test-dir"))
# print('DiskMeta:            ', y.get_meta('/'))


    
