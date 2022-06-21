class Biodiversty:

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def name(self):
        print("DIFFRENT LIVING ORGANISMS HAVE DIFFRENT NAMES")

    def nutrition_mood(self):
        print("DIFFRENT LIVIG_ORGANISMS IN THE FIVE KINGDOM SYSTEM HAVE DIFFRENT NUTRITION MOODS")

    def kingdom(self):
        print("ALL KIND OF LIVING ORGANISMS HAVE DIFFRENT KINGDOMS ACCORDING TO THEIR CELL TYPE")

    def cell_type(self):
        print("DIFFRENT ORGANISMS HAVE DIFFRENT CELL TYPE ")

    def average_age(self):
        print("DIFFRENT LIVING ORGANISMS HAVE DIFFRENT AGE")

    def size(self):
        print("DIFFRENT LIVING ORGANISMS HAVE DIFFRENT SIZE")

    def nails(self):
        print("DIFFRENT LIVING ORGANISMS HAVE DIFFRENT number of nails")
    def legs(self):
        print("DIFFRENT LIVING ORGANISMS HAVE DIFFRENT number of legs")


class Lion(Biodiversty):

    def name(self):
        print("Lion")

    def nutrition_mood(self):
        print("hetrotropic")

    def kingdom(self):
        print("Kingdom Animalia")

    def cell_type(self):
        print("multicellular eukaryotic")

    def average_age(self):
        print(8,"to",10,"years")

    def size(self):
        print(1.2,"m")

    def nails(self):
        print(18,"nails")

    def legs(self):
        print(4,"legs")


class Rose(Biodiversty):

    def name(self):
        print("Rose")

    def nutrition_mood(self):
        print("autotropic")

    def kingdom(self):
        print("Kingdom Plantae")

    def cell_type(self):
        print("multicellular eukaryotic")

    def average_age(self):
        print(6, "to", 100, "years")

    def size(self):
        print(17.5, "cm")

    def nails(self):
        print("Don't have nails")

    def legs(self):
        print("Don't have legs")

obj_bio = Biodiversty()
obj_anim = Lion()
obj_plan = Rose()

obj_bio.name()
obj_bio.kingdom()
obj_bio.cell_type()
obj_bio.average_age()
obj_bio.nutrition_mood()
obj_bio.size()
obj_bio.nails()
obj_bio.legs()



obj_anim.name()
obj_anim.kingdom()
obj_anim.cell_type()
obj_anim.average_age()
obj_anim.nutrition_mood()
obj_anim.size()
obj_anim.nails()
obj_anim.legs()
obj_anim.set_color("BROWN")
print(obj_anim.get_color())


obj_plan.name()
obj_plan.kingdom()
obj_plan.cell_type()
obj_plan.average_age()
obj_plan.nutrition_mood()
obj_plan.size()
obj_plan.nails()
obj_plan.legs()
obj_plan.set_color("RED")
print(obj_anim.get_color())












