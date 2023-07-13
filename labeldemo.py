from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
    def _init_(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Hello World!", row = 0, column = 0)

def main():
        LabelDemo().mainloop()
        
if __name__ == "__main__":
        main()
