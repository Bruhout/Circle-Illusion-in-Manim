from manim import *

class scene(Scene):
    def construct(self):
        theta=ValueTracker(0)
        cir=Circle(radius=3.5,color=WHITE)

        dots=VGroup()

        def give_path(x):
            return[
                3.5*np.cos(theta.get_value()+x)*np.cos(x),
                3.5*np.cos(theta.get_value()+x)*np.sin(x),
                0
            ]
        phi=0
        while phi<PI:
            self.add(Line([3.5*np.cos(phi),3.5*np.sin(phi),0],[-3.5*np.cos(phi),-3.5*np.sin(phi),0],color=BLUE))
            phi+=PI/8
            

        hmm=0
        while hmm<PI:
            dot=Dot()
            dot.add_updater(lambda mob, x=hmm:mob.move_to(give_path(x)))
            dots.add(dot)
            hmm+=PI/8

        self.add(cir,dots)
        self.play(theta.animate(rate_func=linear).set_value(2*PI),run_time=5)
        