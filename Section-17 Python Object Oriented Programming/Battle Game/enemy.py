class Enemey:
    def __init__(self, health_point, magical_point) -> None:
        self.max_hp = health_point;
        self.health_point = health_point;
        self.max_mp = magical_point;
        self.mp = magical_point;
        
    def get_hp(self):
        return self.hp
        