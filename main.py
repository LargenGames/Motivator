import kivymd
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
import random


praise = ['Ты молодец', "У тебя всё получится", "Я в тебя верю", "Никогда не сдавайся",
          "Не бойся ошибиться", "Ты сможешь", "Ты сильнее, чем думаешь", "Ты умнее, чем думаешь",
          "Ты можешь всё", "Ты важен", "Ты неповторим", "Верь в себя", "Попробуй что давно мечатешь"]


class MotivatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return (
            MDScreen(
                MDRaisedButton(
                    text=str(random.choice(praise)),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    on_release=self.update_button_text)
                )
            )

    def update_button_text(self, instance):
        instance.text = str(random.choice(praise))


MotivatorApp().run()