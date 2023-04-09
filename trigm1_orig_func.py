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