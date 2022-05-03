# -*- encoding:utf-8 -*-

from manimlib import *
import numpy as np

class Transition(Scene):
    def construct(self) -> None:
        mathresult = Tex("\\approx","\\frac{1}{9}").set_color_by_tex("\\frac{1}{9}", BLUE_C).shift(3.6*RIGHT).scale(3)
        question = Tex("E","(","X", ")", "=").set_color_by_tex("X" , GREEN_B)
        expec_value = DecimalNumber(0.11 ,text_config={"font": "monospace"}).set_color(YELLOW_C).move_to(question).shift(1.3*RIGHT)
        expectation = VGroup(question, expec_value).scale(2.5).move_to(ORIGIN + LEFT)
        expectation_a = VGroup(expectation, mathresult)
        expectation_a.generate_target()
        expectation_a.target.scale(1/2.5).to_corner(LEFT+UP)
        hightlight = Rectangle(expectation_a.target.get_width()+0.4, expectation_a.target.get_height()+0.4).set_backstroke(BLUE_E).move_to(expectation_a.target)   
        self.play(MoveToTarget(expectation_a), ShowCreation(hightlight),run_time = 1.5)
        headText = Text("More rigorous proof", font="monospace", t2c={"proof" : BLUE_E}).to_edge(UP).shift(0.4*DOWN+1.3*RIGHT).scale(1.3)
        self.play(ShowCreation(headText),run_time = 2.5)
        self.wait(4)

        line = Line(ORIGIN+2*LEFT, ORIGIN+6*RIGHT).shift(0.5*DOWN)
        start = Dot(ORIGIN+2*LEFT+0.5*DOWN, radius = 0.05)
        end = Dot(ORIGIN+6*RIGHT+0.5*DOWN, radius = 0.05)
        pointO = Tex("O").set_color(TEAL_E).move_to(start).shift(0.5*UP)
        pointM = Tex("M").set_color(TEAL_E).move_to(end).shift(0.5*UP)
        segment = VGroup(line, start, end, pointO, pointM)
        dotR = Dot(ORIGIN+4*RIGHT+0.5*DOWN, radius = 0.05).set_color(YELLOW_D)
        pointR = Tex("R").set_color(YELLOW_D).move_to(dotR).shift(0.5*UP)
        dotS = Dot(ORIGIN+1*LEFT+0.5*DOWN, radius = 0.05).set_color(YELLOW_D)
        pointS = Tex("S").set_color(YELLOW_D).move_to(dotS).shift(0.5*UP)
        R = VGroup(dotR, pointR)
        S = VGroup(dotS, pointS)
        self.play(ShowCreation(segment), ShowCreation(R), ShowCreation(S),run_time = 3)
        self.wait(2.5)

        distribofR = Tex("R\sim U(0, 1)").move_to(headText)
        distribofS = Tex("S\sim U(0, 1)").next_to(distribofR, UP)
        distriboofRS = VGroup(distribofR, distribofS).shift(2*DOWN)
        highlightuniform = Rectangle(distriboofRS.get_width()+0.4, distriboofRS.get_height()+0.4).set_backstroke(TEAL_B).move_to(distriboofRS)
        self.play(ShowCreation(distriboofRS), ShowCreation(highlightuniform), run_time = 2)
        self.wait(3.5)

        self.wait(1.5)
        OS = Line(start.get_center(), dotS.get_center())
        rv = BraceLabel(OS, "X", DOWN)
        distribofX = Text("Distribution of",font="monospace").next_to(rv[1], LEFT)
        hightlightofdistrib = Rectangle(rv[1].get_width()+distribofX.get_width()+0.5, distribofX.get_height()+0.4).set_backstroke(RED_E).move_to(distribofX).shift(0.3*RIGHT)
        self.play(ShowCreation(rv), ShowCreation(distribofX), ShowCreation(hightlightofdistrib))
        distrib = VGroup(distribofX, rv[1])
        pdf = Tex("{p}_", "X(x)", font="monospace").move_to(distrib).shift(DOWN)
        distribofX.generate_target()
        self.add(distribofX.target)
        self.play(TransformMatchingShapes(distrib, pdf))
        pdf.generate_target()
        cdf = Tex("{F}_", "X(x)", font="monospace").move_to(pdf).shift(4*RIGHT)
        self.play(pdf.target.animate.shift(4*RIGHT) , TransformMatchingTex(pdf.target, cdf), run_time = 2.5)
        self.wait(5)
        hightlightcdf = Rectangle(cdf.get_width()+0.4, cdf.get_height()+0.4).set_backstroke(GREEN_E).move_to(cdf)
        easytoget = Text("Maybe easier to get", font = "monospace").set_color(BLUE_E).move_to(cdf).shift(DOWN)
        cdf_a = VGroup(cdf, hightlightcdf)
        cdf_a.generate_target()
        cdf_a.target.to_corner(LEFT+UP)
        self.play(ShowCreation(hightlightcdf), FadeIn(easytoget), run_time = 1.5)
        self.wait(2)
        self.play(FadeOut(expectation_a),FadeOut(hightlight),FadeOut(headText), FadeOut(segment), FadeOut(R), 
                  FadeOut(S), FadeOut(rv), FadeOut(distrib), FadeOut(distribofX.target), FadeOut(pdf), FadeOut(hightlightofdistrib),
                  FadeOut(distriboofRS),FadeOut(highlightuniform),
                  FadeOut(easytoget), MoveToTarget(cdf_a))
        self.wait()

