from tkinter import *
from tkinter import ttk
from time import sleep
COINS = [1,2,5,0.01,0.02,0.05,0.10,0.20,0.50]
NUMBERS = [0,1,2,3,4,5,6,7,8,9]
GOODS = ["Towar 30 - 1.80zł", "Towar 31 - 1.90zł", "Towar 32 - 2.00 zł", "Towar 33- 2.50zł", "Towar 34- 2.80zł", "Towar 35- 2.95zł", "Towar 36- 3.50zł",
         "Towar 37 - 2.25zł", "Towar 38 - 1.35zł", "Towar 39 - 2.80zł","Towar 40 - 1.90zł", "Towar 41 - 2.10zł", "Towar 42- 1.95zł", "Towar 43 - 2.40zł",
         "Towar 44 - 3.00zł", "Towar 45 - 3.10zł", "Towar 46 - 2.80zł", "Towar 47 - 3.15zł", "Towar 48 - 2.74zł", "Towar 49 - 2.15zł", "Towar 50 - 3.30zł"]

moneyDic = {'5':2,'2':2,'1':2,'0.5':2,'0.2':2,'0.1':2,'0.05':2,'0.02':2,'0.01':2}

class Goods:
    def __init__(self,number,price,amount=5):
        if number<30 or number>50:
            print("Błędny numer produktu")
        else:
            self.number = number
            self.price = price
            self.amount = amount
    def getPrice(self):
        return self.price
    def getAmount(self):
        return self.amount
    def decAmount(self):
        self.amount=self.amount-1
    @staticmethod
    def buyGoods(number,price):
        firstWindow=Tk()
        firstWindow.title("Maszyna z napojami")
        firstFrame=ttk.Frame(firstWindow)
        firstFrame.grid(column=7,row=7,sticky=(N,W,E,S))
        if number > 50:
            label = ttk.Label(firstFrame, text="Błędny numer produktu").grid(row=1,column=1)
            numTextField.config(state="normal")
            numTextField.delete('1.0',END)
            checkPriceButt.config(state="disabled")
            
        elif number < 30:
            label = ttk.Label(firstFrame, text="Błędny numer produktu").grid(row=1,column=1)
            numTextField.config(state="normal")
            numTextField.delete('1.0',END)
            checkPriceButt.config(state="disabled")
            proceedButt.config(state="disabled")
            
        elif _productList[number-30].getAmount() <=0:
            label = ttk.Label(firstFrame, text="Brak towaru!").grid(row=1,column=1)
            numTextField.config(state="normal")
            numTextField.delete('1.0',END)
            checkPriceButt.config(state="disabled")
            proceedButt.config(state="disabled")
            
        elif _productList[number-30].getPrice() > price:
            label = ttk.Label(firstFrame, text="Za mało pieniędzy").grid(row=1,column=1)
            label = ttk.Label(firstFrame, text="Cena produktu to " + str(_productList[number-30].getPrice()) + "zł").grid(row=2,column=1)
            
        elif _productList[number-30].getPrice() == price:
            piggybank.firstCheck()
            label = ttk.Label(firstFrame, text="Zakupiłeś towar numer: " + str(number) +".\n" + "Kosztował: " + str(_productList[number-30].getPrice()) + "zł").grid(row=2,column=1)
            piggybank.makeEmpty()
            label = ttk.Label(firstFrame, text="Twoja reszta wynosi: " + "{:.2f}".format(piggybank.getSum()) + "zł").grid(row=3,column=1)
            _productList[number-30].decAmount()
            abadonButt.config(state="disabled")
            priceTextField.delete('1.0',END)
            numTextField.config(state="normal")
            numTextField.delete('1.0',END)
            checkPriceButt.config(state="disabled")
            proceedButt.config(state="disabled")
            
        elif _productList[number-30].getPrice() < price:
            piggybank.firstCheck()
            piggybank.addCoins(Coin((-1)*_productList[number-30].getPrice()))
            if(mainCheck(piggybank.getSum(),5)):
                sleep(0.05)
                lastCheck(piggybank.getSum(),5)
                label = ttk.Label(firstFrame, text="Zakupiłeś towar numer: " + str(number) +".\n" + "Kosztował: " + str(_productList[number-30].getPrice()) + "zł").grid(row=2,column=1)
                label = ttk.Label(firstFrame, text="Twoja reszta wynosi: " + "{:.2f}".format(piggybank.getSum()) + "zł").grid(row=3,column=1)
                print("{:.2f}".format(piggybank.getSum()))
                piggybank.makeEmpty()
                _productList[number-30].decAmount()
                abadonButt.config(state="disabled")
                priceTextField.delete('1.0',END)
                numTextField.config(state="normal")
                numTextField.delete('1.0',END)
                checkPriceButt.config(state="disabled")
                proceedButt.config(state="disabled")
                for k, v in moneyDic.items():
                    print(k, v)

            else:
                piggybank.addCoins(Coin(_productList[number-30].getPrice()))
                piggybank.backCheck()
                label = ttk.Label(firstFrame, text="Nie mogę wydać reszty. Wrzuć odliczoną kwotę!").grid(row=2,column=1)
                label = ttk.Label(firstFrame, text="Towar który wybrałeś: (" + str(number) +") kosztuje: " + str(_productList[number-30].getPrice()) + "zł").grid(row=3,column=1)
                label = ttk.Label(firstFrame, text="Zwracam wrzuconą kwotę: " + "{:.2f}".format((piggybank.getSum())) + "zł").grid(row=4,column=1)
                piggybank.makeEmpty()
                checkPriceButt.config(state="disabled")
                proceedButt.config(state="disabled")
                abadonButt.config(state="disabled")
                
    @staticmethod
    def checkPrice(number):
        secondWindow=Tk()
        secondWindow.title("Maszyna z napojami")
        secondFrame=ttk.Frame(secondWindow)
        secondFrame.grid(column=7,row=7,sticky=(N,W,E,S))
        if number > 50:
            label = ttk.Label(secondFrame, text="Błędny numer produktu").grid(row=1,column=1)
        elif number < 30:
            label = ttk.Label(secondFrame, text="Błędny numer produktu").grid(row=1,column=1)
        else:
            label = ttk.Label(secondFrame, text="Cena produktu wynosi: " + "{:.2f}".format(_productList[number-30].getPrice()) + "zł").grid(row=3,column=1)

        
