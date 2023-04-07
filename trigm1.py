from manim import *
from math import sin, asin, cos, acos, tan, atan

class InverseTrigs(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-4, 4, PI/2],
            tips=False,
        )

        sin_graph = ax.plot(lambda t: sin(t), x_range=[-2*PI, 2*PI], color=BLUE_C)
        inv_sin = ax.plot(lambda t: sin(t), x_range=[-PI/2, PI/2], color=BLUE_E)
        inv_sin.rotate(PI, axis=UP)
        inv_sin.rotate(PI/2)

        self.play(Write(ax), rate_func=smooth)
        self.play(Create(sin_graph), run_time=4)
        self.play(ReplacementTransform(sin_graph, inv_sin), run_time=4)