import sys
import yadisk
import os


def main():
    token = input('Введите токен: ')
    realize = check_auth(token)
    if realize:
        operations()
    else:
        print('Токен либо неверный, либо он больше не действителен')
        print('Попробуйте ещё раз')
        print('---------------------------------------------------'
        main()
        

def operations():
    print('''
        Все файлы удаляются/заливаются в созданную программой папку
        В главной директории Яндекс.Диска, которая называется YandexDiskClient
        Команды:
            !upload (путь)
            - загрузить файл с вашего устройва на Яндекс.Диск
            !download (путь на я.д) (путь на устройстве)
            - скачать файл из яндекс диска по указанному пути
        ''')
              
def create_dict_disk():
    try:
        y.mkdir('/YandexDiskClient')
    except:
        if y.exists('/YandexDiskClient'):
            print('Папка найдена')
          
        else:
            print('Папка не обнаружена либо существует')

              



def check_auth(token):
    
    

def load():
    path = input('Введите путь файла в вашей системе: ')
    if os.exists(path):
        print('Выбран файл: ', path.split('/')[-1])
    else:
        print('По вашему пути ничего не было найдено')
        print('Повторите попытку')
        load()
        








    main()

def main():
    YandexDiskOperaget_auth
       
class YandexDiskOperations():
    def __init__(self):
        access = self.get_auth()
        if access:
              
    def get_auth(self):
        self.y = yadisk.YaDisk("94885fad3a5e407b8cda5af348597aae", "59d96c74713947b9bad0f691dffb5699")
        url = y.get_code_url()
        with open("data.txt", "rb") as token_txt:
              token = token_txt
        try:
            response = y.get_token(code)
        except yadisk.exceptions.BadRequestError:
            sys.exit(1)
        y.token = response.access_token

        if self.y.check_token():
            print("Токен получен")
        else:
            print("Срок жизни токена истек, либо введён не правильно")
            break

    def
class Encription():

class Decription():

class InputBox():
    def __init__(self):
        YandexDiskOperations.self.sys_argv[1]

if __name__ == '__main__':
    print('''
    Это приложение работает через код подтверждения.
    Для начала работы перейдите по ссылке:
    https://oauth.yandex.ru/authorize?response_type=code&client_id=94885fad3a5e407b8cda5af348597aae
    После - отправьте сюда свой токен доступа
    ''')
    start = YandexDiskOperations()




