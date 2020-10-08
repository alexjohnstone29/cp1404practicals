from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesToKm(App):
    def build(self):
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def convert(self):
        value = self.check_miles()
        result = value * MILES_TO_KM
        self.root.ids.output.text = str(result)

    def handle_increment(self, difference):
        value = self.check_miles() + difference
        self.root.ids.miles.text = str(value)
        self.convert()

    def check_miles(self):
        try:
            value = float(self.root.ids.miles.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKm().run()
