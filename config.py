import os

# YouTube configs
STREAM_KEY = os.getenv('STREAM_KEY')
# SERVER_URL = 'rtmp://a.rtmp.youtube.com/live2'
SERVER_URL = 'rtmp://b.rtmp.youtube.com/live2?backup=1'
URL = f'{SERVER_URL}/{STREAM_KEY}'
FPS = 30

# Matrix configs
WIDTH = 1280
HEIGHT = 720
CELL_SIZE = 20
BOARD_WIDTH = WIDTH // CELL_SIZE
BOARD_HEIGHT = HEIGHT // CELL_SIZE

# Telegram configs
BOT_TOKEN = os.getenv('BOT_TOKEN')
ALLOWED_ID = -1001757398982
