from manim import *
from manimlib import *
from numpy import sin, arcsin, cos, arccos, arctan
from math import acos, asin

class InvUnitCircle(Scene):
    def construct(self):

        '''
        Muestra del recorrido de la circunferencia como el valor de x
        '''

        # ejes
        unit_axes = Axes(
            x_range = [-2, 2, 1],
            y_range = [-2, 2, 1],
            x_length = 4,
            y_length = 4,
            tips = False,
        )

        graph_axes = Axes(
            x_range = [-2*PI, 2*PI, PI/2],
            y_range = [-PI, PI, 1],
            x_length = 7,
            y_length = 5,
            tips = False
        )

        graph_axes_2 = Axes(
            x_range = [-2*PI, 2*PI, 1],
            y_range = [-PI, PI, PI/2],
            x_length = 7,
            y_length = 5,
            tips = False
        ).shift(RIGHT*3)
        
        # circulo unitario
        unit_circle = Circle(radius=1, color=WHITE)

        self.play(DrawBorderThenFill(unit_axes))
        self.play(DrawBorderThenFill(unit_circle))

        # lineas del triangulo
        theta = ValueTracker(0)

        sin_line = always_redraw( lambda : Line(
            (
            # inicio de la linea
            cos(theta.get_value()),     # x
            sin(theta.get_value()),     # y
            0                           # z
            ),
            (
            # punto final de la linea
            cos(theta.get_value()),     # x
            0,                          # y
            0                           # z
            ),
            #propiedades
            color=BLUE
        ).shift(LEFT*4))

        cos_line = always_redraw( lambda : Line(
            (
            # inicio de la linea
            0,                          # x
            0,                          # y
            0,                          # z
            ),
            (
            # punto final de la linea
            cos(theta.get_value()),     # x
            0,                          # y
            0,                          # z
            ),
            # propiedades
            color=RED
        ).shift(LEFT*4))

        radius = always_redraw( lambda : Line(
            ORIGIN,
            (cos(theta.get_value()), sin(theta.get_value()), 0),
            color = WHITE
        ).shift(LEFT*4))

        # arco para representar x
        circunference = always_redraw( lambda : Arc(
            radius = 1,
            start_angle = 0,
            angle = theta.get_value(),
            color = YELLOW,
            arc_center = ORIGIN
        ).shift(LEFT*4))

        self.play(
            unit_circle.animate.shift(LEFT*4),
            unit_axes.animate.shift(LEFT*4)
        )

        self.play(
            Create(sin_line),
            Create(cos_line),
            Create(radius),
            Create(circunference)
        )

        self.play(
            Create(graph_axes),
            graph_axes.animate.shift(RIGHT*3)
        )

        # graficas de seno, coseno y recorrido de x
        sin_graph = always_redraw(lambda : graph_axes.plot(lambda x : sin(x), [0, theta.get_value()], color = BLUE))
        cos_graph = always_redraw(lambda : graph_axes.plot(lambda x : sin(x + PI/2), [0, theta.get_value()], color = RED))

        x_val_func = always_redraw(lambda : graph_axes.plot(lambda x : 0, [0, theta.get_value()], color = YELLOW))

        n_sin_graph = always_redraw(lambda : graph_axes.plot(lambda x : sin(x), [theta.get_value(), 0], color = BLUE))
        n_cos_graph = always_redraw(lambda : graph_axes.plot(lambda x : sin(x + PI/2), [theta.get_value(), 0], color = RED))

        n_x_val_func = always_redraw(lambda : graph_axes.plot(lambda x : 0, [theta.get_value(), 0], color = YELLOW))


        self.play(
            theta.animate.increment_value(2*PI),
            Create(sin_graph),
            Create(cos_graph),
            Create(x_val_func),
            run_time = 6
        )
        self.play(
            FadeOut(sin_graph),
            FadeOut(cos_graph),
            FadeOut(x_val_func),
        )

        self.play(theta.animate.set_value(0), run_time = 3)

        self.play(
            theta.animate.increment_value(-2*PI),
            Create(n_sin_graph),
            Create(n_cos_graph),
            Create(n_x_val_func),
            run_time = 6
        )
        self.play(
            FadeOut(n_sin_graph),
            FadeOut(n_cos_graph),
            FadeOut(circunference),
        )

        self.play(
            ReplacementTransform(n_x_val_func, circunference),
        )
        
        self.wait()

        self.play(
            FadeOut(cos_line),
            FadeOut(circunference),
        )

        '''
        Dominio de las funciones inversas y el circulo unitario
        '''
        xvt = ValueTracker(0)

        sin_arc = always_redraw( lambda : Arc(
            radius = 1,
            start_angle = -PI/2,
            angle = xvt.get_value(),
            arc_center = ORIGIN,
            color = ORANGE,
        ).shift(LEFT*4))

        sin_m1_tex = Tex(
            "$f(x) = \sin x$ \
            $\implies f^{-1}(x) = \sin y$",
            font_size = 22
        ).to_edge(UL).shift(RIGHT*0.7)

        sin_m1_domain_tex = MathTex(
            "D_{f^{-1}(x)} = \{ x \in \mathbb{R} \; | -1 \leqslant x \leqslant 1 \}",
            font_size = 22
        ).to_edge(UL).next_to(sin_m1_tex, DOWN)
        sin_m1_idomain_tex = MathTex(
            "I_{f^{-1}(x)} = \{ y \in \mathbb{R} \; | -\\frac{\pi}{2} \leqslant y \leqslant \\frac{\pi}{2} \}",
            font_size = 22,
            color = ORANGE
        ).next_to(sin_m1_domain_tex, DOWN)

        self.play(
            ReplacementTransform(graph_axes, graph_axes_2),
            FadeIn(sin_arc),
            Write(sin_m1_tex),
            Write(sin_m1_domain_tex)
        )

        self.play(theta.animate.increment_value(-PI/2), run_time = 1)
        self.play(
            xvt.animate.increment_value(PI),
            theta.animate.increment_value(PI),
            sin_m1_domain_tex.animate(run_time = 0.3).set_color(BLUE),
            run_time = 3
        )

        y_line = graph_axes_2.plot(
            lambda x : 0,
            [(-PI/2)*1.44, (PI/2)*1.44],
            color = BLUE
        ).rotate(PI/2).set_color(color = [ORANGE, RED_A])
        
        x_line = graph_axes_2.plot(
            lambda x : 0,
            [-1, 1],
            color = BLUE_D
        )

        self.play(
            ReplacementTransform(sin_arc, y_line),
            ReplacementTransform(sin_line, x_line),
            run_time = 2
        )

        self.play(xvt.animate.increment_value(-PI))

        pi_o2 = MathTex("\\frac{\pi}{2}", font_size = 20).next_to(y_line, UL).shift(DOWN*0.5)
        mpi_o2 = MathTex("-\\frac{\pi}{2}", font_size = 20).next_to(y_line, DL).shift(UP*0.5)

        one = MathTex("1", font_size = 20).next_to(x_line, UL).shift(RIGHT*0.3)
        m_one = MathTex("-1", font_size = 20).next_to(x_line, UR).shift(LEFT*0.5)

        self.play(
            Write(pi_o2),
            Write(mpi_o2),
            Write(one),
            Write(m_one),
            Write(sin_m1_idomain_tex)
        )

        self.wait()

        self.play(
            FadeOut(pi_o2),
            FadeOut(mpi_o2),
            FadeOut(one),
            FadeOut(m_one),
            FadeOut(y_line),
            FadeOut(x_line),
            FadeOut(graph_axes_2),
            FadeOut(unit_axes),
            FadeOut(unit_circle),
            FadeOut(radius),
        )
        
        '''
        Funciones trigonometricas inversas
        '''
        # introduccion con el seno

        xvalue = ValueTracker(-1)

        arcsin_value = always_redraw(
            lambda : DecimalNumber(include_sign = True, font_size = 24)
            .set_value(arcsin(xvalue.get_value()))
            .to_edge(UR)
        )
        arcsin_label = MathTex("\\sin^{-1} x = ", font_size = 24).next_to(arcsin_value, LEFT)

        inv_trigs_axes = Axes(
            x_range = [-6, 6, 1],
            x_length = 12,
            y_range = [-PI, PI, PI/2],
            y_length = 6,
            tips = False
        )

        inv_trigs_plane = NumberPlane(
            x_range = [-6, 6, 1],
            x_length = 12,
            y_range = [-PI, PI, PI/2],
            y_length = 6,
            tips = False
        ).set_opacity(0.3)

        inv_trigs_label_x = NumberLine(
            x_range = [-6, 6, 1],
            length = 12,
            include_tip = False,
            include_numbers = True,
            font_size = 18,
            numbers_to_exclude = [0]
        )

        inv_trigs_label_y = NumberLine(
            x_range = [-PI, PI, PI/2],
            length = 6,
            include_tip = False,
            include_numbers = False,
            font_size = 18
        ).set_opacity(0).shift(UP*0.2 + RIGHT*0.3)

        inv_trigs_label_y.rotate(PI/2)

        inv_trigs_label_y.add_labels({
            -PI     : MathTex("-\pi"),
            -PI/2   : MathTex("-\\frac{\pi}{2}"),
             PI/2   : MathTex("\\frac{\pi}{2}"),
             PI     : MathTex("\pi"),
        })

        self.play(
            Create(inv_trigs_axes),
            Create(inv_trigs_plane),
            Write(inv_trigs_label_x),
            Write(inv_trigs_label_y),
            buff = 0.6,
            run_time = 1.5
        )

        sin_graph = inv_trigs_axes.plot(lambda x : sin(x), [-6, 6], color = BLUE)
        
        self.play(Create(sin_graph))

        inv_sin_graph = inv_trigs_axes.plot(
            lambda x : (PI/3) * sin(PI/3 * x),
            [-PI/2 + 0.047, PI/2 - 0.047]
        ).set_color(color = [TEAL_B, GREEN_A])

        inv_sin_graph.rotate(PI, axis = UP)
        inv_sin_graph.rotate(-PI/2)

        identity_func = inv_trigs_axes.plot(
            lambda x : x,
            [-1, 1],
            color = PURPLE_B
        )

        self.play(
            Write(arcsin_value),
            Write(arcsin_label)
        )
        self.play(
            xvalue.animate.increment_value(2),
            Create(inv_sin_graph),
            rate_func = linear,
            run_time = 3
        )

        self.play(
            ReplacementTransform(inv_sin_graph, identity_func),
            ReplacementTransform(sin_graph, identity_func),
            run_time = 3
        )

        identity_func_label = MathTex("f(f^{-1}(x)) = x", font_size = 22).next_to(inv_sin_graph, UR)

        self.play(Write(identity_func_label))

        self.wait()

        self.play(
            FadeOut(identity_func),
            FadeOut(identity_func_label),
            FadeOut(arcsin_value),
            FadeOut(arcsin_label),
            FadeOut(sin_m1_domain_tex),
            FadeOut(sin_m1_idomain_tex),
            FadeOut(sin_m1_tex)
        )

        self.wait()

        # funcion coseno
        xvalue.set_value(-1)

        arccos_value = always_redraw(
            lambda : DecimalNumber(include_sign = True, font_size = 24)
            .set_value(arccos(xvalue.get_value()))
            .to_edge(UR)
        )
        arcsin_label = MathTex("\\cos^{-1} x = ", font_size = 24).next_to(arccos_value, LEFT)

        cos_graph = inv_trigs_axes.plot(
            lambda x : cos(x),
            [-6, 6],
            color = RED
        )

        inv_cos_graph = inv_trigs_axes.plot(
            lambda x : PI/2 + (PI/3) * sin(PI/3 * x),
            [-PI/2 + 0.047, PI/2 - 0.047]
        ).set_color(color = [RED, GOLD_A])
        inv_cos_graph.rotate(-PI/2)

        cos_m1_tex = MathTex(
            "\cos x = \\sin (\\frac{\pi}{2} - x) \implies \
             \cos^{-1} x = \\frac{\pi}{2} - \sin^{-1} x",
             font_size = 22
        ).to_edge(UL).shift(RIGHT*0.7).set_color(color = [RED, GOLD_A])

        cos_m1_domain_tex = MathTex(
            "D_{ \cos^{-1} x } = \{ x \in \mathbb{R} \; | -1 \leqslant x \leqslant 1 \}",
            font_size = 22
        ).to_edge(UL).next_to(cos_m1_tex, DOWN).set_color(color = [RED, GOLD_A])
        cos_m1_idomain_tex = MathTex(
            "I_{ \cos^{-1} x } = \{ y \in \mathbb{R} \; | \; 0 \leqslant y \leqslant \pi \}",
            font_size = 22
        ).next_to(cos_m1_domain_tex, DOWN).set_color(color = [RED, GOLD_A])

        self.play(
            Write(cos_m1_tex),
            Write(cos_m1_domain_tex),
            Write(cos_m1_idomain_tex),
        )

        self.play(Create(cos_graph))
        
        self.play(
            Write(arccos_value),
            Write(arcsin_label)
        )

        self.play(
            xvalue.animate.increment_value(2),
            Create(inv_cos_graph),
            rate_func = linear,
            run_time = 3
        )

        self.wait()

        # tangente y cotangente

        self.play(
            FadeOut(cos_graph),
            FadeOut(inv_cos_graph),
            FadeOut(arccos_value),
            FadeOut(arcsin_label)
        )

        tan_m1_tex = MathTex(
            "\\tan^{-1} = \\tan y",
            font_size = 22
        ).to_edge(UL).shift(RIGHT).set_color(color = [YELLOW_B, PURPLE])

        tan_m1_domain_tex = MathTex(
            "D_{\\tan^{-1} x } = { \mathbb{R} }",
            font_size = 22
        ).next_to(tan_m1_tex, DOWN).set_color(color = [YELLOW_B, PURPLE])
        tan_m1_idomain_tex = MathTex(
            "I_{\\tan^{-1} x} = \{ y \in \mathbb{R} \; | -\\frac{\pi}{2} \leqslant y \leqslant \\frac{\pi}{2} \}",
            font_size = 22
        ).next_to(tan_m1_domain_tex, DOWN).set_color(color = [YELLOW_B, PURPLE])

        inv_tan_graph = inv_trigs_axes.plot(
            lambda x : arctan(x),
            [-6, 6],
        ).set_color(color = [YELLOW_B, PURPLE])

        self.play(
            ReplacementTransform(cos_m1_tex, tan_m1_tex),
            ReplacementTransform(cos_m1_domain_tex, tan_m1_domain_tex),
            ReplacementTransform(cos_m1_idomain_tex, tan_m1_idomain_tex),
        )

        self.play(Create(inv_tan_graph), run_time = 3)

        cot_m1_tex = MathTex(
            "\cot^{-1} x = \\frac{\pi}{2} - \\tan^{-1} x",
            font_size = 22
        ).to_edge(UL).shift(RIGHT + DOWN*1.5).set_color(color = [GREEN, MAROON])

        cot_m1_domain_tex = MathTex(
            "D_{\cot^{-1} x } = \mathbb{R}",
            font_size = 22
        ).next_to(cot_m1_tex, DOWN).set_color(color = [GREEN, MAROON])

        cot_m1_idomain_tex = MathTex(
            "I_{\cot^{-1} x } = \{ y \in \mathbb{R} \; | \; 0 \leqslant y \leqslant \pi \}",
            font_size = 22
        ).next_to(cot_m1_domain_tex, DOWN).set_color(color = [GREEN, MAROON])

        inv_cot_graph = inv_trigs_axes.plot(
            lambda x : PI/2 - arctan(x),
            [-6, 6],
        ).set_color(color = [GREEN, MAROON])

        self.play(
            ReplacementTransform(tan_m1_tex, cot_m1_tex),
            ReplacementTransform(tan_m1_domain_tex, cot_m1_domain_tex),
            ReplacementTransform(tan_m1_idomain_tex, cot_m1_idomain_tex),
        )

        self.play(Create(inv_cot_graph), run_time = 3)

        self.wait()

        # secante y cosecante

        self.play(
            FadeOut(inv_cot_graph),
            FadeOut(inv_tan_graph)
        )

        sec_m1_tex0 = MathTex(
            "\sec^{-1} x  = \sec y \implies \\\\ \
             x = \\frac{1}{\cos y} \implies \\\\ \
             \cos y = \\frac{1}{x} \implies \\\\ \
             y = \cos^{-1}(\\frac{1}{x})",
             font_size = 22
        ).to_edge(UL).shift(RIGHT).set_color(color = [PURPLE_C, TEAL])
        sec_m1_tex1 = MathTex(
            "\sec^{-1} x  = \sec y",
            font_size = 22
        ).to_edge(UL).shift(RIGHT).set_color(color = [PURPLE_C, TEAL])

        sec_m1_domain_tex = MathTex(
            "D_{\sec^{-1} x } = \mathbb{R} \setminus \{ x \in \mathbb{R} \; | -1 \leq x \leq 1 \}",
            font_size = 22
        ).next_to(sec_m1_tex1, DOWN).set_color(color = [PURPLE_C, TEAL])

        sec_m1_idomain_tex = MathTex(
            "I_{\sec^{-1} x } = \{ y \in \mathbb{R} \; | \; 0 \leqslant y \leqslant \pi \}",
            font_size = 22
        ).next_to(sec_m1_domain_tex, DOWN).set_color(color = [PURPLE_C, TEAL])

        inv_sec_graph_left = inv_trigs_axes.plot(
            lambda x : arccos(1/x),
            [-6, -1]
        ).set_color(color = [PURPLE_C, TEAL])
        inv_sec_graph_right = inv_trigs_axes.plot(
            lambda x : acos(1/x),
            [1, 6]
        ).set_color(color = [PURPLE_C, TEAL])

        self.play(
            ReplacementTransform(cot_m1_tex, sec_m1_tex0),
            FadeOut(cot_m1_domain_tex),
            FadeOut(cot_m1_idomain_tex)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sec_m1_tex0, sec_m1_tex1)
        )
        self.play(
            Write(sec_m1_domain_tex),
            Write(sec_m1_idomain_tex)
        )

        self.play(Create(inv_sec_graph_left))
        self.play(Create(inv_sec_graph_right))

        self.wait()
        # self.play(
        #     FadeOut(inv_sec_graph_left),
        #     FadeOut(inv_sec_graph_right)
        # )

        csc_m1_tex = MathTex(
            "\sec^{-1} = \sec y \implies \csc{^1} = \\frac{\pi}{2} - \sec^{1} x",
            font_size = 22
        ).to_edge(UL).shift(RIGHT).set_color(color = [ORANGE, LIGHT_PINK])

        csc_m1_domain_tex = MathTex(
            "D_{\csc^{-1} x } = R \setminus \{ x \in \mathbb{R} \; | -1 \leq x \leq 1 \}",
            font_size = 22
        ).next_to(csc_m1_tex, DOWN).set_color(color = [ORANGE, LIGHT_PINK])

        csc_m1_idomain_tex = MathTex(
            "I_{\csc^{-1} x } = \{ y \in \mathbb{R} \; | -\\frac{\pi}{2} \leqslant y \leqslant \\frac{\pi}{2} \}",
            font_size = 22
        ).next_to(csc_m1_domain_tex, DOWN).set_color(color = [ORANGE, LIGHT_PINK])

        inv_csc_graph_left = inv_trigs_axes.plot(
            lambda x : PI/2 - acos(1/x),
            [-6, -1]
        ).set_color(color = [LIGHT_PINK, ORANGE])
        inv_csc_graph_right = inv_trigs_axes.plot(
            lambda x : PI/2 - acos(1/x),
            [1, 6]
        ).set_color(color = [ORANGE, LIGHT_PINK])

        self.play(
            ReplacementTransform(sec_m1_tex1, csc_m1_tex),
            ReplacementTransform(sec_m1_domain_tex, csc_m1_domain_tex),
            ReplacementTransform(sec_m1_idomain_tex, csc_m1_idomain_tex)
        )

        self.play(Create(inv_csc_graph_left)),
        self.play(Create(inv_csc_graph_right))

        self.wait()

        # todas las inveras juntas

        self.play(
            FadeOut(csc_m1_tex),
            FadeOut(csc_m1_domain_tex),
            FadeOut(csc_m1_idomain_tex),
        )

        inv_sin_graph = inv_trigs_axes.plot(
            lambda x : (PI/3) * sin(PI/3 * x),
            [-PI/2 + 0.047, PI/2 - 0.047]
        ).set_color(color = [TEAL_B, GREEN_A])
        inv_sin_graph.rotate(PI, axis = UP)
        inv_sin_graph.rotate(-PI/2)

        self.play(Create(inv_cot_graph))
        self.play(Create(inv_tan_graph))
        self.play(Create(inv_cos_graph))
        self.play(Create(inv_sin_graph))

        self.wait(4)

        self.play(
            FadeOut(inv_cot_graph),
            FadeOut(inv_tan_graph),
            FadeOut(inv_cos_graph),
            FadeOut(inv_sin_graph),
            FadeOut(inv_sec_graph_left),
            FadeOut(inv_sec_graph_right),
            FadeOut(inv_csc_graph_left),
            FadeOut(inv_csc_graph_right),
            FadeOut(inv_trigs_axes),
            FadeOut(inv_trigs_label_x),
            FadeOut(inv_trigs_label_y),
            FadeOut(inv_trigs_plane),
        )

        self.wait(2)


