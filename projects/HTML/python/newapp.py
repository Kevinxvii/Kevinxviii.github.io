from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class NoteTaker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Crea un campo di testo per inserire il titolo dell'appunto
        self.title_input = TextInput(hint_text='Titolo', multiline=False)
        self.add_widget(self.title_input)

        # Crea un campo di testo per inserire il contenuto dell'appunto
        self.content_input = TextInput(hint_text='Contenuto')
        self.add_widget(self.content_input)

        # Crea un pulsante per salvare l'appunto
        self.save_button = Button(text='Salva')
        self.save_button.bind(on_press=self.save_note)
        self.add_widget(self.save_button)

    def save_note(self, instance):
        title = self.title_input.text
        content = self.content_input.text

        # Salva l'appunto in un file di testo
        with open('notes.txt', 'a') as f:
            f.write(f'{title}\n{content}\n\n')

        # Pulisce i campi di input
        self.title_input.text = ''
        self.content_input.text = ''

class NoteTakerApp(App):
    def build(self):
        return NoteTaker()

if __name__ == '__main__':
    NoteTakerApp().run()
