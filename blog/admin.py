from django.contrib import admin
from .models import Post  # tecka znamena, ze je to ze stejneho adresare jako stojim (blog.models)

# Register your models here.

admin.site.register(Post)
