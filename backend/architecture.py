from manim import *

class ShapeScene(Scene):
    def construct(self):
        # Create a square
        square = Square(side_length=2, color=BLUE)
        square.to_edge(UP)

        # Create two triangles
        triangle1 = Polygon(
            ORIGIN,
            2*RIGHT,
            2*UP + 2*LEFT,
            color=GREEN
        )
        triangle2 = Polygon(
            ORIGIN,
            2*LEFT,
            2*UP + 2*RIGHT,
            color=GREEN
        )
        triangle1.next_to(square, DOWN, buff=1)
        triangle2.next_to(triangle1, DOWN, buff=1)

        # Create a box with "redis" written on it
        box = Rectangle(width=4, height=1, color=YELLOW)
        redis_text = Text("redis", font_size=24)
        redis_text.move_to(box.get_center())
        box.put_start_and_end_on(LEFT, RIGHT).shift(DOWN * 2)

        # Add shapes to the scene
        self.play(Create(square))
        self.play(Create(triangle1))
        self.play(Create(triangle2))
        self.play(Create(box), Write(redis_text))

   
        self.wait(2)

