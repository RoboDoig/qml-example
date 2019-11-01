from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QVariant, QTimer, QThread, QUrl
from PyQt5.QtQml import QQmlComponent
from PyQt5.QtQuick import QQuickItem


class Interface(QObject):
    def __init__(self, app, context, parent, engine):
        QObject.__init__(self, parent)
        self.app = app
        self.ctx = context
        self.win = parent
        self.engine = engine

    @pyqtSlot(QVariant)
    def on_released(self, obj):
        print(obj.property('x'), obj.property('y'))

    @pyqtSlot(QQuickItem)
    def create_new(self, obj):
        print('new created', obj)

        # Was trying to do within function, couldn't figure out. Instead object gets passed from QML side.
        # new_component = QQmlComponent(self.engine)
        # new_component.loadUrl(QUrl('../CustomDragBox.qml'))
        # itm = new_component.create()
        # itm.setParent(self.win)
        #
        # for child in self.win.findChildren(QObject, 'dragBox'):
        #     print(child, child.property('visible'), child.property('x'), child.parent())
