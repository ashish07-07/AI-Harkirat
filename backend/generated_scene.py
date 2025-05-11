from manim import *

class DataFlow(Scene):
    def construct(self):
        # Create the squares
        frontend = Square(color=BLUE, side_length=2)
        backend = Square(color=GREEN, side_length=2)

        # Create the circle
        data = Circle(color=RED, radius=1)

        # Position the squares and circle
        frontend.to_edge(LEFT)
        backend.to_edge(RIGHT)
        data.move_to(ORIGIN)

        # Add labels to the squares and circle
        frontend_label = Text("Frontend").next_to(frontend, UP)
        backend_label = Text("Backend").next_to(backend, UP)
        data_label = Text("Data").next_to(data, UP)

        # Add all objects to the scene
        self.play(Create(frontend), Write(frontend_label))
        self.play(Create(backend), Write(backend_label))
        self.play(Create(data), Write(data_label))

        # Animate the data moving from frontend to backend
        self.play(data.animate.move_to(frontend.get_center()), run_time=2)
        self.play(data.animate.move_to(backend.get_center()), run_time=2)