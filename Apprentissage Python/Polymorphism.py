from abc import ABC, abstractmethod


class UIControl(ABC):
    # Abstract class
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    # Using UIControl interface
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    # Using UIControl interface
    def draw(self):
        print("DropDownList")


def draw(controls):  # can pass any UIControl Instance
    for control in controls:
        control.draw()


ddl = DropDownList()
print(isinstance(ddl, UIControl))  # Instance of

textBox = TextBox()

draw([ddl, textBox])
