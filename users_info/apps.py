from django.apps import AppConfig


class UsersInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_info'
    
    def ready(self):
        import users_info.signals
