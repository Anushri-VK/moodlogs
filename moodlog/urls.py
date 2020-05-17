from django.urls import path,include
from moodlog.views import dashboard,create_moodlog,signout

urlpatterns = [
	path("dashboard/",dashboard),
	path("create-moodlog/",create_moodlog),
	path("signout/",signout),
]