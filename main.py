import time
from threading import Thread
from streamer import Streamer
from drawer import Matrix
from tg import setup, polling
import config


def main():
    mx = Matrix(config.BOARD_WIDTH, config.BOARD_HEIGHT, config.CELL_SIZE)
    stream = Streamer(config.URL)
    setup(mx.set, mx.clr)
    Thread(target=polling).start()
    try:
        while True:
            stream.send_img(mx.render())
            time.sleep(1 / config.FPS)
    except Exception as ex:
        print(ex)
        exit(-1)


if __name__ == '__main__':
    main()
