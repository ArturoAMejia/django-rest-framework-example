from rest_framework import routers
from drfsimplecrud.api import ProjectViewSet

# Se define la variable router para definir todas las rutas
router = routers.DefaultRouter()

# Se registran las rutas por medio de su url de acceso, se le pasa el ViewSet y el nombre de la ruta
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls

