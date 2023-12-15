from django.contrib.admin.apps import AdminConfig


class MainAdminConfig(AdminConfig):
    default_site = "admin.MainAdminSite"