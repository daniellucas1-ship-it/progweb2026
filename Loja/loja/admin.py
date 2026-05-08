from django.contrib import admin

# Register your models here.
from .models import * #imporata nossos models
admin.site.register(Fabricante) #adiciona a interface do adm
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Produto)
class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
    admin.site.register(Fabricante,FabricanteAdmin)
    admin.site.register(Categoria)
    admin.site.register(Produto)
