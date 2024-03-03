import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QPoint

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('透明ウィンドウ')
        self.setGeometry(0, 0, 1280, 400)
        # ウィンドウを中央に配置
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())


        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景を透明にする
        self.setWindowFlags(Qt.FramelessWindowHint)  # ウィンドウの枠を非表示にする

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        semiTransparentFrame = QFrame(centralWidget)
        semiTransparentFrame.setStyleSheet("background-color: rgba(16, 160, 64, 160);")
        semiTransparentFrame.setFrameShape(QFrame.StyledPanel)
        layout.addWidget(semiTransparentFrame)

        transparentFrame = QFrame(centralWidget)
        transparentFrame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        transparentFrame.setFrameShape(QFrame.StyledPanel)
        layout.addWidget(transparentFrame)

        semiTransparentFrame = QFrame(centralWidget)
        semiTransparentFrame.setStyleSheet("background-color: rgba(16, 160, 64, 160);")
        semiTransparentFrame.setFrameShape(QFrame.StyledPanel)
        layout.addWidget(semiTransparentFrame)

        # マウスイベント用の変数初期化
        self.oldPos = None
        self.isResizing = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()
        elif event.button() == Qt.RightButton:
            self.oldPos = event.globalPos()
            self.isResizing = True

    def mouseMoveEvent(self, event):
        if not self.oldPos:
            return
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        elif event.buttons() == Qt.RightButton and self.isResizing:
            delta = event.globalPos() - self.oldPos
            self.resize(self.width() + delta.x(), self.height() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            self.isResizing = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec_())
