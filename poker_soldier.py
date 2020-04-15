from shapepainter import *


class PokerSoldier:

    def __init__(self, canvas):
        self.__canvas = canvas
        self.__build_card_body()
        self.__build_card_type()
        self.__build_card_number()
        self.__build_card_collar()
        self.__build_head()
        self.__build_face()
        self.__build_weapon()
        self.__build_arm()
        self.__build_leg()
        self.__is_fill = False

    def __build_card_body(self):
        r0 = Rectangle(Point(215, 280), 230, 350)
        r0.transform(Point(1, 0), Point(0.08, 0.9))
        r1 = Rectangle(Point(200, 300), 230, 350)
        s1 = ShapePainter(self.__canvas, [r0, r1])
        self.__card_body = {"c": s1}

    def __build_card_type(self):
        rr = []
        ra = Rectangle(Point(150, 200), 20, 20).clone()
        ra.transform(Point(-1, 2), Point(1, 2))
        for i in range(8):
            rr.append(ra.clone())
        rr[1].move_y(100)
        rr[2].move_y(200)
        rr[3].move_x(100)
        rr[4].move(100, 100)
        rr[5].move(100, 200)
        rr[6].move(50, 50)
        rr[7].move(50, 150)
        s2 = ShapePainter(self.__canvas, rr)
        self.__card_type = {"c": s2}

    def __build_card_number(self):
        rb = Rectangle(Point(100, 180), 5, 5).clone()
        rb.transform(Point(-1, 2), Point(1, 2))
        rc = rb.clone()
        rc.move(200, 240)
        s3 = ShapePainter(self.__canvas, [rb, rc])
        o8u1 = Oval(Point(100, 150), 10, 10)
        o8d1 = Oval(Point(100, 160), 12, 12)
        o8u2 = o8u1.clone()
        o8u2.move(200, 301)
        o8d2 = o8d1.clone()
        o8d2.move(200, 280)
        s4 = ShapePainter(self.__canvas, [o8u1, o8d1, o8u2, o8d2], "red")
        self.__card_number = {"type": s3, "number": s4}

    def __build_card_collar(self, is_fill=False):
        r = 115 / math.cos(math.pi / 4)
        o1 = Oval(Point(142.5, 67.5), r, r)
        o2 = Oval(Point(257.5, 67.5), r, r)
        s5 = ShapePainter(self.__canvas, [o1, o2])
        if is_fill:
            s5.fill("red")
        r2 = Rectangle(Point(200, 0), 280, 250)
        s6 = ShapePainter(self.__canvas, r2, "white")
        self.__card_collar = {"collar": s5, "blank": s6}

    def __build_head(self, is_fill=False):
        r3 = Rectangle(Point(200, 100), 40, 40)
        r3.transform(Point(math.sqrt(2), 1.8), Point(-math.sqrt(2), 1.8))
        s7 = ShapePainter(self.__canvas, r3)
        if is_fill:
            s7.fill("red")
        t1 = Triangle(Point(200, 90), 80)
        t1.transform(Point(1, 0), Point(0, -1))
        s8 = ShapePainter(self.__canvas, t1)
        self.__head = {"hair": s7, "face": s8}

    def __build_eye(self):
        o3 = Oval(Point(190, 80), 14, 7)
        o4 = Oval(Point(190, 80), 6, 6)
        o5 = Oval(Point(210, 80), 14, 7)
        o6 = Oval(Point(210, 80), 6, 6)
        s11 = ShapePainter(self.__canvas, [o3, o5])
        s12 = ShapePainter(self.__canvas, [o4, o6])
        s12.fill("black")
        return {"border": s11, "eye": s12}

    def __build_face(self, is_fill=False):
        eye = self.__build_eye()
        t2 = Triangle(Point(200, 100), 15)
        t2.transform(Point(2, 0), Point(0, -0.5))
        s13 = ShapePainter(self.__canvas, t2)
        t3 = Triangle(Point(200, 105), 10)
        t3.transform(Point(1.2, 0), Point(0, 0.6))
        s14 = ShapePainter(self.__canvas, t3)
        if is_fill:
            s14.fill("red")
        self.__face = {"eye": eye, "beard": s13, "mouse": s14}

    def __build_weapon(self):
        r4 = Rectangle(Point(400, 300), 5, 200)
        r4.transform(Point(1, 0), Point(-0.05, 2))
        o7 = Oval(Point(406, 100), 10, 10)
        t4 = Triangle(Point(408, 72), 80)
        t4.transform(Point(0.3, 0), Point(0.05, -1))
        s15 = ShapePainter(self.__canvas, r4)
        s15.fill("black")
        s17 = ShapePainter(self.__canvas, t4)
        s16 = ShapePainter(self.__canvas, o7)
        self.__weapon = {"body": s15, "circle": s16, "head": s17}

    def __build_arm(self):
        r5 = Rectangle(Point(355, 300), 200, 5)
        r5.transform(Point(0.4, 1), Point(0, 1))
        r6 = Rectangle(Point(45, 300), 200, 5)
        r6.transform(Point(-0.4, 1), Point(0, 1))
        s18 = ShapePainter(self.__canvas, [r5, r6])
        s18.fill("black")
        o8 = Oval(Point(395, 402.5), 30, 20)
        o9 = Oval(Point(5, 402.5), 30, 20)
        s19 = ShapePainter(self.__canvas, [o8, o9])
        self.__arm = {"arm": s18, "hand": s19}

    def __build_leg(self):
        r7 = Rectangle(Point(143, 538), 10, 126)
        r8 = r7.clone()
        r8.move_x(115)
        s20 = ShapePainter(self.__canvas, [r7, r8])
        s20.fill("black")
        self.__leg = {"c": s20}

    def __drop(self, part):
        for ps in part.values():
            if type(ps) == dict:
                for pss in ps.values():
                    pss.drop
                continue
            ps.drop()
        part.clear()

    def __drop_card_body(self):
        self.__drop(self.__card_body)

    def __drop_card_type(self):
        self.__drop(self.__card_type)

    def __drop_card_number(self):
        self.__drop(self.__card_number)

    def __drop_card_collar(self):
        self.__drop(self.__card_collar)

    def __drop_head(self):
        self.__drop(self.__head)

    def __drop_face(self):
        self.__drop(self.__face)

    def __drop_weapon(self):
        self.__drop(self.__weapon)

    def __drop_arm(self):
        self.__drop(self.__arm)

    def __drop_leg(self):
        self.__drop(self.__leg)

    def __drop_eye(self):
        self.__drop(self.__face["eye"])

    def __build_jump_weapon(self):
        r4 = Rectangle(Point(400, 100), 5, 200)
        r4.transform(Point(1, 0), Point(-0.05, 2))
        s15 = ShapePainter(self.__canvas, r4)
        s15.fill("black")
        s16 = ShapePainter(self.__canvas, Rectangle(Point(-100, -100), 0, 0))
        self.__weapon = {"body": s15, "head": s16}

    def __build_jump_arm(self):
        r5 = Rectangle(Point(355, 100), 200, 5)
        r5.transform(Point(-0.4, 1), Point(0, 1))
        r6 = Rectangle(Point(45, 100), 200, 5)
        r6.transform(Point(0.4, 1), Point(0, 1))
        s18 = ShapePainter(self.__canvas, [r5, r6])
        s18.fill("black")
        self.__arm = {"arm": s18}

    def __build_jump_leg(self):
        r7 = Rectangle(Point(103, 538), 10, 126)
        r7.transform(Point(1, 0), Point(-0.4, 1))
        r8 = Rectangle(Point(298, 538), 10, 126)
        r8.transform(Point(1, 0), Point(0.4, 1))
        s20 = ShapePainter(self.__canvas, [r7, r8])
        s20.fill("black")
        self.__leg = {"c": s20}

    def fill(self):
        self.__card_type["c"].fill("red")
        self.__card_number["type"].fill("red")
        self.__weapon["head"].fill("red")
        self.__drop_card_collar()
        self.__build_card_collar(True)
        self.__drop_head()
        self.__build_head(True)
        self.__drop_face()
        self.__build_face(True)
        self.__is_fill = True

    def jump(self):
        self.__drop_arm()
        self.__drop_leg()
        self.__drop_weapon()
        self.__build_jump_weapon()
        self.__build_jump_arm()
        self.__build_jump_leg()
        self.__canvas.after(1000, self.__jump_down)

    def __jump_down(self):
        self.__drop_arm()
        self.__drop_leg()
        self.__drop_weapon()
        self.__build_weapon()
        self.__build_arm()
        self.__build_leg()
        if self.__is_fill:
            self.fill()

    def blink(self):
        self.__drop_eye()
        r0 = Rectangle(Point(190, 80), 14, 2)
        r1 = Rectangle(Point(210, 80), 14, 2)
        s12 = ShapePainter(self.__canvas, [r0, r1])
        s12.fill("black")
        self.__face["eye"] = {"eye": s12}
        self.__canvas.after(100, self.__blink_up)

    def __blink_up(self):
        self.__drop_eye()
        self.__face["eye"] = self.__build_eye()

