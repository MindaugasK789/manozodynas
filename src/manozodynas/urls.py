from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index_view
from .views import terminu_ivedimas_view
from .views import patikrinti_prideti_termina

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
)


urlpatterns += patterns('',
    url(r'naujo_termino_ivedimas',
        terminu_ivedimas_view,
        name='naujo_termino_ivedimas'),
)
urlpatterns += patterns('',
    url(r'termino_pridejimo_tvirtinimas_neigimas',
        patikrinti_prideti_termina,
        name='patikrinti_prideti_termina'),
)


urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)

