class Build:
    """
    The class `Build` will be an object that takes in the elements:
    1. Level
    2. Ascendancy
    3. DPS
    4. Skill(s)
    5. Keystone(s)
    6. Life
    7. Energy Shield (ES)
    The Class will be mapped from the given ascendancy since the website does not directly provide the class, only the ascendancy.
    """
    class_asc = { # Class Ascendancies Mapping
        'Ranger': ['Deadeye', 'Pathfinder', 'Raider'],
        'Duelist': ['Slayer', 'Gladiator', 'Champion'],
        'Shadow': ['Assassin', 'Trickster', 'Saboteur'],
        'Marauder': ['Chieftain', 'Berserker', 'Juggernaut'],
        'Witch': ['Elementalist', 'Occultist', 'Necromancer'],
        'Templar': ['Inquisitor', 'Hierophant', 'Guardian'],
        'Scion': ['Ascendant']    
    }
    
    # Inverse mapping for each ascendancies in class_asc to fetch the class
    class_asc_inverse = {asc: cls_ for cls_, ascs in class_asc.items() for asc in ascs}
    
    def __init__(self, level: int, asc: str, dps: str, skill: str, keystone: str, life: int, es: int):
        self.level = level # Level
        self.cls = self.class_asc_inverse.get(asc, 'Not found') # Class
        self.asc = asc # Ascendancy
        self.dps = dps # Damage per Second
        self.skill = skill # Skill(s), encase in [] when using multiple skills
        self.keystone = keystone # Keystone(s), encase in [] when you have multiple keystones
        self.life = life # HP
        self.es = es # Energy shield
        
    def __str__(self):
        return f'Level {self.level} {self.cls} - {self.asc} \n\
    Skill: {self.skill},\n\
    Keystones: {self.keystone}, \n\
    does {self.dps} damage per second.'