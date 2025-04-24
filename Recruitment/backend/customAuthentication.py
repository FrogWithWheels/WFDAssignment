# imports
from .models import UserModel
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import BaseBackend

# custom authentication class
class CustomAuthentication(BaseBackend):
	# authenticate method
	def authenticate(self, request, username=None, password=None):
		try:
			# try get the user object based on username
			user = UserModel.objects.get(username = username)

			# if the password matches
			if check_password(password, user.password):
				return user 
			else:
				return None

		# if cant find object
		except UserModel.DoesNotExist:
			return None

	# get user method
	def get_user(self, user_id):
		try:
			return UserModel.objects.get(pk = user_id)
		except:
			return None