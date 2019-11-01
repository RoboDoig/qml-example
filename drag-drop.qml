import QtQuick 2.0
import QtQuick.Window 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.13
import QtQuick.Shapes 1.11

ApplicationWindow {
    id: root
    visible: true
    objectName: "applicationWindow"
    width: 640
    height: 480
    title: qsTr("drag-drop")

    Button {
        id: button
        objectName: "button"
        x: 0
        y: 0
        text: qsTr("Create New")
        onClicked: {
            iface.create_new(Qt.createComponent("CustomDragBox.qml").createObject(root))
        }
    }
}

