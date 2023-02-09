cov:
	coverage run --source='./apps' manage.py test && coverage report