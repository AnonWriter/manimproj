from manim import *
import math

class Sets(Scene):
    def construct(self):

        set_A = Circle(color=WHITE)
        label_A = Tex("$A$").next_to(set_A, UL)
        group_A = VGroup(set_A, label_A)

        set_B = Circle(color=WHITE)
        label_B = Tex("$B$").next_to(set_B, UR)
        group_B = VGroup(set_B, label_B)

        set_C = Circle(color=WHITE)
        label_C = Tex("$C$").next_to(set_C, DOWN)
        group_C = VGroup(set_C, label_C)

        set_group = VGroup(group_A, group_B, group_C)

        self.play(Create(group_A), Create(group_B), Create(group_C))
        '''
        self.play(
            group_A.animate.set_opacity(0.3),
            group_B.animate.set_opacity(0.3),
            group_C.animate.set_opacity(0.3),
        )
        self.play(
            group_A.animate.set_fill(WHITE, opacity=0),
            group_B.animate.set_fill(WHITE, opacity=0),
            group_C.animate.set_fill(WHITE, opacity=0),
        )
        '''
        self.play(
            group_A.animate.shift(LEFT*0.5),
            group_B.animate.shift(RIGHT*0.5),
            group_C.animate.shift(DOWN*0.87),
        )
        self.play(set_group.animate.shift(UP*0.7))

        self.wait()

        intersection_ABC = Intersection(set_A, set_B, set_C, fill_opacity=0.6, color=PURPLE_C)
        label_ABC = Tex("$A \cap B \cap C$", color=PURPLE_C).to_edge(UP)

        intersection_AB = Intersection(set_A, set_B)
        intersection_AC = Intersection(set_A, set_C)
        intersection_BC = Intersection(set_B, set_C)

        diff_ABdC = Difference(intersection_AB, intersection_ABC, fill_opacity=0.6, color=BLUE_C)
        diff_ACdB = Difference(intersection_AC, intersection_ABC, fill_opacity=0.6, color=BLUE_C)
        diff_BCdA = Difference(intersection_BC, intersection_ABC, fill_opacity=0.6, color=BLUE_C)

        label_ABdC = Tex("$A \cap B \setminus C,$", color=BLUE_C).to_edge(UP)
        label_ACdB = Tex("$A \cap C \setminus B,$", color=BLUE_C).next_to(label_ABdC, LEFT)
        label_BCdA = Tex("$B \cap C \setminus A$", color=BLUE_C).next_to(label_ABdC, RIGHT)

        group_label_SSdS = VGroup(label_ABdC, label_ACdB, label_BCdA)

        union_AB = Union(set_A, set_B)
        union_AC = Union(set_A, set_C)
        union_BC = Union(set_B, set_C)

        diff_AdBC = Difference(set_A, union_BC, fill_opacity=0.6, color=GREEN_C)
        diff_BdAC = Difference(set_B, union_AC, fill_opacity=0.6, color=GREEN_C)
        diff_CdAB = Difference(set_C, union_AB, fill_opacity=0.6, color=GREEN_C)

        label_AdBC = Tex("$A \setminus (B \cup C),$", color=GREEN_C).to_edge(UP)
        label_BdAC = Tex("$B \setminus (A \cup C),$", color=GREEN_C).next_to(label_AdBC, LEFT)
        label_CdAB = Tex("$C \setminus (A \cup B)$", color=GREEN_C).next_to(label_AdBC, RIGHT)

        group_label_SdSS = VGroup(label_AdBC, label_BdAC, label_CdAB)

        indiff_group = VGroup(
            intersection_ABC,
            diff_ABdC,
            diff_ACdB,
            diff_BCdA,
            diff_AdBC,
            diff_BdAC,
            diff_CdAB,
        )


        self.play(DrawBorderThenFill(intersection_ABC), Write(label_ABC))
        self.play(FadeOut(label_ABC))
        self.play(
            DrawBorderThenFill(diff_ABdC),
            DrawBorderThenFill(diff_ACdB),
            DrawBorderThenFill(diff_BCdA),
            Write(group_label_SSdS),
        )
        self.play(FadeOut(group_label_SSdS))
        self.play(
            DrawBorderThenFill(diff_AdBC),
            DrawBorderThenFill(diff_BdAC),
            DrawBorderThenFill(diff_CdAB),
            Write(group_label_SdSS),
        )
        self.play(FadeOut(group_label_SdSS))
        self.wait()

        self.play(
            set_group.animate.shift(RIGHT*2),
            indiff_group.animate.shift(LEFT*2)
        )
        self.wait()