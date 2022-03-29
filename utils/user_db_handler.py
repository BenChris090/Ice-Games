import json
from datetime import datetime

DB_PATH = "db/users.json"

def read_user(userName:str = None):
    with open(DB_PATH, "r") as file:
        users = json.load(file) #read all content in the data_base.
        if userName is not None:
            user_search = list(filter(lambda user:user["user_name"] == userName, users)) #Search for user
            user = user_search[0] if user_search != [] else {} #verify if user is found
            return user

        return users

def create_user(userName, password):
    users = read_user()
    user = read_user(userName)
    if user == {}:
        user_dict = {
            "user_name":userName,
            "password":password,
            "created at":str(datetime.now())
        }
        users.append(user_dict) #add to dictionary

        with open(DB_PATH, "w") as file:
            json.dump(users, file)
            return True
    return False


def login(userName, password):
    user = read_user(userName)
    if user == {}:
        return False
    else:
        return user["password"] == password