class Proof(Scene):
    def construct(self):
        cdf = Tex("{F}_", "X(x)", font="monospace")
        hightlightcdf = Rectangle(cdf.get_width()+0.4, cdf.get_height()+0.4).set_backstroke(GREEN_E).move_to(cdf)
        cdf_a = VGroup(cdf, hightlightcdf)
        cdf_a.to_corner(LEFT+UP)
        self.add(cdf_a)
        self.wait()
        cdf_calu = Tex("{F}_", "X(x)", "=", "P(X\leqslant x)", "=", "1-P(X> x)",  font="monospace")
        hightlightcdf_calu = Rectangle(cdf_calu.get_width()+0.4, cdf_calu.get_height()+0.4).set_backstroke(GREEN_E).move_to(cdf_calu)
        cdf_c = VGroup(cdf_calu, hightlightcdf_calu)
        cdf_c.to_corner(LEFT+UP)
        self.play(TransformMatchingTex(cdf_a[0], cdf_c[0]), Transform(cdf_a[1], cdf_c[1]))
        self.wait(2)
        cdf_calu.generate_target()
        self.add(cdf_calu.target)
        prob_tar = Tex("P(X > x)", "=", "P(|OS|>x, |SR|>x, |RM|>x)",  font="monospace").to_corner(LEFT+UP).shift(1.5*DOWN)
        self.play(TransformMatchingTex(cdf_calu, prob_tar), run_time = 2)
        self.wait(4)
        self.play(FadeOut(prob_tar))
        line = Line(ORIGIN+1*LEFT, ORIGIN+6*RIGHT).shift(0.5*DOWN)
        start = Dot(ORIGIN+1*LEFT+0.5*DOWN, radius = 0.05)
        end = Dot(ORIGIN+6*RIGHT+0.5*DOWN, radius = 0.05)
        pointO = Tex("O").set_color(TEAL_E).move_to(start).shift(0.5*UP)
        pointM = Tex("M").set_color(TEAL_E).move_to(end).shift(0.5*UP)
        segment = VGroup(line, start, end, pointO, pointM).shift(2*UP)
        dotR = Dot(ORIGIN+3.5*RIGHT+0.5*DOWN, radius = 0.05).set_color(YELLOW_D)
        pointR = Tex("R").set_color(YELLOW_D).move_to(dotR).shift(0.5*UP)
        dotS = Dot(ORIGIN+0.5*DOWN+1.34*RIGHT, radius = 0.05).set_color(YELLOW_D)
        pointS = Tex("S").set_color(YELLOW_D).move_to(dotS).shift(0.5*UP)
        R = VGroup(dotR, pointR).shift(2*UP)
        S = VGroup(dotS, pointS).shift(2*UP)
        self.play(ShowCreation(segment), ShowCreation(R), ShowCreation(S), run_time = 2.5)
        self.wait(4)
        prob_1 = Tex("P\left ( \left| OS\\right|> x \\right )").next_to(segment, LEFT).shift(2.5*LEFT)
        prob_1_res = Tex("=","\left (  1-x\\right )^2").next_to(prob_1).shift(0.05*UP)
        prob_1_a = VGroup(prob_1, prob_1_res)
        self.play(ShowCreation(prob_1_a[0]), run_time = 2)
        self.wait(6)
        dotA =Dot(ORIGIN+0.5*DOWN+0.63*RIGHT, radius = 0.05).set_color(YELLOW_D)
        pointA=Tex("A").set_color(YELLOW_D).move_to(dotA).shift(0.5*UP)
        A = VGroup(dotA, pointA).shift(2*UP)
        self.play(ShowCreation(A))
        self.wait(2)
        OA = BraceLabel(Line(start.get_center(), dotA.get_center()), "x", DOWN)
        #self.play(ShowCreation(OA))
        # OS = BraceLabel(Line(dotA.get_center(), end.get_center()), "(1-x)", DOWN)
        # self.play(ShowCreation(OS))
        expla_1 = Tex("\left| OS\\right|", "=", "\left| OA\\right|", "+","\left| AS\\right|").shift(RIGHT*3.5+UP).set_color_by_tex_to_color_map({"\left| OS\\right|" : RED_E,
                                                                                                                                                "\left| OA\\right|" : MAROON_C,
                                                                                                                                                "\left| AS\\right|" : TEAL_D })
        self.play(ShowCreation(OA), run_time = 2)
        self.play(ShowCreation(expla_1), run_time = 3)        
        self.wait(4)
        self.play(CircleIndicate(pointR), CircleIndicate(pointS))
        self.wait()
        self.play(CircleIndicate(pointA), CircleIndicate(pointM))
        self.wait(5)
        self.play(ShowCreation(prob_1_a[1]))
        self.wait(2)
        self.play(FadeOut(expla_1))
        dotB =Dot(ORIGIN+0.5*DOWN+2.97*RIGHT, radius = 0.05).set_color(YELLOW_D)
        pointB=Tex("B").set_color(YELLOW_D).move_to(dotB).shift(0.5*UP)
        B = VGroup(dotB, pointB).shift(2*UP)
        dotC =Dot(ORIGIN+0.5*DOWN+5.13*RIGHT, radius = 0.05).set_color(YELLOW_D)
        pointC=Tex("C").set_color(YELLOW_D).move_to(dotC).shift(0.5*UP)
        C = VGroup(dotC, pointC).shift(2*UP)
        SB = BraceLabel(Line(dotS.get_center(), dotB.get_center()), "x", DOWN)
        RC = BraceLabel(Line(dotR.get_center(), dotC.get_center()), "x", DOWN)
        self.play(ShowCreation(B), ShowCreation(C))
        self.play(ShowCreation(SB), ShowCreation(RC))
        self.wait(5)

        prob_21 = Tex("P(X>x)").move_to(prob_1).shift(DOWN+0.35*LEFT)
        prob_22 = Tex("=(1-","3","x)^","2").next_to(prob_21, RIGHT)


        prob_31 = Tex("P(X>x)").move_to(prob_21).shift(DOWN)
        prob_32 = Tex("=(1-","n","x)^","{n-1}").next_to(prob_31,RIGHT)
        prob_3 = VGroup(prob_31, prob_32)
        highlightres = Rectangle(prob_3.get_width()+0.3, prob_3.get_height()+0.4).set_backstroke(BLUE_E).move_to(prob_3)

        self.wait()
        starts = Dot(ORIGIN+1*LEFT+2.5*DOWN, radius = 0.05)
        ends = Dot(ORIGIN+6*RIGHT+2.5*DOWN, radius = 0.05)
        pointOs = Tex("O").set_color(TEAL_E).move_to(starts).shift(0.5*UP)
        pointMs = Tex("M").set_color(TEAL_E).move_to(ends).shift(0.5*UP)
        Os = VGroup(starts, pointOs).shift(2*UP)
        Ms = VGroup(ends, pointMs).shift(2*UP)

        dotRs = Dot(ORIGIN+(2*1.63 + 3.5 - 1.63)*RIGHT+2.5*DOWN, radius = 0.05).set_color(YELLOW_D)
        pointRs = Tex("R").set_color(YELLOW_D).move_to(dotRs).shift(0.5*UP)
        dotSs = Dot(ORIGIN+2.5*DOWN+(2*1.63 + 1.34)*RIGHT, radius = 0.05).set_color(YELLOW_D)
        pointSs = Tex("S").set_color(YELLOW_D).move_to(dotSs).shift(0.5*UP)
        Rs = VGroup(dotRs, pointRs).shift(2*UP)
        Ss = VGroup(dotSs, pointSs).shift(2*UP)

        dotAs =Dot(ORIGIN+2.5*DOWN+0.63*RIGHT, radius = 0.05).set_color(YELLOW_D)
        pointAs=Tex("A").set_color(YELLOW_D).move_to(dotAs).shift(0.5*UP)
        As = VGroup(dotAs, pointAs).shift(2*UP)
        dotBs =Dot(ORIGIN+2.5*DOWN+1*1.63*RIGHT+0.63*RIGHT, radius = 0.05).set_color(YELLOW_D)
        pointBs=Tex("B").set_color(YELLOW_D).move_to(dotBs).shift(0.5*UP)
        Bs = VGroup(dotBs, pointBs).shift(2*UP)
        dotCs =Dot(ORIGIN+2.5*DOWN+2*1.63*RIGHT+0.63*RIGHT, radius = 0.05).set_color(YELLOW_D)
        pointCs=Tex("C").set_color(YELLOW_D).move_to(dotCs).shift(0.5*UP)
        Cs = VGroup(dotCs, pointCs).shift(2*UP)


        Points = VGroup(Bs,Cs,Rs,Ss,As, Os, Ms)

        #self.play(*[ShowCreation(point)for point in Points])

        OAs = Line(start.get_center(), dotA.get_center())
        ASs = Line(dotA.get_center(), dotS.get_center())
        SBs = Line(dotS.get_center(), dotB.get_center())
        BRs = Line(dotB.get_center(), dotR.get_center())
        RCs = Line(dotR.get_center(), dotC.get_center())
        CMs = Line(dotC.get_center(), end.get_center())
        
        OAss = Line(starts.get_center(), dotAs.get_center())
        ABss = Line(dotAs.get_center(), dotBs.get_center())
        SRss = Line(dotSs.get_center(), dotRs.get_center())
        BCss = Line(dotBs.get_center(), dotCs.get_center())
        RMss = Line(dotRs.get_center(), ends.get_center())
        CSss = Line(dotCs.get_center(), dotSs.get_center())
        lines = VGroup(OAs,ASs,SBs,BRs,RCs,CMs,OAss, ABss, SRss, BCss, RMss, CSss)
        OCs = BraceLabel(Line(starts.get_center(), dotCs.get_center()), "3x", DOWN) 
        self.play(*[ShowCreation(point)for point in Points],TransformFromCopy(OAs, OAss), TransformFromCopy(ASs, CSss), TransformFromCopy(SBs, ABss), 
                 TransformFromCopy(BRs, SRss), TransformFromCopy(RCs, BCss), TransformFromCopy(CMs, RMss), ShowCreation(OCs))
        self.wait(8)
        self.play(ShowCreation(prob_21), ShowCreation(prob_22))
        self.wait(7)
        self.play(TransformFromCopy(prob_21, prob_31) ,TransformFromCopy(prob_22, prob_32), ShowCreation(highlightres))
        self.wait(10)
        
        cdf_res = Tex("{F}_", "X(x)", "=","1-(1-","n","x)^","{n-1}", font="monospace")
        hightlightcdf_res = Rectangle(cdf_res.get_width()+0.4, cdf_res.get_height()+0.4).set_backstroke(GREEN_E).move_to(cdf_res)
        cdf_res = VGroup(cdf_res, hightlightcdf_res)
        cdf_res.to_corner(LEFT+UP)
        others = VGroup(OCs, OA,SB, RC, A,B,C,R,S,segment)
        probs = VGroup(prob_1_a, prob_21, prob_22)
        self.play(*[FadeOut(mob)for mob in lines], *[FadeOut(mob)for mob in Points], *[FadeOut(mob)for mob in others], 
                  *[FadeOut(mob)for mob in probs], *[FadeOut(mob)for mob in prob_3], FadeOut(highlightres),FadeOut(hightlightcdf_calu),FadeOut(cdf_a),FadeOut(cdf_calu.target),
                   TransformMatchingTex(cdf_c[0], cdf_res[0]), ShowCreation(cdf_res[1]))
        self.wait()
            
        pass
