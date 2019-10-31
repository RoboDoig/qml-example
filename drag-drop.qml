import QtQuick 2.0
import QtQuick.Window 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.13
import QtQuick.Shapes 1.11

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("drag-drop")

    CustomDragBox {
        id: customDragBox
        x: 270
        y: 190
    }
}

