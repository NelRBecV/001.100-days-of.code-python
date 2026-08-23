from turtle import Turtle


class ScreenText(Turtle):
    def __init__(self, text: str = "", move: bool = False, align: str = "center", font: tuple = ("Courier", 12, "bold")):
        super().__init__()
        self.text = text
        self.align = align
        self.move = move
        self.font = font
        self.goto(0, 0)
        self.penup()
        self.color('white')
        self.hideturtle()

    def set_pos(self, pos: tuple):
        self.goto(pos)

    def set_text(self, content: str):
        self.clear()
        self.write(content, self.move, self.align, self.font)

    def set_font(self, font_type: str,size: int, width: str):
        self.write(self.text, self.move, self.align, (font_type, size, width))
