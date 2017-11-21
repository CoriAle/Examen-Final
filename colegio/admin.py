from django.contrib import admin
from .models import Alumno
from .models import Profesor
from .models import Materia
from .models import Nota
from .models import Grado

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Nota)
admin.site.register(Grado)
