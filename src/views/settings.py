from PyQt6.QtMultimedia import QSoundEffect
import views
from assets.animations import Animation
from PyQt6.QtCore import QParallelAnimationGroup, QPoint, QRect, QUrl, Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QComboBox, QLabel, QPushButton, QSlider, QWidget
from backend.sound import play, changeVol


class Settings_Renderer:
    def __init__(self, window) -> None:
        self.window = window
        self.effect = QSoundEffect()
        self.animation = QParallelAnimationGroup()

    def render(self):
        self.mainPage = QWidget()
        self.mainPage.resizeEvent = lambda event: self.responser(
            self.mainPage.geometry()
        )
        # Main Background

        self.settingsBG = QLabel(self.mainPage)
        self.settingsBG.setPixmap(QPixmap("../img/main_bg.png"))
        self.settingsBG.setScaledContents(True)

        # Mask
        self.settingsBM = QLabel(self.mainPage)
        self.settingsBM.setStyleSheet("background-color: rgba(0, 0, 0, 170);")
        self.animation.addAnimation(Animation.unfade(self.settingsBM, 300))

        # font
        font = QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)

        # header
        self.header = QLabel(self.mainPage)
        self.header.setGeometry(QRect(0, 70, self.window.width(), 70))
        self.header.setStyleSheet(
            "background-color: transparent; font-size: 56px; font-family: Comfortaa; color: #ebcb8b"
        )
        self.header.setText("Settings")
        self.header.setAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignCenter
        )

        # in-game sound
        self.gameBackgroundMusic = QLabel(self.mainPage)
        self.gameBackgroundMusic.setGeometry(QRect(520, 250, 200, 61))
        self.gameBackgroundMusic.setText("In-Game Sound")
        self.gameBackgroundMusic.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignLeft
        )
        self.gameBackgroundMusic.setFont(font)
        self.gameBackgroundMusic.setStyleSheet(
            "color: #ebcb8b;background-color: transparent"
        )

        # background game sound
        self.inGameMusic = QLabel(self.mainPage)
        self.inGameMusic.setText("Background Music")
        self.inGameMusic.setGeometry(QRect(520, 340, 200, 61))
        self.inGameMusic.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignLeft
        )
        self.inGameMusic.setStyleSheet("color: #ebcb8b;background-color: transparent")
        self.inGameMusic.setFont(font)

        # seletion of bg music
        self.songBoxLabel = QLabel(self.mainPage)
        self.songBoxLabel.setText("Audio")
        self.songBoxLabel.setGeometry(QRect(520, 460, 200, 61))
        self.songBoxLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignLeft
        )
        self.songBoxLabel.setStyleSheet("color: #ebcb8b;background-color: transparent")
        self.songBoxLabel.setFont(font)

        # in-game sound slider
        self.gameBackgroundMusicSlider = QSlider(self.mainPage)
        self.gameBackgroundMusicSlider.setGeometry(QRect(920, 250, 300, 61))
        self.gameBackgroundMusicSlider.setOrientation(Qt.Orientation.Horizontal)
        self.gameBackgroundMusicSlider.setValue(100)
        self.gameBackgroundMusicSlider.setStyleSheet(
            """
            QSlider{
                background-color: transparent
            }

            QSlider::handle{
                background-color: #ebcb8b;
                border-radius: 10px
            }
            """
        )
        # self.gameBackgroundMusicSlider.setFont(font)
        # elf.gameSoundSlider.valueChanged.connect(self.updateSound)

        # bg sound slider
        self.inGameMusicSlider = QSlider(self.mainPage)
        self.inGameMusicSlider.setGeometry(QRect(920, 340, 300, 61))
        self.inGameMusicSlider.setValue(100)
        self.inGameMusicSlider.setOrientation(Qt.Orientation.Horizontal)
        self.inGameMusicSlider.setStyleSheet(
            "color: #ebcb8b;background-color: transparent"
        )
        self.inGameMusicSlider.setStyleSheet(
            """
            QSlider{
                background-color: transparent
            }

            QSlider::handle{
                background-color: #ebcb8b;
                border-radius: 10px
            }
            """
        )
        self.inGameMusicSlider.setFont(font)
        self.inGameMusicSlider.valueChanged.connect(self.updateSound)

        # bg-audio selector
        self.songBox = QComboBox(self.mainPage)
        self.songBox.setGeometry(QRect(920, 440, 300, 61))
        self.songBox.setFont(font)
        self.songBox.setStyleSheet(
            "color: #ebcb8b;background-color: rgb(125, 125, 125);"
        )

        self.songBox.addItem("casino1")
        self.songBox.addItem("casino2")
        self.songBox.addItem("casino3")
        self.songBox.currentTextChanged.connect(self.updatePlayer)

        # back-button
        self.menuPushButton = QPushButton(self.mainPage)
        self.menuPushButton.setGeometry(QRect(710, 670, 271, 61))
        self.menuPushButton.setFont(font)
        self.menuPushButton.setText("Back to Main Menu")
        self.menuPushButton.setStyleSheet(
            "color: #ebcb8b;\n" "background-color: rgb(125, 125, 125);"
        )

        self.menuPushButton.clicked.connect(
            lambda: self.window.setCentralWidget(
                views.menu.MenuRenderer(self.window).render()
            )
        )

        self.animation.start()
        return self.mainPage

    def updatePlayer(self, _):
        volume = self.gameBackgroundMusicSlider.value() / 100
        song = self.songBox.currentText()
        play(sound=song, volume=volume)

    def updateSound(self, _):
        changeVol(self.inGameMusicSlider.value() / 100)

    def responser(self, geometry: QRect):
        self.settingsBG.setGeometry(geometry)
        self.settingsBG.move(QPoint(0, 0))
        self.settingsBM.setGeometry(self.settingsBG.geometry())
        self.header.setGeometry(QRect(0, 70, self.window.width(), 100))
        self.gameBackgroundMusic.setGeometry(
            QRect(0.35 * self.settingsBG.width(), 250, 200, 61)
        )
        self.inGameMusic.setGeometry(
            QRect(0.35 * self.settingsBG.width(), 340, 200, 61)
        )
        self.songBoxLabel.setGeometry(
            QRect(0.35 * self.settingsBG.width(), 460, 200, 61)
        )
        self.gameBackgroundMusicSlider.setGeometry(
            QRect(0.6 * self.settingsBG.width(), 250, 0.1 * self.settingsBG.width(), 20)
        )

        self.inGameMusicSlider.setGeometry(
            QRect(0.6 * self.settingsBG.width(), 340, 0.1 * self.settingsBG.width(), 20)
        )

        self.songBox.setGeometry(
            QRect(0.6 * self.settingsBG.width(), 440, 0.1 * self.settingsBG.width(), 61)
        )

        self.menuPushButton.setGeometry(
            QRect(0.43 * self.settingsBG.width(), 670, 271, 61)
        )
