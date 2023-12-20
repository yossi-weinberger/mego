class Player:
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    def get_name(self):
        return self.name

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        self._lives = lives

    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return "name: {0.name}, lives: {0._lives}, level: {0.level}, score: {0.score}".format(self)