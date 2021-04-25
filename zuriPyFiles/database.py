import csv, os, re
import sys


here = os.path.dirname(os.path.relpath(__file__))
abs_path = os.path.abspath(".")
subdir = "data_record"
dbpath = os.path.join(here, subdir)
created = False
# created =True
def create(account_number, user_details):
    # global created
    filename = str(account_number) + ".csv"
    filepath = os.path.join(dbpath, filename)

    ## the except FileExistsError already checks if account number exists
    if does_email_exist(user_details[3]):
        print("User with this email already exists")
        sys.exit
        # atm.main()
    # if does_account_number_exist(account_number) == True or does_email_exist(account_number) == True:
    #     print("user exists")
    else:
        try:
            db = open(filepath, "x")
            
        except FileExistsError:
            #check if has content
            # delete file
            if has_content(account_number) == False:
                print("Data not properly saved")
                delete(account_number)
            else:
                print("file exists")
        else:
            for i in user_details:
                db.write(str(i)+",")                ##remember to delete if a file exists
            db.close()
            # return True
        
            # print(created)
    # finally:

def delete(account_number):
    filename = str(account_number) + ".csv"
    filepath = os.path.join(dbpath, filename)
    os.remove(filepath)

def has_content(account_number):
    filename = str(account_number) + ".csv"
    filepath = os.path.join(dbpath, filename)
    if os.stat(filepath).st_size == 0:
        return False  # meaning file is empty
    return True
    

def read(account_number):
    filename = str(account_number) + ".csv"
    filepath = os.path.join(dbpath, filename)
    user_file_regex = re.compile(r'(\d{10})(.\w+)')  #regex to check for the type of account number being passed
    mo = user_file_regex.search(str(account_number))

    try:
        if mo == None:
            content = open(filepath, "r")
        else:
            filename = str(account_number)
            filepath = os.path.join(dbpath, filename)
            content = open(filepath, "r")
            
    except FileNotFoundError:
        print("User not found")
    except TypeError:
        print("Invalid account number")
    else:
        return content.readline()
    return False
def does_email_exist(email):
    all_users = os.listdir(dbpath)
    # print(all_users)
    for user in all_users:
        user_list = read(user)
        if str(email) in user_list:
            # print("user exist")
            return True

def does_account_number_exist(account_number):
    all_users = os.listdir(dbpath)
    # print(all_users)
    user_data = str(account_number) + ".csv"
    # print(user_data)
    if user_data in all_users:
        return True
    else:
        return False


def authenticated_user(account_number, password):

    if does_account_number_exist(account_number):

        user = read(account_number).split(",")
        # print(user)
        # print(user[4])
        if str(password) == user[4]:
            return user

    return False

def update(account_number, type, value):
    user = read(account_number).split(",")
    # print(user)
    if type == "deposit" or type == "withdraw":
        user[5] = value
        del user[6:]
    if type == "transfer":
        user[5] = int(user[5]) + value
        del user[6:]
    if type == "firstname":
        user[1] = value
        del user[6:]
    if type == "lastname":
        user[2] = value
        del user[6:]
    if type == "email":
        user[3] = value
        del user[6:]
    if type == "password":
        user[4] = value
        del user[6:]

    update_record(account_number, user)
         

def update_record(account_number, new_user_details):
    filename = str(account_number) + ".csv"
    filepath = os.path.join(dbpath, filename)
    file = open(filepath, "w")
    for i in new_user_details:
        file.write(str(i) + ",")
    file.close



update(9048190772, "lastname", "Oyinade")
# authenticated_user(7694271791, 1111)

# create(1111111221, ["boyy", 4, 9, 6])
# print(has_content(1111111111))
# does_email_exist(4)
# print(does_account_number_exist(1111111111))
# print(read('1111111111.csv'))
