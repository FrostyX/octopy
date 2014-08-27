from pygithub3 import Github


class User:

	"""
	https://developer.github.com/v3/users/#response
	https://developer.github.com/v3/repos/#response
	"""

	user = None

	def __init__(self, login):
		gh = Github()
		self.user = gh.users.get(login)

	def __getattr__(self, item):
		return self.user.__dict__[item]

	def repositories(self):
		gh = Github()
		return gh.repos.list(self.user.login).all()
