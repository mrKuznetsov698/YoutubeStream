import subprocess
from PIL import Image


class Streamer:
    def __init__(self, stream_url: str):
        self.cmd = cmd = f'ffmpeg -f image2pipe -i - -re -f lavfi -i anullsrc -vf format=yuv420p -c:v libx264 -b:v 2000k -maxrate 4500k -bufsize 4000k -g 50 -c:a aac -f flv {stream_url}'
        self.process = subprocess.Popen(cmd.split(' '), stdin=subprocess.PIPE, stderr=open('stream.log', 'w'))

    def send_img(self, img: Image):
        try:
            img.save(self.process.stdin, 'bmp')
        except Exception as ex:
            print(ex)
            self.process.stdin.close()
            self.process.stderr.close()
            self.process.wait()
            exit(-1)
