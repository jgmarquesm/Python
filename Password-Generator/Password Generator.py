from zxcvbn import zxcvbn as se
from datetime import datetime
import PySimpleGUI as sg
import pyperclip
import string
import random
import os

symbols = "!$%&()*+,-./:;<=>?@[\]^_`{|}~"

sg.theme("DarkBlue17")


def password1(size):
    all_char = string.digits
    pw = ""
    for car in range(size):
        rand_char = random.choice(all_char)
        pw += rand_char
    return pw


def password2(size):
    all_char = string.ascii_letters + string.digits + symbols
    pw = ""
    for char in range(size):
        rand_char = random.choice(all_char)
        pw += rand_char
    return pw


def password3(size):
    all_char = string.ascii_letters + string.digits + symbols
    pw = ""
    pw += random.choice(string.ascii_uppercase)
    pw += random.choice(string.ascii_lowercase)
    pw += random.choice(string.digits)
    pw += random.choice(symbols)
    for char in range(size - 4):
        rand_char = random.choice(all_char)
        pw += rand_char
    return pw


def strengthVerification(pw):
    strength_estimator = se(pw)
    score = strength_estimator["score"]
    if score == 0:
        return "Score 0: Your password is terrible!"
    elif score == 1:
        return "Score 1: Your password is not good and not safe!"
    elif score == 2:
        return "Score 2: Your password is good, but not safe enough!"
    elif score == 3:
        return "Score 3: Your password is in a good way to stay safe!"
    elif score == 4:
        return "Score 4: Your password is the best forever! And safer too!"


