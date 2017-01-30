import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from math import *
from time import strftime
 
num = 0.0
newNum = 0.0
sumAll = 0.0
operator = ""
 
opVar = False
sumIt = 0
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        self.line = QtGui.QLineEdit(self)
        font= QtGui.QFont("Times",15)
        self.line.setFont(font)
        self.line.move(5,5)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.resize(390,60)
        self.lcd=QtGui.QLCDNumber(self)
        self.lcd.move(110,355)
        self.lcd.resize(200,60)
        self.timer= QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)
        self.lcd.display(strftime("%H"+":"+"%M"))



        
        zero = QtGui.QPushButton("0",self)
        zero.move(10,300)
        zero.resize(45,50)
 
        one = QtGui.QPushButton("1",self)
        one.move(10,245)
        one.resize(45,50)
 
        two = QtGui.QPushButton("2",self)
        two.move(60,245)
        two.resize(45,50)
 
        three = QtGui.QPushButton("3",self)
        three.move(110,245)
        three.resize(45,50)
 
        four = QtGui.QPushButton("4",self)
        four.move(10,190)
        four.resize(45,50)
 
        five = QtGui.QPushButton("5",self)
        five.move(60,190)
        five.resize(45,50)
 
        six = QtGui.QPushButton("6",self)
        six.move(110,190)
        six.resize(45,50)
 
        seven = QtGui.QPushButton("7",self)
        seven.move(10,135)
        seven.resize(45,50)
 
        eight = QtGui.QPushButton("8",self)
        eight.move(60,135)
        eight.resize(45,50)
 
        nine = QtGui.QPushButton("9",self)
        nine.move(110,135)
        nine.resize(45,50)
 
        switch = QtGui.QPushButton("+/-",self)
        switch.move(60,300)
        switch.resize(45,50)
        switch.clicked.connect(self.Switch)
 
        point = QtGui.QPushButton(".",self)
        point.move(110,300)
        point.resize(45,50)
        point.clicked.connect(self.pointClicked)
 
        div = QtGui.QPushButton("/",self)
        div.move(160,135)
        div.resize(45,50)
 
        mult = QtGui.QPushButton("*",self)
        mult.move(160,190)
        mult.resize(45,50)
 
        minus = QtGui.QPushButton("-",self)
        minus.move(160,245)
        minus.resize(45,50)
 
        plus = QtGui.QPushButton("+",self)
        plus.move(160,300)
        plus.resize(45,50)

        power= QtGui.QPushButton("^",self)
        power.move(310,300)
        power.resize(45,50)
 
        sqrt = QtGui.QPushButton("√",self)
        sqrt.move(210,135)
        sqrt.resize(45,50)
        sqrt.clicked.connect(self.Sqrt)
 
        squared = QtGui.QPushButton("x²",self)
        squared.move(210,190)
        squared.resize(45,50)
        squared.clicked.connect(self.Squared)

        sin= QtGui.QPushButton("sin",self)
        sin.move(260,135)
        sin.resize(45,50)
        sin.clicked.connect(self.sin)

        cos= QtGui.QPushButton("cos",self)
        cos.move(260,190)
        cos.resize(45,50)
        cos.clicked.connect(self.cos)

        tan= QtGui.QPushButton("tan",self)
        tan.move(260,245)
        tan.resize(45,50)
        tan.clicked.connect(self.tan)

        fact= QtGui.QPushButton("!",self)
        fact.move(260,300)
        fact.resize(45,50)
        fact.clicked.connect(self.fact)

        exp= QtGui.QPushButton("e^",self)
        exp.move(310,135)
        exp.resize(45,50)
        exp.clicked.connect(self.exp)

        PI= QtGui.QPushButton("PI",self)
        PI.move(360,135)
        PI.resize(45,50)
        PI.clicked.connect(self.PI)

        ln= QtGui.QPushButton("ln",self)
        ln.move(310,190)
        ln.resize(45,50)
        ln.clicked.connect(self.ln)

        log= QtGui.QPushButton("log",self)
        log.move(310,245)
        log.resize(45,50)
        log.clicked.connect(self.log)

        asin= QtGui.QPushButton("asin",self)
        asin.move(360,190)
        asin.resize(45,50)
        asin.clicked.connect(self.asin)

        acos= QtGui.QPushButton("acos",self)
        acos.move(360,245)
        acos.resize(45,50)
        acos.clicked.connect(self.acos)

        atan= QtGui.QPushButton("atan",self)
        atan.move(360,300)
        atan.resize(45,50)
        atan.clicked.connect(self.atan)

        equal = QtGui.QPushButton("=",self)
        equal.move(210,245)
        equal.resize(45,105)
        equal.clicked.connect(self.Equal)
 
        c = QtGui.QPushButton("C",self)
        c.move(270,70)
        c.resize(120,60)
        c.clicked.connect(self.C)
 
        ce = QtGui.QPushButton("CE",self)
        ce.move(140,70)
        ce.resize(120,60)
        ce.clicked.connect(self.CE)
 
        back = QtGui.QPushButton("Back",self)
        back.move(10,70)
        back.resize(120,60)
        back.clicked.connect(self.Back)
 
        nums = [zero,one,two,three,four,five,six,seven,eight,nine]
 
        ops = [back,c,ce,div,mult,minus,plus,equal,power]
 
        rest = [switch,squared,sqrt,point,sin,cos,tan,fact,exp]
 
        for i in nums:
            i.setStyleSheet("color:white;Background-Color:black")
            i.clicked.connect(self.Nums)
 
        for i in ops:
            i.setStyleSheet("color:red;")
 
        for i in ops[3:9]:
            i.clicked.connect(self.Operator)
         
             
