import simplegui
import time

#########################################################
#######################GUI###############################
#########################################################

data = [[55],[94, 48],[95, 30, 96],[77, 71, 26, 67],[97, 13, 76, 38, 45],
        [7, 36, 79, 16, 37, 68],[48, 7, 9, 18, 70, 26, 6],[18, 72, 79, 46, 59, 79,29, 90],
        [20, 76, 87, 11, 32, 7, 7, 49, 18],[27, 83, 58, 35, 71, 11, 25, 57, 29, 85],
        [14, 64, 36, 96, 27, 11, 58, 56, 92, 18, 55],
        [2, 90, 3, 60, 48, 49, 41, 46, 33, 36, 47, 23],
        [92, 50, 48, 2, 36, 59, 42, 79, 72, 20, 82, 77, 42],
        [56, 78, 38, 80, 39, 75, 2, 71, 66, 66, 1, 3, 55, 72],
        [44, 25, 67, 84, 71, 67, 11, 61, 40, 57, 58, 89, 40, 56, 36],
        [85, 32, 25, 85, 57, 48, 84, 35, 47, 62, 17, 1, 1, 99, 89, 52],
        [6, 71, 28, 75, 94, 48, 37, 10, 23, 51, 6, 48, 53, 18, 74, 98, 15],
        [27, 2, 92, 23, 8, 71, 76, 84, 15, 52, 92, 63, 81, 10, 44, 10, 69, 93]]

def draw_handler(canvas):
    canvas.draw_text('A', (20, 20), 12, 'Red')
    canvas.draw_text('B', [30, 50], 20, 'Blue')
    canvas.draw_text('C', (80, 50), 12, 'Gray', 'serif')

    
def draw_matrix(canvas):
    global data
    put = data[0][0].putanja
    width = 850
    height = 500
    poz = []
    for i in range(len(data) - 1, -1, -1):
        podwidth = width / len(data[i])
        if i != len(data) - 1:
            poz = IzracunajPozicije(poz)
        nova = []
        for j in range (len(data[i])):
            if i != 0:
                if put[i-1] == j:
                    color = "White"
                else:
                    color = "Red"
            else:
                color = "White"
            if i == len(data) - 1:
                canvas.draw_text(str(data[i][j].value), [(j)*podwidth+10, (i+1)*25+5], 20, color)
                poz += [(j) * podwidth+10]
            else:
                canvas.draw_text(str(data[i][j].value), [poz[j], (i+1)*25+5], 20, color)
                if i == len(data) - 1:
                    canvas.draw_text(str(data[i][j].value), [(j)*podwidth+10, (i+1)*25+5], 20, color)
                    poz += [(j) * podwidth+10]
                else:
                    canvas.draw_text(str(data[i][j].value), [poz[j], (i+1)*25+5], 20, color)
    message = "Maximum sum descent: " + str(data[0][0].broj)
    canvas.draw_text(message, [10, 490], 20, "White")
            
                
        
        
def IzracunajPozicije(poz):
    nova = []
    for i in range(len(poz) - 1):
        nova += [int((poz[i] + poz[i+1])/2)]
    return nova


#########################################################
###############Algoritam pretrage########################
#########################################################

class Polje(object):
    def __init__(self, broj):
        self.broj = broj
        self.value = broj
        self.putanja = []

    def setPutanja(self, putanja):
        self.putanja = putanja

    def setBroj(self, broj):
        self.broj = broj
        
       

def bottomup(data):
    while len(data) != 1:
        zadnji = len(data) - 1
        for i in range(len(data[zadnji])-1):
            frame.set_draw_handler(draw_matrix)
            if data[zadnji][i].broj != '#' and data[zadnji][i+1].broj != '#' and data[zadnji - 1][i].broj != '#':
                if data[zadnji][i].broj > data[zadnji][i + 1].broj:
                    data[zadnji - 1][i].setBroj(data[zadnji - 1][i].broj + data[zadnji][i].broj)
                    data[zadnji - 1][i].setPutanja([i] + data[zadnji][i].putanja)
                else:
                    data[zadnji - 1][i].setBroj(data[zadnji - 1][i].broj + data[zadnji][i+1].broj)
                    data[zadnji - 1][i].setPutanja([i+1] + data[zadnji][i+1].putanja)
            elif data[zadnji][i].broj == '#' and data[zadnji][i+1].broj != '#':
                data[zadnji - 1][i].setBroj(data[zadnji - 1][i].broj + data[zadnji][i+1].broj)
                data[zadnji - 1][i].setPutanja([i+1] + data[zadnji][i+1].putanja)
            elif data[zadnji][i].broj != '#' and data[zadnji][i+1].broj == '#':
                data[zadnji - 1][i].setBroj(data[zadnji - 1][i].broj + data[zadnji][i].broj)
                data[zadnji - 1][i].setPutanja([i] + data[zadnji][i].putanja)
            frame.set_draw_handler(draw_matrix)
        data = data[:-1]
        


def PretvoriUObjekte(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = Polje(data[i][j])
            
def MaximumSumDescent(data):
    bottomup(data)
    

            
####################################################
##################Inicijalizacija###################
####################################################

frame = simplegui.create_frame('Testing', 900, 500)
PretvoriUObjekte(data)
frame.set_draw_handler(draw_matrix)
frame.start()

MaximumSumDescent(data)