_productList = [Goods(30,1.80),Goods(31,1.90),Goods(32,2.00),Goods(33,2.50),Goods(34,2.80),Goods(35,2.95),Goods(36,3.50),Goods(37,2.25,0),Goods(38,1.35),
                Goods(39,2.80),Goods(40,1.90),Goods(41,2.10),Goods(42,1.95,0),Goods(43,2.40,0),Goods(44,3.00),Goods(45,3.10),Goods(46,2.80),Goods(47,3.15,0),
                Goods(48,2.74),Goods(49,2.15),Goods(50,3.30)]
class Coin:
    tab=[1,2,5,10,20,50,100,200,500]
    
    def __init__(self,value):
        value = value*100
        for i in range (0,9):
            #if value == self.tab[i]:
            self.value=value
            self.value=self.value/100
            break
        #else:
            #self.value=0
    def __del__(self):
        pass
    def getWartosc(self):
        return "{:.2f}".format(self.value)



class MoneyBox(Coin):
    _myList = []
    def __init__(self):
        pass
    def addCoins(self,coin):
        if isinstance(coin,Coin):
            self._myList.append(coin)
        else:
            return 0

    def getSum(self):
        sum=0
        end = len(self._myList)
        for i in range(0,end):
            sum += float(self._myList[i].getWartosc())
        return round(sum,2)
                
    def makeEmpty(self):
            del self._myList[:]

    def abadonOperation(self):
        thirdWindow=Tk()
        thirdWindow.title("Reszta")
        thirdFrame=ttk.Frame(thirdWindow)
        thirdFrame.grid(column=7,row=7,sticky=(N,W,E,S))
        label = ttk.Label(thirdFrame, text="Wydaje reszte: " + "{:.2f}".format((piggybank.getSum())) + "zł").grid(row=1,column=1)
        del self._myList[:]
        
    def firstCheck(self):
        for i in range(0,len(self._myList)):
            if float(self._myList[i].getWartosc()) == 5.0:
                moneyDic['5']+=1
            elif float(self._myList[i].getWartosc()) == 2.0:
                moneyDic['2']+=1
            elif float(self._myList[i].getWartosc()) == 1.0:
                moneyDic['1']+=1
            elif float(self._myList[i].getWartosc()) == 0.5:
                moneyDic['0.5']+=1
            elif float(self._myList[i].getWartosc()) == 0.2:
                moneyDic['0.2']+=1
            elif float(self._myList[i].getWartosc()) == 0.1:
                moneyDic['0.1']+=1
            elif float(self._myList[i].getWartosc()) == 0.05:
                moneyDic['0.05']+=1
            elif float(self._myList[i].getWartosc()) == 0.02:
                moneyDic['0.02']+=1
            elif float(self._myList[i].getWartosc()) == 0.01:
                moneyDic['0.01']+=1
        for k, v in moneyDic.items():
            print(k, v)

    def backCheck(self):
        for i in range(0,len(self._myList)):
            if float(self._myList[i].getWartosc()) == 5.0:
                moneyDic['5']-=1
            elif float(self._myList[i].getWartosc()) == 2.0:
                moneyDic['2']-=1
            elif float(self._myList[i].getWartosc()) == 1.0:
                moneyDic['1']-=1
            elif float(self._myList[i].getWartosc()) == 0.5:
                moneyDic['0.5']-=1
            elif float(self._myList[i].getWartosc()) == 0.2:
                moneyDic['0.2']-=1
            elif float(self._myList[i].getWartosc()) == 0.1:
                moneyDic['0.1']-=1
            elif float(self._myList[i].getWartosc()) == 0.05:
                moneyDic['0.05']-=1
            elif float(self._myList[i].getWartosc()) == 0.02:
                moneyDic['0.02']-=1
            elif float(self._myList[i].getWartosc()) == 0.01:
                moneyDic['0.01']-=1
        for k, v in moneyDic.items():
            print(k, v)
        


