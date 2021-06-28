screen_helper = """
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "center"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "70dp", "70dp"
            source: "logo.png"

    MDLabel:
        text: "Nde Lucien"
        font_style: "Button"
        halign: "center"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "chelucien08@gmail.com"
        font_style: "Caption"
        halign: "center"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list

            ItemDrawer:
                icon : "shield-check-outline"
                text: "Covid Checker"
                text_color: 2/255, 117/255, 216/255, 1
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "main"

            ItemDrawer:
                icon : "map-marker-radius"
                text: "Emmergency Centers"
                text_color: 2/255, 117/255, 216/255, 1
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "emmergency"

            ItemDrawer:
                icon : "clock-start"
                text: "Realtime Covid Data"
                text_color: 2/255, 117/255, 216/255, 1
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "realtime_covid"

<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon

<ListItemWithCheckbox>:

    IconLeftWidget:
        icon: root.icon

    RightCheckbox:

<Check>:
    group: 'age_group'
    size_hint: None, None
    size: dp(48), dp(48)


ScreenManager:
    id: scr_mngr

    home: home
    login: login
    register: register
    main_page: main_page


    MDScreen:
        id: home
        name: 'home'
        on_enter:
            app.anim_home(register_btn)
            app.anim_home(login_btn)

        orientation: 'horizontal'
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.jpg'


        MDRoundFlatButton:
            id: register_btn
            text: 'Create an Account'
            pos_hint :  {"center_x": .5, "center_y": .25}
            font_size: 15
            size_hint_x: .5
            md_bg_color: 1, 1, 1, 1
            line_color: 49/255, 55/255, 253/255, 1
            on_press:
                root.transition.direction = 'left'
                root.current = 'register'

        MDRoundFlatButton:
            id: login_btn
            text: 'Sign In'
            pos_hint :  {"center_x": .5, "center_y": .15}
            font_size: 15
            size_hint_x: .5
            md_bg_color: 1, 1, 1, 1
            line_color: 49/255, 55/255, 253/255, 1
            on_press:
                root.transition.direction = 'left'
                root.current = 'login'


    MDScreen:
        id: login
        name: 'login'
        on_enter:
            app.anim(back_l)
            app.anim1(back1_l)
            app.icons(icon_l)
            app.text(label_l)

        MDFloatLayout:
            id : login_layout
            MDFloatLayout:
                id: back_l
                size_hint_y: .6
                pos_hint: {"center_y": 1.8}
                radius: [0, 0, 0, 40]
                canvas:
                    Color:
                        rgb: (2/255, 117/255, 216/255, 1)
                    Rectangle:
                        size: self.size
                        pos: self.pos

            MDFloatLayout:
                id: back1_l
                size_hint_y: .6
                pos_hint: {"center_y": 1.85}
                radius: [0, 0, 0, 40]
                canvas:
                    Color:
                        rgb: (2/255, 117/255, 216/255, 1)
                    Ellipse:
                        size: self.size
                        pos: self.pos

            MDIconButton:
                id: icon_l
                icon: "account-circle"
                pos_hint :  {"center_x": .5, "center_y": .8}
                user_font_size: "60sp"
                elevation_normal: 12
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                id: label_l
                text: f"[font=Arial]User Login[/font]"
                markup: True
                pos_hint: {"center_y": .75}
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "H5"
                opacity: 0

            MDTextField:
                id: username
                hint_text: "Enter Username"
                size_hint_x: .8
                pos_hint: {"center_x": .5, "center_y": .46}
                current_hint_text_color: 2/255, 117/255, 216/255, 1
                color_mode: "custom"
                line_color_focus: 2/255, 117/255, 216/255, 1
                icon_right: "account"

            MDTextField:
                id: password
                hint_text: "Enter Password"
                size_hint_x: .8
                pos_hint: {"center_x": .5, "center_y": .34}
                current_hint_text_color: 2/255, 117/255, 216/255, 1
                password: True
                color_mode: "custom"
                line_color_focus: 2/255, 117/255, 216/255, 1
                icon_right: "eye-off"

            MDRaisedButton:
                text: "Login"
                pos_hint: {"center_x": .5, "center_y":.2}
                size_hint_x: .5
                md_bg_color: 2/255, 117/255, 216/255, 1
                on_press: app.login_validate()

            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x": .78, "center_y": .1}
                user_font_size: "18sp"
                elevation_normal: 12
                theme_text_color: "Custom"
                text_color: 2/255, 117/255, 216/255, 1
                on_press:
                    root.transition.direction = 'right'
                    root.current = 'home'

            MDTextButton:
                text: "cancel"
                pos_hint: {"center_x": .87, "center_y": .1}
                custom_color: 2/255, 117/255, 216/255, 1
                on_press:
                    root.transition.direction = 'right'
                    root.current = 'home'


    MDScreen:
        id: register
        name: 'register'
        on_enter:
            app.anim(back)
            app.anim1(back1)
            app.icons1(icon)
            app.text(label)

        MDFloatLayout:
            id: register_layout
            MDFloatLayout:
                id: back
                size_hint_y: .6
                pos_hint: {"center_y": 1.8}
                radius: [0, 0, 0, 70]
                canvas:
                    Color:
                        rgb: (2/255, 117/255, 216/255, 1)
                    Rectangle:
                        size: self.size
                        pos: self.pos

            MDFloatLayout:
                id: back1
                size_hint_y: .3
                pos_hint: {"center_y": 1.8}
                radius: [0, 0, 0, 70]
                canvas:
                    Color:
                        rgb: (2/255, 117/255, 216/255, 1)
                    Ellipse:
                        size: self.size
                        pos: self.pos

            MDIconButton:
                id: icon
                icon: "account-circle"
                pos_hint :  {"center_x": .5, "center_y": 1}
                user_font_size: "60sp"
                elevation_normal: 12
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                id: label
                text: f"[font=Arial]User Registration[/font]"
                markup: True
                pos_hint: {"center_y": .80}
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "H5"
                opacity: 0

            MDTextField:
                id: full_name
                hint_text: "Enter Full Names"
                size_hint_x: .8
                pos_hint: {"center_x": .5, "center_y": .63}
                current_hint_text_color: 0, 0, 0, 1
                color_mode: "custom"
                line_color_focus: 2/255, 117/255, 216/255, 1
                icon_right: "account"

            MDTextField:
                id: reg_username
                hint_text: "Enter Username"
                size_hint_x: .8
                pos_hint: {"center_x": .5, "center_y": .53}
                current_hint_text_color: 0, 0, 0, 1
                color_mode: "custom"
                line_color_focus: 2/255, 117/255, 216/255, 1
                icon_right: "account"

            MDTextField:
                id: reg_email
                hint_text: "Enter Email"
                size_hint_x: .8
                pos_hint: {"center_x": .5, "center_y": .43}
                current_hint_text_color: 0, 0, 0, 1
                color_mode: "custom"
                line_color_focus: 2/255, 117/255, 216/255, 1
                icon_right: "email"

            MDTextField:
                id: reg_pass
                hint_text: "Enter Password"
                size_hint_x: .8
                pos_hint: {"center_x": .5, "center_y": .33}
                current_hint_text_color: 0, 0, 0, 1
                password: True
                color_mode: "custom"
                line_color_focus: 2/255, 117/255, 216/255, 1
                icon_right: "eye-off"

            MDTextField:
                id : reg_c_pass
                hint_text: "Confirm Password"
                size_hint_x: .8
                pos_hint: {"center_x": .5, "center_y": .23}
                current_hint_text_color: 0, 0, 0, 1
                password: True
                color_mode: "custom"
                line_color_focus: 2/255, 117/255, 216/255, 1
                icon_right: "eye-off"

            MDRaisedButton:
                text: "Register"
                pos_hint: {"center_x": .5, "center_y":.13}
                size_hint_x: .5
                md_bg_color: 2/255, 117/255, 216/255, 1
                on_press:
                    app.register_validate()


            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x": .78, "center_y": .06}
                user_font_size: "18sp"
                elevation_normal: 12
                theme_text_color: "Custom"
                text_color: 2/255, 117/255, 216/255, 1
                on_press:
                    root.transition.direction = 'right'
                    root.current = 'home'

            MDTextButton:
                text: "cancel"
                pos_hint: {"center_x": .87, "center_y": .06}
                custom_color: 2/255, 117/255, 216/255, 1
                on_press:
                    root.transition.direction = 'right'
                    root.current = 'home'


    MDScreen:
        id: main_page
        name: 'main_page'


        MDBottomAppBar :
            MDToolbar :
                id : toolbar
                title : "COPA"
                left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                right_action_items : [["dots-vertical" , lambda x : print("Vertical dots are pressed")]]
                icon: 'logout'
                text_color: 1, 1, 1, 1
                type : "bottom"
                mode : "end"
                on_action_button :
                    root.transition.direction = 'right'
                    app.logout()

        MDNavigationLayout:
            x: toolbar.height

            ScreenManager:
                id: screen_manager

                Screen:
                    name: "main"

                    MDCard:
                        id : start_card
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "280dp", "220dp"
                        pos_hint: {"center_x": 0.5, "center_y": .53}
                        border_radius: 12
                        radius: [10]


                        MDBoxLayout:
                            size_hint_y: None
                            padding: "8dp"
                            height: self.minimum_height

                            MDLabel:
                                text: "Coronavirus Self-Checker"
                                halign: "center"
                                size_hint_y: None
                                size: self.texture_size
                                theme_text_color: "Primary"

                        MDSeparator:
                            height: "3dp"

                        MDLabel:
                            text: "A tool to help you make decisions on when to seek testing and medical care "
                            halign : "center"

                        MDSeparator:
                            height: "3dp"

                        MDBoxLayout:
                            size_hint_y: None
                            padding: "8dp"
                            height: self.minimum_height
                            anchor_x: "center"
                            canvas:
                                Rectangle:
                                    pos: self.pos
                                    size: self.size
                            AnchorLayout:
                                anchor_x: "center"
                                size_hint_y: None
                                height: "28dp"

                                MDRaisedButton:
                                    text: "Get Started"
                                    halign: 'center'
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    elevation_normal: 12
                                    on_release:
                                        app.covid_checker()
                                        app.slide_out(start_card)
                                        app.slide_in(disclaimer_card)


                    MDCard:
                        id: disclaimer_card
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "280dp", "430dp"
                        pos_hint: {"center_x": 1.6, "center_y": .53}
                        border_radius: 12
                        radius: [10]

                        MDBoxLayout:
                            size_hint_y: None
                            height: self.minimum_height
                            padding: "8dp"

                            MDLabel:
                                text: "Disclaimer"
                                halign: "center"
                                size_hint_y: None
                                font_style: "H5"
                                size: self.texture_size
                                theme_text_color: "Primary"

                        MDSeparator:
                            height: "3dp"

                        MDLabel:
                            text: "The purpose of the Coronavirus Self-Checker is to help you make decisions about seeking appropriate medical care. This system is not intended for the diagnosis or treatment of disease, including COVID-19. This project was made possible through a partnership with the CDC Foundation and is enabled by Microsoft’s Azure platform. CDC’s collaboration with a non-federal organization does not imply an endorsement of any one particular service, product, or enterprise."
                            halign : "center"

                        MDSeparator:
                            height: "3dp"

                        GridLayout:
                            cols: 2
                            size_hint_y: None
                            height: self.minimum_height
                            padding: "28dp", "8dp"

                            MDRaisedButton:
                                text : "I don't agree"
                                pos_hint: {"center_x": 0.2, "center_y": 0.5}
                                font_size: 13
                                size_hint_x: .5
                                on_press:
                                    app.cancel_checker()
                                    app.slide_back_out(disclaimer_card)
                                    app.slide_back_in(start_card)

                            MDRaisedButton:
                                text : "I agree"
                                pos_hint: {"center_x": 0.8, "center_y": 0.5}
                                font_size: 13
                                size_hint_x: .5
                                on_press:
                                    app.cancel_checker()
                                    app.slide_out(disclaimer_card)
                                    app.slide_in(country_1_card)

                    MDCard:
                        id : country_1_card
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "280dp", "200dp"
                        pos_hint: {"center_x": 1.6, "center_y": .53}
                        border_radius: 12
                        radius: [10]

                        MDBoxLayout:
                            size_hint_y: None
                            padding: "8dp"
                            height: self.minimum_height
                            canvas:
                                Rectangle:
                                    pos: self.pos
                                    size: self.size

                            MDLabel:
                                text: "Location"
                                halign: "center"
                                size_hint_y: None
                                size: self.texture_size
                                theme_text_color: "Primary"

                        MDSeparator:
                            height: "3dp"

                        MDLabel:
                            text: "Are you in Cameroon or a Cameroonian territory right now? "
                            halign : "center"

                        MDSeparator:
                            height: "3dp"

                        GridLayout:
                            cols: 2
                            size_hint_y: None
                            height: self.minimum_height
                            padding: "28dp", "8dp"

                            MDRaisedButton:
                                text: "No"
                                elevation_normal: 12
                                size_hint_x: .5
                                on_press:
                                    app.covid_country('Out of Cameroon')
                                    app.slide_out(country_1_card)
                                    app.slide_in(is_you_card)

                            MDRaisedButton:
                                text: "Yes"
                                elevation_normal: 12
                                size_hint_x: .5
                                on_press:
                                    app.covid_country('Cameroon')
                                    app.slide_out(country_1_card)
                                    app.slide_in(country_2_card)

                    MDCard:
                        id : country_2_card
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "280dp", "220dp"
                        pos_hint: {"center_x": 1.6, "center_y": .53}
                        border_radius: 12
                        radius: [10]

                        MDBoxLayout:
                            size_hint_y: None
                            padding: "8dp"
                            height: self.minimum_height

                            MDLabel:
                                text: "Location - Continue"
                                halign: "center"
                                size_hint_y: None
                                size: self.texture_size
                                theme_text_color: "Primary"

                        MDSeparator:
                            height: "3dp"

                        MDLabel:
                            text: " Where in Cameroon or in which Cameroonian territory are you currently located?"
                            halign : "center"

                        MDTextField:
                            id : location_data
                            hint_text: "Enter your location"
                            size_hint_x: .8
                            pos_hint: {"center_x": .5}
                            color_mode: "custom"

                        MDSeparator:
                            height: "3dp"

                        MDBoxLayout:
                            size_hint_y: None
                            padding: "8dp"
                            height: self.minimum_height

                            AnchorLayout:
                                anchor_x: "center"
                                size_hint_y: None
                                height: "28dp"

                                MDRaisedButton:
                                    text: "Submit"
                                    halign: 'center'
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    elevation_normal: 12
                                    on_press:
                                        app.covid_location()
                                        app.slide_out(country_2_card)
                                        app.slide_in(is_you_card)

                    MDCard:
                        id : is_you_card
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "280dp", "200dp"
                        pos_hint: {"center_x": 1.6, "center_y": .53}
                        border_radius: 12
                        radius: [10]

                        MDBoxLayout:
                            size_hint_y: None
                            padding: "8dp"
                            height: self.minimum_height

                            MDLabel:
                                text: "Identity Check"
                                halign: "center"
                                size_hint_y: None
                                size: self.texture_size
                                theme_text_color: "Primary"

                        MDSeparator:
                            height: "3dp"

                        MDLabel:
                            text: "Are you answering for yourself or someone else?"
                            halign : "center"


                        MDSeparator:
                            height: "3dp"

                        GridLayout:
                            cols: 2
                            size_hint_y: None
                            height: self.minimum_height
                            padding: "28dp", "8dp"


                            MDRaisedButton:
                                text: "Yes"
                                halign: 'center'
                                pos_hint: {"center_x": .25, "center_y": .5}
                                elevation_normal: 12
                                size_hint_x: .5
                                on_press:
                                    app.covid_identity("Account Holder")
                                    app.slide_out(is_you_card)
                                    app.slide_in(age_card)

                            MDRaisedButton:
                                text: "No"
                                halign: 'center'
                                pos_hint: {"center_x": .75, "center_y": .5}
                                elevation_normal: 12
                                size_hint_x: .5
                                on_press:
                                    app.covid_identity("Not Account Holder")
                                    app.slide_out(is_you_card)
                                    app.slide_in(age_card)

                    MDCard:
                        id : age_card
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "280dp", "450dp"
                        pos_hint: {"center_x": 1.6, "center_y": .54}
                        border_radius: 12
                        radius: [10]

                        MDBoxLayout:
                            size_hint_y: None
                            padding: "8dp"
                            height: self.minimum_height

                            MDLabel:
                                text: "Age Gate"
                                halign: "center"
                                size_hint_y: None
                                size: self.texture_size
                                theme_text_color: "Primary"

                        MDSeparator:
                            height: "3dp"

                        MDBoxLayout:
                            orientation: "vertical"
                            height: self.minimum_height

                            ScrollView:
                                MDList:
                                    id: scroll_age
                                    MDBoxLayout:
                                        size_hint_y: None
                                        padding: "8dp"
                                        height: self.minimum_height

                                        MDLabel:
                                            text: "What is your age?"
                                            halign: "center"

                        MDSeparator:
                            height: "3dp"

                        MDBoxLayout:
                            size_hint_y: None
                            padding: "8dp"
                            height: self.minimum_height

                            AnchorLayout:
                                anchor_x: "center"
                                size_hint_y: None
                                height: "28dp"

                                MDRaisedButton:
                                    text: "Submit"
                                    halign: 'center'
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    elevation_normal: 12
                                    on_press:
                                        app.slide_out(age_card)
                                        app.slide_in(age_card)

                Screen:
                    name: "emmergency"

                    MDLabel:
                        text: "Emergency Response Locations"
                        halign: "center"

                Screen:
                    name: "realtime_covid"

                    MDLabel:
                        text: "Real Time Covid Data"
                        halign: "center"

            MDNavigationDrawer:
                id: nav_drawer

                ContentNavigationDrawer:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer










"""
