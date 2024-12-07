from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (360, 640)
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.pickers import MDModalDatePicker, MDModalInputDatePicker
from kivymd.uix.snackbar import (
    MDSnackbar, MDSnackbarSupportingText, MDSnackbarText
)

KV = '''
#primera pantalla
MDScreenManager:

    MDScreen:
        name: "screen A"
        md_bg_color:[0, 0, 0, 1]
#animacion
        MDHeroFrom:
            id: hero_from
            tag: "hero"
            size_hint: None, None
            size: "260dp", "260dp"
            pos_hint: {"center_x": .5, "top": .85}

#logo
            FitImage:
                source: "qbar.png"
                size_hint: None, None
                size: hero_from.size
#Ir al menu principal
        MDButton:
            pos_hint: {"center_x": .5,'top': 0.35}
            style: "outlined"
            theme_line_color: 'Custom'
            line_color: [0.874, 0.718, 0.369, 1]
            line_width: 3
            theme_bg_color: "Custom"
            md_bg_color: 'black'
            theme_width: "Custom"
            height: "56dp"
            width: '150dp'
            on_release:
                root.current_heroes = ["hero"]
                root.current = "screen B"

            MDButtonText:
                theme_text_color: "Custom"
                text: "Gestión de eventos"
                text_color: [0.874, 0.718, 0.369, 1]
                pos_hint: {"center_x": .5, "center_y": .5}
#Finazas
        MDButton:
            pos_hint: {"center_x": .5,'top': 0.23}
            style: "outlined"
            theme_line_color: 'Custom'
            line_color: [0.874, 0.718, 0.369, 1]
            line_width: 3
            theme_width: "Custom"
            height: "56dp"
            width: '150dp'
            theme_bg_color: "Custom"
            md_bg_color: 'black'
            y: "36dp"


            MDButtonText:
                text: "Finanzas"
                theme_text_color: "Custom"
                text_color: [0.874, 0.718, 0.369, 1]
                pos_hint: {"center_x": .5, "center_y": .5}
#menu principal
    MDScreen:
        name: "screen B"
        hero_to: hero_to

        MDHeroTo:
            id: hero_to
            tag: "hero"
            size_hint: None, None
            size: "80dp", "80dp"
            pos_hint: {"center_x": .85,"top": .98}


#Botón de regresar
        MDButton:
            style: "filled"
            theme_width: "Custom"
            height: "40dp"
            width: '60dp'
            theme_bg_color: "Custom"
            md_bg_color: 'black'
            pos_hint: {"center_x": .15, "top": 0.95}
            on_release:
                root.current_heroes = ["hero"]
                root.current = "screen A"
            MDButtonIcon:
                icon: "arrow-left"
#Botón de calendario
        MDButton:
            style: "elevated"
            on_release: app.show_date_picker()
            pos_hint: {'center_x': 0.5,"top": 0.8}
            theme_width: "Custom"
            height: "56dp"
            size_hint_x: .6
            MDButtonIcon:
                icon: "calendar-plus"

            MDButtonText:
                text: "Calendario"
                pos_hint: {"center_x": .5, "center_y": .5}
#Botón para gestionar eventos
        MDButton:
            style: "elevated"
            pos_hint: {'center_x': 0.5,"top": 0.67}
            theme_width: "Custom"
            height: "56dp"
            size_hint_x: .6
            MDButtonIcon:
                icon: "clipboard-list-outline"

            MDButtonText:
                text: "Gestión de eventos"
                pos_hint: {"center_x": .5, "center_y": .5}

'''


class NavigationScreen(MDApp):
    events=[]
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cornsilk"
        return Builder.load_string(KV)


#instancias del calendario
    def on_cancel(self, instance_date_picker):
        instance_date_picker.dismiss()

    def show_modal_input_date_picker(self, *args):
        def on_edit(*args):
            date_dialog.dismiss()
            Clock.schedule_once(self.show_date_picker, 0.2)
        def on_cancel(self, instance_date_picker):
            instance_date_picker.dismiss()
        def on_ok(self, instance_date_picker):
            today_date=instance_date_picker.set_text_full_date()
            print(today_date)
            MDSnackbar(
                MDSnackbarSupportingText(
                    text=f"Se agregó evento para el día {today_date}",
                ),
                y=dp(24),
                orientation="horizontal",
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
                background_color="olive"
            ).open()
            instance_date_picker.dismiss()
            return today_date
        date_dialog = MDModalInputDatePicker(text_button_ok='Agregar evento',text_button_cancel='Cancelar')
        date_dialog.bind(on_cancel=self.on_cancel)
        date_dialog.bind(on_edit=on_edit)
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.open()

    def on_edit(self, instance_date_picker):
        instance_date_picker.dismiss()
        Clock.schedule_once(self.show_modal_input_date_picker, 0.2)

    def on_ok(self, instance_date_picker):
        today_date=instance_date_picker.set_text_full_date()
        self.events.append(instance_date_picker.set_text_full_date())
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"Se agregó evento para el día {today_date}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5,'top':0.95},
            size_hint_x=0.5,
            background_color="olive"
        ).open()
        return today_date


    def show_date_picker(self, *args):
        date_dialog = MDModalDatePicker(text_button_ok='Agregar evento',text_button_cancel='Cerrar')
        date_dialog.open()
        date_dialog.bind(on_cancel=self.on_cancel)
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.bind(on_edit=self.on_edit)


NavigationScreen().run()
print(NavigationScreen().events)
