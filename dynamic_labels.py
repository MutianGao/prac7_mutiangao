from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, *args):
        super().__init__(*args)
        self.name_list = {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_widgets(self):
        self.root.ids.entries_box.add_widget()
        #for name in self.name_list:
            #print(name)





DynamicLabelsApp().run()
