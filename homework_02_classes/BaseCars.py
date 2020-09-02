class BaseCars:
    SOUND = 'beep'
    WHEELS = 4

    def honk_the_horn(self):
        return self.SOUND

    def __str__(self):
        return self.honk_the_horn()
