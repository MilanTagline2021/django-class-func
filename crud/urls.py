from django.contrib import admin
from django.urls import path
from func_app.views import get_student_api#,hello_world, hello_post,
from class_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/',hello_world),
    # path('post/',hello_post),
    # path('getstudent/',get_student_api),
    # path('poststudent/',post_student_api),
    path('student/',views.StudentApi.as_view())
]
