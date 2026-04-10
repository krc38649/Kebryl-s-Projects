### classes for RunSim
class Player:
    def __init__(self, name, age,):
        self.name = name
        self.age = age
        self.week = 1
        self.money = 100
        self.fitness = 50
        self.health = 100
        self.experience = 0
        self.stamina = 50
        self.hills = 0
        self.weekly_mileage = 0
        self.schedule = {}

player = Player("Runner", 16) #default player, will be changed when the user creates their own

class Competitor:
    def __init__(self, name, fitness, health, experience, stamina, hills):
        self.name = name
        self.fitness = fitness
        self.health = health
        self.experience = experience
        self.stamina = stamina
        self.hills = hills

class Course:
    def __init__(self, name, distance, terrain, difficulty):
        self.name = name
        self.distance = distance
        self.terrain = terrain
        self.difficulty = difficulty
        self.postseason = False

class PostseasonCourse(Course):
    def __init__(self, name, distance, terrain, difficulty, event_name):
        super().__init__(name, distance, terrain, difficulty)
        self.postseason = True
        self.event_name = event_name
        self.qualification_cutoff = 5 if event_name == "Districts" else 3 if event_name == "Regions" else None

class Shoe:
    def __init__(self, name, cost, fitness_boost, health_boost, stamina_boost):
        self.name = name
        self.cost = cost
        self.fitness_boost = fitness_boost
        self.health_boost = health_boost
        self.stamina_boost = stamina_boost

class TrainingPlan:
    def __init__(self, name, cost, fitness_increase, health_increase, stamina_increase):
        self.name = name
        self.cost = cost
        self.fitness_increase = fitness_increase
        self.health_increase = health_increase
        self.stamina_increase = stamina_increase

class Upgrade:
    def __init__(self, name, cost, fitness_boost, health_boost, stamina_boost):
        self.name = name
        self.cost = cost
        self.fitness_boost = fitness_boost
        self.health_boost = health_boost
        self.stamina_boost = stamina_boost

class RaceResult:
    def __init__(self, course_name, position, finishing_time, exp_gained):
        self.course_name = course_name
        self.position = position
        self.finishing_time = finishing_time
        self.exp_gained = exp_gained
