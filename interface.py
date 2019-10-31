from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QVariant, QTimer, QThread
import time


class Interface(QObject):
    signal_start_job = pyqtSignal()

    def __init__(self, app, context, parent):
        QObject.__init__(self, parent)
        self.app = app
        self.ctx = context
        self.win = parent

        self.progressBar = self.win.findChild(QObject, 'progressBar')

        self.worker = Worker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.signal_start_job.connect(self.worker.run)

    @pyqtSlot()
    def action(self):
        print('action')

    @pyqtSlot()
    def button(self):
        self.thread.start()
        self.signal_start_job.emit()
        self.worker.timerVal.connect(self.update_progress_bar)

    @pyqtSlot(float)
    def update_progress_bar(self, value):
        progress = (5000-value)/5000
        self.progressBar.setProperty('value', progress)


class Worker(QObject):
    timerVal = pyqtSignal(float)

    @pyqtSlot()
    def run(self):
        timer = QTimer()
        timer.start(5000)
        while timer.remainingTime() > 0:
            self.timerVal.emit(timer.remainingTime())
            time.sleep(0.05)
        self.timerVal.emit(timer.remainingTime())
