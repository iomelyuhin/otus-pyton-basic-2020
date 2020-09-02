class BaseCars:
    SOUND = 'Бибииип'
    WHEELS = 4

    def honk_the_horn(self):
        return self.SOUND

    def __str__(self):
        return self.honk_the_horn()
