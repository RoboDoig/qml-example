import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.13

Rectangle {
    id: rectangle
    objectName: "dragBox"
    width: 100
    height: 100
    color: "#fdfdfd"
    radius: 0
    border.width: 4

    MouseArea {
        anchors.fill: parent
        drag.target: rectangle
        onReleased: iface.on_released(parent)
        propagateComposedEvents: true
    }

    ProgressBar {
        id: progressBar
        x: 8
        y: 76
        width: 84
        height: 24
        value: 0.5
    }
}
