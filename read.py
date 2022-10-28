from venv import EnvBuilder
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
            with open("answer.txt", "r") as file:
                print(file.readlines()[-1])




observer = Observer()
observer.schedule(Handler(), path="G:\ПрогПитон\pz4")
observer.start()
try:
    while 1:
        pass
except KeyboardInterrupt:
    observer.stop()s
    print("Handler stoped")
