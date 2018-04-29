from django.contrib import admin

# Register your models here.
from .models import Character, Race, RaceFeatures, Subrace, SubraceFeatures
admin.site.register(Character)
admin.site.register(Race)
admin.site.register(RaceFeatures)
admin.site.register(Subrace)
admin.site.register(SubraceFeatures)

from .models import CharacterClass, CharacterClassSpellList, CharacterClassFeatures
admin.site.register(CharacterClass)
admin.site.register(CharacterClassSpellList)
admin.site.register(CharacterClassFeatures)

from .models import CharacterSubclass, CharacterSubclassSpellList, CharacterClassStartingEquipment, Spell, CharacterSubclassFeatures
admin.site.register(CharacterSubclass)
admin.site.register(CharacterSubclassSpellList)
admin.site.register(CharacterClassStartingEquipment)
admin.site.register(Spell)
admin.site.register(CharacterSubclassFeatures)

from .models import FeatRanking, Feat, Weapon, Armor, Equipment, Properties
admin.site.register(FeatRanking)
admin.site.register(Feat)
admin.site.register(Armor)
admin.site.register(Equipment)
admin.site.register(Weapon)
admin.site.register(Properties)

