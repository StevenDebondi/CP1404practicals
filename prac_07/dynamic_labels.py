from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob", "Sally", "Harry"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Button(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
