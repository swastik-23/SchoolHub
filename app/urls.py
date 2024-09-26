from django.urls import path
import app.app_admin.views as admin_views
import app.app_account.views as account_views

urlpatterns = [
   path("admin/create/student/", admin_views.create_student),
   path("admin/create/teacher/", admin_views.create_teacher),
   path("admin/create/account/", admin_views.create_account),
    path("admin/login/", admin_views.login),
    path("admin/", admin_views.get_admin_info),
]


