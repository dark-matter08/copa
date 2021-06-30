from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
# from main_kv import screen_helper
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem, MDList, IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDLabel
import backend



Window.size = (365, 600)

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")

class Check(MDCheckbox):
    pass

class RightCheckbox(IRightBodyTouch, Check):
    '''Custom right container.'''

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class ScreenLayout(BoxLayout):
    scr_mngr = ObjectProperty()

    def change_screen(self, screen, direction, *args):
        MDApp.get_running_app().root.transition.direction = direction
        MDApp.get_running_app().root.current = screen

class CopaApp(MDApp):

    def build(self):
        # screen = Builder.load_string(screen_helper)
        # return screen
        self.load_kv("main.kv")

    def on_start(self):
        global cur, con
        cur, con = backend.db_connector()
        with open("session.txt", "r+") as file:
            content = file.read()
            if content == "":
                ScreenLayout.change_screen(ScreenLayout, "home", "right")
            else:
                ScreenLayout.change_screen(ScreenLayout, "main_page", "left")


        ages = ["<2", "2-4", "5-9", "10-12", "13-17", "18-29", "30-39", "40-49", "50-59", "60-64", "65-69", "70-79", "80+"]

        for i in ages:
            self.root.ids.scroll_age.add_widget(
                ListItemWithCheckbox(
                    text=f"{i} years old",
                    icon="car-brake-abs",
                    on_active = lambda x: send_age(i)
                    )
            )

    def error_label(self, error_msg, widget, pos_y_1, pos_y_fin):

        error = MDLabel(
            text = error_msg,
            halign = "center",
            theme_text_color = "Custom",
            text_color = (1, 0, 0, 1),
            size_hint_x = .95,
            pos_hint = {"center_x": .5, "center_y": pos_y_1},
            opacity = 0,
            font_size = 17
        )

        # widget.remove_widget(error)
        for child in widget.children:
            # print(child.width)
            if child.width == 346.75:
                widget.remove_widget(child)
        widget.add_widget(error)
        self.error_anim(error, pos_y_fin)

    def login_validate(self):
        with open("session.txt", "w+") as file:
            content = file.read()
            file.write("")

        username = self.root.ids.username.text
        password = self.root.ids.password.text
        login_layout = self.root.ids.login_layout

        print(self.root)

        if username == "" or password == "":
            self.error_label("Please fill in all fields", login_layout, .2, .27)
            return

        print(username, password)
        login = backend.user_login(username, password, cur, con)

        if login == "True":
            print("Logging in")

            with open("session.txt", "w+") as file:
                content = file.read()
                username = username.lower()
                file.write(username)

            ScreenLayout.change_screen(ScreenLayout, "main_page", "left")
        else:
            self.error_label(login, login_layout, .2, .27)

    def logout(self):
        with open("session.txt", "w+") as file:
            content = file.read()
            file.write("")

        ScreenLayout.change_screen(ScreenLayout, "home", "right")

    def register_validate(self):
        full_name = self.root.ids.full_name.text
        reg_username = self.root.ids.reg_username.text
        reg_email = self.root.ids.reg_email.text
        reg_pass = self.root.ids.reg_pass.text
        reg_c_pass = self.root.ids.reg_c_pass.text
        register_layout = self.root.ids.register_layout

        if full_name == "" or reg_username == "" or reg_email == "" or reg_pass == "" or reg_c_pass == "":
            self.error_label("Please fill in all fields", register_layout, .13, .19)
            return

        register = backend.create_user_account(full_name, reg_username, reg_email, reg_pass, reg_c_pass, cur, con)
        print(register)

        if register == "True":
            ScreenLayout.change_screen(ScreenLayout, "login", "left")
        else:
            self.error_label(register, register_layout, .13, .19)

    def covid_checker(self):
        backend.start_covid_checker()

    def cancel_checker(self):
        backend.cancel_covid_checker()

    def covid_country(self, country):
        backend.country_covid_checker(country)

    def covid_location(self):
        location = "Buea"
        backend.location_covid_checker(location)

    def covid_identity(self, identity):
        backend.identity_covid_checker(identity)

    def send_age(self, age_range):
        pass

    # Animations

    def anim(self, widget):
        anim =  Animation(pos_hint={"center_y":1.16})
        anim.start(widget)

    def anim1(self, widget):
        anim =  Animation(pos_hint={"center_y":.85})
        anim.start(widget)

    def anim_home(self, widget):
        anim =  Animation(pos_hint={"center_x":.5})
        anim.start(widget)

    def icons(self, widget):
        anim = Animation(pos_hint={"center_y": .8})
        anim += Animation(pos_hint={"center_y": .85})
        anim.start(widget)

    def icons1(self, widget):
        anim = Animation(pos_hint={"center_y": .95})
        anim += Animation(pos_hint={"center_y": .90})
        anim.start(widget)

    def text(self, widget):
        anim = Animation(opacity=0, duration=2)
        anim += Animation(opacity=1)
        anim.start(widget)

    def error_anim(self, widget, pos):
        anim1 = Animation(pos_hint={"center_y": pos})
        anim = Animation(opacity=0, duration=.5)
        anim += Animation(opacity=1)
        anim.start(widget)
        anim1.start(widget)

# ================================================== Card Slider Animations ===================================================

    def slide_out(self, widget):
        anim =  Animation(pos_hint={"center_y":1.9})
        anim.start(widget)

    def slide_in(self, widget):
        anim =  Animation(pos_hint={"center_x":.5})
        anim.start(widget)

    def slide_back_out(self, widget):
        anim =  Animation(pos_hint={"center_x":1.6})
        anim.start(widget)

    def slide_back_in(self, widget):
        anim =  Animation(pos_hint={"center_y":0.53})
        anim.start(widget)


# ================================================ End of Card Slider Animations ==============================================



CopaApp().run()
