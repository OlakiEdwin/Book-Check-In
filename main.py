from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
import sqlite3

from kivymd.uix.boxlayout import MDBoxLayout

conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

Window.size = (350, 600)

KV = '''
<ContentNavigationDrawer>:
    screen_manager: screen_manager
    nav_drawer: nav_drawer

    BoxLayout:
        orientation: 'vertical'
        Image:
            source: 'bg.jpg'
        MDList:
            OneLineListItem:
                text: "Register"
                icon: 'home-account'
                on_press:
                    root.toggle_drawer()
                    root.screen_manager.current = "screen2"

            OneLineListItem:
                text: "Check In"
                on_press:
                    root.toggle_drawer()
                    root.screen_manager.current = "screen3"

            OneLineListItem:
                text: "Notes"
                on_press:
                    root.toggle_drawer()
                    root.screen_manager.current = "screen4"

            OneLineListItem:
                text: "Bookshelf"
                on_press:
                    root.toggle_drawer()
                    root.screen_manager.current = "screen5"

            OneLineListItem:
                text: "Community and Recommendations"
                on_press:
                    root.toggle_drawer()
                    root.screen_manager.current = "screen6"
        Widget:

Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: toolbar
            md_bg_color: (245 / 255, 245 / 255, 220 / 255, 1)
            title: "Check In"
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            right_action_items: [['magnify', lambda x: None], ['dots-vertical', lambda x: None]]
        Widget:

        MDBottomAppBar:
            md_bg_color: (245 / 255, 245 / 255, 220 / 255, 1)
            id: bottombar
            MDTopAppBar:
                icon: 'home'
                type: 'bottom'
                left_action_items: [['share-variant', lambda x: root.manager.current("screen1")]]
                right_action_items: [['magnify', lambda x: None],['account', lambda x: None]]
                mode: "center"
    MDNavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager
            Screen:
                name: "screen1"
                BoxLayout:
                    padding: 12
                    spacing: 12
                    orientation: 'vertical'
                    Widget:
                    Image:
                        source: 'bg.jpg'
                        icon_color: 6, 3, 0, 0
                        halign: 'center'
                        font_size: 100
                    MDLabel:
                        id: show
                        text: 'Login here'
                        halign: 'center'
                    MDTextField:
                        hint_text: "Username"
                        mode: "rectangle"
                        id: user
                        icon_left: "account"
                        foreground_color: (0, 1, 0, 1)
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    MDTextField:
                        hint_text: "Password"
                        mode: "rectangle"
                        id: password
                        icon_left: "key-variant"
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20            
                        pos_hint: {"center_x": 0.5}
                        password: True
                    MDFillRoundFlatButton:
                        text: "LOG IN"
                        font_size: 15
                        width: 500
                        pos_hint: {"center_x": 0.5}
                        on_press:
                            app.submit()
                    Widget
            Screen:
                name: "screen2"
                BoxLayout:
                    padding: 12
                    spacing: 12
                    orientation: 'vertical'
                    Widget:    
                    Image:
                        source: 'bg.jpg'
                        icon_color: 6, 3, 0, 0
                        halign: 'center'
                        font_size: 100
                    MDTextField:
                        hint_text: "Name"
                        mode: "rectangle"
                        id: register_name_input
                        icon_left: "account"
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    MDTextField:
                        hint_text: "Email"
                        mode: "rectangle"
                        id: register_email_input
                        icon_left: "account"
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    MDTextField:
                        hint_text: "Phone"
                        mode: "rectangle"
                        id: register_phone_input
                        icon_left: "account"
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    MDTextField:
                        hint_text: "Password"
                        mode: "rectangle"
                        id: register_password_input
                        icon_left: "key-variant"
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        height: 20
                        font_size: 20            
                        pos_hint: {"center_x": 0.5}
                        password: True
                    MDFillRoundFlatButton:
                        text: "REGISTER"
                        font_size: 15
                        pos_hint: {"center_x": 0.5}
                        on_press:
                            app.submit_register_info(register_name_input.text, register_email_input.text, register_phone_input.text, register_password_input.text)
                    Widget
            Screen:
                name: "screen3"
                BoxLayout:
                    padding: 12
                    spacing: 12
                    orientation: 'vertical'
                    Widget:    
                    Image:
                        source: 'bg.jpg'
                        icon_color: 6, 3, 0, 0
                        halign: 'center'
                        font_size: 100
                    MDTextField:
                        hint_text: "Book type:"
                        mode: "rectangle"
                        id: book_type_input
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    MDTextField:
                        hint_text: "Book Title:"
                        mode: "rectangle"
                        id: book_title_input
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    GridLayout:
                        rows: 1
                        cols: 2
                        MDFillRoundFlatButton:
                            text: "SUBMIT"
                            font_size: 15
                            pos_hint: {"center_x": 0.5}
                            on_press:
                                app.submit_book_info(book_type_input.text, book_title_input.text)
                        MDFillRoundFlatButton:
                            text: "CANCEL"
                            font_size: 15
                            pos_hint: {"center_x": 0.5}
                            on_press:
                                book_type_input.text = ""
                                book_title_input.text = ""
                    Widget
            Screen:
                name: "screen4"
                BoxLayout:
                    padding: 12
                    spacing: 12
                    orientation: 'vertical'
                    Widget:    
                    Image:
                        source: 'bg.jpg'
                        icon_color: 6, 3, 0, 0
                        halign: 'center'
                        font_size: 100
                    MDTextField:
                        hint_text: "Feedback:"
                        mode: "rectangle"
                        id: feedback_input
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    MDTextField:
                        hint_text: "Book Title:"
                        mode: "rectangle"
                        id: feedback_title_input
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    GridLayout:
                        rows: 1
                        cols: 2
                        MDFillRoundFlatButton:
                            text: "SUBMIT"
                            font_size: 15
                            pos_hint: {"center_x": 0.5}
                            on_press:
                                app.submit_feedback_info(feedback_input.text, feedback_title_input.text)
                        MDFillRoundFlatButton:
                            text: "CANCEL"
                            font_size: 15
                            pos_hint: {"center_x": 0.5}
                            on_press:
                                feedback_input.text = ""
                                feedback_title_input.text = ""
                    Widget
            Screen:
                name: "screen5"
                BoxLayout:
                    padding: 12
                    spacing: 12
                    orientation: 'vertical'
                    Widget:    
                    Image:
                        source: 'bg.jpg'
                        icon_color: 6, 3, 0, 0
                        halign: 'center'
                        font_size: 100
                    MDTextField:
                        hint_text: "Name of Book:"
                        mode: "rectangle"
                        id: book_name_input
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    MDTextField:
                        hint_text: "Category:"
                        mode: "rectangle"
                        id: book_category_input
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    GridLayout:
                        rows: 1
                        cols: 2
                        MDFillRoundFlatButton:
                            text: "SELECT"
                            font_size: 15
                            pos_hint: {"center_x": 0.5}
                            on_press:
                                app.select_book_info(book_name_input.text, book_category_input.text)
                        MDFillRoundFlatButton:
                            text: "CANCEL"
                            font_size: 15
                            pos_hint: {"center_x": 0.5}
                            on_press:
                                book_name_input.text = ""
                                book_category_input.text = ""
                    Widget

            Screen:
                name: "screen6"
                BoxLayout:
                    padding: 12
                    spacing: 12
                    orientation: 'vertical'
                    Widget:    
                    Image:
                        source: 'bg.jpg'
                        icon_color: 6, 3, 0, 0
                        halign: 'center'
                        font_size: 100
                    MDTextField:
                        hint_text: "Community Name:"
                        mode: "rectangle"
                        id: community_name_input
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    MDTextField:
                        hint_text: "Recommendation:"
                        mode: "rectangle"
                        id: recommendation_input
                        foreground_color: 0, 1, 0, 1
                        size_hint_x: None
                        width: 270
                        font_size: 20
                        pos_hint: {"center_x": 0.5}
                    GridLayout:
                        rows: 1
                        cols: 2
                        MDFillRoundFlatButton:
                            text: "SUBMIT"
                            font_size: 15
                            pos_hint: {"center_x": 0.5}
                            on_press:
                                app.submit_community_info(community_name_input.text, recommendation_input.text)
                        MDFillRoundFlatButton:
                            text: "CANCEL"
                            font_size: 15
                            pos_hint: {"center_x": 0.5}
                            on_press:
                                community_name_input.text = ""
                                recommendation_input.text = ""
                    Widget

<ElementCard@MDCard>:
    image: ''
    rate: ''
    price: ""
    orientation: 'vertical'
    size_hint_x: .5
    size_hint_y: None
    height: dp(150)
    padding: dp(15)
    spacing: dp(10)
    radius: [25]
    MDBoxLayout:
        height: dp(70)
        widith: dp(50)
        size_hint_y: None
        Image:
            source: root.image
    MDBoxLayout:
        size_hint_y: None
        height: dp(20)
        MDIcon:
            icon: 'star'
            theme_text_color: 'Custom'
            text_color: 1, 1, 0, 1
            halign: "center"
            size_hint_x: .25
        MDLabel:
            text: root.rate
    MDLabel:
        text: root.price
        font_style: 'H5'
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = None
    nav_drawer = None

    def toggle_drawer(self):
        self.nav_drawer.toggle()


class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def submit(self):
        username = self.root.ids.user.text
        password = self.root.ids.password.text

        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()

        self.root.ids.show.text = f'{username} has been registered'
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    def submit_register_info(self, name, email, phone, password):
        # logic for handling registration information here
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Password: {password}")

    def submit_book_info(self, book_type, book_title):
        # logic for handling book information here
        print(f"Book Type: {book_type}, Book Title: {book_title}")

    def submit_feedback_info(self, feedback, book_title):
        # for handling feedback information here
        print(f"Feedback: {feedback}, Book Title: {book_title}")

    def select_book_info(self, book_name, book_category):
        # logic for handling book selection information here
        print(f"Book Name: {book_name}, Category: {book_category}")

    def submit_community_info(self, community_name, recommendation):
        # logic for handling community and recommendation information here
        print(f"Community Name: {community_name}, Recommendation: {recommendation}")


MainApp().run()
