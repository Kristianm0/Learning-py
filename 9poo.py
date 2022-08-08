# multiple inheritance

class Phone:
    def __init__(self):
        pass
    def call(self):
        print("Calling...")
    def busy(self):
        print("busy...")

class Camera:
    def __init__(self):
        pass
    def photography(self):
        print("Taking a photo...")

class Play:
    def __init__(self):
        pass
    def music_play(self):
        print("Playing music...")
    def video_play(self):
        print("Playing video")

class Smartphone(Phone, Camera, Play ):
    def __del__(self):
        print("Phone off")

movil = Smartphone()
print(movil.call())
