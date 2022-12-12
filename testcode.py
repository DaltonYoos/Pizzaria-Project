import os
os.envirion.setdefault("DJANGO_SETTINGS_MODULE", 'Pizzaria.settings')

import django
django.setup()

from Pizzas.models import Pizza

pizza = Pizza.objects.all()

print(pizza)

for p in pizza:
    print(p)
    