from django.contrib import admin

from django.urls import path, include

from blog.feeds import LatestArticlesFeed
from drfsite import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('feeds/latest/', LatestArticlesFeed(), name='latest_articles_feed'),  # RSS-лента

]


# if settings.DEBUG:
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
