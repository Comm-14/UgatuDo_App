from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import webbrowser

# Create a database or connect to one
conn = sqlite3.connect('UGATODO.db')
# Create a cursor
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE if not exists ToDoList(
    Task text)
    ''')

# Commit the changes
conn.commit()

# Close our connection
conn.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(980, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(980, 560))
        MainWindow.setMaximumSize(QtCore.QSize(980, 560))
        MainWindow.setTabletTracking(False)
        MainWindow.setToolTip("")
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.0284091, x2:1, y2:0, stop:0.170455 rgba(233, 223, 197, 255), stop:0.642045 rgba(204, 216, 225, 255));\n"
"\n"
"")
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.AddItem_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_it())
        self.AddItem_Button.setGeometry(QtCore.QRect(40, 300, 300, 60))
        self.AddItem_Button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.0284091, x2:1, y2:0, stop:0.534091 rgba(233, 223, 197, 255), stop:0.806818 rgba(224, 221, 206, 255));")
        self.AddItem_Button.setCheckable(False)
        self.AddItem_Button.setDefault(False)
        self.AddItem_Button.setFlat(False)
        self.AddItem_Button.setObjectName("AddItem_Button")

        self.DataEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.DataEdit.setGeometry(QtCore.QRect(200, 180, 140, 40))
        self.DataEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.0284091, x2:1, y2:0, stop:0.534091 rgba(233, 223, 197, 255), stop:0.806818 rgba(224, 221, 206, 255));")
        self.DataEdit.setObjectName("DataEdit")

        self.TimeTable_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : webbrowser.open('https://lk.ugatu.su/raspisanie/#timetable'))
        self.TimeTable_Button.setGeometry(QtCore.QRect(40, 460, 300, 60))
        self.TimeTable_Button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.0284091, x2:1, y2:0, stop:0.534091 rgba(233, 223, 197, 255), stop:0.806818 rgba(224, 221, 206, 255));")
        self.TimeTable_Button.setObjectName("TimeTable_Button")

        self.TypeOfWorkLeft_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.TypeOfWorkLeft_ComboBox.setEnabled(True)
        self.TypeOfWorkLeft_ComboBox.setGeometry(QtCore.QRect(140, 240, 200, 40))
        self.TypeOfWorkLeft_ComboBox.setTabletTracking(False)
        self.TypeOfWorkLeft_ComboBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.0284091, x2:1, y2:0, stop:0.534091 rgba(233, 223, 197, 255), stop:0.806818 rgba(224, 221, 206, 255));")
        self.TypeOfWorkLeft_ComboBox.setEditable(False)
        self.TypeOfWorkLeft_ComboBox.setFrame(True)
        self.TypeOfWorkLeft_ComboBox.setObjectName("TypeOfWorkLeft_ComboBox")
        self.TypeOfWorkLeft_ComboBox.addItem("Другое")
        self.TypeOfWorkLeft_ComboBox.addItem("Лекция")
        self.TypeOfWorkLeft_ComboBox.addItem("Практика")
        self.TypeOfWorkLeft_ComboBox.addItem("Лабораторная")
        self.TypeOfWorkLeft_ComboBox.addItem("Сессия")
        self.TypeOfWorkLeft_ComboBox.addItem("Курсовая работа")

        self.NewTask_Text = QtWidgets.QLabel(self.centralwidget)
        self.NewTask_Text.setGeometry(QtCore.QRect(90, 25, 201, 30))
        self.NewTask_Text.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0284091, x2:1, y2:0, stop:0.534091 rgba(233, 223, 197, 255), stop:0.806818 rgba(224, 221, 206, 255));")
        self.NewTask_Text.setObjectName("NewTask_Text")

        self.TypeOfWork_Text = QtWidgets.QLabel(self.centralwidget)
        self.TypeOfWork_Text.setGeometry(QtCore.QRect(40, 245, 100, 30))
        self.TypeOfWork_Text.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(233, 223, 197);")
        self.TypeOfWork_Text.setObjectName("TypeOfWork_Text")

        self.DeleteItem_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.Delete_it())
        self.DeleteItem_Button.setGeometry(QtCore.QRect(40, 380, 300, 60))
        self.DeleteItem_Button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.0284091, x2:1, y2:0, stop:0.534091 rgba(233, 223, 197, 255), stop:0.806818 rgba(224, 221, 206, 255));")
        self.DeleteItem_Button.setObjectName("DeleteItem_Button")

        self.TaskList_Text = QtWidgets.QLabel(self.centralwidget)
        self.TaskList_Text.setGeometry(QtCore.QRect(580, 20, 200, 30))
        self.TaskList_Text.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(204, 216, 225);")
        self.TaskList_Text.setObjectName("TaskList_Text")


        self.AddDate_CheckMark = QtWidgets.QCheckBox(self.centralwidget)
        self.AddDate_CheckMark.setGeometry(QtCore.QRect(42, 184, 140, 30))
        self.AddDate_CheckMark.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.AddDate_CheckMark.setStyleSheet("background-color: rgb(233, 223, 197);")
        self.AddDate_CheckMark.setObjectName("AddDate_CheckMark")


        self.AddTask_Label = QtWidgets.QTextEdit(self.centralwidget)
        self.AddTask_Label.setGeometry(QtCore.QRect(40, 80, 300, 80))
        self.AddTask_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.0284091, x2:1, y2:0, stop:0.534091 rgba(233, 223, 197, 255), stop:0.806818 rgba(224, 221, 206, 255));")
        self.AddTask_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.AddTask_Label.setObjectName("AddTask_Label")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(380, 0, 1, 580))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(625, 90, 0, 22))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.tableWidget = QtWidgets.QListWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(420, 80, 520, 442))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.0284091, x2:1, y2:0, stop:0 rgba(217, 217, 206, 255), stop:0.255682 rgba(210, 217, 219, 255));\n"
            "")
        self.tableWidget.setStyleSheet ("font: 10pt \"MS Shell Dlg 2\";\n")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setObjectName("TaskWidget")

        self.DataEdit.raise_()
        self.TimeTable_Button.raise_()
        self.TypeOfWorkLeft_ComboBox.raise_()
        self.NewTask_Text.raise_()
        self.AddItem_Button.raise_()
        self.TypeOfWork_Text.raise_()
        self.DeleteItem_Button.raise_()
        self.TaskList_Text.raise_()
        self.AddDate_CheckMark.raise_()

        self.AddTask_Label.raise_()
        self.line.raise_()
        self.tableWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Grab all the items from the database
        self.grab_all()

    def grab_all(self):
        # Create a database or connect to one
        conn = sqlite3.connect('UGATODO.db')
        # Create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM ToDoList")
        records = c.fetchall()

        # Commit the changes
        conn.commit()

        # Close our connection
        conn.close()

        # Loop thru records and add to screen
        for record in records:
            self.tableWidget.addItem(str(record[0]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UgatoDo"))
        self.AddItem_Button.setText(_translate("MainWindow", "Добавить Задачу"))
        self.TimeTable_Button.setText(_translate("MainWindow", "Расписание УГАТУ"))
        self.NewTask_Text.setText(_translate("MainWindow", "Новая Задача"))
        self.TypeOfWork_Text.setText(_translate("MainWindow", "Вид Работы"))
        self.DeleteItem_Button.setText(_translate("MainWindow", "Удалить Задачу"))
        self.TaskList_Text.setText(_translate("MainWindow", "Список Задач"))
        self.AddDate_CheckMark.setText(_translate("MainWindow", "Добавить Дату"))



        # Grab items from database



# Add Item to list
    def add_it(self):
        # Добавляю Задачу
        item = self.AddTask_Label.toPlainText()
        self.AddTask_Label.setText("")

        # Добавляю дату
        if self.AddDate_CheckMark.checkState():
            temp_var = self.DataEdit.date()
            var_name = str(temp_var.toPyDate())
            item = item + '    ' + var_name

        # Добавляю вид работы
        type = self.TypeOfWorkLeft_ComboBox.currentText()
        item=item+ '    ' + type
        self.tableWidget.addItem(item)

        # Create a database or connect to one
        conn = sqlite3.connect('UGATODO.db')
        # Create a cursor
        c = conn.cursor()

        # Delete everything in the database table
        c.execute('DELETE FROM ToDoList;', )

        items = []
        # Loop through the listWidget and pull out each item
        for index in range(self.tableWidget.count()):
            items.append(self.tableWidget.item(index))

        for item in items:
            # print(item.text())
            # Add stuff to the table
            c.execute("INSERT INTO ToDoList VALUES (:item)",
                      {
                          'item': item.text(),
                      })

        # Commit the changes
        conn.commit()

        # Close our connection
        conn.close()


    def Delete_it(self):
        # Grab the selected row or current row
        clicked = self.tableWidget.currentRow()

        # Delete selected row
        self.tableWidget.takeItem(clicked)

        # Create a database or connect to one
        conn = sqlite3.connect('UGATODO.db')
        # Create a cursor
        c = conn.cursor()

        # Delete everything in the database table
        c.execute('DELETE FROM ToDoList;', )

        items = []
        # Loop through the listWidget and pull out each item
        for index in range(self.tableWidget.count()):
            items.append(self.tableWidget.item(index))

        for item in items:
            # print(item.text())
            # Add stuff to the table
            c.execute("INSERT INTO ToDoList VALUES (:item)",
                      {
                          'item': item.text(),
                      })

        # Commit the changes
        conn.commit()

        # Close our connection
        conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())