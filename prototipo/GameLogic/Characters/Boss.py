from GameLogic.Characters.Character import Character
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon

class Boss(Character):
    def __init__(self, name: str, sprites: list, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill, surface):
        super().__init__(name, sprites, health, max_health, 
                        x_position, y_position, hitbox_x, 
                        hitbox_y, speed, jump_height, 
                        skill)
        self.__counter = 0
        self.__run_skill = True
        self.window = surface
        
    @property
    def counter(self):
        return self.__counter
    
    @counter.setter
    def counter(self, counter):
        self.__counter = counter

    @property
    def run_skill(self):
        return self.__run_skill

    @run_skill.setter
    def run_skill(self, run_skill):
        self.__run_skill = run_skill
    
    def move(self):
        distance = 400

        if self.health > 0:
            if self.counter >= 0 and self.counter <= distance:
                self.x_position += self.speed
            elif self.counter >= distance and self.counter <= distance*2:
                self.x_position -= self.speed
            else:
                self.counter = 0
            
            self.draw()

        self.counter += 1

    def attacked(self, damage):
        self.health -= damage
    
    def attack(self, collision, target, hit_target, clock):
        if self.health > 0:
            if self.run_skill and clock % (60 * 4):
                self.skill.draw()
                self.skill.move(target)

                if hit_target:
                    self.skill_attack(target)
                    self.run_skill = False
                
                if collision:
                    self.run_skill = False
            else:
                self.skill_reset()

                if clock % (60) == 0:
                    self.run_skill = True
                    return 0
        
        return clock

    def skill_reset(self):
        self.skill.reset(self.x_position, self.y_position + self.hitbox_y)

    def draw(self):
        if self.health > 0:
            self.window.draw_scaled_image("prototipo\Images\pygame_boss.png", 
                        self.hitbox_x, self.hitbox_y, 
                        self.x_position, self.y_position)
