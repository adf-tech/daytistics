from django.apps import AppConfig


class DaytisticsConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'app.daytistics'

	def ready(self):
		import app.activities.signals
