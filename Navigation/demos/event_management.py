import asynckivy
from kivy.core.window import Window
Window.size = (360, 640)
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.pickers import MDModalDatePicker, MDModalInputDatePicker
from kivymd.uix.snackbar import (
    MDSnackbar, MDSnackbarSupportingText, MDSnackbarText
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.list import MDListItemTrailingIcon
from kivymd.uix.button import MDIconButton
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem

class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()





KV = '''
<BaseMDNavigationItem>

    MDNavigationItemIcon:
        icon: root.icon

    MDNavigationItemLabel:
        text: root.text


<BaseScreen>
MDBoxLayout:
    orientation: "vertical"
    md_bg_color: self.theme_cls.backgroundColor

    MDScreenManager:
        id: screen_manager

        MDScreen:
            name: "Próximos"
            ScrollView:
                size_hint_x: .5
        MDScreen:
            name: "Pagos pendientes"

            ScrollView:
                MDBoxLayout:
                    orientation:'vertical'
                    adaptive_height: True
                    MDLabel:
                        adaptive_height: True
                        padding_x: "24dp"
                        padding_y: "11dp"
                        text: "Lista de eventos"
                        theme_font_style: "Custom"
                        pos_hint: {'top':1}
                        font_style: "Display"
                        role: "small"

                    MDList:
                        id: container
                        pos_hint: {"center_x": .5, 'top':0.8}
                    ScrollView:
                        size_hint_x: .5
    MDNavigationBar:
        on_switch_tabs: app.on_switch_tabs(*args)

        BaseMDNavigationItem
            icon: "calendar-edit"
            text: "Próximos"
            active: True

        BaseMDNavigationItem
            icon: "account-cash"
            text: "Pagos pendientes"


<ExpansionPanelItem>
    adaptive_height: True

    MDExpansionPanelHeader:

        MDListItem:
            theme_bg_color: "Custom"
            md_bg_color: self.theme_cls.surfaceContainerLowColor
            ripple_effect: False

            MDListItemHeadlineText:
                text: root.event_name
                pos_hint: {"center_x": .5}

            MDListItemSupportingText:
                id:pay
                text: root.payment
                theme_text_color: "Custom"
                text_color: root.payment_color
                pos_hint:{"center_x": .5}
                icon: 'cash-edit'

            MDListItemTertiaryText:
                text: root.waiters_number
                pos_hint:{"center_x": .5}
            CashButton:
                id:paid
                icon: "cash-edit"
                on_release: app.tap_paid(root,paid)
            TrailingPressedIconButton:
                id: chevron
                icon: "chevron-right"
                on_release: app.tap_expansion_chevron(root, chevron)


    MDExpansionPanelContent:
        orientation: "vertical"
        padding: "12dp", 0, "12dp", "12dp"
        md_bg_color: self.theme_cls.surfaceContainerLowestColor

        MDLabel:
            text: "Meseros"
            adaptive_height: True
            padding_x: "20dp"
            padding_y: "16dp"

        MDListItem:
            theme_bg_color: "Custom"
            md_bg_color: self.theme_cls.surfaceContainerLowestColor

            MDListItemLeadingIcon:
                icon: "account-outline"

            MDListItemHeadlineText:
                text: "Don Memo"

            MDListItemSupportingText:
                text: "9 horas"

        MDListItem:
            theme_bg_color: "Custom"
            md_bg_color: self.theme_cls.surfaceContainerLowestColor

            MDListItemLeadingIcon:
                icon: "account-outline"

            MDListItemHeadlineText:
                text: 'José Juan'

            MDListItemSupportingText:
                text: "7 horas"


'''

class ExpansionPanelItem(MDExpansionPanel):
    event_name=StringProperty()
    payment = StringProperty()
    payment_color=StringProperty()
    waiters_number=StringProperty()


class TrailingPressedIconButton(
    ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
):
    ...
class CashButton(MDIconButton):
    ...



class Example(MDApp):
    def on_start(self):
        async def set_panel_list():
            database=[['Paty 27 de Julio 2024', 'Rayas 12 de Agosto 2024',
            'Lidia 28 de Agosto 2024'],['Pagado',' 200 pendientes','Sin pagar'],
            ['5','3','7']]
            for i in range(3):
                pagado=database[1][i]
                if pagado=='Pagado':
                    c='green'
                elif pagado == 'Sin pagar':
                    c='red'
                else:
                    c='yellow'
                await asynckivy.sleep(0)
                self.root.ids.container.add_widget(ExpansionPanelItem(
                event_name=database[0][i],payment=database[1][i],payment_color=c,
                waiters_number=f'{database[2][i]} Meseros'))

        Clock.schedule_once(lambda x: asynckivy.start(set_panel_list()))

    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        self.root.ids.screen_manager.current = item_text

    def build(self):
        return Builder.load_string(KV)

    def tap_expansion_chevron(
        self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
    ):
        Animation().start(panel)
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(
            chevron
        ) if not panel.is_open else panel.set_chevron_up(chevron)
    def tap_paid(self, panel: MDExpansionPanel,paid:CashButton):
        async def set_payment():
            panel.payment= 'Pagado'
            panel.payment_color='green'

            await asynckivy.sleep(0)
        asynckivy.start(set_payment())


Example().run()