class Calucate(Scene):
    def construct(self):
        cdf_res = Tex("{F}_", "X(x)", "=","1-(1-","n","x)^","{n-1}", font="monospace")
        hightlightcdf_res = Rectangle(cdf_res.get_width()+0.4, cdf_res.get_height()+0.4).set_backstroke(GREEN_E).move_to(cdf_res)
        cdf_res = VGroup(cdf_res, hightlightcdf_res)
        cdf_res.to_corner(LEFT+UP)
        self.add(cdf_res)
        self.wait(3)
        calc1 = TexText(
            
            r"""
\begin{equation}
\begin{split}
E(x)&= \int_{0}^{\frac{1}{n}}xp(x)dx\\
&= \int_{0}^{\frac{1}{n}}xdF(x)\\
&= xF(x)\bigg|_{0}^{\frac{1}{n}} - \int_{0}^{\frac{1}{n}}F(x)dx\\
&= \frac{1}{n}P(X \leq \frac{1}{n}) - \int_{0}^{\frac{1}{n}}P(X \leq x)dx\\
&= \int_{0}^{\frac{1}{n}}(1 - P(X \leq x))dx\\
&= \int_{0}^{\frac{1}{n}}(1-nx)^{n-1}dx\\
\end{split}
\end{equation}
            """, font="Consolas"
        ).scale(0.7).to_edge(LEFT).shift(0.8*DOWN)
        self.play(ShowCreation(calc1))
        self.wait(2)
        highlight1 = Rectangle(cdf_res.get_width()-1, cdf_res.get_height()*2+0.2).set_backstroke(TEAL_D).shift(3.9*LEFT+0.2*UP)
        note1 = Text("Use integration by parts\nto simplify the calculation", font="monospace", t2c={"integration by parts" : GOLD_C}).next_to(highlight1)
        self.play(ShowCreation(highlight1), FadeIn(note1) ,run_time = 2.5,)
        self.wait(7)
        self.play(FadeOut(highlight1), FadeOut(note1))
        self.wait(6)

        calc2 = TexText(
            r"""
            \begin{equation}
\begin{split}
E(x)&= \frac{1}{n}\int_{0}^{1}(1-u)^{n-1}du\\
&= \frac{1}{n}(-\frac{1}{n}(1-u)^{n-1}\bigg|_{0}^{1})\\
&= \frac{1}{n}(-\frac{1}{n}(0-(-1)))\\
&= \frac{1}{n^2}
\end{split}
\end{equation}""", font="Consolas"
        ).scale(0.7).next_to(calc1, RIGHT).shift(1.2*UP)
        note2 = Tex("Let\ ","u", "= nx").set_color_by_tex_to_color_map({"u":YELLOW_D}).next_to(calc2, UP)
        self.play(ShowCreation(calc2), ShowCreation(note2))
        self.wait(3)
        res = Tex(r"E(", r"X", r") = \frac{1}{n^2}").set_color_by_tex("X", GREEN_B).scale(2)
        self.play(FadeOut(calc1), FadeOut(note2),FadeOut(cdf_res), TransformMatchingShapes(calc2, res))
        self.wait(7.5)
        self.wait(3)
        coll1 = Tex(r"E(X_{(k)})=\frac{1}{n}\sum_{i=1}^{k}\frac{1}{n-i+1}").shift(0.5*DOWN+RIGHT)

        note4_text2 = Text("kth shortest", t2s={"k":ITALIC}).scale(0.9).next_to(coll1, 1.5*LEFT)
        note4_text1 = Text("Generally, for").scale(0.9).next_to(note4_text2, 0.5*UP)
        note4_text3 = Text("interval").scale(0.9).next_to(note4_text2, DOWN).shift(0.5*LEFT)
        note4_tex = Tex(r"X_{(k)}").scale(0.9).next_to(note4_text3, 0.5*RIGHT).shift(0.1*DOWN)
        note4 = VGroup(note4_tex, note4_text1, note4_text2, note4_text3)
        self.play(res.animate.shift(UP*2), ShowCreation(coll1), FadeIn(note4))

        self.wait(2)
        note3 = Text("Ordered Statistics").set_color(GOLD_D).next_to(coll1, 2*DOWN)
        highlight = Rectangle(note3.get_width()+0.4, note3.get_height()+0.4).set_backstroke(TEAL_B).move_to(note3)
        self.play(ShowCreation(note3), ShowCreation(highlight))
        self.wait(6)
        self.wait(19)
        mobs = VGroup(res, coll1, note4, note3, highlight)
        self.play(*[FadeOut(mob)for mob in mobs])
        self.wait(2)

        pass
