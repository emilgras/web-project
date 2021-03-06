class Config(object):
	"""
	Common configuration
	"""

	# Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
	"""
	Development configurations
	"""

	DEBUG = True
	SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
	"""
	Production configurations
	"""

	DEBUG = False


app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}