def main():
    global kind, password, passw, window1
    condition = True
    while condition:
        try:
            layout1 = [[sg.Push(), sg.T("Welcome to the Password Generator v.2", font="helvetica 18 bold", text_color="#87CEFA"), sg.Push()],
                       [sg.T("")],
                       [sg.Push(), sg.T("How many characters do you need in this password?", font="arial 11"), sg.Input(key="-PWSIZE-", font="arial 11 bold", size=(10,0)),
                        sg.T("")],
                       [sg.Push()],
                       [sg.Push(), sg.T("Please, choose which one you want", font= "helvetica 12", text_color="#FFD700"), sg.Push()],
                       [sg.B("PW1"), sg.T("- Numeric Password.", font="arial 11"), sg.Push()],
                       [sg.B("PW2"), sg.T("- Alphanumeric Password without requeriments.", font="arial 11"), sg.Push()],
                       [sg.B("PW3"), sg.T("- Alphanumeric Password with requirements (At least 4 characters).", font="arial 11"), sg.Push()],
                       [sg.T(" ")],
                       [sg.Push(), sg.T("Powered by João Gabriel", text_color="#483D8B"), sg.Push()]]

            window1 = sg.Window("Password Generator v.2", layout1)

            event1, values1 = window1.read()

            if event1 == sg.WIN_CLOSED:
                break

            if event1 == "PW1":
                kind = "Numeric"
                pw_size = int(values1["-PWSIZE-"])
                password = password1(pw_size)

            elif event1 == "PW2":
                kind = "Alphanumeric without reqs"
                pw_size = int(values1["-PWSIZE-"])
                password = password2(pw_size)

            elif event1 == "PW3":
                kind = "Alphanumeric with reqs"
                pw_size = int(values1["-PWSIZE-"])
                if pw_size < 4:
                    layoutLT4 = [[sg.T("It must have at least 4 characteres.", font="arial 11")],
                                 [sg.B("OK"), sg.B("Close")]]

                    windowLT4 = sg.Window("Password Generator v.2", layoutLT4, element_justification='c')

                    eventLT4, valuesLT4 = windowLT4.read()

                    if eventLT4 == "OK":
                        window1.close()
                        windowLT4.close()
                        layoutLT4OK = [[sg.Push(), sg.T("How many characters do you need in this password?", font="arial 11"),
                                        sg.In(key="-PWSIZE-", font="arial 11 bold", size=(10,0)), sg.Push()],
                                       [sg.Push(), sg.OK(), sg.Push()]]

                        windowLT4OK = sg.Window("Password Generator v.2", layoutLT4OK)

                        eventLT4OK, valuesLT4OK = windowLT4OK.read()

                        if eventLT4OK == sg.WIN_CLOSED:
                            break

                        else:
                            pw_size = int(valuesLT4OK["-PWSIZE-"])

                        password = password3(pw_size)

                        windowLT4OK.close()
                    elif eventLT4 in (sg.WIN_CLOSED, "Close"):
                        break

                    windowLT4.close()
                else:
                    password = password3(pw_size)

            window1.close()

            now = datetime.now()
            date = now.strftime("%d-%m-%Y %H:%M:%S")

            layout2 = [
                [sg.T("Do you want to customize the output file name?", font="arial 11", text_color="#FFD700")],
                [sg.B("Yes"), sg.B("No")]
            ]
            window2 = sg.Window("Password Generator v.2", layout2, element_justification='c')
            event2, values2 = window2.read()

            if event2 == sg.WIN_CLOSED:
                break

            elif event2 == "Yes":
                layout21 = [[sg.T("What is the file name you want?", font="arial 11"), sg.Input(key="passw", font="arial 11 bold", size=(30,0))],
                            [sg.Push(), sg.OK(), sg.Push()]]

                window21 = sg.Window("Password Generator v.2", layout21)

                event21, values21 = window21.read()

                passw = values21["passw"] + ".txt"

                window21.close()
            elif event2 == "No":
                passw = kind + " Password " + date + ".txt"

            try:
                path_ = "/home/notebook/Área de Trabalho/Github/Projetos/Python/Password Generator v.2/output/"
                os.mkdir(path_)
                complete_path_ = os.path.join(path_, passw)
            except:
                path_ = "/home/notebook/Área de Trabalho/Github/Projetos/Python/Password-Generator/output/"
                complete_path_ = os.path.join(path_, passw)

            pw_file = open(complete_path_, "w")
            pw_file.write("Your Password is: {}".format(password))
            pw_file.close()

            strength = strengthVerification(password)

            if event2 in ("Yes", "No"):
                window2.close()
                layout3 = [[sg.Push(), sg.T("Sucessfully saved.", font="helvetica 15", text_color="#ADFF2F"), sg.Push()],
                           [sg.T("")],
                           [sg.T("Your Password is:", font="arial 11"), sg.T(password, font="arial 11", text_color="#FFD700"), sg.Push()],
                           [sg.T(strength, font="arial 11"), sg.Push()],
                           [sg.T("")],
                           [sg.Push(), sg.B("Copy to clipboard"), sg.Push()]]

                window3 = sg.Window("Password Generator v.2", layout3)

                event3, values3 = window3.read()

                if event3 == sg.WIN_CLOSED:
                    break
                elif event3 == "Copy to clipboard":
                    pyperclip.copy(password)

                    layout4 = [[sg.Push(), sg.T("Sucessfully saved.", font="helvetica 15", text_color="#ADFF2F"), sg.Push()],
                               [sg.T("")],
                               [sg.T("Your Password is:", font="arial 11"), sg.T(password, font="arial 11", text_color="#FFD700"), sg.Push()],
                               [sg.T(strength, font="arial 11"), sg.Push()],
                               [sg.T("")],
                               [sg.Push(), sg.T("The password has been copied to the clipboard!", font="arial 11 bold", text_color="#87CEFA"), sg.Push()],
                               [sg.T("")],
                               [sg.Push(), sg.B("OK"), sg.Push()]]

                    window4 = sg.Window("Password Generator v.2", layout4)

                    event4, values4 = window4.read()

                    if event4 in (sg.WIN_CLOSED, "OK"):
                        break

                    window4.close()

                window3.close()

        except:
            layoutexcept = [[sg.Push(), sg.T("Oops! Something went wrong.", font="arial 12 bold", text_color="#FF6347"), sg.Push()],
                            [sg.T("")],
                            [sg.Push(), sg.B("Try again"), sg.B("Close"), sg.Push()]]

            windowexcept = sg.Window("Password Generator v.2 - ERRO", layoutexcept)

            eventexcept, valuesexcept = windowexcept.read()

            if eventexcept == "Try again":
                window1.close()
                condition = True
            elif eventexcept in (sg.WIN_CLOSED, "Close"):
                condition = False

            windowexcept.close()


if __name__ == "__main__":
    main()
