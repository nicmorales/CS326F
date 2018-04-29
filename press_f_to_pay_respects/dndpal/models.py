"""
TO-DO:
Things to ask Alan:
- Implement __str__ representations of the models
- Have Alan change the help text for stuff as appropriate
"""

from django.db import models

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

from django.contrib.auth.models import User

# Create your models here.


class Character(models.Model):
    char_id= models.PositiveIntegerField(default = 1, unique=True, primary_key = True, help_text = "Enter Character ID")
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    char_name = models.CharField( default = '', max_length = 30, help_text = "Enter a name for your character")
    char_class = models.ForeignKey('CharacterClass', on_delete=models.SET_NULL, null = True)
    race = models.ForeignKey('Race', on_delete=models.SET_NULL, null = True)
    subrace = models.ForeignKey('Subrace', on_delete=models.SET_NULL, null = True)
    level = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the level your character")

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
    proficiency_list = models.CharField( default = '', max_length = 30, help_text = "Enter the list of proficiencies for this character in JSON format.")
    ability_list = models.CharField( default = '', max_length = 1000, help_text = "Enter the list of abilities for this character in JSON format.")
    spell_list = models.CharField( default = '', max_length = 1000, help_text = "Enter the list of spells for this character in JSON format.")
    gold = models.IntegerField(default=0, help_text="Enter the gold of the character")
    silver = models.IntegerField(default=0, help_text="Enter the gold of the character")
    copper = models.IntegerField(default=0, help_text="Enter the gold of the character")

    armor = models.ForeignKey('Armor', on_delete=models.SET_NULL, null = True)
    weapon = models.ForeignKey('Weapon', on_delete=models.SET_NULL, null = True)
    items = models.CharField(default = '', max_length = 5000, help_text = "Enter list of inventory items")
    max_hp = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the max hitpoints for your character")
    temp_hp = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the temporary hitpoints for your character")
    cur_hp = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the current hitpoints for your character")
    armor_class = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the armor class for your character")
    init = models.PositiveSmallIntegerField(default = 1, help_text = "Enter the initiative bonus for your character")
    bonus_list = models.CharField( default = '', max_length = 1000, help_text = "Enter the list of bonuses for this character in JSON format.")

    strength = models.SmallIntegerField(default= 0, help_text="Enter the strength state for your character.")
    dexterity = models.SmallIntegerField(default= 0, help_text="Enter the dexterity state for your character.")
    constitution = models.SmallIntegerField(default= 0, help_text="Enter the constitution state for your character.")
    intelligence = models.SmallIntegerField(default= 0, help_text="Enter the intelligence state for your character.")
    wisdom = models.SmallIntegerField(default= 0, help_text="Enter the wisdowm state for your character.")
    charisma = models.SmallIntegerField(default= 0, help_text="Enter the charisma state for your character.")

    character_view = models.CharField( default = '', max_length = 30, help_text = "Enter view for character (simple/guided/manual).")




    def __str__(self):
        return self.char_name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this Character.
        """
        return reverse('character-detail', args=[str(self.name)])

class Race(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this race")
    description = models.CharField(default = '', max_length = 5000, help_text = "Enter a description of this race (backstory, beliefs, etc.)")
    speed = models.SmallIntegerField(default=0, help_text="Enter the speed for this race")
    # Only applied once at character creation, will use a JS parser (or something) to parse the raw string (format of string is JSON)
    # object and apply the mods to the characters stats
    modifiers = models.CharField(default = '', max_length = 20, help_text = "Enter the stats modifiers in JSON format. Ex: {\"str\": 2, \"dex\": 8}")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this Race.
        """
        return reverse('race-detail', args=[str(self.name)])

