import sys
import os
import sqlite3
import inspect
import cv2
import moviepy.editor as mpe
import pygame
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QFileDialog, QTableWidgetItem, \
                             QMessageBox, QHBoxLayout, QLabel, QColorDialog, QDoubleSpinBox, QPushButton)
from PyQt5.QtGui import QPixmap, QColor, QIcon, QImage, QPainter, QPen, QBrush
from PIL import Image, ImageFilter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint

# Переменные с ником пользователя, его сохранённой музыкой и сохранёнными изображениями
USER = ''
SAVED_IMAGE = list()
SAVED_MUSIC = list()


# Создание формы музыкального редактора
class Piano_Form(object):
    def setupUi(self, Form):
        self.setWindowTitle('Создание музыки')
        Form.setObjectName("Form")
        Form.resize(935, 369)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(750, 10, 131, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color:red;\n""")
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 40, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: white;\n"
                                      "text-color: black;\n"
                                      "border: 2px solid black;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 40, 30, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:black;\n"
                                        "color:white;\n"
                                        "border: 2px solid grey;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 30, 40, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: white;\n"
                                        "text-color: black;\n"
                                        "border: 2px solid black;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 40, 30, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:black;\n"
                                        "color:white;\n"
                                        "border: 2px solid grey;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 30, 40, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: white;\n"
                                        "text-color: black;\n"
                                        "border: 2px solid black;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 40, 30, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color:black;\n"
                                        "color:white;\n"
                                        "border: 2px solid grey;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 30, 40, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: white;\n"
                                        "text-color: black;\n"
                                        "border: 2px solid black;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 40, 30, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color:black;\n"
                                        "color:white;\n"
                                        "border: 2px solid grey;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(290, 30, 40, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: white;\n"
                                        "text-color: black;\n"
                                        "border: 2px solid black;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 40, 30, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color:black;\n"
                                         "color:white;\n"
                                         "border: 2px solid grey;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(360, 30, 40, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: white;\n"
                                         "text-color: black;\n"
                                         "border: 2px solid black;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(400, 40, 30, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color:black;\n"
                                         "color:white;\n"
                                         "border: 2px solid grey;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(430, 30, 40, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: white;\n"
                                         "text-color: black;\n"
                                         "border: 2px solid black;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(470, 40, 30, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color:black;\n"
                                         "color:white;\n"
                                         "border: 2px solid grey;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(500, 30, 40, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: white;\n"
                                         "text-color: black;\n"
                                         "border: 2px solid black;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(540, 40, 30, 190))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color:black;\n"
                                         "color:white;\n"
                                         "border: 2px solid grey;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(580, 40, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: white;\n"
                                         "text-color: black;\n"
                                         "border-radius: 40px;\n"
                                         "border: 2px solid black;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(630, 130, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: white;\n"
                                         "text-color: black;\n"
                                         "border-radius: 40px;\n"
                                         "border: 2px solid black;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(740, 0, 3, 400))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(650, 270, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("source/image/tarelki.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(15, 240, 30, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(86, 240, 31, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(156, 240, 31, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(225, 240, 40, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(290, 240, 50, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(367, 240, 30, 51))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(437, 240, 30, 51))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 300, 50, 50))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("source/image/banjo.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(600, 220, 50, 50))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("source/image/baraban.png"))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(110, 300, 50, 50))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("source/image/cello.png"))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(180, 300, 50, 50))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("source/image/clarenet.png"))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(250, 300, 50, 50))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("source/image/contrabass.png"))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(320, 300, 50, 50))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("source/image/guitar.png"))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(390, 300, 50, 50))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("source/image/rockguitar.png"))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(460, 300, 50, 50))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("source/image/clarnet2.png"))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(500, 250, 50, 50))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("source/image/banjo2.png"))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(540, 300, 50, 50))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("source/image/cello2.png"))
        self.label_19.setObjectName("label_19")
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(750, 90, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(750, 130, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Музыкальный редактор"))
        self.radioButton.setText(_translate("Form", "Rec"))
        self.pushButton.setText(_translate("Form", "Q"))
        self.pushButton_2.setText(_translate("Form", "A"))
        self.pushButton_3.setText(_translate("Form", "W"))
        self.pushButton_4.setText(_translate("Form", "S"))
        self.pushButton_5.setText(_translate("Form", "E"))
        self.pushButton_6.setText(_translate("Form", "D"))
        self.pushButton_7.setText(_translate("Form", "R"))
        self.pushButton_8.setText(_translate("Form", "F"))
        self.pushButton_9.setText(_translate("Form", "T"))
        self.pushButton_10.setText(_translate("Form", "G"))
        self.pushButton_11.setText(_translate("Form", "Y"))
        self.pushButton_12.setText(_translate("Form", "H"))
        self.pushButton_13.setText(_translate("Form", "U"))
        self.pushButton_14.setText(_translate("Form", "J"))
        self.pushButton_15.setText(_translate("Form", "I"))
        self.pushButton_16.setText(_translate("Form", "K"))
        self.pushButton_17.setText(_translate("Form", "Z"))
        self.pushButton_18.setText(_translate("Form", "X"))
        self.label_3.setText(_translate("Form", "ДО"))
        self.label_4.setText(_translate("Form", "РЕ"))
        self.label_5.setText(_translate("Form", "МИ"))
        self.label_6.setText(_translate("Form", "ФА"))
        self.label_7.setText(_translate("Form", "СОЛЬ"))
        self.label_8.setText(_translate("Form", "ЛЯ"))
        self.label_9.setText(_translate("Form", "СИ"))
        self.pushButton_19.setText(_translate("Form", "Добавить в видео"))
        self.pushButton_20.setText(_translate("Form", "Сохранить"))


# Музыкальный редактор
class Piano(QMainWindow, Piano_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('source/image/icon.png'))
        valid = QMessageBox.question(self, '',
                                     "Для работы с клавиатурой включите ENG раскладку!",
                                     QMessageBox.Yes)
        # Словарь для проигрывания мелодий при нажатии на клавишу-ключ
        self.sounds = {
            'Q': 'source/music/do.mp3',
            'W': 'source/music/re.mp3',
            'E': 'source/music/mi.mp3',
            'R': 'source/music/fa.mp3',
            'T': 'source/music/sol.mp3',
            'Y': 'source/music/lia.mp3',
            'U': 'source/music/si.mp3',
            'I': 'source/music/banjo2.mp3',
            'A': 'source/music/banjo.mp3',
            'S': 'source/music/cello.mp3',
            'D': 'source/music/clarinet.mp3',
            'F': 'source/music/contrabasson.mp3',
            'G': 'source/music/guitar.mp3',
            'H': 'source/music/rock_guitar2.mp3',
            'J': 'source/music/clarinet2.mp3',
            'K': 'source/music/cello2.mp3',
            'Z': 'source/music/baraban.mp3',
            'X': 'source/music/dishes.mp3'
        }
        self.keyboard_keys = {
            81: 'Q',
            65: 'A',
            87: 'W',
            83: 'S',
            69: 'E',
            68: 'D',
            82: 'R',
            70: 'F',
            84: 'T',
            71: 'G',
            89: 'Y',
            72: 'H',
            85: 'U',
            74: 'J',
            73: 'I',
            75: 'K',
            90: 'Z',
            88: 'X',
        }
        # Переменная для записи музыки
        self.recording = list()
        self.pushButton.clicked.connect(self.sound)
        self.pushButton_2.clicked.connect(self.sound)
        self.pushButton_3.clicked.connect(self.sound)
        self.pushButton_4.clicked.connect(self.sound)
        self.pushButton_5.clicked.connect(self.sound)
        self.pushButton_6.clicked.connect(self.sound)
        self.pushButton_7.clicked.connect(self.sound)
        self.pushButton_8.clicked.connect(self.sound)
        self.pushButton_9.clicked.connect(self.sound)
        self.pushButton_10.clicked.connect(self.sound)
        self.pushButton_11.clicked.connect(self.sound)
        self.pushButton_12.clicked.connect(self.sound)
        self.pushButton_13.clicked.connect(self.sound)
        self.pushButton_14.clicked.connect(self.sound)
        self.pushButton_15.clicked.connect(self.sound)
        self.pushButton_16.clicked.connect(self.sound)
        self.pushButton_17.clicked.connect(self.sound)
        self.pushButton_18.clicked.connect(self.sound)
        self.pushButton_19.clicked.connect(self.add_music_in_video)
        self.pushButton_20.clicked.connect(self.save_music)
        self.playsound = pygame.mixer.init()

    # Звучание при нажатии на клавишу
    def sound(self):
        pygame.mixer.music.load(self.sounds[self.sender().text()])
        pygame.mixer.music.play()
        if self.radioButton.isChecked():
            self.recording.append(self.sounds[self.sender().text()])

    # Сохранение музыки
    def save_music(self):
        if len(self.recording) == 0:
            valid = QMessageBox.question(self, '',
                                         "Выберите REC для записи!", QMessageBox.Yes)
        else:
            file_name = QFileDialog.getSaveFileName(self, 'Сохранить',
                                                    '', "Музыка(*.mp3)")[0]
            with open(file_name, 'wb') as music:
                for elem in self.recording:
                    music.write(open(elem, 'rb').read())
            self.recording = list()
        self.radioButton.setChecked(False)

    # Проигрывание музыки при нажатии на клавишу
    def keyPressEvent(self, event):
        if event.key() in self.keyboard_keys.keys():
            pygame.mixer.music.load(self.sounds[self.keyboard_keys[event.key()]])
            pygame.mixer.music.play()
            if self.radioButton.isChecked():
                self.recording.append(self.sounds[self.keyboard_keys[event.key()]])

    def add_music_in_video(self):
        global SAVED_MUSIC
        if len(self.recording) == 0:
            valid = QMessageBox.question(self, '',
                                         "Выберите REC для записи!", QMessageBox.Yes)
        else:
            file_name = QFileDialog.getSaveFileName(self, 'Сохранить',
                                                    '', "Музыка(*.mp3)")[0]
            if len(file_name) > 0:
                with open(file_name, 'wb') as music:
                    for elem in self.recording:
                        music.write(open(elem, 'rb').read())
                connect = sqlite3.connect('RedactorDB.db')
                cursor = connect.cursor()
                result = cursor.execute('''SELECT save_mp3 FROM Users
                    WHERE login = ?''', (USER,)).fetchone()
                if (result is None) or (result[0] == '') or (result[0] is None):
                    result = file_name
                else:
                    result = result[0] + '?' + file_name
                SAVED_MUSIC = result
                result = cursor.execute('''UPDATE Users
                    SET save_mp3 = ?
                    WHERE login = ?''', (SAVED_MUSIC, USER)).fetchall()
                connect.commit()
                connect.close()
        self.recording = list()
        self.radioButton.setChecked(False)


# Форма фоторедактора
class PhotoEditor_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(941, 701)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(580, 0, 3, 570))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 570, 580, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(593, 20, 90, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 20, 90, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(790, 20, 140, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 590, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(30, 630, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(84, 630, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(110, 630, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 660, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(240, 583, 3, 110))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 590, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox_3 = QtWidgets.QSpinBox(Form)
        self.spinBox_3.setGeometry(QtCore.QRect(340, 630, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(Form)
        self.spinBox_4.setGeometry(QtCore.QRect(410, 630, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(390, 630, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 660, 76, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(710, 70, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(580, 70, 360, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(590, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(720, 155, 140, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(590, 211, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(720, 214, 140, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(590, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(720, 280, 140, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(590, 340, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(720, 350, 140, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(590, 410, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(720, 420, 140, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(593, 480, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(722, 490, 140, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(710, 540, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(620, 590, 30, 30))
        self.pushButton_12.setStyleSheet("background-color:black;")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(670, 590, 100, 30))
        self.pushButton_14.setStyleSheet("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(750, 650, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(620, 650, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(850, 590, 40, 40))
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(580, 580, 3, 110))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Фоторедактор"))
        self.pushButton.setText(_translate("Form", "Открыть"))
        self.pushButton_2.setText(_translate("Form", "Сохранить"))
        self.pushButton_3.setText(_translate("Form", "Добавить в видео"))
        self.label_2.setText(_translate("Form", "Создать изображение"))
        self.label_3.setText(_translate("Form", "x"))
        self.pushButton_4.setText(_translate("Form", "ОК"))
        self.label_4.setText(_translate("Form", "Изменить размеры изображения"))
        self.label_5.setText(_translate("Form", "x"))
        self.pushButton_5.setText(_translate("Form", "ОК"))
        self.label_6.setText(_translate("Form", "Фильтры"))
        self.label_7.setText(_translate("Form", "Чёрно-белый"))
        self.pushButton_6.setText(_translate("Form", "Применить"))
        self.label_8.setText(_translate("Form", "Контрастность"))
        self.pushButton_7.setText(_translate("Form", "Применить"))
        self.label_9.setText(_translate("Form", "Негатив"))
        self.pushButton_8.setText(_translate("Form", "Применить"))
        self.label_10.setText(_translate("Form", "Оттенки серого"))
        self.pushButton_9.setText(_translate("Form", "Применить"))
        self.label_11.setText(_translate("Form", "Сепия"))
        self.pushButton_10.setText(_translate("Form", "Применить"))
        self.label_12.setText(_translate("Form", "Контур"))
        self.pushButton_11.setText(_translate("Form", "Применить"))
        self.label_13.setText(_translate("Form", "Рисование"))
        self.pushButton_14.setText(_translate("Form", "Изменить цвет"))
        self.comboBox.setItemText(0, _translate("Form", "5"))
        self.comboBox.setItemText(1, _translate("Form", "1"))
        self.comboBox.setItemText(2, _translate("Form", "3"))
        self.comboBox.setItemText(3, _translate("Form", "8"))
        self.comboBox.setItemText(4, _translate("Form", "10"))
        self.label_14.setText(_translate("Form", "Размер кисти"))


# Фоторедактор
class PhotoEditor(QMainWindow, PhotoEditor_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('source/image/icon.png'))
        self.spinBox.setRange(1, 500)
        self.spinBox_2.setRange(1, 500)
        self.spinBox_3.setRange(1, 500)
        self.spinBox_4.setRange(1, 500)
        self.pushButton.clicked.connect(self.load_image)
        self.pushButton_2.clicked.connect(self.save_image)
        self.pushButton_3.clicked.connect(self.add_img_in_video)
        self.pushButton_4.clicked.connect(self.create_image)
        self.pushButton_5.clicked.connect(self.change_img_size)
        self.pushButton_6.clicked.connect(self.wh_b_filter)
        self.pushButton_7.clicked.connect(self.contrast)
        self.pushButton_8.clicked.connect(self.negative)
        self.pushButton_9.clicked.connect(self.shades_of_grey)
        self.pushButton_10.clicked.connect(self.sepia)
        self.pushButton_11.clicked.connect(self.contur)
        self.pushButton_12.clicked.connect(self.change_drawing_box_value)
        self.pushButton_14.clicked.connect(self.change_brushColor)
        self.pushButton_15.clicked.connect(self.eraser)
        self.comboBox.currentIndexChanged.connect(self.change_brushSize)
        self.open_image = ''
        self.update_flag = False
        self.drawing = False
        self.drawing_box = False
        self.brushSize = 3
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

    # Отрисовка и добавление изображений
    def paintEvent(self, event):
        if self.update_flag:
            canvasPainter = QPainter(self)
            canvasPainter.drawImage(self.image.rect(), self.image, self.image.rect())
            self.flag = False

    def load_image(self):
        img_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку',
                                               '', "Картинка(*.png *.jpg *png)")[0]
        img_name = img_name[:]
        if len(img_name) > 0:
            self.open_image = Image.open(img_name)
            if 500 < self.open_image.size[0] or 500 < self.open_image.size[1]:
                valid = QMessageBox.question(self, '',
                                             'Максимальный размер изображений 500 x 500!', QMessageBox.Yes)
            else:
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(img_name)
                self.update_flag = True

    def create_image(self):
        new_image = Image.new("RGB", (int(self.spinBox.text()), int(self.spinBox_2.text())), (255, 255, 255))
        img_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                               '', "Картинка(*.png *.jpg *png)")[0]
        if len(img_name) > 0:
            new_image.save(img_name)
            self.open_image = Image.open(img_name)
            self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
            self.image.load(img_name)
            self.update_flag = True

        else:
            valid = QMessageBox.question(self, '',
                                         'Для создания изображения его необходимо сохранить!', QMessageBox.Yes)

    def change_img_size(self):
        if self.open_image != '':
            img_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                                   '', "Картинка(*.png *.jpg *png)")[0]
            if len(img_name) > 0:
                self.image.save(img_name)
                self.open_image = Image.open(img_name)
                resized_image = self.open_image.resize((int(self.spinBox_3.text()), int(self.spinBox_4.text())))
                resized_image.save(img_name)
                self.open_image = Image.open(img_name)
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(img_name)
                self.update_flag = True
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение!', QMessageBox.Yes)

    # Смена значения переменной drawing_box, чтобы кисть для рисования не была активна всегда
    def change_drawing_box_value(self):
        if self.open_image != '':
            if self.drawing_box == True:
                self.drawing_box = False
            else:
                self.drawing_box = True
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение!', QMessageBox.Yes)
        self.brushColor = Qt.black
        self.pushButton_12.setStyleSheet("background-color:black;")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing_box == True:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() and Qt.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update_flag = True
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def change_brushColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pushButton_12.setStyleSheet("background-color: {}".format(
                color.name()))
            self.brushColor = color

    def change_brushSize(self):
        self.brushSize = int(self.comboBox.currentText())

    # Активация ластика
    def eraser(self):
        self.brushColor = Qt.white

    # ФИЛЬТРЫ

    def wh_b_filter(self):
        if self.open_image != '':
            img_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                                   '', "Картинка(*.png *.jpg *png)")[0]
            if len(img_name) > 0:
                coefficient = (((255 + 50) // 2) * 3)
                self.image.save(img_name)
                self.open_image = Image.open(img_name)
                pixels = self.open_image.load()
                x, y = self.open_image.size
                for i in range(x):
                    for j in range(y):
                        rgb = (pixels[i, j][0] + pixels[i, j][1] + pixels[i, j][2])
                        if rgb > coefficient:
                            pixels[i, j] = (255, 255, 255)
                        else:
                            pixels[i, j] = (0, 0, 0)
                self.open_image.save(img_name)
                self.open_image = Image.open(img_name)
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(img_name)
                self.update_flag = True
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение!', QMessageBox.Yes)

    def contrast(self):
        if self.open_image != '':
            img_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                                   '', "Картинка(*.png *.jpg *png)")[0]
            if len(img_name) > 0:
                self.image.save(img_name)
                self.open_image = Image.open(img_name)
                pixels = self.open_image.load()
                x, y = self.open_image.size
                middle_value_bright = 0
                for i in range(x):
                    for j in range(y):
                        r = pixels[i, j][0]
                        g = pixels[i, j][1]
                        b = pixels[i, j][2]
                        middle_value_bright += (r * 0.299) + (g * 0.587) + (b * 0.114)
                middle_value_bright /= (x * y)

                chanel = list()
                for i in range(256):
                    value = int(middle_value_bright + 2 * (i - middle_value_bright))
                    if value < 0:
                        temp = 0
                    elif value > 255:
                        temp = 255
                    chanel.append(value)

                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        pixels[i, j] = (chanel[r], chanel[g], chanel[b])
                self.open_image.save(img_name)
                self.open_image = Image.open(img_name)
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(img_name)
                self.update_flag = True
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение!', QMessageBox.Yes)

    def negative(self):
        if self.open_image != '':
            img_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                                   '', "Картинка(*.png *.jpg *png)")[0]
            if len(img_name) > 0:
                self.image.save(img_name)
                self.open_image = Image.open(img_name)
                pixels = self.open_image.load()
                x, y = self.open_image.size
                for i in range(x):
                    for j in range(y):
                        r = int(255 - pixels[i, j][0])
                        g = int(255 - pixels[i, j][1])
                        b = int(255 - pixels[i, j][2])
                        pixels[i, j] = (r, g, b)
                self.open_image.save(img_name)
                self.open_image = Image.open(img_name)
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(img_name)
                self.update_flag = True
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение!', QMessageBox.Yes)

    def shades_of_grey(self):
        if self.open_image != '':
            img_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                                   '', "Картинка(*.png *.jpg *png)")[0]
            if len(img_name) > 0:
                self.image.save(img_name)
                self.open_image = Image.open(img_name)
                pixels = self.open_image.load()
                x, y = self.open_image.size
                for i in range(x):
                    for j in range(y):
                        r = int(pixels[i, j][0] * 0.22)
                        g = int(pixels[i, j][1] * 0.72)
                        b = int(pixels[i, j][2] * 0.07)
                        shades = (r + g + b)
                        pixels[i, j] = (shades, shades, shades)
                self.open_image.save(img_name)
                self.open_image = Image.open(img_name)
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(img_name)
                self.update_flag = True
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение!', QMessageBox.Yes)

    def sepia(self):
        if self.open_image != '':
            img_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                                   '', "Картинка(*.png *.jpg *png)")[0]
            if len(img_name) > 0:
                self.image.save(img_name)
                self.open_image = Image.open(img_name)
                pixels = self.open_image.load()
                x, y = self.open_image.size
                for i in range(x):
                    for j in range(y):
                        r = int(pixels[i, j][0] * 0.393 + pixels[i, j][1] * 0.769 + pixels[i, j][2] * 0.189)
                        g = int(pixels[i, j][0] * 0.349 + pixels[i, j][1] * 0.686 + pixels[i, j][2] * 0.168)
                        b = int(pixels[i, j][0] * 0.272 + pixels[i, j][1] * 0.534 + pixels[i, j][2] * 0.131)
                        pixels[i, j] = (r, g, b)
                self.open_image.save(img_name)
                self.open_image = Image.open(img_name)
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(img_name)
                self.update_flag = True
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение!', QMessageBox.Yes)

    def contur(self):
        if self.open_image != '':
            img_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                                   '', "Картинка(*.png *.jpg *png)")[0]
            if len(img_name) > 0:
                self.image.save(img_name)
                self.open_image = Image.open(img_name)
                self.open_image = self.open_image.filter(ImageFilter.CONTOUR)
                self.open_image.save(img_name)
                self.open_image = Image.open(img_name)
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(img_name)
                self.update_flag = True
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение!', QMessageBox.Yes)

    def add_img_in_video(self):
        global SAVED_IMAGE, USER
        if self.open_image != '':
            file_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                                    '', "Картинка(*.png *.jpg *png)")[0]
            if len(file_name) > 0:
                self.image.save(file_name)
                self.open_image = Image.open(file_name)
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(file_name)
                self.update_flag = True
                connect = sqlite3.connect('RedactorDB.db')
                cursor = connect.cursor()
                result = cursor.execute('''SELECT save_img FROM Users
                WHERE login = ?''', (USER,)).fetchone()
                if (result is None) or (result[0] == '') or (result[0] is None):
                    result = file_name
                else:
                    result = result[0] + '?' + file_name
                SAVED_IMAGE = result
                result = cursor.execute('''UPDATE Users
                SET save_img = ?
                WHERE login = ?''', (SAVED_IMAGE, USER)).fetchall()
                connect.commit()
                connect.close()
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение в поле для редактирования!', QMessageBox.Yes)

    def save_image(self):
        if self.open_image != '':
            img_name = QFileDialog.getSaveFileName(self, 'Сохранить картинку',
                                                   '', "Картинка(*.png *.jpg *png)")[0]
            if len(img_name) > 0:
                self.image.save(img_name)
                self.open_image = Image.open(img_name)
                self.image = QImage(self.open_image.size[0], self.open_image.size[1], QImage.Format_RGB32)
                self.image.load(img_name)
                self.update_flag = True
        else:
            valid = QMessageBox.question(self, '',
                                         'Загрузите изображение!', QMessageBox.Yes)


# Форма видеоредактора
class VideoEditor_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1110, 746)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color:#d0eaf5;")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 800, 520))
        self.scrollArea.setStyleSheet("background-color:#b7db97;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 798, 518))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(820, 10, 281, 192))
        self.tableWidget.setStyleSheet("background-color:white;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(820, 240, 221, 23))
        self.pushButton.setStyleSheet("background-color:white;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 210, 220, 23))
        self.pushButton_2.setStyleSheet("background-color:white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1050, 240, 20, 23))
        self.pushButton_3.setStyleSheet("background-color:white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(820, 280, 281, 192))
        self.tableWidget_2.setStyleSheet("background-color:white;")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(820, 480, 220, 23))
        self.pushButton_4.setStyleSheet("background-color:white;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(820, 510, 221, 23))
        self.pushButton_5.setStyleSheet("background-color:white;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(1050, 510, 20, 23))
        self.pushButton_6.setStyleSheet("background-color:white;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(20, 630, 550, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("background-color:#d0eaf5;")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 670, 550, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("background-color:#d0eaf5;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(530, 630, 140, 30))
        self.pushButton_8.setStyleSheet("background-color:white;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 580, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(180, 580, 51, 30))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 570, 240, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 620, 260, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(0, 710, 310, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(820, 700, 280, 23))
        self.pushButton_7.setStyleSheet("background-color:white;")
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Видеоредактор"))
        self.pushButton.setText(_translate("Form", "Добавить сохранённые изображения"))
        self.pushButton_2.setText(_translate("Form", "Загрузить изображение"))
        self.pushButton_3.setText(_translate("Form", "с"))
        self.pushButton_4.setText(_translate("Form", "Загрузить музыку"))
        self.pushButton_5.setText(_translate("Form", "Добавить сохранённую музыку"))
        self.pushButton_6.setText(_translate("Form", "c"))
        self.radioButton.setText(_translate("Form", "Увеличение изображений  в соответствие  максимальным размерам"))
        self.radioButton_2.setText(_translate("Form", "Уменьшение изображений  в соответствие минимальным размерам"))
        self.pushButton_8.setText(_translate("Form", "Выбрать цвет фона"))
        self.label.setText(_translate("Form", "Кадров в секунду"))
        self.pushButton_7.setText(_translate("Form", "Сохранить"))


class VidoeEditor(QMainWindow, VideoEditor_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('source/image/icon.png'))
        self.pushButton.clicked.connect(self.add_saved_image)
        self.pushButton_2.clicked.connect(self.add_image)
        self.pushButton_3.clicked.connect(self.clear_saved_image)
        self.pushButton_4.clicked.connect(self.add_music)
        self.pushButton_5.clicked.connect(self.add_saved_music)
        self.pushButton_6.clicked.connect(self.clear_saved_music)
        self.pushButton_7.clicked.connect(self.save_video)
        self.pushButton_8.clicked.connect(self.choice_background)
        self.pushButton_9 = QPushButton('Редактировать изображения', self)
        self.pushButton_9.resize(280, 23)
        self.pushButton_9.move(820, 640)
        self.pushButton_9.setStyleSheet("background-color:white;")
        self.pushButton_10 = QPushButton('Создать музыку', self)
        self.pushButton_10.resize(280, 23)
        self.pushButton_10.move(820, 670)
        self.pushButton_10.setStyleSheet("background-color:white;")
        self.pushButton_9.clicked.connect(self.open_photo_editor)
        self.pushButton_10.clicked.connect(self.open_music_editor)
        self.flag_add_image = True
        self.flag_add_music = True
        self.doubleSpinBox.setRange(0.1, 100.0)
        self.doubleSpinBox.setValue(1.0)
        self.load_tables()
        self.horisontal_box = QHBoxLayout(self)
        self.pnl = QWidget(self)
        self.background_image_color = (255, 255, 255)
        self.images = list()
        self.music = list()

    # Загрузка таблиц для отображения выбранных изображений и музыки
    def load_tables(self):
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Изображение', 'Удалить'])
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.itemChanged.connect(self.pre_delete_image)
        self.tableWidget_2.itemChanged.connect(self.delete_music1)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setHorizontalHeaderLabels(['Выбранная музыка', 'Удалить'])
        self.tableWidget_2.resizeColumnsToContents()

    def add_image(self):
        if self.flag_add_image:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку',
                                                '', "Картинка(*.png *.jpg *.jpeg)")[0]
            if len(fname) > 0:
                self.images.append([fname, ''])
        self.tableWidget.setRowCount(len(self.images))
        for i, row in enumerate(self.images):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem.split('/')[-1]))
                self.tableWidget.item(i, j).setBackground(QColor(181, 237, 133))
        self.tableWidget.resizeColumnsToContents()
        self.flag_add_image = True
        self.pnl = QWidget(self)
        self.horisontal_box = QHBoxLayout(self)
        self.scrollArea.setWidget(self.pnl)
        for elem in self.images:
            self.pixmap = QPixmap(elem[0])
            lbl = QLabel()
            lbl.setPixmap(self.pixmap)
            self.horisontal_box.addWidget(lbl)
        self.pnl.setLayout(self.horisontal_box)
        self.scrollArea.setWidget(self.pnl)

    # Добавление сохранённых изображений
    def add_saved_image(self):
        global SAVED_IMAGE
        if len(SAVED_IMAGE) != 0:
            for elem in SAVED_IMAGE.split('?'):
                if os.path.isfile(elem):
                    self.images.append([elem, ''])
            self.flag_add_image = False
            self.add_image()
        else:
            valid = QMessageBox.question(self, '',
                                         'У вас нет сохранённых изображений!', QMessageBox.Yes)

    # Очистка списка сохранённых изображений
    def clear_saved_image(self):
        global SAVED_IMAGE
        if len(SAVED_IMAGE) != 0:
            valid = QMessageBox.question(self, '',
                                         'ВСЕ сохранённые изображения будут удалены!'
                                         'Продолжить?', QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                connect = sqlite3.connect('RedactorDB.db')
                cursor = connect.cursor()
                result = cursor.execute('''UPDATE Users
                SET save_img = ?
                WHERE login = ?''', ('', USER))
                connect.commit()
                connect.close()
                SAVED_IMAGE = list()
        else:
            valid = QMessageBox.question(self, '',
                                         'У вас нет сохранённых изображений!', QMessageBox.Yes)

    # Функция для вызова обновления таблицы, т.к. иначе функция delete_image() будет вызываться при каждом
    # внесении изменений в таблицу
    def pre_delete_image(self):
        self.delete_image()

    # Удаление ненужных изображений
    def delete_image(self):
        if inspect.stack()[2][3] == '<module>':
            i = 1
            for j in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(j, i)
                if item is not None:
                    if item.text() == '-':
                        valid = QMessageBox.question(self, '',
                                                     'Изображение будет удалено!'
                                                     'Продолжить?', QMessageBox.Yes, QMessageBox.No)
                        if len(self.images) >= j + 1 and valid == QMessageBox.Yes:
                            del self.images[j]
                            self.flag_add_image = False
                            self.add_image()
                        else:
                            self.tableWidget.setItem(j, i, QTableWidgetItem(''))

    def add_music(self):
        if self.flag_add_music:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать музыку',
                                                '', "Музыка(*.mp3)")[0]
            if len(fname) > 0:
                self.music.append([fname, ''])
        self.tableWidget_2.setRowCount(len(self.music))
        for i, row in enumerate(self.music):
            for j, elem in enumerate(row):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(elem.split('/')[-1]))
                self.tableWidget_2.item(i, j).setBackground(QColor(181, 237, 133))
        self.tableWidget_2.resizeColumnsToContents()
        self.flag_add_music = True

    def add_saved_music(self):
        global SAVED_MUSIC
        if len(SAVED_MUSIC) != 0:
            for elem in SAVED_MUSIC.split('?'):
                if os.path.isfile(elem):
                    self.music.append([elem, ''])
            self.flag_add_music = False
            self.add_music()
        else:
            valid = QMessageBox.question(self, '',
                                         'У вас нет сохранённой музыки!', QMessageBox.Yes)

    def clear_saved_music(self):
        global SAVED_MUSIC
        if len(SAVED_MUSIC) != 0:
            valid = QMessageBox.question(self, '',
                                         'ВСЯ сохранённая музыка будет удалена!'
                                         'Продолжить?', QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                connect = sqlite3.connect('RedactorDB.db')
                cursor = connect.cursor()
                result = cursor.execute('''UPDATE Users
                SET save_mp3 = ?
                WHERE login = ?''', ('', USER))
                connect.commit()
                connect.close()
                SAVED_MUSIC = list()
        else:
            valid = QMessageBox.question(self, '',
                                         'У вас нет сохранённой музыки!', QMessageBox.Yes)

    def delete_music1(self):
        self.delete_music()

    def delete_music(self):
        if inspect.stack()[2][3] == '<module>':
            i = 1
            for j in range(self.tableWidget_2.rowCount()):
                item = self.tableWidget_2.item(j, i)
                if item is not None:
                    if item.text() == '-':
                        valid = QMessageBox.question(self, '',
                                                     'Аудио-файл будет будет удален!'
                                                     'Продолжить?', QMessageBox.Yes, QMessageBox.No)
                        if len(self.music) >= j + 1 and valid == QMessageBox.Yes:
                            del self.music[j]
                            self.flag_add_music = False
                            self.add_music()
                        else:
                            self.tableWidget_2.setItem(j, i, QTableWidgetItem(''))

    # Выбор фона для увеличения изображенний
    def choice_background(self):
        self.background_image_color = QColorDialog.getColor().name()

    # Увеличение изображений
    def increase_images(self):
        max_x = 0
        max_y = 0
        for elem in self.images:
            img = Image.open(elem[0])
            x, y = img.size
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
        counter = 0
        for elem in self.images:
            new_image = Image.new("RGB", (max_x, max_y), self.background_image_color)
            img = Image.open(elem[0])
            x, y = img.size
            x0 = (max_x - x) // 2
            y0 = (max_y - y) // 2
            new_image.paste(img, (x0, y0))
            new_image.save(f'image{counter}.jpg')
            elem[0] = f'image{counter}.jpg'
            counter += 1

    # Уменьшение изображений
    def decrease_images(self):
        min_x = 10000000000000
        min_y = 10000000000000
        for elem in self.images:
            img = Image.open(elem[0])
            x, y = img.size
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
        counter = 0
        for elem in self.images:
            original_image = Image.open(elem[0])
            resized_image = original_image.resize((min_x, min_y))
            resized_image.save(f'image_i_o{counter}.jpg')
            elem[0] = f'image_i_o{counter}.jpg'
            counter += 1

    # Создание видео
    def make_video(self):
        frames = [elem[0] for elem in self.images]
        frame = cv2.imread(frames[0])
        writer = cv2.VideoWriter('output_slides_m.avi', cv2.VideoWriter_fourcc(*'MJPG'),
                                 float(self.doubleSpinBox.text().replace(',', '.')), (frame.shape[1], frame.shape[0]),
                                 isColor=len(frame.shape) > 2)
        for frame in map(cv2.imread, frames):
            writer.write(frame)
        writer.release()
        cv2.destroyAllWindows()
        if len(self.music) == 0:
            valid = QMessageBox.question(self, '',
                                         'Вы не добавили музыку в видео!'
                                         'Продолжить без музыки?', QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                valid = QMessageBox.question(self, '',
                                             'Видео сохранено в папку с редактором!'
                                             'Имя файла - output_slides_m.avi', QMessageBox.Yes)
                self.images = list()
                self.music = list()
                self.tableWidget.clear()
                self.tableWidget_2.clear()
                self.load_tables()
                self.pnl = QWidget(self)
                self.horisontal_box = QHBoxLayout(self)
                self.scrollArea.setWidget(self.pnl)
        else:
            valid = QMessageBox.question(self, '',
                                         'Внимание! Возможно несовпадение длины ряда изображений с длиной музыки!\n'
                                         'Продолжить?', QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                with open('music_for_slides.mp3', 'wb') as music:
                    for elem in self.music:
                        music.write(open(elem[0], 'rb').read())
                my_clip = mpe.VideoFileClip(r'output_slides_m.avi')
                file_name = QFileDialog.getSaveFileName(self, 'Сохранить видео',
                                                        '', "Видео(*.mp4)")[0]
                if len(file_name) > 0:
                    my_clip.write_videofile(rf'{file_name}', audio='music_for_slides.mp3')
                    self.images = list()
                    self.music = list()
                    self.tableWidget.clear()
                    self.tableWidget_2.clear()
                    self.load_tables()
                    self.pnl = QWidget(self)
                    self.horisontal_box = QHBoxLayout(self)
                    self.scrollArea.setWidget(self.pnl)

    def open_photo_editor(self):
        self.photoEditor = PhotoEditor()
        self.photoEditor.show()

    def open_music_editor(self):
        self.musicEditor = Piano()
        self.musicEditor.show()

    def save_video(self):
        if self.radioButton_2.isChecked():
            if len(self.images) > 4:
                self.decrease_images()
                self.make_video()
            else:
                valid = QMessageBox.question(self, '',
                                             'Для создания видео добавьте 5 и более изображений!', QMessageBox.Yes)
        else:
            if len(self.images) > 4:
                self.increase_images()
                self.make_video()
            else:
                valid = QMessageBox.question(self, '',
                                             'Для создания видео добавьте 5 и более изображений!', QMessageBox.Yes)


# Форма регистрации
class Registration_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(409, 389)
        Form.setStyleSheet(" background-image: url('source/image/background_enter.jpg');")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 50, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(71, 133, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(64, 187, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(65, 248, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 130, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 190, 220, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 250, 220, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 310, 220, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Регистрация"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.label_2.setText(_translate("Form", "Логин"))
        self.label_3.setText(_translate("Form", "Пароль"))
        self.label_4.setText(_translate("Form", "Пароль"))
        self.pushButton.setText(_translate("Form", "Зарегистрироваться"))


# Регистрация
class Registration(QMainWindow, Registration_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('source/image/icon.png'))
        self.pushButton.clicked.connect(self.registration)
        self.connect = sqlite3.connect('RedactorDB.db')
        self.cursor = self.connect.cursor()

    def registration(self):
        global SAVED_IMAGE, SAVED_MUSIC, USER
        login, password1, password2 = self.lineEdit.text(), self.lineEdit_2.text(), \
                                      self.lineEdit_3.text()
        if len(login) == 0 or len(password2) == 0 or len(password2) == 0:
            valid = QMessageBox.question(self, 'Error',
                                         'Все поля должны быть заполнены!', QMessageBox.Yes)
        else:
            logins = self.cursor.execute(f'''SELECT login FROM Users''').fetchall()
            logins = [elem[0] for elem in logins]
            if login not in logins:
                if password1 == password2:
                    result = self.cursor.execute(f'''INSERT INTO Users(login,password)
                     VALUES(?,?)''', (login, password1,)).fetchall()
                    self.connect.commit()
                    USER = login
                    self.videoEditor = VidoeEditor()
                    self.videoEditor.show()
                else:
                    valid = QMessageBox.question(self, 'Error',
                                                 'Пароли не совпадают!',
                                                 QMessageBox.Yes)
            else:
                valid = QMessageBox.question(self, 'Error',
                                             'Пользователь с таким логином уже существует!',
                                             QMessageBox.Yes)


# Форма входа
class Enter_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet(" background-image: url('source/image/background_enter.jpg');")
        Form.resize(419, 385)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 40, 260, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(129, 130, 201, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 180, 201, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 240, 141, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 270, 141, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Вход"))
        self.label.setText(_translate("Form", "Видеоредактор"))
        self.label_2.setText(_translate("Form", "Логин"))
        self.label_3.setText(_translate("Form", "Пароль"))
        self.pushButton.setText(_translate("Form", "Вход"))
        self.pushButton_2.setText(_translate("Form", "Регистрация"))


# Вход
class Enter(QMainWindow, Enter_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('source/image/icon.png'))
        self.connect = sqlite3.connect('RedactorDB.db')
        self.cursor = self.connect.cursor()
        self.pushButton.clicked.connect(self.enter)
        self.pushButton_2.clicked.connect(self.registration)

    def enter(self):
        global USER, SAVED_IMAGE, SAVED_MUSIC
        login, password = self.lineEdit.text(), self.lineEdit_2.text()
        if len(login) == 0 or len(password) == 0:
            valid = QMessageBox.question(self, 'Error',
                                         'Все поля должны быть заполнены!', QMessageBox.Yes)
        else:
            logins = self.cursor.execute(f'''SELECT login FROM Users''').fetchall()
            logins = [elem[0] for elem in logins]
            if login in logins:
                result = self.cursor.execute(f'''SELECT password FROM Users
                WHERE login = ?''', (login,)).fetchone()
                if password == str(result[0]):
                    USER = login
                    result = self.cursor.execute('''SELECT save_img FROM Users
                               WHERE login = ?''', (USER,)).fetchone()
                    if result[0] is None:
                        SAVED_IMAGE = ''
                    else:
                        SAVED_IMAGE = result[0]
                    result = self.cursor.execute('''SELECT save_mp3 FROM Users
                               WHERE login = ?''', (USER,)).fetchone()
                    if result[0] is None:
                        SAVED_MUSIC = ''
                    else:
                        SAVED_MUSIC = result[0]
                    self.videoEditor = VidoeEditor()
                    self.videoEditor.show()
                else:
                    valid = QMessageBox.question(self, 'Error',
                                                 'Неверный пароль!', QMessageBox.Yes)
            else:
                valid = QMessageBox.question(self, 'Error',
                                             'Неверное имя пользователя!', QMessageBox.Yes)

    def registration(self):
        self.registration = Registration()
        self.registration.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Enter()
    ex.show()
    sys.exit(app.exec_())