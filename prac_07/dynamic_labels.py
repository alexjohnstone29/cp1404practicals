from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabels(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_label(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            temp_label.bind(on_release=self.press_entry)
            self.root.ids.entries_box.test(temp_label)

    def press_entry(self):
        self.status_text = "what {}".format(self.names)







DynamicLabels().run()
