from manim import *

class DataFlow(Scene):
    def construct(self):
        backend = Square(color=BLUE, side_length=2)
        frontend = Square(color=GREEN, side_length=2)
        data = Circle(color=RED, radius=1)

        backend.to_edge(LEFT)
        frontend.to_edge(RIGHT)
        data.move_to(ORIGIN)

        self.play(Create(backend), Write(Text("Backend", color=WHITE).move_to(backend.get_center())))
        self.play(Create(frontend), Write(Text("Frontend", color=WHITE).move_to(frontend.get_center())))
        self.play(Create(data), Write(Text("Data", color=WHITE).move_to(data.get_center())))

        self.wait(2)