def checkNumber(number):
    if(number == 3):
        numTextField.config(state=DISABLED)

def mainCheck(wyplac,ile):
    s1 = (int)(wyplac/ile)
    #print("wyplac: " + str(wyplac))
    #print("ile: " + str(ile))
    #print("ile musi byc calosci " + str(s1))
    if moneyDic[str(ile)]>=s1:
        s2 = wyplac - (ile*s1)
        s2 = round(s2,3)
        #print(s2)
        if s2>=2:
            if(mainCheck(s2,2)):
                return True
        elif s2>=1:
            if(mainCheck(s2,1)):
                return True
        elif s2>=0.50:
            if(mainCheck(s2,0.50)):
                return True
        elif s2>=0.20:
            if(mainCheck(s2,0.20)):
                return True
        elif s2>=0.10:
            if(mainCheck(s2,0.10)):
                return True
        elif s2>=0.05:
            if(mainCheck(s2,0.05)):
                return True
        elif s2>=0.02:
            if(mainCheck(s2,0.02)):
                return True
        elif s2>=0.01:
            if(mainCheck(s2,0.01)):
                return True
        else:
            return True
    else:
        return False

def lastCheck(wyplac,ile):
    #print("Printuje wyplac/ile" + str(wyplac) + "/" +str(ile))
    s1 = (int)(wyplac/ile)
    #print("printuje s1, ktore wpuszcza do odejmowania:" + str(s1))
    if moneyDic[str(ile)]>=s1:
        s2 = wyplac - (ile*s1)
        s2 = round(s2,3)
        print("Odejmuje od " + str(ile) + " tyle: " +str(s1))
        moneyDic[str(ile)]-=s1
        #print("printuje s2" + str(s2))
        if s2>=2:
            if(lastCheck(s2,2)):
                return True
        elif s2>=1:
            if(lastCheck(s2,1)):
                return True
        elif s2>=0.50:
            if(lastCheck(s2,0.50)):
                return True
        elif s2>=0.20:
            if(lastCheck(s2,0.20)):
                return True
        elif s2>=0.10:
            if(lastCheck(s2,0.10)):
                return True
        elif s2>=0.05:
            if(lastCheck(s2,0.05)):
                return True
        elif s2>=0.02:
            if(lastCheck(s2,0.02)):
                return True
        elif s2>=0.01:
            if(lastCheck(s2,0.01)):
                return True
        else:
            return True
    else:
        return False

