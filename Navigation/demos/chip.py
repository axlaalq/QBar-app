from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.uix.chip import MDChip, MDChipText, MDChipTrailingIcon
from kivymd.uix.list import MDListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
Window.size = (360, 640)
from kivymd.uix.list import MDListItem, MDListItemHeadlineText,MDListItemLeadingIcon,MDListItemSupportingText,MDListItemTertiaryText,MDListItemTrailingCheckbox


import asynckivy

Builder.load_string(
    '''
<CustomOneLineIconListItem>

    MDListItem:

    MDListItemLeadingIcon:
        icon: "account"

    MDListItemHeadlineText:
        text: "Headline"

    MDListItemSupportingText:
        text: "Supporting text"


    MDListItemTrailingCheckbox:


<PreviewIconsScreen>

    MDBoxLayout:
        orientation: "vertical"
        spacing: "14dp"
        padding: "20dp"

        MDTextField:
            id: search_field
            mode: "outlined"
            on_text: root.set_list_md_icons(self.text, True)

            MDTextFieldLeadingIcon:
                icon: "magnify"

            MDTextFieldHintText:
                text: "Search icon"

        MDBoxLayout:
            id: chip_box
            spacing: "12dp"


        RecycleView:
            id: rv
            viewclass: "CustomOneLineIconListItem"
            key_size: "height"

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: "vertical"
    '''
)


class CustomOneLineIconListItem(MDListItem):
    pass


class PreviewIconsScreen(MDScreen):
    filter = ListProperty()  # list of tags for filtering icons

    def set_filter_chips(self):
        '''Asynchronously creates and adds chips to the container.'''

        async def set_filter_chips():
            for tag in [["Tiene carro",'car'],["Cercano al evento",'map-marker-distance'], ["Rango",'seal']]:
                await asynckivy.sleep(0)
                chip = MDChip(
                    MDChipText(text=tag[0]),
                    MDChipTrailingIcon(icon=tag[1]),
                    type="filter",
                    md_bg_color="#303A29",
                )
                chip.bind(active=lambda x, y, z=tag: self.set_filter(y, z))
                self.ids.chip_box.add_widget(chip)
        asynckivy.start(set_filter_chips())

    def set_filter(self, active: bool, tag: str) -> None:
        '''Sets a list of tags for filtering icons.'''

        if active:
            self.filter.append(tag)
        else:
            self.filter.remove(tag)

    def set_list_md_icons(self, text="", search=False) -> None:
        '''Builds a list of icons.'''

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "icon": name_icon,
                    "text": name_icon,
                }
            )

        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            for tag in self.filter:
                if tag.lower() in name_icon:
                    if search:
                        if text in name_icon:
                            add_icon_item(name_icon)
                    else:
                        add_icon_item(name_icon)


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviewIconsScreen()

    def build(self) -> PreviewIconsScreen:
        self.theme_cls.theme_style = "Dark"
        return self.screen

    def on_start(self) -> None:
        self.screen.set_list_md_icons()
        self.screen.set_filter_chips()


Example().run()
