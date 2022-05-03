# -*- encoding:utf-8 -*-

from manimlib import *
import numpy as np

class Reference(Scene):
    def construct(self):
        ref = Text("Reference").to_corner(UP+LEFT)
        ref_1 = Text(r"H.A.David, H.N.Nagaraja, Order Statistics(pp. 133-135,", font="Consolas", t2s={"Order Statistic":ITALIC}).scale(0.4)
        ref_2 = Text(r"and p. 153),New Jersey: John Wiley Sons,", font="Consolas").scale(0.4).next_to(ref_1, 0.5*RIGHT)
        ref_5 = Text(r"Inc., Hoboken.").scale(0.4).next_to(ref_2, 0.5*RIGHT)
        ref1 = VGroup(ref_1, ref_2, ref_5).next_to(ref, DOWN).shift(5.2*RIGHT)
        ref_3 = Text(r"Spivey, M.(2010, December). If a 1 meter rope...", font="Consolas").scale(0.4).to_edge(LEFT)
        ref_4 = Text(r"""Retrieved from""", font="Consolas").scale(0.4).next_to(ref_3, 0.5*RIGHT)
        ref_6 = Text(r"https://math.stackexchange.com/questions/13959/").scale(0.4).next_to(ref_4, 0.5*RIGHT).shift(0.03*DOWN)
        ref2 = VGroup(ref_3, ref_4, ref_6).next_to(ref1, DOWN).shift(0.05*RIGHT)

        lib = Text("Animation Engine").next_to(ref2, DOWN).to_edge(LEFT)
        manim = Text("Manim:https://github.com/3b1b/manim", font="Consolas").scale(0.4).next_to(lib, DOWN).to_edge(LEFT).shift(0.5*RIGHT)
        
        sc = Text("Source Code").next_to(manim, DOWN).to_edge(LEFT)
        sc_link = Text("" ,font="Consolas").scale(0.4).next_to(sc, DOWN).to_edge(LEFT).shift(0.5*RIGHT)

        gm = Text("Group Member").next_to(sc_link, DOWN).to_edge(LEFT)
        gm_all = Text("陈嘉宁   钱凯恒   沈桐乐   吴冕志", font = "宋体").scale(0.4).next_to(gm, DOWN).to_edge(LEFT).shift(0.5*RIGHT)

        mobs = VGroup(ref, ref1, ref2, lib, manim, sc, sc_link, gm, gm_all)
        self.play(*[FadeIn(mob)for mob in mobs])
        self.wait(3)
        self.play(*[FadeOut(mob)for mob in mobs])
        pass