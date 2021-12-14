from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include('profiles.urls', namespace="profiles")),
    path("admin/", admin.site.urls),
]



#   path('author-polls/', include('polls.urls', namespace='author-polls')),


# urlpatterns = [
#     path("", views.index, name="index"),
#     path("lettings/", views.lettings_index, name="lettings_index"),
#     path("lettings/<int:letting_id>/", views.letting, name="letting"),
#     path("profiles/", views.profiles_index, name="profiles_index"),
#     path("profiles/<str:username>/", views.profile, name="profile"),
#     path("admin/", admin.site.urls),
# ]