class Player:

    active_players = 0

    @classmethod  # decorator
    def display_active_players(cls):
        return f"There are currently {cls.active_players} active players"

    # @classmethod
    # def from_string(cls, data_str):
    #     f_name, l_name, state, rocket = data_str.split(",")
    #     return cls(f_name, l_name, state, rocket)

    def __init__(self, f_name,l_name,state):
        self.f_name = f_name
        self.l_name = l_name
        self.state = state
        self._lives = 3
        self._level = 1
        self._score = 0
        Player.active_players += 1

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    # @score.setter
    # def score(self, score):
    #     self._score = score

    def __repr__(self):
        return "Name: {0.f_name} {0.l_name},\n State: {0.state},\n Lives: {0.lives},\n Level: {0.level},\n Score {0.score}".format(self)


class Super_player(Player):
    active_players = 0
    @classmethod
    def from_string(cls, data_str):
        f_name, l_name, state, rocket = data_str.split(",")
        return cls(f_name, l_name, state, rocket)

    def __init__(self, f_name,l_name, state, weapon):
        super().__init__(f_name, l_name, state)
        self.weapon = weapon
        Super_player.active_players += 1


jon = Super_player("jon", "lenon","USA", "gun")
jon = Player("morty", "sanchez","israel")
rick = Super_player.from_string("Rick, sanchez, USA, rocket")
print(jon)
print(rick)
print(Player.active_players)
print(Super_player.active_players)