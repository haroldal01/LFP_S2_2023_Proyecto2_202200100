class Printer:
    def __init__(self):
        self.text = ""
    
    def add(self,text):
        self.text += text

    def add_line(self,text):
        self.text += text + "\n"

    def get_text(self):
        return self.text