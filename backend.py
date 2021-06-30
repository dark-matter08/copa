import mysql.connector
from kivymd.uix.dialog import MDDialog
import re
from kivymd.uix.button import MDRaisedButton, MDFlatButton

def db_connector():

    try:
        # try connecting to remote db
        print("============== Trying online servers... ===============")
        con = mysql.connector.connect(
        user = "ndelgiyy_copa",
        password = "Nixo2018",
        host = "premium154.web-hosting.com",
        port = 5522,
        database = "ndelgiyy_copa"
        )
        cur = con.cursor()

        print("===================")
        print("Online DB Connected")
        print("===================")

    except Exception as e:
        print("===================")
        print(e)
        print("===================")
        # try connecting to local db
        # ssh key password: ~41Kt5D^XRs@
        print("=============== Trying offline servers... ==============")
        try:
            con = mysql.connector.connect(
            user = "root",
            password = "",
            host = "localhost",
            database = "copa"
            )
            cur = con.cursor()
            print("====================")
            print("Offline DB Connected")
            print("====================")
        except Exception as e:
            print("===================")
            print(e)
            print("===================")
            show_alert_dialog("No connection!")
            cur = ""
            con = ""
            print("===================")
            print("====== Error ======")
            print("===================")


    return cur, con

def show_alert_dialog( message):
    global dialog
    dialog = MDDialog(
        title = "Connecting...",
        text = message,
        pos_hint = {"center_x": .5, "center_y": .5},
        size_hint_x = .8,
        size_hint_y = .1,
        buttons=[
            MDRaisedButton(
                text="OK"
            ),
        ],
    )

    # dialog.buttons = (button)
    dialog.open()


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# for validating an Email
def check(email):

    if(re.search(regex,email)):
        pass

    else:
        return "Invalid email, check the format and try again"


def create_user_account(full_name, username, email, password, c_pass, cur, con):
    try:
        cur.execute("SELECT * FROM user WHERE username =%s",(username,))
        rows = cur.fetchall()
        if rows:
            return "User with this username already exists"
            print ("User with this username already exists")
        else:
            if (c_pass != password):
                return "your username and password do not match"
                print ("your username and password do not match")

            else:

                if check(email):
                    return check(email)
                else:
                    cur.execute("SELECT * FROM user WHERE email =%s",(email,))
                    rows = cur.fetchall()
                    if rows:
                        return "User with this email already exists"
                        print ("User with this email already exists")
                    else:
                        cur.execute("INSERT INTO user(full_name, username, email, password, active) VALUES (%s, %s, %s, %s, %s)",(full_name, username, email, password, 0))
                        con.commit()

                        print("worked!!!")
                        return "True"
    except Exception as e:
        return "No connection, Try again later"
        # show_alert_dialog(f"{e}\nCheck your Connection to the server and try again later")

def user_login( username, password, cur, con):
    try:
        cur.execute("SELECT * FROM user WHERE username=%s AND password=%s",(username, password))
        rows = cur.fetchall()

        if rows:
            return "True"
        else:
            print ("These login details are invalid, Please try again")
            return "These login details are invalid, Please try again"

    except Exception as e:
        return "No connection, Try again later"
        # show_alert_dialog(f"Check your Connection to the server and try again later")

def start_covid_checker():
    pass
    # try:
    #     now = dt.now()
    #     date = now.date()
    #     time = now.time()
    # except Exception as e:
    #     raise

def cancel_covid_checker():
    pass

def country_covid_checker(country):
    pass

def location_covid_checker(location):
    pass

def identity_covid_checker(identity):
    pass

# db_connector()
