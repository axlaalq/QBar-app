from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.uix.pickers import MDModalDatePicker
from kivymd.uix.snackbar import (
    MDSnackbar, MDSnackbarSupportingText, MDSnackbarText
)
class calendar201(MDApp):

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
