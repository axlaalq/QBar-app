from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.pickers import MDModalDatePicker
from kivymd.uix.snackbar import (
    MDSnackbar, MDSnackbarSupportingText, MDSnackbarText
)
Window.size = (360, 640)
KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
#Botón de regresar
    MDButton:
        style: "elevated"
        theme_width: "Custom"
        height: "40dp"
        width: '100dp'
        pos_hint: {"center_x": .15, "top": 0.95}

        MDButtonIcon:
            icon: "arrow-left"

        MDButtonText:
            text: "Back"
#Botón de calendario
    MDButton:
        style: "elevated"
        on_release: app.show_date_picker()
        pos_hint: {'center_x': 0.5,"top": 0.87}
        theme_width: "Custom"
        height: "56dp"
        size_hint_x: .5
        MDButtonIcon:
            icon: "calendar-blank-outline"

        MDButtonText:
            text: "Calendario"
            pos_hint: {"center_x": .5, "center_y": .5}
#Base de datos
    MDButton:
        style: "elevated"
        pos_hint: {'center_x': 0.5,"top": 0.77}
        theme_width: "Custom"
        height: "56dp"
        size_hint_x: .5
        MDButtonIcon:
            icon: "account"

        MDButtonText:
            text: "Equipo"
            pos_hint: {"center_x": .5, "center_y": .5}
#Lista de eventos
    MDButton:
        style: "elevated"
        pos_hint: {'center_x': 0.5,"top": 0.67}
        theme_width: "Custom"
        height: "56dp"
        size_hint_x: .5
        MDButtonIcon:
            icon: "view-list"
            MDBadge:
                text: "2"

        MDButtonText:
            text: "Eventos"
            pos_hint: {"center_x": .5, "center_y": .5}
'''


class Example(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return Builder.load_string(KV)



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


    def show_date_picker(self, *args):
        date_dialog = MDModalDatePicker()
        date_dialog.open()
        date_dialog.bind(on_cancel=self.on_cancel)
        date_dialog.bind(on_ok=self.on_ok)


Example().run()
