import sys
import yadisk
import os
import pyAesCrypt
from os import stat, remove
import random


class YandexDiskOperations():
    def __init__(self):
        self.get_auth()
        print('n4')
        self.dict_func = {'copy': self.copy, 'download': self.download, 'download_public': self.download_public,
                          'mkdir': self.mkdir, 'move': self.move, 'listdir': self.listdir,
                          'is_dir': self.is_dir, 'is_file': self.is_file, 'exists': self.exists, 'get_disk_info': self.get_disk_info,
                          'get_files': self.get_files, 'get_last_uploaded': self.get_last_uploaded, 'get_meta': self.get_meta, 'get_public_meta': self.get_public_meta,'get_public_resourses': self.get_public_resourses,
                          'get_public_type': self.get_public_type}

    def additional_func(self):
        # print(locals())
        print(sys.argv)
        # locals()[sys.argv[1]](sys.argv[2], sys.argv[3])
        self.dict_func[sys.argv[1]](sys.argv[2], sys.argv[3])
              
    def get_auth(self):
        self.y = yadisk.YaDisk("94885fad3a5e407b8cda5af348597aae", "59d96c74713947b9bad0f691dffb5699")
        url = self.y.get_code_url()
        # with open("data.txt", "rb") as token_txt:
        #    code = token_txt
        code = input('Введите код: ')
        try:
            response = self.y.get_token(code)
            print('Connecting')
        except yadisk.exceptions.BadRequestError:
            print('Неверный код либо его срок жизни истек')
            sys.exit(1)
        self.y.token = response.access_token
        print('n3')

        if self.y.check_token():
            print("Токен получен")
        else:
            print("Срок жизни токена истек, либо введён не правильно")
        

    def copy(self, from_path, to_path):
        try:
            operation = self.y.copy(from_path, to_path)
            while True:
                status = self.y.get_operation_status(operation.href)
                if status == "in-progress":
                    time.sleep(5)
                    print("Still waiting...")
                elif status == "success":
                    print("Success")
                    break
                else:
                    print("Не выполнено, ошибка: {0}".format(status))
                    break
        except:
            print('Ошибка в выполнении')
              
    def download(self, from_path, to_path):
        try:
            operation = self.y.download(from_path, to_path)
            while True:
                status = self.y.get_operation_status(operation.href)
                if status == "in-progress":
                    time.sleep(5)
                    print("Still waiting...")
                elif status == "success":
                    print("Success")
                    break
                else:
                    print("Не выполнено, ошибка: {0}".format(status))
                    break
        except:
            print('Ошибка в выполнении')

    def download_public(self, url, to_path):
        try:
            operation = self.y.download_public(url, to_path)
            while True:
                status = self.y.get_operation_status(operation.href)
                if status == "in-progress":
                    time.sleep(5)
                    print("Still waiting...")
                elif status == "success":
                    print("Success")
                    break
                else:
                    print("Не выполнено, ошибка: {0}".format(status))
                    break
        except:
            print('Ошибка в выполнении')

    def mkdir(self, path, **kwargs):
        try:
            operation = self.y.mkdir(path)
            print('Status: success')
        except:
            print('Не выполнено, ошибка')

    def move(self, from_path, to_path):
        try:
            operation = self.y.move(from_path, to_path)
            while True:
                status = self.y.get_operation_status(operation.href)
                if status == "in-progress":
                    time.sleep(5)
                    print("Still waiting...")
                elif status == "success":
                    print("Success")
                    break
                else:
                    print("Не выполнено, ошибка: {0}".format(status))
                    break
        except:
            print('Ошибка в выполнении')


    def listdir(self, path, **kwargs):
        try:
            operation = self.y.listdir(path)
            print(operation)
        except:
            print('Не выполнено, ошибка')

    def is_dir(self, path, **kwargs):
        try:
            operation = self.y.is_dir(path)
            print(operation)
        except:
            print('Не выполнено, ошибка')

    def is_file(self, path, **kwargs):
        try:
            operation = self.y.is_file(path)
            print(operation)
        except:
            print('Не выпонено, ошибка')

    def exists(self, path, *kwargs):
        try:
            operation = self.y.exists(path)
            if operation:
                print('Существует')
            else:
                print('Не существует')
        except:
            print('Ошибка в выполнении')

    def get_disk_info(self, **kwargs):
        print(self.y.get_disk_info())

    def get_files(self, **kwargs):
        print(self.y.get_files())

    def get_last_uploaded(self, **kwargs):
        try:
            operation = self.y.get_last_uploaded()
        except:
            print('Не выполнено, ошибка')

    def get_meta(self, path, **kwargs):
        try:
            operation = self.y.get_meta(path)
            print(operation)
        except:
            print('Не выполнено, ошибка')

    def get_public_meta(self, key, **kwargs):
        try:
            operation = self.y.get_public_meta(key)
            print(operation)
        except:
            print('Не выполнено, ошибка')

    def get_public_resourses(self, **kwargs):
        try:
            operation = self.y.get_public_meta()
            print(operation)
        except:
            print('Не выполнено, ошибка')
            
    def get_public_type(self, key, **kwargs):
        try:
            operation = self.y.get_public_type(key)
            print(operation)
        except:
            print('Не выполнено, ошибка')

    def get_trash_meta(self, path, **kwargs):
        try:
            operation = self.y.get_trash_meta(path)
            print(operation)
        except:
            print('Не выпонено, ошибка')

    def get_trash_type(self, path, **kwargs):
        try:
            operation = self.y.get_trash_type(path)
            print(operation)
        except:
            print('Не выполнено, ошибка')

          
class Encription():
    def __init__(self, from_path, to_path, **kwargs):
        bufferSize = 64 * 1024
        password = random.randint(1385, 9732)

        print('Ваш сгенерированный пароль: ', password)
        print('Запишите его! Иначе не сможете расшифровать файл')
        with open(from_path, "rb") as fIn:
            with open(to_path, "wb") as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)


class Decription():

    def __init__(self, from_path, to_path, password, **kwargs):
        password = password
        encFileSize = stat(from_path).st_size
        # decrypt
        with open("data.txt.aes", "rb") as fIn:
            try:
                with open("dataout.txt", "wb") as fOut:
                    # decrypt file stream
                    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
            except ValueError:
                # remove output file on error
                remove("dataout.txt")



class InputBox():
    def __init__(self):
        self.smth = YandexDiskOperations()

    def another_func(self): 
        self.smth.additional_func()


if __name__ == '__main__':
    print('''
    Это приложение работает через код подтверждения.
    Для начала работы перейдите по ссылке:
    https://oauth.yandex.ru/authorize?response_type=code&client_id=94885fad3a5e407b8cda5af348597aae
    (Неактивно):После - создайте папку token.txt и вствьте его туда(Неактивно)
    (Активно)И введите код сюда(Активно)
    ''')
    # start = YandexDiskOperations()
    location = InputBox()
    location.another_func()



