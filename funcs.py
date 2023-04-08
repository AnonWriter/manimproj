from manim import *
import math

class Functions(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10, 10, PI/2],
            y_range=[-4, 4],
            x_length=12,
            tips=False,
        )

        ax_labels = NumberLine(
            x_range=[-10, 10, PI/2],
            length=12,
            include_numbers=False
        )

        ax_labels.add_labels({
            -3*PI: Tex("$-3\pi$"),
            -5*PI/2: Tex("$\\frac{-5\pi}{2}$"),
            -2*PI: Tex("$-2\pi$"),
            -3*PI/2: Tex("$-\\frac{3\pi}{2}$"),
            -PI: Tex("$-\pi$"),
            -PI/2: Tex("$-\\frac{\pi}{2}$"),
            PI/2: Tex("$\\frac{\pi}{2}$"),
            PI: Tex("$\pi$"),
            3*PI/2: Tex("$\\frac{3\pi}{2}$"),
            2*PI: Tex("$2\pi$"),
            5*PI/2: Tex("$\\frac{5\pi}{2}$"),
            3*PI: Tex("$3\pi$"),
        })

        graph = ax.plot(
            lambda x : (4 * math.sin(x)) / PI\
                + (4 * math.sin(3 * x)) / (3 * PI)\
                + (4 * math.sin(5 * x)) / (5 * PI)\
                + (4 * math.sin(7 * x)) / (7 * PI)\
                + (4 * math.sin(9 * x)) / (9 * PI)\
                + (4 * math.sin(11 * x)) / (11 * PI)\
                + (4 * math.sin(13 * x)) / (13 * PI)\
                + (4 * math.sin(15 * x)) / (15 * PI)\
                + (4 * math.sin(17 * x)) / (17 * PI)\
                + (4 * math.sin(19 * x)) / (19 * PI)\
                + (4 * math.sin(21 * x)) / (21 * PI)\
                + (4 * math.sin(23 * x)) / (23 * PI)\
                + (4 * math.sin(25 * x)) / (25 * PI)\
                + (4 * math.sin(27 * x)) / (27 * PI),
            x_range=[-10, 10],
            color=YELLOW_B
        )

        sin_graphs = VGroup()
        for n in range(1,27,2):
            n_graph = ax.plot(
                lambda x: (4 * math.sin(n * x)) / (n * PI),
                x_range=[-10, 10],
                color=GREEN_B
            )
            sin_graphs.add(n_graph)

        func_text = MathTex(
                "\phi(x) = \
                \\frac{4 \sin x}{\pi} + \\frac{4 \sin 3x}{3 \pi} + \
                \\frac{4 \sin 5x}{5 \pi} + \\frac{4 \sin 7x}{7 \pi} + \
                \\frac{4 \sin 7x}{7 \pi} + ...",
                color=YELLOW_B
            )
        func_text.to_edge(UL)

        self.play(Write(ax), Write(ax_labels))
        self.wait()
        self.play(FadeOut(ax_labels))
        self.play(Write(func_text))
        self.play(Create(graph), run_time=4, rate_func=smooth)
        self.wait(2)
        self.play(Transform(graph, sin_graphs), run_time=2)
        self.wait(2)