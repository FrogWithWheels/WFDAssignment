from .models import UserModel
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import BaseBackend

class CustomAuthentication(BaseBackend):
	def authenticate(self, request, username=None, password=None):
		try:
			user = UserModel.objects.get(username = username)
			if check_password(password, user.password):
				return user
			else:
				return None
		except UserModel.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return UserModel.objects.get(pk = user_id)
		except:
			return None