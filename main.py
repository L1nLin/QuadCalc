import math
import time

a_str = ""
b_str = ""
c_str = ""


def endprompt():
    print("", "Operation completed. Please choose one of the following options:", "1: Back to main menu",
          "2: Close application", sep="\n")


# endprompt for "command not recognized."
def endprompt_err():
    print("1: Back to main menu")
    print("2: Close application")


def wrong_comm():
    global stay
    global sel
    while True:
        print("Command not recognized. Please try again.")
        endprompt_err()
        sel = input()
        if sel == "1":
            print("Returning to main menu.")
            time.sleep(2)
            stay = False
            break
        elif sel == "2":
            closeprompt()
            time.sleep(3)
            exit()
        else:
            continue


def closeprompt():
    print("", "Closing application.", sep="\n")

def mainmenu():
    while True:
        print("Please select an option", "1: Calculate axis intersection", "2: Exit", sep="\n")
        sel = input()  # selection variable
        if sel == "2":
            print("Exit application? (Y/N)")
            yn = input()
            if yn == "Y" or yn == "y":
                print("Closing application.")
                time.sleep(2)
                exit()
            elif yn == "N" or yn == "n":
                print("Returning to main menu.")
                time.sleep(2)
                print("")
                continue
            else:
                print("Command not recognized. Returning to main menu.")
                time.sleep(3)
                print("")
                continue
        elif sel == "1":
            break
        else:
            print("Command not recognized.")
            time.sleep(1)
            print("")
            continue


def calculator():  # calculator variable input system
    global a_str
    global b_str
    global c_str
    global a
    global b
    global c
    global sel
    global stay
    global goto
    global mode

    goto = False
    stay = True

    while True:
        print("PLease select mode.", "1: Vertex form", "2: Standard form", "3: Cancel", sep="\n")
        mode = input()
        if mode == "1" or mode == "2":
            while True:
                print("Enter value for a. Enter 'c' to cancel.")
                a_str = input()
                try:
                    a_str = float(a_str)
                    break
                except:
                    if a_str == "C" or a_str == "c":
                        print("Operation cancelled. Returning to 'mode' menu.")
                        time.sleep(1)
                        goto = True
                        break
                    else:
                        print("Variable must be a number. Please try again.", "", "", sep="\n")
                        time.sleep(1)
                        continue
            while True:
                if goto == True:
                    break
                else:
                    print("Enter value for b/h. Enter 'c' to cancel.")
                    b_str = input()
                    try:
                        b_str = float(b_str)
                        break
                    except:
                        if b_str == "C" or b_str == "c":
                            print("Operation cancelled. Returning to 'mode' menu.")
                            time.sleep(1)
                            goto = True
                            break
                        else:
                            print("Variable must be a number. Please try again.", "", "", sep="\n")
                            time.sleep(1)
                            continue
            while True:
                if goto == True:
                    break
                else:
                    print("Enter value for c/k. Enter 'c' to cancel.")
                    c_str = input()
                    try:
                        c_str = float(c_str)
                        break
                    except:
                        if c_str == "C" or c_str == "c":
                            print("Operation cancelled. Returning to 'mode' menu.")
                            time.sleep(1)
                            goto = True
                            break
                        else:
                            print("Variable must be a number. Please try again.", "", "", sep="\n")
                            time.sleep(1)
                            continue
        if goto == True:
            continue

        else:
            if mode == "3":
                stay = False
                print("Returning to main menu.")
                time.sleep(2)
                print("")
                break

            elif mode != "1" and mode != "2":
                print("Command not recognized. Please try again.")
                time.sleep(0.5)
                print("")

            else:
                break


def internalcalc():  # result calculation based on user input
    global a_str
    global b_str
    global c_str
    global a
    global b
    global c
    global stay
    global sel
    a = float(a_str)
    b = float(b_str)
    c = float(c_str)
    while stay:
        if mode == "1":
            a_std = a
            b_std = 2 * b * a
            c_std = ((b * b) * a) + c

            a = a_std
            b = b_std
            c = c_std

        try:
            result1 = (-b + math.sqrt((b ** 2.0) - 4.0 * a * c)) / 2.0 * a
            result2 = (-b - math.sqrt((b ** 2.0) - 4.0 * a * c)) / 2.0 * a
        except ValueError:
            print("", "The function has no intersections with the x-axis.", sep="\n")
            time.sleep(1.5)
            endprompt()
            sel = input()
            if sel == "1":
                print("Returning to main menu.")
                a = ""
                b = ""
                c = ""
                time.sleep(2)
                stay = False
                continue
            elif sel == "2":
                closeprompt()
                time.sleep(3)
                exit()
            else:
                wrong_comm()
        if result2 == result1:
            print("", "The value for x is " + str(round(result1, 2)) + ". The function has "
                                                                       "a single intersection with the x-axis.", sep="\n")
            time.sleep(1.5)
            endprompt()
            sel = input()
            if sel == "1":
                print("Returning to main menu.")
                time.sleep(2)
                stay = False
                continue
            elif sel == "2":
                closeprompt()
                time.sleep(3)
                exit()
            else:
                wrong_comm()
        else:
            time.sleep(1)
            print("", "The value for x_1 is " + str(round(result1, 2)) + ".",
                  "The value for x_2 is " + str(round(result2, 2)) + ".", sep="\n")
            time.sleep(1.5)
            endprompt()
            sel = input()
            if sel == "1":
                print("Returning to main menu.")
                time.sleep(2)
                stay = False
                continue
            elif sel == "2":
                closeprompt()
                time.sleep(3)
                exit()
            else:
                wrong_comm()

while True:
    mainmenu()
    calculator()
    internalcalc()
    
