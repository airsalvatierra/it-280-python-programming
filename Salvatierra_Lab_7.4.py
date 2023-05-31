import platform
import subprocess
import threading
import time

IMAGE_NAME = 'zophie.jpg'
MP3_NAME = 'Scots Wha Hae.mp3'
OPERATING_SYSTEMS_PRE_COMMANDS = {
    'Windows': ['cmd', '/c', 'start', ''],
    'Darwin': ['open'],
}
STOP_FLAG = threading.Event()


def open_media_file(file_name: str):
    """
    Open a file with the default application according the corresponding
    Operating System 
    """
    # Getting the appropiate command according the OS
    operating_system = platform.system()
    pre_commnand = OPERATING_SYSTEMS_PRE_COMMANDS.get(
        operating_system, ['xdg-open']
    )

    #  Display/play the media file with the corresponding default application
    subprocess.Popen(pre_commnand + [file_name])

    # send termination thread signal after a couple of seconds
    seconds = 2 if file_name == IMAGE_NAME else 5
    time.sleep(seconds)
    STOP_FLAG.set()


# Start a thread for each file
threads = []
for file_name in [IMAGE_NAME, MP3_NAME]:
    thread = threading.Thread(target=open_media_file, args=(file_name,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print('The image and the mp3 file were displayed/played without problem')
