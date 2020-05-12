import sys
import yadisk
import os
import pyAesCrypt
from os import stat, remove
import random


class YandexDiskOperations():
    def __init__(self):
        self.get_auth()
        self.dict_func = {'copy': self.copy, 'download': self.download, 'download_public': self.download_public,
                          'mkdir': self.mkdir, 'move': self.move, 'listdir': self.listdir,
                          'is_dir': self.is_dir, 'is_file': self.is_file, 'exists': self.exists, 'get_disk_info': self.get_disk_info,
                          'get_files': self.get_files, 'get_last_uploaded': self.get_last_uploaded, 'get_meta': self.get_meta,'get_public_resourses': self.get_public_resourses,
                          'upload': self.upload,
                          'encripto': self.encripto, 'decripto': self.decripto,
                          'get_trash_meta': self.get_trash_meta, 'get_trash_type': self.get_trash_type, 'remove_trash': self.remove_trash}

    def additional_func(self):
        # print(locals())
        # print(sys.argv)
        # locals()[sys.argv[1]](sys.argv[2], sys.argv[3])
        # self.dict_func[sys.argv[1]](sys.argv[2], sys.argv[3])
        try:
            res = sys.argv[3]
            self.dict_func[sys.argv[1]](sys.argv[2], sys.argv[3])
        except IndexError:
            self.dict_func[sys.argv[1]](sys.argv[2])
            
              
    def get_auth(self):
        self.y = yadisk.YaDisk("94885fad3a5e407b8cda5af348597aae", "59d96c74713947b9bad0f691dffb5699")
        url = self.y.get_code_url()
        # with open("data.txt", "rb") as token_txt:
        #    code = token_txt
        code = input('Enter a code: ')
        try:
            response = self.y.get_token(code)
            print('Connecting')
        except yadisk.exceptions.BadRequestError:
            print('Неверный код либо его срок жизни истек')
            sys.exit(1)
        self.y.token = response.access_token
        # print('n3')

        if self.y.check_token():
            print("Токен получен")
        else:
            print("Срок жизни токена истек, либо введён не правильно")
        

    def copy(self, from_path, to_path, *kwargs):
        try:
            operation = self.y.copy(from_path, to_path)
            print('Success')
        except:
            print('execution error')

    # def copy(self, from_, to_, *kwargs):
    #    operation = self.y.copy(from_, to_)
    #    status = self.y.get_operaton_status(operation.href)

    def upload(self, from_, to_, *kwargs):
        try:
            with open(from_, "rb") as f:
                self.y.upload(f, to_)
        except:
            print('execution error')
            
    def download(self, from_path, to_path, *kwargs):
        try:
            operation = self.y.download(from_path, to_path)
        except:
            print('execution error')

    def download_public(self, url, to_path, *kwargs):
        try:
            operation = self.y.download_public(url, to_path)
        except:
            print('execution error')

    def mkdir(self, path, *kwargs):
        try:
            operation = self.y.mkdir(path)
            print('Success')
        except:
            print('execution error')

    def move(self, from_path, to_path, *kwargs):
        try:
            operation = self.y.move(from_path, to_path)
        except:
            print('execution error')

    def listdir(self, path, *kwargs):
        try:
            operation = self.y.listdir(path)
        except:
            print('execution error')

    def is_dir(self, path, *kwargs):
        try:
            operation = self.y.is_dir(path)
            print(operation)
        except:
            print('execution error')

    def is_file(self, path, *kwargs):
        try:
            operation = self.y.is_file(path)
            print(operation)
        except:
            print('execution error')

    def exists(self, path, *kwargs):
        try:
            operation = self.y.exists(path)
            if operation:
                print('exist')
            else:
                print('not exist')
        except:
            print('execution error')

    def get_disk_info(self, *kwargs):
        print(self.y.get_disk_info())
        print('Success')

    def get_files(self, *kwargs):
        print(self.y.get_files())
        print('Success')

    def get_last_uploaded(self, *kwargs):
        try:
            operation = self.y.get_last_uploaded()
        except:
            print('execution error')

    def get_meta(self, path, *kwargs):
        try:
            operation = self.y.get_meta(path)
            print(operation)
        except:
            print('execution error')

#    def get_public_meta(self, key, **kwargs):
#        try:
#            operation = self.y.get_public_meta(key)
#            print(operation)
#        except:
#            print('execution error')

    def get_public_resourses(self, *kwargs):
        try:
            operation = self.y.get_public_meta()
            print(operation)
        except:
            print('execution error')
            
#    def get_public_type(self, key, **kwargs):
#        try:
#            operation = self.y.get_public_type(key)
#            print(operation)
#        except:
#            print('execution error')

    def get_trash_meta(self, path, *kwargs):
        try:
            operation = self.y.get_trash_meta(path)
            print(operation)
        except:
            print('execution error')

    def get_trash_type(self, path, *kwargs):
        try:
            operation = self.y.get_trash_type(path)
            print(operation)
        except:
            print('execution error')

    def remove_trash(self, path, *kwargs):
        try:
            operation = self.y.remove_trash(path)
        except:
            print('execution error')

    def encripto(self, from_, to_):
        bufferSize = 64 * 1024
        password = input('Введите пароль для генерации ключа шифрования: ')
        if password == '':
            password = random.randint(1385, 9732)
            print('Ваш сгенерированный пароль: ', password)
            print('Запишите его! Иначе не сможете расшифровать файл')
        with open(from_, "rb") as fIn:
            with open(to_, "wb") as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
        print('Success')


    def decripto(self, from_, to_):
        bufferSize = 64 * 1024
        password = input('Введите пароль для дешифрования: ')
        encFileSize = stat(from_).st_size
        # decrypt
        with open(from_, "rb") as fIn:
            try:
                with open(to_, "wb") as fOut:
                    # decrypt file stream
                    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
            except:
                print('execution error')
        print('Success')
    

          
# class Encription():
#    def __init__(self, from_path, to_path):
#        self.from_path = from_path
#        self.to_path = to_path
#
#   def encrypt(self, from_path, to_path):
        


# class Decription():
#    def __init__(self, from_path, to_path, password):
#        self.from_path = from_path
#       self.to_path = to_path
#        self.password = password
#       
#    def decript(self, from_path, to_path, password):
        


class InputBox():
    def __init__(self):
        self.smth = YandexDiskOperations()

    def another_func(self): 
        self.smth.additional_func()


if __name__ == '__main__':
    # start = YandexDiskOperations()
    location = InputBox()
    location.another_func()



