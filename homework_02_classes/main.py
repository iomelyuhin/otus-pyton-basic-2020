from ferrari import Ferrari


class BaseCars:
    SOUND = 'beep'
    WHEELS = 4

    def honk_the_horn(self):
        return self.SOUND


f = Ferrari(BaseCars)
#
f.__init__(fuel=40)
f.go(3)
f.add_fuel(20)
f.go(3)
