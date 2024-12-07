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
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ObjectProperty
KV = '''
# Define the ScreenManager with its screens
MDScreenManager:
    MainScreen:
        name: "main_screen"
    MenuScreen:
        name: "menu_screen"
    EventDetails:
        name: "event_details"
    WaitersPicker:
        name: "waiters_picker"
#primera pantalla
<MainScreen>:
    MDScreen:
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
                source: "../qbar.png"
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
                app.root.current = "menu_screen"

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

#-------------------------------------------------------------------------------
#menu principal
<MenuScreen>:
    MDScreen:
        hero_to: hero_to
        md_bg_color: app.theme_cls.backgroundColor

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
                app.root.current = "main_screen"
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
#-------------------------------------------------------------------------------
<EventDetails>:
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        id: 'event_details'
        MDLabel:
            text: root.selected_date_text
            halign: "center"
            role: "large"
            theme_text_color: "Primary"
            pos_hint: {"center_x": 0.5, "center_y": 0.9}
        MDTextField:
            mode: "outlined"
            size_hint_x: None
            width: "240dp"
            pos_hint: {"center_x": .5, "center_y": .8}

            MDTextFieldHintText:
                text: 'Nombre del cliente'

            MDTextFieldHelperText:
                text: "Seleccione el nombre del evento"
                mode: "persistent"
        MDTextField:
            mode: "outlined"
            size_hint_x: None
            width: "240dp"
            pos_hint: {"center_x": .5, "center_y": .65}



            MDTextFieldHintText:
                text: '#'

            MDTextFieldHelperText:
                text: "Número de meseros"
                mode: "persistent"


        MDTextField:
            mode: "outlined"
            size_hint_x: None
            width: "190dp"
            pos_hint: {"center_x": .43, "center_y": .5}

            MDTextFieldHintText:
                text: 'Ingrese coordenadas'

            MDTextFieldHelperText:
                text: "Ubicación del evento"
                mode: "persistent"

        MDFabButton:
            icon: "map-marker-circle"
            style: "small"
            pos_hint: {"center_x": .775, "center_y": .5}


        MDTextField:
            mode: "outlined"
            size_hint_x: None
            width: "240dp"
            pos_hint: {"center_x": .5, "center_y": .35}



            MDTextFieldHintText:
                text: 'Ingrese la hora del evento'

            MDTextFieldHelperText:
                text: "Hora del evento"
                mode: "persistent"

        MDButton:
            style: "elevated"
            pos_hint: {"center_x": .7, "center_y": .15}
            on_release:
                app.root.current = "waiters_picker"
            MDButtonIcon:
                icon: "check-bold"

            MDButtonText:
                text: "Confirmar"
        MDButton:
            style: "elevated"
            pos_hint: {"center_x": .3, "center_y": .15}
            on_release:
                app.root.current = "menu_screen"
            MDButtonIcon:
                icon: "cancel"

            MDButtonText:
                text: "Cancelar"

#-------------------------------------------------------------------------------
#Waiters selection
<WaitersPicker>:
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        #Botón de regresar
        MDButton:
            style: "filled"
            theme_width: "Custom"
            height: "40dp"
            width: '60dp'
            pos_hint: {"center_x": .15, "top": 0.95}
            on_release:
                app.root.current = "event_details"
            MDButtonIcon:
                icon: "arrow-left"
        MDButton:
            style: "filled"
            pos_hint: {"center_x": 0.5, "top": 0.1}
            on_release:
                app.event_created()
                app.root.current = 'menu_screen'
            MDButtonIcon:
                icon: "content-save"

            MDButtonText:
                text: "Guardar"
'''

# Define the MainScreen
class MainScreen(MDScreen):
    pass

# Define the MenuScreen
class MenuScreen(MDScreen):
    pass

# Define the EventDetails screen
class EventDetails(MDScreen):
    selected_date_text = StringProperty('Error al cargar fecha')

class WaitersPicker(MDScreen):
    pass

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
            self.today_date=instance_date_picker.set_text_full_date()
            print(self.today_date)
            self.root.current = 'event_details'
            instance_date_picker.dismiss()
            return self.today_date
        date_dialog = MDModalInputDatePicker(text_button_ok='Agregar evento',text_button_cancel='Cancelar')
        date_dialog.bind(on_cancel=self.on_cancel)
        date_dialog.bind(on_edit=on_edit)
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.open()

    def on_edit(self, instance_date_picker):
        instance_date_picker.dismiss()
        Clock.schedule_once(self.show_modal_input_date_picker, 0.2)

    def on_ok(self, instance_date_picker):
        self.today_date=instance_date_picker.set_text_full_date()
        print(self.today_date)
        self.events.append(instance_date_picker.set_text_full_date())

        # Switch to the event details screen
        self.root.current = 'event_details'
        screen = self.root.get_screen('event_details')
        # Update the label's text with the chosen date
        screen.selected_date_text = f"Fecha del evento: {self.today_date}"
        instance_date_picker.dismiss()

        return self.today_date



    def show_date_picker(self, *args):
        date_dialog = MDModalDatePicker(text_button_ok='Agregar evento',text_button_cancel='Cerrar')
        date_dialog.open()
        date_dialog.bind(on_cancel=self.on_cancel)
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.bind(on_edit=self.on_edit)
    def event_created(self,*args):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"Se agregó evento para el día {self.today_date}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5,'top':0.95},
            size_hint_x=0.5,
            background_color="olive"
        ).open()


NavigationScreen().run()
print(NavigationScreen().events)
