from manim import *
from manimlib import *
from numpy import sin, arcsin, cos, arccos, tan, arctan

class Formulas(Scene):
    def construct(self):

        tex1 = Tex("Si")

        sin_tex = Tex("$f(x) = \sin x$")
        
        sin_domain = Tex(
            "$D_f = \{ \mathbb{R} \}$, y \
             \\noindent $I_f = \{ x | -1 \le x \le 1 \}$"
        )
        sin_domain.next_to(tex1, DOWN)
        sin_domain.next_to(sin_tex, DOWN)

        self.play(Write(tex1), tex1.animate.shift(UP*0.5))

        self.play(
            Write(sin_tex),
            run_time=2.5
        )
        self.play(
            Write(sin_domain),
            run_time=2.5
        )
        self.wait()

        g_tex1 = VGroup(tex1, sin_tex, sin_domain)
        self.play(g_tex1.animate.shift(UP*2.7))

        tex2 = Tex("Entonces")

        self.play(Write(tex2), tex2.animate.shift(UP*0.5))

        sinm1_tex = Tex("$f^{-1}(x) = \sin y$")
        sinm1_domain = Tex("$D_{f^{-1}} = \{ x | -1 \le x \le 1\}$, pero")
        sinm1_idomain = Tex("$I_{f^{-1}} = \{ x | - \\frac{\pi}{2} \le x \le \\frac{\pi}{2} \}$")
        sinm1_tex.next_to(tex2, DOWN)
        sinm1_domain.next_to(sinm1_tex, DOWN)
        sinm1_idomain.next_to(sinm1_domain, DOWN)

        self.play(
            Write(sinm1_tex),
            run_time=2.5
        )
        self.play(
            Write(sinm1_domain),
            run_time=2.5
        )
        self.play(Write(sinm1_idomain))
        self.wait()

        self.clear()
        self.wait()

        

class InverseTrigs(Scene):
    def construct(self):
        ax = Axes(
            x_range = [-4, 4, 1],
            y_range = [-4, 4, PI/2],
            tips = False,
            x_length = 7,
            y_length = 7,
        )

        ax_asinf = Axes(
            x_range = [-4, 4, 1],
            y_range = [-4, 4, PI/2],
            tips = False,
            x_length = 7,
            y_length = 7,
        )

        self.play(Write(ax), Write(ax_asinf), rate_func=smooth)

        # grafica del seno
        sin_graph = ax.plot(lambda t: sin(t), x_range=[-PI, PI], color=BLUE_C)

        # grafica de seno para ajustarla al arcoseno
        inv_sin = ax.plot(lambda t: sin(t), x_range=[-PI/2, PI/2], color=YELLOW)
        inv_sin.rotate(PI, axis=UP)
        inv_sin.rotate(-PI/2)

        # grafica de seno para ajustarla al arcocoseno
        inv_cos = ax.plot(lambda t: PI/2 + sin(t), x_range=[-PI/2, PI/2], color=RED)
        inv_cos.rotate(-PI/2)

        # self.play(Create(sin_graph),run_time=4)
        self.play(Create(inv_sin))
        self.wait()

        '''
        self.play(
            ax.animate.shift(LEFT*3),
            inv_sin.animate.shift(LEFT*3),
            ax_asinf.animate.shift(RIGHT*3),
            a_asin.animate.shift(RIGHT*3)
        )
        self.wait()
        '''

        self.play(Create(inv_cos))
        self.wait()

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


        arcsin_value = lambda x : arcsin(x)
        
        

        self.wait()