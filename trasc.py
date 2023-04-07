from manim import *
import math, numpy, mpmath

class Graph(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-7,7],
            y_range=[-5,5],
            x_length=8,
            y_length=5,
        ).set_opacity(0.1)
        plane.shift(RIGHT*3)

        axesp1 = Axes(
            x_range=[-7, 7, PI/2],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=5,
            tips=False,
            x_axis_config={
                'include_numbers' : False,
                'tick_size' : 0.07,
            },
            y_axis_config={
                'include_numbers' : True
            }
        )
        axesp1.shift(RIGHT*3)

        labelsp1 = NumberLine(
            x_range=[-7, 7, PI/2],
            length=8,
            include_tip=False,
            include_numbers=False
        )

        labelsp1.add_labels({
            -2*PI: Tex("$-2\pi$"),
            -3*PI/2: Tex("$-\\frac{3\pi}{2}$"),
            -PI: Tex("$-\pi$"),
            -PI/2: Tex("$-\\frac{\pi}{2}$"),
            PI/2: Tex("$\\frac{\pi}{2}$"),
            PI: Tex("$\pi$"),
            3*PI/2: Tex("$\\frac{3\pi}{2}$"),
            2*PI: Tex("$2\pi$"),
        })
        labelsp1.shift(RIGHT*3)
        

        plane2 = NumberPlane(
            x_range=[-7, 7],
            y_range=[-5, 5]
        ).set_opacity(0.1)

        axesp2 = Axes(
            x_range=[-7, 7, PI/2],
            y_range=[-5, 5, 1],
            x_length=None,
            y_length=None,
            tips=False,
            x_axis_config={
                'include_numbers' : False,
                'tick_size' : 0.07,
            },
            y_axis_config={
                'include_numbers' : True
            }
        )

        axesp2c = Axes(
            x_range=[-7, 7, 1],
            y_range=[-5, 5, 1],
            x_length=None,
            y_length=None,
            tips=False,
            x_axis_config={
                'include_numbers' : True,
            },
            y_axis_config={
                'include_numbers' : True
            }
        )

        labelsp2 = NumberLine(
            x_range=[-7, 7, PI/2],
            include_tip=False,
            include_numbers=False
        )

        labelsp2.add_labels({
            -2*PI: Tex("$-2\pi$"),
            -3*PI/2: Tex("$-\\frac{3\pi}{2}$"),
            -PI: Tex("$-\pi$"),
            -PI/2: Tex("$-\\frac{\pi}{2}$"),
            PI/2: Tex("$\\frac{\pi}{2}$"),
            PI: Tex("$\pi$"),
            3*PI/2: Tex("$\\frac{3\pi}{2}$"),
            2*PI: Tex("$2\pi$"),
        })

        unit_circle = NumberPlane(
            x_range=[-2,2],
            y_range=[-2,2],
            x_length=4,
            y_length=4
        ).set_opacity(0.1)

        axescircle = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=4,
            tips=False,
            x_axis_config={
                'include_numbers' : True,
            },
            y_axis_config={
                'include_numbers' : True
            }
        )

        #unit_circle.shift(LEFT*4)

        theta = ValueTracker(2*PI)

        #Circulo unitario
        circle = Circle(1, color = WHITE)
        circle2 = Circle(1, color = WHITE)
        #circle.shift(LEFT*4)

        '''
        nsin(mx)
        donde n controla la amplitud de la funcion seno
              m controla la frecuencia de la funcion seno 
        '''
        #Funciones en el plano_1 y el plano_2
        fsin = always_redraw(lambda : plane.plot(lambda x : math.sin(x), x_range=[-2*PI,theta.get_value()], color = BLUE))
        fsin2 = plane2.plot(lambda x : math.sin(x), x_range=[-7,7], color = BLUE)
        fsin3 = plane2.plot(lambda x : PI*math.sin(2.71*x) + PI/2, x_range=[-7,7], color = BLUE)

        fcos = always_redraw(lambda : plane.plot(lambda x : math.cos(x), x_range=[-2*PI,theta.get_value()], color = RED))
        fcos2 = plane2.plot(lambda x : math.cos(x), x_range=[-7,7], color = RED)
        fcos3 = plane2.plot(lambda x : 1.41*math.cos(x/2), x_range=[-7,7], color = RED)

        sftan = always_redraw(lambda : plane.plot(lambda x : math.tan(x), x_range=[-PI/2 + 0.2, PI/2-0.2], color = YELLOW))
        sftan2 = always_redraw(lambda : plane.plot(lambda x : math.tan(x), x_range=[-PI/2 + PI + 0.2, PI/2 - 0.2 + PI], color = YELLOW))

        sfcot = always_redraw(lambda : plane.plot(lambda x : 1/math.tan(x), x_range=[-PI+0.2, -0.2], color = GREEN))
        sfcot2 = always_redraw(lambda : plane.plot(lambda x : 1/math.tan(x), x_range=[-PI + 0.2 + PI, PI -0.2], color = GREEN))

        sfsec = always_redraw(lambda : plane.plot(lambda x : 1/math.cos(x), x_range=[-PI/2+0.2, PI/2-0.2], color = PURPLE))
        sfsec2 = always_redraw(lambda : plane.plot(lambda x : 1/math.cos(x), x_range=[-PI/2+0.2 + PI, PI/2-0.2 + PI], color = PURPLE))

        sfcsc = always_redraw(lambda : plane.plot(lambda x : 1/math.sin(x), x_range=[-PI + 0.2, -0.2], color = ORANGE))
        sfcsc2 = always_redraw(lambda : plane.plot(lambda x : 1/math.sin(x), x_range=[-PI + 0.2 + PI, PI-0.2], color = ORANGE))


        ftan2 = VGroup()
        ftan3 = VGroup()
        for n in range(-4, 4):
            gtan2 = plane2.plot(
                lambda x : math.tan(x),
                x_range=[(-PI/2)+0.2 + n*PI, (PI/2)-0.2 + n*PI],
                color = YELLOW
            )
            gtan3 = plane2.plot(
                lambda x : math.tan(2.71*x)/3,
                x_range=[(-PI/2)+0.2 + n*PI, (PI/2)-0.2 + n*PI],
                color = YELLOW
            )
            ftan2.add(gtan2)
            ftan3.add(gtan3)
        
        fcot2 = VGroup()
        fcot3 = VGroup()
        for n in range(-2, 4):
            gcot2 = plane2.plot(
                lambda x : 1/math.tan(x),
                x_range=[-PI+0.2 + n*PI, n*PI - 0.2],
                color = GREEN
            )
            gcot3 = plane2.plot(
                lambda x : 1/math.tan(x/2),
                x_range=[-PI+0.2 + n*PI, n*PI - 0.2],
                color = GREEN
            )
            fcot2.add(gcot2)
            fcot3.add(gcot3)

        fsec2 = VGroup()
        fsec3 = VGroup()
        for n in range(-2,3):
            gsec2 = plane2.plot(
                lambda x : 1/math.cos(x),
                x_range=[-PI/2+0.2 + n*PI, PI/2-0.2 + n*PI],
                color = PURPLE
            )
            gsec3 = plane2.plot(
                lambda x : 1/math.cos(x)**2,
                x_range=[-PI/2+0.2 + n*PI, PI/2-0.2 + n*PI],
                color = PURPLE
            )
            fsec2.add(gsec2)
            fsec3.add(gsec3)

        fcsc2 = VGroup()
        fcsc3 = VGroup()
        for n in range(-2,4):
            gcsc2 = plane2.plot(
                lambda x : 1/math.sin(x),
                x_range=[-PI+0.2 + n*PI, n*PI-0.2],
                color = ORANGE
            )
            gcsc3 = plane2.plot(
                lambda x : -((1/math.sin(x/2)/3)**4),
                x_range=[-PI+0.2 + n*PI, n*PI-0.2],
                color = ORANGE
            )
            fcsc2.add(gcsc2)
            fcsc3.add(gcsc3)

        #Seno y coseno dentro del circulo unitario
        line_de = always_redraw(lambda: Line((np.cos(theta.get_value()), np.sin(theta.get_value()), 0), (np.cos(theta.get_value()), 0, 0), color=BLUE).shift(LEFT*4))
        sin_line = always_redraw(lambda: Line((np.cos(theta.get_value()), np.sin(theta.get_value()), 0), (np.cos(theta.get_value()), 0, 0), color=BLUE))
        line_sa = always_redraw(lambda: Line((0, 0, 0), (np.cos(theta.get_value()), 0, 0), color=RED).shift(LEFT*4))
        cos_line = always_redraw(lambda: Line((0, 0, 0), (np.cos(theta.get_value()), 0, 0), color=RED))
        radius = always_redraw(lambda: Line(ORIGIN, (np.cos(theta.get_value()), np.sin(theta.get_value()), 0), color=WHITE).shift(LEFT*4))
        radius_line = always_redraw(lambda: Line(ORIGIN, (np.cos(theta.get_value()), np.sin(theta.get_value()), 0), color=WHITE))

        #Valores del seno en pantalla
        pio2 = Tex("$\\frac{\pi}{2}$").next_to(circle, UP)
        pic = Tex("$\pi$").next_to(circle, LEFT)
        tpio2 = Tex("$\\frac{3\pi}{2}$").next_to(circle, DOWN)
        twpi = Tex("$2\pi$").next_to(circle, RIGHT)

        dsin_value = always_redraw(lambda: DecimalNumber(include_sign=True).set_value(np.sin(theta.get_value())).next_to(pio2, UP).shift(RIGHT).set_color(BLUE))
        cos_value = always_redraw(lambda: DecimalNumber(include_sign=True).set_value(np.cos(theta.get_value())).next_to(pio2, UP).shift(RIGHT).set_color(RED))
        sin_value = always_redraw(lambda: DecimalNumber(include_sign=True).set_value(np.sin(theta.get_value())).next_to(cos_value, UP).set_color(BLUE))


        dsin_lab = Tex("$\sin x = $", color = BLUE).next_to(dsin_value, LEFT).shift(LEFT*4)
        cos_lab = Tex("$\cos x = $", color = RED).next_to(cos_value, LEFT).shift(LEFT*4)
        sin_lab = Tex("$\sin x = $", color = BLUE).next_to(sin_value, LEFT).shift(LEFT*4)

        #Texto
        sint = Tex("$f(x)= \sin x$", color=BLUE).shift(UP*3+RIGHT*3)
        cost = Tex("$f(x)= \cos x$", color=RED).shift(UP*3+RIGHT*3)
        tant = Tex("$f(x)= \\tan x = \\frac{\sin x}{\cos x}$", color=YELLOW).shift(UP*3+RIGHT*3)
        cott = Tex("$f(x)= \cot x = \\frac{1}{\\tan x} = \\frac{\cos x}{\sin x}$", color=GREEN).shift(UP*3+RIGHT*3)
        sect = Tex("$f(x)= \sec x = \\frac{1}{\cos x}$", color=PURPLE).shift(UP*3+RIGHT*3)
        csct = Tex("$f(x)= \csc x = \\frac{1}{\sin x}$", color=ORANGE).shift(UP*3+RIGHT*3)
        
        #Animaciones
        self.play(Create(circle), rate_func=smooth, run_time=1)
        self.play(circle.animate.set_opacity(0.5))
        self.play(circle.animate.set_fill(WHITE, opacity=0))
        self.play(Write(axescircle))
        self.wait(1)
        self.play(FadeOut(axescircle))

        self.play(DrawBorderThenFill(unit_circle))
        self.play(Write(pio2), Write(pic), Write(tpio2), Write(twpi), run_time=0.3)
        self.play(
            circle.animate.shift(LEFT*4),
            unit_circle.animate.shift(LEFT*4),
            pio2.animate.shift(LEFT*4),
            pic.animate.shift(LEFT*4),
            tpio2.animate.shift(LEFT*4),
            twpi.animate.shift(LEFT*4),
        )

        self.play(DrawBorderThenFill(plane), Write(axesp1), Write(labelsp1))

        self.play(Create(line_de), Create(radius), run_time=0.3)
        self.play(Create(sint), run_time=0.5)
        self.wait(1)
        self.play(Create(dsin_value), Create(dsin_lab), run_time=0.2)
        self.play(theta.animate.increment_value(TAU*2), Create(fsin), rate_func=smooth, run_time=5)
        self.wait(1)
        self.play(FadeOut(fsin))

        self.play(Create(line_sa))
        self.wait(1)
        self.play(ReplacementTransform(sint, cost), run_time=0.5)
        self.play(ReplacementTransform(dsin_value, cos_value), ReplacementTransform(dsin_lab, cos_lab), run_time=0.2)
        self.play(theta.animate.increment_value(TAU*2), Create(fcos), rate_func=smooth, run_time=5)
        self.wait(1)
        self.play(FadeOut(fcos))

        theta = ValueTracker(3*PI/2)
        
        self.play(ReplacementTransform(cost, tant), run_time=0.5)
        self.play(Write(sin_lab), Write(sin_value), run_time=0.5)
        self.play(theta.animate.increment_value(PI), Create(sftan), rate_func=smooth, run_time=5)
        self.play(theta.animate.increment_value(PI), Create(sftan2), rate_func=smooth, run_time=5)
        self.wait(1)
        self.play(FadeOut(sftan), FadeOut(sftan2))

        theta = ValueTracker(PI)

        self.play(ReplacementTransform(tant, cott), run_time=0.5)
        self.play(theta.animate.increment_value(PI), Create(sfcot), rate_func=smooth, run_time=5)
        self.play(theta.animate.increment_value(PI), Create(sfcot2), rate_func=smooth, run_time=5)
        self.wait(1)
        self.play(FadeOut(sfcot), FadeOut(sfcot2))

        theta = ValueTracker(3*PI/2)

        self.play(ReplacementTransform(cott, sect), run_time=0.5)
        self.play(theta.animate.increment_value(PI), Create(sfsec), rate_func=smooth, run_time=5)
        self.play(theta.animate.increment_value(PI), Create(sfsec2), rate_func=smooth, run_time=5)
        self.wait(1)
        self.play(FadeOut(sfsec2), FadeOut(sfsec))

        theta = ValueTracker(PI)

        self.play(ReplacementTransform(sect, csct), run_time=0.5)
        self.play(theta.animate.increment_value(PI), Create(sfcsc), rate_func=smooth, run_time=5)
        self.play(theta.animate.increment_value(PI), Create(sfcsc2), rate_func=smooth, run_time=5)
        self.wait(1)
        self.play(FadeOut(sfcsc2), FadeOut(sfcsc))

        
        self.play(
            FadeOut(csct),
            FadeOut(line_de),
            FadeOut(line_sa),
            FadeOut(radius),
            FadeOut(pio2),
            FadeOut(pic),
            FadeOut(tpio2),
            FadeOut(twpi),
            FadeOut(circle),
            FadeOut(sin_value),
            FadeOut(cos_value),
            FadeOut(cos_lab),
            FadeOut(sin_lab),
            FadeOut(plane),
            FadeOut(unit_circle),
            FadeOut(axesp1),
            FadeOut(labelsp1),
            run_time=0.5)

        self.wait(1)
      
        self.play(DrawBorderThenFill(plane2), Write(axesp2), Write(labelsp2))

        self.play(Create(fsin2), run_time=2.5)
        self.play(Create(fcos2), run_time=2.5)
        self.play(Create(ftan2), run_time=2.5)
        self.play(Create(fcot2), run_time=2.5)
        self.play(Create(fsec2), run_time=2.5)
        self.play(Create(fcsc2), run_time=2.5)

        self.wait(7)

        self.play(ReplacementTransform(fsin2, fsin3))
        self.play(ReplacementTransform(fcos2, fcos3))
        self.play(ReplacementTransform(ftan2, ftan3))
        self.play(ReplacementTransform(fcot2, fcot3))
        self.play(ReplacementTransform(fsec2, fsec3))
        self.play(ReplacementTransform(fcsc2, fcsc3))

        self.play(
            Write(radius_line),
            ReplacementTransform(axesp2, axesp2c),
            ReplacementTransform(fsin3, sin_line),
            ReplacementTransform(fcos3, cos_line),
            ReplacementTransform(ftan3, circle2),
            ReplacementTransform(fcot3, circle2),
            ReplacementTransform(fsec3, circle2),
            ReplacementTransform(fcsc3, circle2),
            FadeOut(labelsp2)
            )

        self.play(plane2.animate.set_opacity(0.5), axesp2c.animate.set_opacity(0.7))
        self.play(theta.animate.increment_value(2*PI), rate_func=smooth, run_time=5)

        self.wait(1.5)

        self.play(FadeOut(plane2),
            FadeOut(axesp2c),
            FadeOut(sin_line),
            FadeOut(cos_line),
            FadeOut(radius_line),
            )
        self.wait(1.5)
        self.play(FadeOut(circle2))
        self.wait(2)
        