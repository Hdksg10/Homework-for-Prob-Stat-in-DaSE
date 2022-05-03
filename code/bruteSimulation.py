# -*- encoding:utf-8 -*-

import sys
sys.path.append("C:/Users/Rhywu/manimproject/code/shaders")

from manimlib import *
from simulator import Simulator
import numpy as np


class Simulation(Scene):
    def construct(self):
        question = Tex("E","(","X", ")", "=").set_color_by_tex("X" , GREEN_D)
        questionsignal = Text("？", font="微软雅黑")
        expectation = VGroup(question, questionsignal).arrange(RIGHT).shift(4*LEFT+0.5*UP)
        #speech = SpeechBubble()
        hightlight = Rectangle(expectation.get_width()+0.4, expectation.get_height()+0.4).set_backstroke(BLUE_E).move_to(expectation)
        self.add(expectation, hightlight)        
        expec_demicial = 0.0
        expec_tex = Tex("E(", "X", ")", "=").set_color_by_tex("X",GREEN_B).shift(LEFT*6 + UP*2.5)
        expec_value = DecimalNumber(text_config={"font": "monospace"}).set_color(YELLOW_C).shift(LEFT*4.7 + UP*2.5)
        #expectation = VGroup(expec_tex, expec_value).arrange(RIGHT).shift(LEFT*5 + UP*3.5)
        #self.add(expec_tex, expec_value)
        self.play(FadeOut(hightlight),ReplacementTransform(question, expec_tex), ReplacementTransform(questionsignal, expec_value))
        simulatorr = Simulator()
        case = simulatorr.getMin()
        x = DecimalNumber(case[1], text_config={"font": "monospace"}).scale(0.75)
        min = DecimalNumber(case[0], text_config={"font": "monospace"}).scale(0.75)
        y = DecimalNumber(case[0], text_config={"font": "monospace"}).scale(0.75)
        z = DecimalNumber(case[2], text_config={"font": "monospace"}).scale(0.75)
        lengths =  VGroup(x,y,z)
        lengths.arrange(RIGHT)
        lengths.shift(LEFT * 5 + UP)
        min.shift(UP*0.6 + LEFT * 5 + UP)
        self.play(
            *[CountInFrom(cord, 0)for cord in lengths], run_time = 0.5
        )
        self.add(lengths)
        expec_demicial = min.get_value()
        self.play(TransformFromCopy(lengths, min))
        self.play(ChangeDecimalToValue(expec_value, expec_demicial), runtime = 0.2)
        # self.play(
        #     *[FadeOut(cord)for cord in lengths], runtime = 0.1
        # )
        self.play(ShowPassingFlashAround(expec_value), *[FadeOut(cord)for cord in lengths], runtime = 1)
        self.wait()
        trails =  VGroup()
        for offset in range(1, 10):
            temp = simulatorr.getMin()
            expec_demicial = expec_demicial + temp[0]
            tempMin = DecimalNumber(temp[0], text_config={"font": "monospace"}).shift(UP*0.6 + LEFT * 5 + RIGHT * offset + UP).scale(0.75)
            trails.add(tempMin)
            pass
        expec_demicial = expec_demicial / 10
        self.play(
            *[CountInFrom(res, 0)for res in trails],
            ChangeDecimalToValue(expec_value, expec_demicial), runtime = 0.02
        )
        self.add(trails)
        trailsList = VGroup()
        trails.add(min)
        trailsList.add(trails)
        for frequency in range(0, 8):
            tempTrails = VGroup()
            temp_expec = 0.0
            for offset in range(0, 10):
                temp = simulatorr.getMin()
                temp_expec = temp_expec + temp[0]
                tempMin = DecimalNumber(temp[0], text_config={"font": "monospace"}).shift(UP*0.6 + LEFT * 5 + RIGHT * offset + UP).scale(0.75)
                tempTrails.add(tempMin)
            temp_expec = temp_expec / 10
            expec_demicial = (expec_demicial + temp_expec)/2
            tempTrails.shift(DOWN*(frequency + 1)*0.5)
            if frequency < 10:
                self.play(
                    *[FadeInFromPoint(mob, DOWN*5+mob.get_center())for mob in tempTrails],
                    ChangeDecimalToValue(expec_value, expec_demicial),
                    runtime = 0.05*(10-frequency)
                )
            trailsList.add(tempTrails)
            # else:
            #     self.add(tempTrails)
            #     self.play(
            #         #*[FadeInFromPoint(mob, DOWN*5+mob.get_center())for mob in tempTrails],
            #         ChangeDecimalToValue(expec_value, expec_demicial)
            #     )
        self.wait()
        expec_value.set_value(expec_demicial)
        expectation = VGroup(expec_tex, expec_value)
        expectation.generate_target()
        expectation.target.scale(2.5).move_to(ORIGIN + LEFT)
        self.play(
            *[FadeOut(mob)for mob in trailsList],
            runtime = 0.1
        )
        self.play(MoveToTarget(expectation))
        mathresult = Tex("\\approx","\\frac{1}{9}").set_color_by_tex("\\frac{1}{9}", BLUE_C).shift(3.6*RIGHT).scale(3)
        self.play(FadeIn(mathresult))
        self.add(mathresult)
        self.wait()
        pass