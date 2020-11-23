import os

# Import environment variables
DISCORD_ACCESS_TOKEN = os.environ['DISCORD_ACCESS_TOKEN']

# Redis server FQDN - determined by Docker DNS within docker-compose.yml
REDIS_SERVER = 'redis'

# Redis server port
REDIS_PORT = 6379