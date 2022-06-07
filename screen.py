from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import question4 as q4
import main
import question6 as q6
import question7 as q7




class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(1200,1000)
        layout = QVBoxLayout()


        self.combobox = QComboBox()
        self.combobox.addItem('CISI')
        self.combobox.addItem('cacm')
        self.combobox.setStyleSheet('height : 40')
        layout.addWidget( self.combobox)

        # data = ('apple','banana','tomato','potato','bread')
        # model = QStandardItemModel(len(data), 1)
        # model.setHorizontalHeaderLabels(['data'])

        # for row, data in enumerate(data):
        #     item = QStandardItem(data)
        #     model.setItem(row, 0, item)
        
        # filter_proxy_model = QSortFilterProxyModel()
        # filter_proxy_model.setSourceModel(model)
        # filter_proxy_model.setFilterKeyColumn(0)

        self.search = QLineEdit()
        self.search.setStyleSheet('font-size: 35px; height: 60px')
        #search.textChanged.connect(filter_proxy_model.setFilterRegExp)
        layout.addWidget(self.search)

        self.sugLabel1 = QLabel('',self)
        self.sugLabel1.mouseDoubleClickEvent=self.mousePressEvent
        self.resLabel = QLabel('gklfngkhsa',self)

        searchButton = QPushButton("search", self)
        searchButton.setGeometry(200, 150, 100, 30)             # setting geometry of button
        searchButton.clicked.connect(lambda:self.clickSearch())     # adding action to a button
        layout.addWidget(searchButton)
        # table = QTableView()
        # table.setModel(filter_proxy_model)
        # layout.addWidget(table)

        layout.addWidget(self.sugLabel1)
        layout.addWidget(self.resLabel)
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        

    # def current_text_changed(self, s):
    #     print("Current text: ",s)
    sugQuery=""
    i=0

    def clickSearch(self):
        self.sugQuery=q4.f(self.combobox.currentText(),self.search.text())
        ss="Do you mean:  "
        ss+=self.sugQuery
        self.sugLabel1.setText(ss)


    def mousePressEvent(self,event):
        print(self.sugQuery)
        # res=main.main_func(self.sugQuery,self.combobox.currentText())
        # res=q7.cos_sim(q6.load_tfidf(()self.combobox.currentText),q6.online_tfidf(self.sugQuery,"LL"))
        # res=main.online(self.sugQuery,self.tfidf_dataset[self.i])
        # self.resLabel.setText(str(res))

        # X=q6.load_tfidf(self.combobox.currentText())
        # Y=q6.online_tfidf(self.sugQuery,"LL")
        # res=q7.cos_sim(X,Y)
        res=main.main_func(self.sugQuery,self.combobox.currentText())
        print(res)
        # self.resLabel.setText(str(res))
        # print(X.toarray())
        # print(Y.toarray())
        
    

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()