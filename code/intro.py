# -*- encoding:utf-8 -*-
from manimlib import *
import numpy as np


class appendix(Scene):
    def construct(self):
        quote = Text("""All models are wrong, but some are useful.""", t2c={'wrong': RED_C, 'useful' : GREEN_B}, font="Consolas").move_to(LEFT*1+UP*2.1)
        writer = Text("-George E. P. Box", font="Consolas").set_color(YELLOW).move_to(UP*1.4+2.5*RIGHT)
        quote_CN = Text("""所有模型都是错误的, 但它们中的某些是有用的.""", font = "微软雅黑", t2c={'错误': RED_C, '有用' : GREEN_B}).move_to(LEFT*1.6+DOWN*0.4)
        writer_CN = Text("——乔治·博克斯", font = "微软雅黑").set_color(YELLOW).move_to(DOWN+2.5*RIGHT+DOWN*0.4)
        self.play(ShowCreation(quote),ShowCreation(quote_CN), run_time = 2.5)
        self.play(ShowCreation(writer),ShowCreation(writer_CN),  run_time = 2.5)
        self.wait()
        self.play(FadeOut(quote), FadeOut(quote_CN), FadeOut(writer), FadeOut(writer_CN))
        pass



class introduction(Scene):
    def getmin(self, o, a, b, s, res):
        oa = a.get_center() - o.get_center()
        ab = b.get_center() - a.get_center()
        bs = s.get_center() - b.get_center()
        res.append(min(oa[0], ab[0], bs[0]))


    def construct(self):
        stick = Rectangle(0.1,3.5).set_fill(WHITE, 1).shift(1*UP+0.5*UP)
        stick.generate_target()
        sticks = VGroup()
        sticks.add(Rectangle(0.1,0.98).set_fill(WHITE, 1).rotate(PI/2))
        sticks.add(Rectangle(0.1,0.595).set_fill(WHITE, 1).rotate(PI/2))
        sticks.add(Rectangle(0.1,1.925).set_fill(WHITE, 1).rotate(PI/2))
        sticks.arrange(RIGHT)
        sticks.shift(1.5*DOWN+LEFT*3.8)
        self.play(stick.animate.rotate(PI/2).shift(3.5*DOWN+LEFT*3.8+0.5*UP))
        self.play(Transform(stick, sticks))
        brace = BraceLabel(sticks[1],"X" ,brace_direction=UP)
        brace[1].set_color(GREEN_D)
        self.play(ShowCreation(brace))
        self.play(CircleIndicate(brace[1]))
        self.wait()
        question = Tex("E","(","X", ")", "=").set_color_by_tex("X" , GREEN_D)
        questionsignal = Text("？", font="微软雅黑")
        expectation = VGroup(question, questionsignal).arrange(RIGHT).shift(4*LEFT+0.5*UP)
        #speech = SpeechBubble()
        hightlight = Rectangle(expectation.get_width()+0.4, expectation.get_height()+0.4).set_backstroke(BLUE_E).move_to(expectation)        
        self.play(TransformMatchingParts(brace, expectation), FadeIn(hightlight))
        self.add(brace)
        self.wait(3)

        physics = Text("Physics perspective...Complex", t2c = {'Complex' : RED_E}, font="Consolas").shift(2*RIGHT+0.5*UP)
        maths = Text("Probabilistic perspective...Clear", t2c = {'Clear' : GREEN_E}, font="Consolas").shift(2.2*RIGHT+0.5*UP)
        maths.generate_target()
        maths.target.shift(1*UP)
        self.play(ShowCreation(physics), run_time = 3)
        self.wait()
        self.play(TransformMatchingShapes(physics, maths), run_time = 2)
        self.wait(2)
        line = Line(ORIGIN+2*LEFT, ORIGIN+6*RIGHT).shift(0.5*DOWN)
        start = Dot(ORIGIN+2*LEFT+0.5*DOWN, radius = 0.05)
        end = Dot(ORIGIN+6*RIGHT+0.5*DOWN, radius = 0.05)
        pointO = Tex("O").set_color(TEAL_E).move_to(start).shift(0.5*UP)
        pointM = Tex("M").set_color(TEAL_E).move_to(end).shift(0.5*UP)
        segment = VGroup(line, start, end, pointO, pointM)
        self.play(MoveToTarget(maths),FadeOut(brace), FadeOut(stick), ShowCreation(segment))
        dotR = Dot(ORIGIN+4*RIGHT+0.5*DOWN, radius = 0.05).set_color(YELLOW_D)
        pointR = Tex("R").set_color(YELLOW_D).move_to(dotR).shift(0.5*UP)
        dotS = Dot(ORIGIN+1*LEFT+0.5*DOWN, radius = 0.05).set_color(YELLOW_D)
        pointS = Tex("S").set_color(YELLOW_D).move_to(dotS).shift(0.5*UP)
        R = VGroup(dotR, pointR)
        S = VGroup(dotS, pointS)

        distance = VGroup(Tex("X", "=", "min(OS,SR,RM)", "=").set_color_by_tex("X", GREEN_D)
            ,DecimalNumber(0.0, num_decimal_places = 2, font="monospace").set_color(YELLOW_D)).arrange(RIGHT)
        distance[1].add_updater(
            lambda diff:diff.set_value(min((dotS.get_center() - start.get_center())[0], 
                                           (dotR.get_center() - dotS.get_center())[0],
                                           (end.get_center() - dotR.get_center())[0]) / 8)
        )
        distance.shift(2*RIGHT + 0.5 * UP)
        self.play(ShowCreation(distance))

        self.play(R.animate.shift(1.32*RIGHT), S.animate.shift(0.44*LEFT), run_time = 1.7)
        self.play(R.animate.shift(3*LEFT), S.animate.shift(2*RIGHT), run_time = 1.7)
        self.play(R.animate.shift(3.55*RIGHT), S.animate.shift(1.33*LEFT), run_time = 1.7)
        self.play(R.animate.shift(4*LEFT), S.animate.shift(2.31*RIGHT), run_time = 1.7)
        
        self.wait(5)


        