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

        self.time_length = 5000

    @pyqtSlot()
    def action(self):
        print('action')

    @pyqtSlot()
    def button(self):
        self.worker.time_length = self.time_length
        self.thread.start()
        self.signal_start_job.emit()
        self.worker.timerVal.connect(self.update_progress_bar)

    @pyqtSlot(float)
    def update_progress_bar(self, value):
        progress = (self.time_length-value)/self.time_length
        self.progressBar.setProperty('value', progress)

    @pyqtSlot(str)
    def set_time(self, string):
        try:
            self.time_length = float(string)
        except:
            print('invalid value')


class Worker(QObject):
    timerVal = pyqtSignal(float)
    time_length = 5000

    @pyqtSlot()
    def run(self):
        timer = QTimer()
        timer.start(self.time_length)
        while timer.remainingTime() > 0:
            self.timerVal.emit(timer.remainingTime())
            time.sleep(0.05)
        self.timerVal.emit(timer.remainingTime())
