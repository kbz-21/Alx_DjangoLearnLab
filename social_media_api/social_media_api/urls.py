from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    # path('posts/', include('posts.urls')),
    # path('api-auth/', include('rest_framework.urls')),  # for browsable API login/logout

    path('api/', include('posts.urls')),       # your posts & comments endpoints under /api/
    path('api/auth/', include('rest_framework.urls')),  # optional browsable login
]