class RaceFeatures(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this race feature")
    race = models.ForeignKey('Race', on_delete=models.CASCADE, null = True)
    description = models.CharField(default= '', max_length = 5000, help_text = "Enter a description of this feature; i.e. what this feature does")
    required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this feature")

class Subrace(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the subrace")
    parent_race = models.ForeignKey('Race', on_delete=models.CASCADE, null = True)
    description = models.CharField(default= '', max_length = 5000, help_text = "Enter a description of this sub-race (backstory, beliefs, etc.)")
    modifiers = models.CharField(default = '', max_length = 20, help_text = "Enter the stats modifiers in JSON format. Ex: {\"str\": 2, \"dex\": 8}")
    def __str__(self):
        return self.name


class SubraceFeatures(models.Model):
    subrace = models.ForeignKey('Subrace', on_delete=models.CASCADE, null = True)
    required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this feature")
    sub_feature_name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this feature")
    #name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the subrace")
    description = models.CharField(default= '', max_length = 5000, help_text = "Enter a description for these features")

class CharacterClass(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this class")
    descrtiption = models.CharField(default = '', max_length = 1000, help_text = "Enter a description of this class")
    hitpoints = models.PositiveIntegerField(default = 10, help_text = "Enter the hitdie of this class")
    skill_proficiency_limit = models.PositiveSmallIntegerField(default = 5, help_text = "Enter the max amount of skills this class can be proficient in")
    skill_list = models.CharField(default = '', max_length = 100, help_text = "Enter a comma separated skill list. Ex: \"Acrobatics,Intimidation\" \(without the quotations\)")
    armor_prof = models.CharField(default = "", max_length = 10000, help_text = "Enter a comma separated of armor proficiencies list for the class")
    weapon_prof = models.CharField(default = "", max_length = 10000, help_text = "Enter a comma separated of weapon proficiencies list for the class")
    saving_throws = models.CharField(default = "", max_length = 10000, help_text = "Enter a comma separated list of saving throws for the class")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this class.
        """
        return reverse('class-detail', args=[str(self.name)])

class CharacterClassSpellList(models.Model):
    character_class = models.ForeignKey('CharacterClass', on_delete=models.CASCADE, null = True)
    required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this spell")
    ranking = models.SmallIntegerField(default= 0, null=True, help_text="Enter the recommended ranking of this spell relative to the other spells available for this class on a scale from 1-5. 5 being the best and 1 being the worst.")
    spell_list = models.ForeignKey('Spell', on_delete=models.CASCADE)
    ran_note = models.CharField(default = "", max_length = 10000, help_text = "Enter the ranking note for this spell for this class")

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
    required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this spell")
    ranking = models.SmallIntegerField(default= 0, null=True, help_text="Enter the recommended ranking of this spell relative to the other spells available for this class on a scale from 1-5. 5 being the best and 1 being the worst.")
    spell_list = models.ForeignKey('Spell', on_delete=models.CASCADE)
    ran_note = models.CharField(default = "", max_length = 10000, help_text = "Enter the ranking note for this feat for this subclass")



class Spell(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the spell")
    spell_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the spell level of this spell")
    # Saved as an int, but should be interpreted as number of seconds
    cast_time = models.CharField(default = "", max_length = 10000, help_text = "Enter the action it takes to cast the spell.")
    # Amount of hit point damage it does. If it is a healing spell, enter the amount of hit points it heals.
    # Saved as an int, but should be interpreted as number of feet
    duration = models.CharField(default = "", max_length = 10000, help_text = "Enter the duration of the spell in rounds.")
    range = models.CharField(default = "", max_length = 10000, help_text = "Enter the range of the spell in feet. If the range is a touch, enter the value: Touch")
    #Units: feet
    area_effected = models.CharField(default = "", max_length = 10000, blank=True, help_text = "If the spell affects an area, enter the area affected by the spell (in feet).")
    materials = models.CharField(default = "", max_length = 10000, blank=True, help_text = "If the Spell has material components, enter the materials separated with commas.")
    components = models.CharField(default = "", max_length = 10000, help_text = "Enter the spell components of this spell")
    
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

    description = models.CharField(default = "", max_length = 10000, help_text = "Enter the spell description")

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this spell.
        """
        return reverse('spell-detail', args=[str(self.name)])

class FeatRanking(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the feat this ranking describes")
    required_level = required_level = models.SmallIntegerField(default= 0, null=True, help_text="Enter the required level for this spell")
    ranking = models.SmallIntegerField(default= 0, help_text="Enter the ranking of this feature relative to the other features available for this class.")
    ran_note = models.CharField(default = "", max_length = 10000, help_text = "Enter the ranking note for this feat")

class Feat(models.Model):
    descrtiption = models.CharField(default = '', max_length = 1000, help_text = "Enter a description of this feat.")
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the feat")
    strength = models.SmallIntegerField(default= 0, help_text="Enter the modification to the strength stat.")
    dexterity = models.SmallIntegerField(default= 0, help_text="Enter the modification to the dexterity stat.")
    constitution = models.SmallIntegerField(default= 0, help_text="Enter the modification to the constitution stat.")
    intelligence = models.SmallIntegerField(default= 0, help_text="Enter the modification to the intelligence stat.")
    wisdowm = models.SmallIntegerField(default= 0, help_text="Enter the modification to the wisdom stat.")
    charisma = models.SmallIntegerField(default= 0, help_text="Enter the modification to the charisma stat.")

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this feat.
        """
        return reverse('book-detail', args=[str(self.name)])

class CharacterClassStartingEquipment(models.Model):
    character_class = models.ForeignKey('CharacterClass', on_delete=models.CASCADE, null=True)
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

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this equipment.
        """
        return reverse('equipment-detail', args=[str(self.name)])

class Armor(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the armor")
    armor_bonus = models.SmallIntegerField(default= 0, help_text="Enter the armor bonus for this item in pounds.")
    max_dexterity =  models.SmallIntegerField(default= 0, help_text="Enter the maximum amount of bonus AC from dex modifier.")
    is_stealth = models.BooleanField(default = False, help_text="Is the armor stealthy?")
    #Units: Pounds (lbs)
    weight = models.SmallIntegerField(default= 0, help_text="Enter the weight for this item in pounds.")
    gold = models.IntegerField(default=0, help_text="Enter the gold-price component for this armor")
    silver = models.IntegerField(default=0, help_text="Enter the silver-price component for this armor")
    copper = models.IntegerField(default=0, help_text="Enter the copper-price component for this armor")
    required_strength = models.SmallIntegerField(default= 0, help_text="Enter the required strength to use this armor.")
    required_materials = models.CharField(default = "", max_length = 10000, help_text = "Enter the required materials to cast this spell in JSON format.")
    armor_type = models.CharField(default = "", max_length = 10000, help_text = "Enter a comma separated list for the class")
    # light, medium, or heavy armor?

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this armor.
        """
        return reverse('armor-detail', args=[str(self.name)])

class Weapon(models.Model):
    name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of this weapon")
    gold = models.IntegerField(default=0, help_text="Enter the gold-price component for this weapon")
    silver = models.IntegerField(default=0, help_text="Enter the silver-price component for this weapon")
    copper = models.IntegerField(default=0, help_text="Enter the copper-price component for this weapon")

    damage = models.CharField(default = "", max_length = 10000, help_text = "Enter the damage die of this weapon")

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
    range = models.CharField(default = "", max_length = 10000, help_text = "Enter the range of the weapon.")
    #Unit: Pounds (lb)
    weight = models.SmallIntegerField(default= 0, help_text="Enter the weight for this item in pounds.")
    weapon_type = models.CharField(default = "", max_length = 10000, help_text = "Enter the weapon category of the weapon. IE: Simple, Martial, etc.")

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this weapon.
        """
        return reverse('weapon-detail', args=[str(self.name)])


class Properties(models.Model):
    name = models.CharField(default = '', max_length = 100, help_text = "Enter the name of this property.")
    weapon = models.ForeignKey('Weapon', on_delete=models.CASCADE, null=True)
    description = models.CharField(default = "", max_length = 10000, help_text = "Enter the description of this property")
