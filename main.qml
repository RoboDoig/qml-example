import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.13

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("qml-example")

    MenuBar {
        x: 0
        y: 0
        width: 640
        height: 40
        Menu {
            title: qsTr("File")
            MenuItem {
                text: qsTr("Action")
                onTriggered: iface.action()
            }

            MenuItem {
                text: qsTr("Quit")
                onTriggered: Qt.quit()
            }
        }
    }

    Button {
        id: button
        x: 270
        y: 220
        text: qsTr("Start")
        onClicked: iface.button()
    }

    ProgressBar {
        id: progressBar
        objectName: "progressBar"
        x: 220
        y: 283
        value: 0
    }

    TextInput {
        id: textInput
        x: 280
        y: 194
        width: 80
        height: 20
        text: qsTr("5000")
        horizontalAlignment: Text.AlignHCenter
        font.pixelSize: 12

        onTextChanged: iface.set_time(text)
    }
}