piggybank=MoneyBox()
#def sprawdz():
#    for i in range(0,100):
#       piggybank.addCoins(Coin(0.01))
#sprawdz()
# Tworzenie okna
mainWindow=Tk()
mainWindow.title("Maszyna z napojami")
goodsWindow = Tk()
goodsWindow.title("Napoje")
# Tworzenie siatki na przyciski
mainFrame=ttk.Frame(mainWindow,borderwidth=2)
goodsFrame = ttk.Frame(goodsWindow,borderwidth=2)
# Umieszczenie siatki w oknie
mainFrame.grid(column=0, row=0, sticky=(N, E, W))
goodsFrame.grid(column=0,row=0,sticky=(N,E,W))
# Dodanie przycisków do wrzucania monet
i=0
j=0
k=0
label = ttk.Label(mainFrame, text=" Wrzucona kwota:").grid(row=0,column=1)
priceTextField = Text(mainFrame, height=1, width=8)
priceTextField.grid(column=2,row=0)
priceTextField.insert(END,piggybank.getSum())
label = ttk.Label(mainFrame, text="      ").grid(row=0,column=3)
label = ttk.Label(mainFrame, text="Numer produktu:").grid(row=0,column=5)
label = ttk.Label(mainFrame, text="      ").grid(row=4,column=2,columnspan=4)
numTextField = Text(mainFrame,height=1,width=8)
numTextField.grid(column=6,row=0)

for c in COINS:
    butt = ttk.Button(mainFrame, text="{:.2f}".format(c)+" zł",
            command=lambda z=c: piggybank.addCoins(Coin(z)) or priceTextField.delete('1.0',END) or priceTextField.insert(END,piggybank.getSum()) or priceTextField.insert(END,"zł") or abadonButt.config(state="normal"))
    if COINS[0]<=c<=COINS[2]:
        butt.grid(column=i, row=1)
        i+=1
    elif COINS[3]<=c<=COINS[5]:
        butt.grid(column=j,row=3)
        j+=1
    elif COINS[6]<=c<=COINS[8]:
        butt.grid(column=k,row=2)
        k+=1
i=4
j=4
k=4
for c in NUMBERS:
    butt = ttk.Button(mainFrame,text=str(c),
            command=lambda c=c: numTextField.insert(END,str(c)) or checkNumber(len(numTextField.get('1.0',END))) or abadonButt.config(state="normal") or checkPriceButt.config(state="normal") or proceedButt.config(state="normal"))
    if c == 0:
        butt.grid(column=5, row=4)
    elif 1<=c<=3:
        butt.grid(column=i, row=1)
        i+=1
    elif 4<=c<=6:
        butt.grid(column=j, row=2)
        j+=1
    elif 7<=c<=9:
        butt.grid(column=k, row=3)
        k+=1
i=0
for c in GOODS:
    label = ttk.Label(goodsFrame, text=c)
    label.grid(row = i, column=1)
    i+=1

#Dodatnie przycisku zatwierdzenia wyboru
proceedButt = ttk.Button(mainFrame, text="Zatwierdź wybór",
    command=lambda: Goods.buyGoods(int(numTextField.get('1.0',END)),piggybank.getSum()))
proceedButt.grid(column=1,row=7)
proceedButt.config(state="disabled")

# Dodanie przycisku sprawdzenia wartości zawartości
abadonButt = ttk.Button(mainFrame, text="Przerwij zakup",
    command=lambda: piggybank.abadonOperation() or priceTextField.delete('1.0',END) or numTextField.config(state="normal") or numTextField.delete('1.0',END) or checkPriceButt.config(state="disabled"))
abadonButt.grid(column=2, row=7)
abadonButt.config(state="disabled")
# Dodanie przycisku sprawdzenia ceny
checkPriceButt = ttk.Button(mainFrame, text="Sprawdź cenę",
    command = lambda: Goods.checkPrice(int(numTextField.get('1.0',END))) or numTextField.config(state="normal") or numTextField.delete('1.0',END) or checkPriceButt.config(state="disabled") or proceedButt.config(state="disabled"))
checkPriceButt.grid(column=3, row =7)
checkPriceButt.config(state="disabled")
mainloop()



