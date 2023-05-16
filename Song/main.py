import sys
from moviepy.editor import concatenate_audioclips, AudioFileClip
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon, QFont
from pathlib import Path
from gtts import gTTS
import time
from pygame import mixer

import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Крутая штучка')

        self.songs = []
        self.res_songs = []
        self.count = 0

        self.edit_line1 = QLineEdit(self)
        self.edit_line1.setFixedWidth(200)

        self.label1 = QLabel(self)
        self.label1.setText('Путь к mp3')
        self.label1.setFont(QFont('Arial', pointSize=16))
        self.label1.setFixedWidth(2000)

        self.choose1 = QPushButton(self)
        self.choose1.setText('Выберите')
        self.choose1.setFont(QFont('Arial', 14))
        self.choose1.clicked.connect(self.showDialog_choose1)

        self.button2 = QPushButton(self)
        self.button2.setText('Отправить')
        self.button2.clicked.connect(self.click_button2)

        self.button1 = QPushButton(self)
        self.button1.setText('Смешать')
        self.button1.clicked.connect(self.click_button1)

        self.button3 = QPushButton(self)
        self.button3.setText('Играй')
        self.button3.clicked.connect(self.click_button3)

        self.edit_line1.move(500, 300)
        self.label1.move(500, 270)
        self.choose1.move(710, 300)

        self.button1.move(500, 500)
        self.button2.move(500, 400)
        self.button3.move(610, 500)

    def click_button1(self):
        random.shuffle(self.songs)
        for i in range(0, len(self.songs) - 1, 2):
            song1 = self.songs[i]
            song2 = self.songs[i + 1]
            res_song = song1[:-4] + "_" + song2.split('/')[-1]
            self.create_mp3(res_song)
            res_path = self.concatenate_audio_moviepy([song1, song2], res_song)
            self.res_songs.append(res_path)

    def click_button2(self):
        self.songs.append(self.edit_line1.text())
        self.edit_line1.clear()

    def click_button3(self):
        if len(self.res_songs) > self.count:
            self.play_music(self.res_songs[self.count])
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("End")
            dlg.setText("Songs is over")
        self.count += 1

    def showDialog_choose1(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            self.edit_line1.setText(fname[0])

    @staticmethod
    def create_mp3(path):
        print(path)
        file = "Some text"
        speak = gTTS(file, lang='en')
        speak.save(path)
        print(path)

    @staticmethod
    def concatenate_audio_moviepy(audio_clip_paths, output_path):
        clips = [AudioFileClip(c) for c in audio_clip_paths]
        final_clip = concatenate_audioclips(clips)
        final_clip.write_audiofile(output_path)
        return output_path

    @staticmethod
    def play_music(song):
        mixer.init()
        mixer.music.load(song)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.showMaximized()
    sys.exit(app.exec())
