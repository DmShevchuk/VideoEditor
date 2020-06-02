import sys
import os
import sqlite3
import inspect
import cv2
import moviepy.editor as mpe
import pygame
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QFileDialog, QTableWidgetItem,
                             QMessageBox, QHBoxLayout, QLabel, QColorDialog, QPushButton)
from PyQt5.QtGui import QPixmap, QColor, QIcon, QImage, QPainter, QPen
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt, QPoint
from ui_forms import RegistrationForm, EnterForm, PianoForm, PhotoEditorForm, VideoEditorForm

# Переменные с ником пользователя, его сохранённой музыкой и изображениями
USER = ''
SAVED_IMAGE = list()
SAVED_MUSIC = list()


# Музыкальный редактор
class Piano(QMainWindow, PianoForm):
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


# Фоторедактор
class PhotoEditor(QMainWindow, PhotoEditorForm):
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
        self.pushButton_11.clicked.connect(self.contour)
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
            # Максимальный размер 500 * 500 пикселей обусловлен скоростью обновления полотна,
            # а также скоростью наложения фильтров
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

    def contour(self):
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


class VidoeEditor(QMainWindow, VideoEditorForm):
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
        # Проверка, что функция вызвана другой функцией
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

    # Вызов функции удаления музыки
    # Иначе удаление будет происходить при любом изменении в таблице с музыкой
    def delete_music1(self):
        self.delete_music()

    def delete_music(self):
        # Проверка, что функция была вызвана другой функцией
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

    # Увеличение изображений, чтобы при создании видео все картинки были одного размера
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

    # Уменьшение изображений, чтобы при создании видео все картинки были одного размера
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
        # Создаём видео из добавленных изображений
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
                # Записываем добавленную музыку
                with open('music_for_slides.mp3', 'wb') as music:
                    for elem in self.music:
                        music.write(open(elem[0], 'rb').read())
                my_clip = mpe.VideoFileClip(r'output_slides_m.avi')
                file_name = QFileDialog.getSaveFileName(self, 'Сохранить видео',
                                                        '', "Видео(*.mp4)")[0]
                if len(file_name) > 0:
                    # Добавляем музыку в видео
                    my_clip.write_videofile(rf'{file_name}', audio='music_for_slides.mp3')
                    # Очищаем все поля редактора для дальнейшей работы
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


# Регистрация
class Registration(QMainWindow, RegistrationForm):
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


# Вход
class Enter(QMainWindow, EnterForm):
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
        # Проверка правильности введённых данных
        else:
            logins = self.cursor.execute(f'''SELECT login FROM Users''').fetchall()
            logins = [elem[0] for elem in logins]
            if login in logins:
                result = self.cursor.execute(f'''SELECT password FROM Users
                WHERE login = ?''', (login,)).fetchone()
                if password == str(result[0]):
                    # Загрузка сохранённых ранее изображений и музыки в соответствующие переменные
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
                    # Открытие окна редактора
                    self.videoEditor = VidoeEditor()
                    self.videoEditor.show()
                else:
                    valid = QMessageBox.question(self, 'Error',
                                                 'Неверный пароль!', QMessageBox.Yes)
            else:
                valid = QMessageBox.question(self, 'Error',
                                             'Неверное имя пользователя!', QMessageBox.Yes)

    # Вызов формы регистрации
    def registration(self):
        self.registration = Registration()
        self.registration.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Enter()
    ex.show()
    sys.exit(app.exec_())
