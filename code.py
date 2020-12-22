import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from random import choice
from time import sleep


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        user = open("participants.txt",'r')
        a = user.readlines()
        self.a = list(map(lambda s: s.strip(), a))

    
#Window...
        self.setWindowTitle('Ticket Winner')
        self.setWindowIcon(QIcon('picture1.jpeg'))
        self.setGeometry(100, 40, 1500, 950)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('stone.jpg'))
        #self.background.setGeometry(500, 40, 1200, 1000)

        #Intro Labels
        self.head = QLabel('WELCOME!!', self)
        self.head.setFont(QFont('Impact',50))
        self.head.move(600, 10)
        self.head.setStyleSheet('color: white')
        
        self.subhead = QLabel('TO THE LIVE DRAW OF THE AVENGERS ENDGAME PROMOTION', self)
        self.subhead.setFont(QFont('Impact',20))
        self.subhead.move(475, 100)
        self.subhead.setStyleSheet('color: grey')

        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('picture.jpeg'))
        self.image.move(368.5, 200)
        
        self.image1 = QLabel(self)
        self.image1.setPixmap(QPixmap('ticket.jpg'))
        self.image1.move(150, 10)
        self.image1.setVisible(False)
        
 
        self.btn = QPushButton('Let\'s Begin!', self)
        self.btn.setFont(QFont('Copperplate Gothic Bold', 40))
        self.btn.clicked.connect(self.run)
        self.btn.resize(500, 100)
        self.btn.move(500, 700)
        self.btn.setStyleSheet('')
        self.btn.setStyleSheet('background-color: rgb(138,4d3,226)')
        
        self.btn2 = QPushButton(self)
        self.btn2.setText('Stop')
        self.btn2.setGeometry(500, 700, 500, 100)
        self.btn2.setFont(QFont('Copperplate Gothic Bold', 40))
        self.btn2.clicked.connect(self.stop)
        self.btn2.setVisible(False)

        self.winner = QLabel('{}'.format(choice(self.a).upper()),self)
        self.winner.setStyleSheet('color: rgb(100,50,32)')
        self.winner.resize(1000, 100)
        self.winner.move(600, 250)
        self.winner.setFont(QFont('Gabriola', 50))
        self.winner.setVisible(False)
        
        self.names = NameChanger(self, self.a)
        self.names.setStyleSheet('color: white')
        self.names.resize(1000, 100)
        self.names.move(600, 400)
        self.names.setFont(QFont('Broadway', 40))
        self.names.setVisible(False)    
       
        self.show()

    def run(self):
        self.head.setVisible(False)
        self.subhead.setVisible(False)
        self.image.setVisible(False)
        self.btn.setVisible(False)
        self.btn2.setVisible(True)
        self.names.setVisible(True)

    def stop(self):
        self.btn2.setVisible(False)
        self.names.setVisible(False)
        self.winner.setVisible(True)
        self.image.setVisible(False)
        self.image1.setVisible(True)
        self.background.setVisible(False)
        


class NameChanger(QLabel):
    def __init__(self, parent, names, speed=50):

        self.names = names

        QLabel.__init__(self, parent)
        #self.setGeometry POSITION …
        timer = QTimer(self)
        timer.timeout.connect(self.animate)
        timer.setInterval(speed)
        
        timer.start()
        
    def animate(self):
    
        self.setText(choice(self.names))
           
        
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
