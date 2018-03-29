"""
TO-DO: 
Things to ask Alan:
- Implement __str__ representations of the models
- Have Alan change the help text for stuff as appropriate
"""

from django.db import models

# Create your models here.

    
class Character(models.Model):
    name = models.CharField( default = '', max_length = 30, help_text = "Enter a name for your character")
    level = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the level your character")
    race = models.ForeignKey('Race', on_delete=models.SET_NULL, null = True)
    subrace = models.ForeignKey('Subrace', on_delete=models.SET_NULL, null = True)
    character_class = models.ForeignKey('CharacterClass', on_delete=models.SET_NULL, null = True)

    armor_class = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the armor class for your character")
    initiative = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the armor class for your character")
    speed = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the speed for your character")
    max_hit = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the max hitpoints for your character")
    temp_hit = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the temporary hitpoints for your character")
    profeciencies = models.CharField( default = '', max_length = 30, help_text = "Enter the list of proficiencies for this character in JSON format.")  


    strength = models.SmallIntegerField(default= 0, help_text="Enter the strength state for your character.")
    dexterity = models.SmallIntegerField(default= 0, help_text="Enter the dexterity state for your character.")
    constitution = models.SmallIntegerField(default= 0, help_text="Enter the constitution state for your character.")
    intelligence = models.SmallIntegerField(default= 0, help_text="Enter the intelligence state for your character.")
    wisdowm = models.SmallIntegerField(default= 0, help_text="Enter the wisdowm state for your character.")
    charisma = models.SmallIntegerField(default= 0, help_text="Enter the charisma state for your character.")

    weapon = models.ForeignKey('Weapon', on_delete=models.SET_NULL, null = True)

    gold = models.IntegerField(default=0, help_text="Enter the gold of the character")
    silver = models.IntegerField(default=0, help_text="Enter the gold of the character")
    copper = models.IntegerField(default=0, help_text="Enter the gold of the character")
    
    # In tuple: First field is the value that gets saved in the database, Second is the one the human sees
    ALIGNMENT_CHOICES = (
        ('LG', 'Lawful Good'),
        ('NG', 'Neutral Good'),
        ('CG', 'Chaotic Good'),

        ('LN', 'Lawful Neutral'),
        ('NN', 'True Neutral'),
        ('CN', 'Chaotic Neutral'),

        ('LE', 'Lawful Evil'),
        ('NE', 'True Neutral'),
        ('CE', 'Chaotic Evil')
    )


    alignment = models.CharField(max_length = 2, choices = ALIGNMENT_CHOICES, default = 'NN')

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this race")
    description = models.CharField(default = '', max_length = 5000, help_text = "Enter a description of this race (backstory, beliefs, etc.)")
    speed = models.SmallIntegerField(default=0, help_text="Enter the speed for this race")
    # Only applied once at character creation, will use a JS parser (or something) to parse the raw string (format of string is JSON) 
    # object and apply the mods to the characters stats
    modifiers = models.CharField(default = '', max_length = 20, help_text = "Enter the stats modifiers in JSON format. Ex: {\"str\": 2, \"dex\": 8}")


    def __str__(self):
        return self.name