#---------Window settings -------------------------------
         
        self.setGeometry(300,300,405,440)
        self.setFixedSize(405,440)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()
 
    def Nums(self):
        global num
        global newNum
        global opVar
         
        sender = self.sender()
         
        newNum = int(sender.text())
        setNum = str(newNum)
 
 
        if opVar == False:
            self.line.setText(self.line.text() + setNum)
             #self.lcd.display(self.line.text()+setNum)
 
        else:
            self.line.setText(setNum)
            #self.lcd.display(setNum)
            opVar = False
             
         
 
    def pointClicked(self):
        global opVar
         
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")
             
 
    def Switch(self):
        global num
         
        try:
            num = int(self.line.text())
             
        except:
            num = float(self.line.text())
      
        num = num - num * 2
 
        numStr = str(num)
         
        self.line.setText(numStr)
 
    def Operator(self):
        global num
        global opVar
        global operator
        global sumIt
 
        sumIt += 1
 
        if sumIt > 1:
            self.Equal()
 
        num =float(self.line.text())
 
        sender = self.sender()
 
        operator = sender.text()
         
        opVar = True
 
 
 
    def Equal(self):
        global num
        global newNum
        global sumAll
        global operator
        global opVar
        global sumIt
 
        sumIt = 0
 
        newNum = self.line.text()
 
        print(num)
        print(newNum)
        print(operator)
         
        if operator == "+":
            sumAll = float(num) + float(newNum)
 
        elif operator == "-":
            sumAll = float(num) - float(newNum)
 
        elif operator == "/":
            sumAll = float(num) / float(newNum)
 
        elif operator == "*":
            sumAll = float(num) * float(newNum)
            
        elif operator =="^":
            sumAll=pow(float(num),float(newNum))
             
        print(sumAll)
        self.line.setText(str(sumAll))
        opVar = True
 
    def Back(self):
        self.line.backspace()
 
    def C(self):
        global newNum
        global sumAll
        global operator
        global num
         
        self.line.clear()
 
        num = 0.0
        newNum = 0.0
        sumAll = 0.0
        operator = ""
 
    def CE(self):
        self.line.clear()

    def Time(self):
        self.lcd.display(strftime("%H"+":"+"%M"))
 
    def Sqrt(self):
        global num
         
        num = float(self.line.text())
        n = sqrt(num)
        num = n
 
        self.line.setText(str(num))
 
    def Squared(self):
        global num
         
        num = float(self.line.text())
 
        n = num ** 2
 
        num = n
 
        self.line.setText(str(n))

    def sin(self):
        global num
        num=float(self.line.text())
        n=sin(radians(num))
        num=n
        self.line.setText(str(num))

    def cos(self):
        global num
        num=float(self.line.text())
        n=cos(radians(num))
        num=n
        self.line.setText(str(num))

    def tan(self):
        global num
        num=float(self.line.text())
        n=tan(radians(num))
        num=n
        self.line.setText(str(num))

    def fact(self):
        global num
        num=float(self.line.text())
        n=factorial(num)
        num=n
        self.line.setText(str(num))

    def exp(self):
        global num
        num=float(self.line.text())
        n=exp(num)
        num=n
        self.line.setText(str(num))

    def ln(self):
        global num
        num=float(self.line.text())
        n=log(num)
        num=n
        self.line.setText(str(num))

    def log(self):
        global num
        num=float(self.line.text())
        n=log10(num)
        num=n
        self.line.setText(str(num))

    def PI(self):
        global newNum
        newNum=pi
        self.line.setText(str(newNum))

    def asin(self):
        global num
        num=float(self.line.text())
        n=asin(num)
        num=n
        self.line.setText(str(num))

    def acos(self):
        global num
        num=float(self.line.text())
        n=acos(num)
        num=n
        self.line.setText(str(num))

    def atan(self):
        global num
        num=float(self.line.text())
        n=atan(num)
        num=n
        self.line.setText(str(num))

   

 
def main():
    app = QtGui.QApplication(sys.argv)
    main= Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
