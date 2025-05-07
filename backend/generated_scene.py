from manim import *

class ThreeSquares(Scene):
    def construct(self):
        # Create three squares
        square1 = Square(side_length=2).shift(LEFT * 2)
        square2 = Square(side_length=2)
        square3 = Square(side_length=2).shift(RIGHT * 2)

        # Create labels for the squares
        label1 = Text("AI").move_to(square1.get_center())
        label2 = Text("AI").move_to(square2.get_center())
        label3 = Text("AI").move_to(square3.get_center())

        # Add squares and labels to the scene
        self.play(Create(square1), Write(label1))
        self.play(Create(square2), Write(label2))
        self.play(Create(square3), Write(label3))

        # Add arrows between the squares
        arrow1 = Arrow(square1.get_right(), square2.get_left(), color=WHITE)
        arrow2 = Arrow(square2.get_right(), square3.get_left(), color=WHITE)

        self.play(Create(arrow1))
        self.play(Create(arrow2))

        # Wait for a moment
        self.wait(2)

        # Clean up
        self.play(FadeOut(square1), FadeOut(label1), FadeOut(arrow1))
        self.play(FadeOut(square2), FadeOut(label2), FadeOut(arrow2))
        self.play(FadeOut(square3), FadeOut(label3))