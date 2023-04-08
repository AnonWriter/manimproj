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
            y_range = [-1.5, 1.5, 1],
            x_length = 7,
            y_length = 4,
            tips = False
        )
        
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

        
