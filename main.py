import sys
import psycopg2
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                             QTableWidgetItem, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt



class Window(QWidget): 
    def __init__(self): 
        super(Window, self).__init__() 
 
        self.setWindowTitle("Расписание") 
        self.vbox = QVBoxLayout(self) 
 
        self._connect_to_db() 
 
        self.tabs = QTabWidget(self) 
        self.vbox.addWidget(self.tabs) 

        self._create_shedule_tab() 
        self._create_shedule1_tab()  
        self._create_shedule2_tab()

    def _connect_to_db(self): 
        self.conn = psycopg2.connect(database="raspisanie", 
                                               user="postgres", 
                                               password="2002", 
                                               host="localhost", 
                                               port="5432") 
        self.cursor = self.conn.cursor() 

    def _create_shedule_tab(self): 
        self.shedule_tab = QWidget()

        self.monday_gbox = QGroupBox("Понедельник") 

        self.svbox = QVBoxLayout() 
        self.shbox1 = QHBoxLayout() 
        self.shbox2 = QHBoxLayout() 
        self.shbox3 = QHBoxLayout()
         
        self.svbox.addLayout(self.shbox2) 
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox1)
 
        self.shbox2.addWidget(self.monday_gbox)  
        self.monday_table = QTableWidget() 
        self._create_monday_table() 
       

        self.tuesday_gbox = QGroupBox("Вторник")

        self.shbox2.addWidget(self.tuesday_gbox) 
        self.tuesday_table = QTableWidget()
        self._create_tuesday_table() 
 
        self.wednesday_gbox = QGroupBox("Среда")

        self.shbox2.addWidget(self.wednesday_gbox) 
        self.wednesday_table = QTableWidget() 
        self._create_wednesday_table() 
               
        self.thursday_gbox = QGroupBox("Четверг")

        self.shbox3.addWidget(self.thursday_gbox) 
        self.thursday_table = QTableWidget() 
        self._create_thursday_table() 
               
        self.friday_gbox = QGroupBox("Пятница")

        self.shbox3.addWidget(self.friday_gbox) 
        self.friday_table = QTableWidget() 
        self._create_friday_table() 
               
        self.saturday_gbox = QGroupBox("Суббота")

        self.shbox3.addWidget(self.saturday_gbox) 
        self.saturday_table = QTableWidget() 
        self._create_saturday_table() 
 
        self.update_shedule_button = QPushButton("Update") 
        self.update_shedule_button.clicked.connect(self._update_shedule) 

        self.shbox1.addWidget(self.update_shedule_button) 

        self.shedule_tab.setLayout(self.svbox) 
        self.tabs.addTab(self.shedule_tab, "Расписание") 

    def _create_shedule1_tab(self): 
        self.shedule1_tab = QWidget()

        self.svbox1=QVBoxLayout()

        self.teacher_gbox = QGroupBox("Преподаватели")

        self.svbox1.addWidget(self.teacher_gbox) 
        self.teacher_table = QTableWidget() 
        self._create_teacher_table() 

        self.update_shedule1_button = QPushButton("Update") 
        self.update_shedule1_button.clicked.connect(self._update_shedule1) 

        self.svbox1.addWidget(self.update_shedule1_button) 


        self.shedule1_tab.setLayout(self.svbox1) 
        self.tabs.addTab(self.shedule1_tab, "Преподаватели") 

    def _create_shedule2_tab(self): 
        self.shedule2_tab = QWidget()

        self.svbox1=QVBoxLayout()

        self.subj_gbox = QGroupBox("Преподаватели")

        self.svbox1.addWidget(self.subj_gbox) 
        self.subj_table = QTableWidget() 
        self._create_subj_table() 

        self.update_shedule2_button = QPushButton("Update") 
        self.update_shedule2_button.clicked.connect(self._update_shedule2) 

        self.svbox1.addWidget(self.update_shedule2_button) 


        self.shedule2_tab.setLayout(self.svbox1) 
        self.tabs.addTab(self.shedule2_tab, "Предметы") 
 
    def _create_monday_table(self): 
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.monday_table.setColumnCount(7) 
        self.monday_table.setHorizontalHeaderLabels(["ID","Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_monday_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.monday_table) 
        self.monday_gbox.setLayout(self.mvbox) 
 
    def _create_tuesday_table(self): 
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.tuesday_table.setColumnCount(7) 
        self.tuesday_table.setHorizontalHeaderLabels(["ID","Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_tuesday_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.tuesday_table) 
        self.tuesday_gbox.setLayout(self.mvbox) 
 
    def _create_wednesday_table(self): 
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.wednesday_table.setColumnCount(7) 
        self.wednesday_table.setHorizontalHeaderLabels(["ID","Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_wednesday_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.wednesday_table) 
        self.wednesday_gbox.setLayout(self.mvbox) 
         
    def _create_thursday_table(self): 
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.thursday_table.setColumnCount(7) 
        self.thursday_table.setHorizontalHeaderLabels(["ID","Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_thursday_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.thursday_table) 
        self.thursday_gbox.setLayout(self.mvbox) 

    def _create_friday_table(self): 
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.friday_table.setColumnCount(7) 
        self.friday_table.setHorizontalHeaderLabels(["ID","Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_friday_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.friday_table) 
        self.friday_gbox.setLayout(self.mvbox) 

    def _create_saturday_table(self):  
        self.saturday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.saturday_table.setColumnCount(7) 
        self.saturday_table.setHorizontalHeaderLabels(["ID","Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_saturday_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.saturday_table) 
        self.saturday_gbox.setLayout(self.mvbox) 

    def _create_teacher_table(self): 
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 

        self.teacher_table.setColumnCount(5) 
        self.teacher_table.setHorizontalHeaderLabels(["ID","Teacher", "Subject",""]) 
    
        self._update_teacher_table() 
    
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.teacher_table) 
        self.teacher_gbox.setLayout(self.mvbox) 

    def _create_subj_table(self): 
        self.subj_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
    
        self.subj_table.setColumnCount(5) 
        self.subj_table.setHorizontalHeaderLabels(["Subject",""]) 
    
        self._update_subj_table() 
    
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.subj_table) 
        self.subj_gbox.setLayout(self.mvbox)    

    def _update_monday_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='понедельник'") 
 
        records = list(self.cursor.fetchall()) 
 
 
        self.monday_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.monday_table.setItem(i, 0, QTableWidgetItem(str(r[0]))) 
            self.monday_table.item(i,0).setFlags(self.monday_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.monday_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.monday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.monday_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.monday_table.setCellWidget(i, 6, deleteButton)  

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.monday_table)) 

        addButton = QPushButton("Add") 
        self.monday_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.monday_table)) 
 
        self.monday_table.resizeRowsToContents() 

    def _update_tuesday_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='вторник'") 
 
        records = list(self.cursor.fetchall()) 
 
        self.tuesday_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.tuesday_table.setItem(i, 0, QTableWidgetItem(str(r[0]))) 
            self.tuesday_table.item(i,0).setFlags(self.tuesday_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.tuesday_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.tuesday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.tuesday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.tuesday_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.tuesday_table.setCellWidget(i, 6, deleteButton)  
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day1_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.tuesday_table)) 

        addButton = QPushButton("Add") 
        self.tuesday_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.tuesday_table)) 
 
        self.tuesday_table.resizeRowsToContents() 

    def _update_wednesday_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='среда'") 
 
        records = list(self.cursor.fetchall()) 
 
        self.wednesday_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.wednesday_table.setItem(i, 0, QTableWidgetItem(str(r[0]))) 
            self.wednesday_table.item(i,0).setFlags(self.wednesday_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.wednesday_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.wednesday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.wednesday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.wednesday_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.wednesday_table.setCellWidget(i, 6, deleteButton)  
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day2_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.wednesday_table)) 

        addButton = QPushButton("Add") 
        self.wednesday_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.wednesday_table)) 
 
        self.wednesday_table.resizeRowsToContents() 
 
    def _update_thursday_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='четверг'") 
    
        records = list(self.cursor.fetchall()) 
    
        self.thursday_table.setRowCount(len(records)+1) 
    
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
                
            self.thursday_table.setItem(i, 0, QTableWidgetItem(str(r[0]))) 
            self.thursday_table.item(i,0).setFlags(self.thursday_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.thursday_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.thursday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.thursday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.thursday_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.thursday_table.setCellWidget(i, 6, deleteButton)  
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day3_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.thursday_table)) 
    
        addButton = QPushButton("Add") 
        self.thursday_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.thursday_table)) 

        self.thursday_table.resizeRowsToContents() 
   
    def _update_friday_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='пятница'") 
            
        records = list(self.cursor.fetchall()) 
            
        self.friday_table.setRowCount(len(records)+1) 
            
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
                        
            self.friday_table.setItem(i, 0, QTableWidgetItem(str(r[0]))) 
            self.friday_table.item(i,0).setFlags(self.friday_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.friday_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.friday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.friday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.friday_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.friday_table.setCellWidget(i, 6, deleteButton) 
 
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day4_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.friday_table))  

        addButton = QPushButton("Add") 
        self.friday_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.friday_table)) 
            
        self.friday_table.resizeRowsToContents() 

    def _update_saturday_table(self): 
        self.cursor.execute("SELECT id,day, subject,room_numb, start_time FROM timetable WHERE day='суббота'") 
 
        records = list(self.cursor.fetchall()) 
 
        self.saturday_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.saturday_table.setItem(i, 0, QTableWidgetItem(str(r[0]))) 
            self.saturday_table.item(i,0).setFlags(self.saturday_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.saturday_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.saturday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.saturday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.saturday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.saturday_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.saturday_table.setCellWidget(i, 6, deleteButton) 
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day5_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.saturday_table)) 

        addButton = QPushButton("Add") 
        self.saturday_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.saturday_table)) 
 
        self.thursday_table.resizeRowsToContents() 

    def _update_teacher_table(self): 
        self.cursor.execute("SELECT id, full_name, subject FROM teacher") 
 
        records = list(self.cursor.fetchall()) 
 
        self.teacher_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
            
            self.teacher_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.teacher_table.item(i,0).setFlags(self.teacher_table.item(i,0).flags() ^ Qt.ItemIsEditable)

            self.teacher_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.teacher_table.setItem(i, 2, QTableWidgetItem(str(r[2]))) 
            joinButton = QPushButton("Join") 
            deleteButton = QPushButton("Delete") 
            self.teacher_table.setCellWidget(i, 3, joinButton) 
            self.teacher_table.setCellWidget(i, 4, deleteButton) 
            
            joinButton.clicked.connect(lambda ch, num=i: self._change_teacher_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_teacher_from_table(num)) 

        addButton = QPushButton("Add") 
        self.teacher_table.setCellWidget(i+1, 3, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_teacher_table(i+1)) 

        self.teacher_table.resizeRowsToContents() 

    def _update_subj_table(self): 
        self.cursor.execute("SELECT name FROM subject") 
 
        records = list(self.cursor.fetchall()) 
 
        self.subj_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.subj_table.setItem(i, 0, QTableWidgetItem(str(r[0]))) 
            joinButton = QPushButton("Join") 
            deleteButton = QPushButton("Delete") 
            self.subj_table.setCellWidget(i, 1, joinButton) 
            self.subj_table.setCellWidget(i, 2, deleteButton) 
            
            joinButton.clicked.connect(lambda ch, num=i: self._change_subj_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_subj_from_table(num)) 

        addButton = QPushButton("Add") 
        self.subj_table.setCellWidget(i+1, 1, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_subj_table(i+1)) 

        self.subj_table.resizeRowsToContents() 

    def _change_day_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.monday_table.columnCount()):  
            try:  
                row.append(self.monday_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _change_day1_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.tuesday_table.columnCount()):  
            try:  
                row.append(self.tuesday_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  
      
    def _change_day2_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.wednesday_table.columnCount()):  
            try:  
                row.append(self.wednesday_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields") 

    def _change_day3_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.thursday_table.columnCount()):  
            try:  
                row.append(self.thursday_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _change_day4_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.friday_table.columnCount()):  
            try:  
                row.append(self.friday_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  
      
    def _change_day5_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.saturday_table.columnCount()):  
            try:  
                row.append(self.saturday_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _change_teacher_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.teacher_table.columnCount()):  
            try:  
                row.append(self.teacher_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE teacher SET full_name=%s, subject=%s WHERE id=%s",(str(row[1]),str(row[2]),int(row[0])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _change_subj_from_table(self, rowNumb):  
        row = list() 

        try:  
            row.append(self.subj_table.item(rowNumb, 0).text())  
        except:  
            row.append(None)
        self.cursor.execute("SELECT * FROM subject")
        Sp = list(self.cursor.fetchall())  
        row.append(str(Sp[rowNumb]))
        row[1]=row[1].replace(",","")
        row[1]=row[1].replace("(","")
        row[1]=row[1].replace(")","")
        row[1]=row[1].replace("'","")
        print(row)
        try:
            self.cursor.execute("UPDATE subject SET name=%s WHERE name=%s",(str(row[0]),str(row[1])))
            self.conn.commit()

        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _delete_timetable_from_table(self, rowNumb, table):  
        row = list()  
        for i in range(table.columnCount()):  
            try:  
                row.append(table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        print(row)
        try:
            self.cursor.execute("DELETE FROM timetable WHERE id=%s AND day=%s AND subject=%s AND room_numb=%s AND start_time=%s",(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _delete_teacher_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.teacher_table.columnCount()):  
            try:  
                row.append(self.teacher_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        print(row)
        try:
            self.cursor.execute("DELETE FROM teacher WHERE id = %s AND full_name=%s AND subject=%s",(str(row[0]),str(row[1]),str(row[2])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _delete_subj_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.subj_table.columnCount()):  
            try:  
                row.append(self.subj_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        print(row)
        try:
            self.cursor.execute("DELETE FROM  subject WHERE name=%s",(str(row[0]),))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _add_timetable_table(self, rowNumb, table):
        self.cursor.execute("SELECT id FROM timetable") 
        records = list(self.cursor.fetchall())
        b=list()
        for a in range (len(records)):
            b.append(str(records[a]))
            b[a]=b[a].replace(",","")
            b[a]=b[a].replace("(","")
            b[a]=b[a].replace(")","")
            b[a]=b[a].replace("'","")
        print (type(b[0])) 
        id=max(b,key=lambda i: int(i))
        row = list()  
        for i in range(table.columnCount()):  
            try:  
                row.append(table.item(rowNumb, i).text())  
            except:  
                row.append(None) 
        print(id, row) 
        try:
            self.cursor.execute("INSERT INTO timetable (id, day, subject, room_numb, start_time) VALUES (%s, %s, %s, %s, %s)",(int(id)+1,str(row[1]),str(row[2]),str(row[3]),str(row[4])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _add_teacher_table(self, rowNumb):
        self.cursor.execute("SELECT id FROM teacher") 
        records = list(self.cursor.fetchall())
        b=list()
        for a in range (len(records)):
            b.append(str(records[a]))
            b[a]=b[a].replace(",","")
            b[a]=b[a].replace("(","")
            b[a]=b[a].replace(")","")
            b[a]=b[a].replace("'","")
        print (type(b[0])) 

        id=max(b,key=lambda i: int(i))
        row = list()  
        for i in range(self.teacher_table.columnCount()):  
            try:  
                row.append(self.teacher_table.item(rowNumb, i).text())  
            except:  
                row.append(None) 
        print(id, row) 
        try:
            self.cursor.execute("INSERT INTO teacher (id, full_name, subject) VALUES (%s, %s, %s)",(int(id)+1,str(row[1]),str(row[2])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _add_subj_table(self, rowNumb):
        row = list()  
        for i in range(self.subj_table.columnCount()):  
            try:  
                row.append(self.subj_table.item(rowNumb, i).text())  
            except:  
                row.append(None) 
        print(id, row) 
        try:
            self.cursor.execute("INSERT INTO subject (name) VALUES (%s)",(str(row[0]),))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _update_shedule(self): 
        self.monday_table.clear() 
        self._create_monday_table()
        self.tuesday_table.clear() 
        self._create_tuesday_table()
        self.wednesday_table.clear() 
        self._create_wednesday_table()
        self.thursday_table.clear() 
        self._create_thursday_table()
        self.friday_table.clear() 
        self._create_friday_table()
        self.saturday_table.clear() 
        self._create_saturday_table()

    def _update_shedule1(self):
        self.teacher_table.clear()
        self._create_teacher_table()

    def _update_shedule2(self):
        self.subj_table.clear()
        self._create_subj_table()


if __name__ == '__main__':
    app =QApplication(sys.argv)
    win = Window()
    win.show()
    sys.argv(app.exec_())
 
 