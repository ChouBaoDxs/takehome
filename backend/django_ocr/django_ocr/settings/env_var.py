import os

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

OPEN_SWAGGER = os.getenv('OPEN_SWAGGER', 'True').lower() == 'true'

# 默认使用 sqlite 数据库
DB_USE_MYSQL = os.getenv('DB_USE_MYSQL', 'False').lower() == 'true'
# 下面的数据库变量只有在 DB_USE_MYSQL=True 时生效
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