class RaceFeatures(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this race feature")
    race = models.ForeignKey('Race', on_delete=models.CASCADE, null = True)
    description = models.CharField(default= '', max_length = 5000, help_text = "Enter a description of this feature; i.e. what this feature does")
    required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this feature")

class Subrace(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the subrace")
    parent_race = models.ForeignKey('Race', on_delete=models.CASCADE, null = True)
    description = models.CharField(default= '', max_length = 5000, help_text = "Enter a description of this sub-race (backstory, beliefs, etc.)")

    def __str__(self):
        return self.name


class SubraceFeatures(models.Model):
    subrace = models.ForeignKey('Subrace', on_delete=models.CASCADE, null = True)
    required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this feature")
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this feature")
    models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the subrace")
    description = models.CharField(default= '', max_length = 5000, help_text = "Enter a description for these features")

class CharacterClass(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this class")
    descrtiption = models.CharField(default = '', max_length = 1000, help_text = "Enter a description of this class")
    hitpoints = models.PositiveIntegerField(default = 10, help_text = "Enter the hit points for this character")
    skill_proficiency_limit = models.PositiveSmallIntegerField(default = 5, help_text = "Enter the max amount of skills this class can be proficient in")


    def __str__(self):
        return self.name

class CharacterClassSpellList(models.Model):
    character_class = models.ForeignKey('CharacterClass', on_delete=models.CASCADE, null = True)
    required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this spell")
    ranking = models.SmallIntegerField(default= 0, null=True, help_text="Enter the ranking of this spell relative to the other spells available for this class.")

class CharacterClassFeatures(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this class feature")
    character_class = models.ForeignKey('CharacterClass', on_delete=models.CASCADE, null = True)
    description = models.CharField(default= '', max_length = 5000, help_text = "Enter a description of this feature; i.e. what this feature does")
    required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this feature")

class CharacterSubclass(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this Subclass")
    descrtiption = models.CharField(default = '', max_length = 1000, help_text = "Enter a description of this Subclass")
    parent_class = models.ForeignKey('CharacterClass', on_delete=models.CASCADE, null=True)
    required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this Subclass")
    ranking = models.SmallIntegerField(default= 0, null=True, help_text="Enter the ranking of this subclass relative to the other subclasses available for this class.")


class CharacterSubclassSpellList(models.Model):
    subclass = models.ForeignKey('CharacterSubclass', on_delete=models.CASCADE, null = True)
    required_level = required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this spell")
    ranking = models.SmallIntegerField(default= 0, null=True, help_text="Enter the ranking of this spell relative to the other spells available for this class.")


class Spells(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the spell")
    # Saved as an int, but should be interpreted as number of seconds
    cast_time = models.PositiveIntegerField(default = 6, help_text = "Enter the amount of seconds it takes the spell to cast. If a spell takes 1 turn, enter in the value: TBD.")
    # Amount of hit point damage it does. If it is a healing spell, enter the amount of hit points it heals.
    damage = models.PositiveIntegerField(default=1, help_text="The base hit point damage of the spell. If this is a healing spell, enter in the amount of hit points it heals for")
    # Saved as an int, but should be interpreted as number of feet
    range = models.PositiveIntegerField(default = 10, help_text = "Enter the range of the spell in feet. If the range is infinite, enter the value: TBD")
    #Units: feet
    area_effected = models.PositiveIntegerField(default = 1, help_text = "Enter the area affected by the spell after it connects (in feet).")
    required_materials = models.CharField(default = "", max_length = 10000, help_text = "Enter the required materials to cast this spell in JSON format.")
    component_1 = models.CharField(default = "", max_length = 10000, help_text = "Enter the first component to cast this spell in JSON format.")
    component_2 = models.CharField(default = "", max_length = 10000, help_text = "Enter the second component to cast this spell in JSON format.")
   
    SCHOOL_CHOICES = (
        ('ab', 'Abjuration'),
        ('co', 'Conjuration'),
        ('di', 'Divination'),
        ('en', 'Enchantment'),
        ('ev', 'Evocation'),
        ('il', 'Illusion'),
        ('ne', 'Necromancy'),
        ('tr', 'Transmutation'),
        ('un', 'Universal')
    )

    school = models.CharField(max_length = 2, choices = SCHOOL_CHOICES, default = 'ab')

class FeatRanking(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the feat ranking")
    required_level = required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this spell")
    ranking = models.SmallIntegerField(default= 0, help_text="Enter the ranking of this feature relative to the other features available for this class.")

class Feat(models.Model):
    descrtiption = models.CharField(default = '', max_length = 1000, help_text = "Enter a description of this feat.")

    strength = models.SmallIntegerField(default= 0, help_text="Enter the modification to the strength stat.")
    dexterity = models.SmallIntegerField(default= 0, help_text="Enter the modification to the dexterity stat.")
    constitution = models.SmallIntegerField(default= 0, help_text="Enter the modification to the constitution stat.")
    intelligence = models.SmallIntegerField(default= 0, help_text="Enter the modification to the intelligence stat.")
    wisdowm = models.SmallIntegerField(default= 0, help_text="Enter the modification to the wisdom stat.")
    charisma = models.SmallIntegerField(default= 0, help_text="Enter the modification to the charisma stat.")

class CharacterClassStartingEquipment(models.Model):
    character_class = models.ForeignKey('CharacterClass', on_delete=models.CASCADE, null=True)
    amount = models.SmallIntegerField(default= 2, null=True, help_text="Enter the number of starting items this class starts with") 
    items = models.CharField(default = '', max_length = 1000, help_text = "Enter a list of the items in JSON format. Ex: {\"item_1\": \"Spatula\", \"item_2\": \"Dishsoap\"}")

class Equipment(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the equipment")
    gold = models.IntegerField(default=0, help_text="Enter the gold-price component for this equipment")
    silver = models.IntegerField(default=0, help_text="Enter the silver-price component for this equipment")
    copper = models.IntegerField(default=0, help_text="Enter the copper-price component for this equipment")
    #Units: Pounds (lbs)
    weight = models.SmallIntegerField(default= 0, help_text="Enter the weight for this item in pounds.")
    descrtiption = models.CharField(default = '', max_length = 1000, help_text = "Enter a description of this item.")
    capacity = models.SmallIntegerField(default= 0, help_text = "Enter the amount of this item you have before any uses.")

class Armor(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the armor")
    armor_bonus = models.SmallIntegerField(default= 0, help_text="Enter the armor bonus for this item in pounds.")
    max_dexterity =  models.SmallIntegerField(default= 0, help_text="Enter the weight for this item in pounds.")
    is_stealth = models.BooleanField(default = False, help_text="Alan put something here :^)")
    #Units: Pounds (lbs)
    weight = models.SmallIntegerField(default= 0, help_text="Enter the weight for this item in pounds.")
    gold = models.IntegerField(default=0, help_text="Enter the gold-price component for this armor")
    silver = models.IntegerField(default=0, help_text="Enter the silver-price component for this armor")
    copper = models.IntegerField(default=0, help_text="Enter the copper-price component for this armor")
    required_strength = models.SmallIntegerField(default= 0, help_text="Enter the required strength to use this armor.")
    required_materials = models.CharField(default = "", max_length = 10000, help_text = "Enter the required materials to cast this spell in JSON format.")

class Weapon(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this weapon")
    gold = models.IntegerField(default=0, help_text="Enter the gold-price component for this weapon")
    silver = models.IntegerField(default=0, help_text="Enter the silver-price component for this weapon")
    copper = models.IntegerField(default=0, help_text="Enter the copper-price component for this weapon")

    damage = models.PositiveIntegerField(default=1, help_text="The base hit point damage of this weapon.")

    DAMAGE_TYPE_CHOICES = (
        ('ac', 'Acid'),
        ('bl', 'Bludgeoning'),
        ('co', 'Cold'),
        ('fi', 'Fire'),
        ('fo', 'Force'),
        ('li', 'Lightning'),
        ('ne', 'Necrotic'),
        ('pi', 'Piercing'),
        ('po', 'Poisoning'),
        ('ps', 'Psychic'),
        ('ra', 'Radiant'),
        ('sl', 'Slashing'),
        ('th', 'Thunder'),
    )
    damage_type = models.CharField(max_length = 2, choices = DAMAGE_TYPE_CHOICES, default = 'ab')
    #Unit: Feet (ft)
    range = models.PositiveIntegerField(default = 10, help_text = "Enter the range of the weapon in feet.")
    #Unit: Pounds (lb)
    weight = models.SmallIntegerField(default= 0, help_text="Enter the weight for this item in pounds.")

    
class Properties(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this property.")
    weapon = models.ForeignKey('Weapon', on_delete=models.CASCADE, null=True)
    description = models.ForeignKey('CharacterSubclass', on_delete=models.CASCADE, null = True)
    