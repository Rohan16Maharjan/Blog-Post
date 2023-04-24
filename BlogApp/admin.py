from django.contrib import admin
from .models import Home, About, Contact,Home2

# Register your models here.
admin.site.register(Home)
admin.site.register(Home2)
admin.site.register(About)
admin.site.register(Contact)
