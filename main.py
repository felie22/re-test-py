import sys
import os
import yaml

from service import Service

path = os.path.dirname(__file__) # путь к папке проекта, в данном случае project

config_list = {}
with open(os.path.join(path, "config.yaml"), "r") as f:  #  к проету добавлен файл конфиг. r -чтение. 
    config_list = yaml.load(f, Loader=yaml.FullLoader)

print(config_list)
print(path, __file__, path + "\\\nconfig.yaml")
# sys.exit() - остановка программы, дальше выполняться не будет

service = Service(config_list["baseUrl"])
is_connected = service.connect("auth/token", password = config_list["password"], login = config_list["login"])
if is_connected == False:
    print("Не сегодня")
    sys.exit()

list = [1, 2, 3]
dict = {
    "one":1, 
    "two":2, 
    "three":3
}

print(list[0], dict["one"])