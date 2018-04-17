# from django import forms
# from djang.forms import ModelForm
# from .models import Armor

# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _

# class CustomArmorForm(ModelForm):
# 	class Meta:
# 		model = Armor
# 		fields = '__all__'
# 		labels = { 'name':_('Armor Name'), 'is_stealth':_('Stealth'), }
# 		initial = 

# 	# name = forms.CharField(initial='Armor Name', max_length = 100, help_text = "Enter the name of the armor")
#  #    armor_bonus = forms.SmallIntegerField(help_text="Enter the armor bonus (AC) for this item in pounds.")
#  #    max_dexterity = forms.SmallIntegerField(initial=0, help_text="Enter the maximum amount of bonus AC from dex modifier.")
#  #    is_stealth = forms.BooleanField(help_text="Is the armor not loud?")
#  #    # armor class (light, med, heavy)?
#  #    #Units: Pounds (lbs)
#  #    weight = forms.SmallIntegerField(help_text="Enter the weight for this item in pounds.")
# 	# gold = forms.IntegerField(help_text="Enter the gold-price component for this armor")
# 	# silver = forms.IntegerField(help_text="Enter the silver-price component for this armor")
# 	# copper = forms.IntegerField(help_text="Enter the copper-price component for this armor")
# 	# required_strength = forms.SmallIntegerField(required=False, default= 0, help_text="Enter the required strength to use this armor.")
#  #    required_materials = forms.CharField(default = "", max_length = 10000, help_text = "Enter the required materials to cast this spell in JSON format.")

#     def clean_required_stength(self):
#     	data =  self.cleaned_data['required_strength']
#     	# Check number is not negative
#     	if data < 0:
#     		raise ValidationError(_('Invalid strength requirement; value is negative'))
#     	# Check number is not above 20
#     	if data > 20:
#     		raise ValidationError(_('Invalid strength requirement; value is greater than maximum stength, 20'))

#     	return data

#     def clean_gold(self):
#     	data =  self.cleaned_data['gold']
#     	# Check number is not negative
#     	if data < 0:
#     		raise ValidationError(_('Invalid gold price; cost is negative'))
#     	return data

#     def clean_silver(self):
#     	data =  self.cleaned_data['silver']
#     	# Check number is not negative
#     	if data < 0:
#     		raise ValidationError(_('Invalid silver price; cost is negative'))
#     	return data

#     def clean_copper(self):
#     	data =  self.cleaned_data['copper']
#     	# Check number is not negative
#     	if data < 0:
#     		raise ValidationError(_('Invalid copper price; cost is negative'))
#     	return data


#     def clean_required_materials(self):
#     	pass
#     	# I have no idea how to enforce JSON format


# class Armor(models.Model):
#     def get_absolute_url(self):
#         """
#         Returns the url to access a detail record for this armor.
#         """
#         return reverse('armor-detail', args=[str(self.name)])