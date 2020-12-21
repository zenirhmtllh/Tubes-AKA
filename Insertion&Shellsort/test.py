from tkinter import*
from tkinter import ttk
import random
import time
import sys
import threading

root = Tk()
root.title('tugas AKA')
root.maxsize(1920, 1080)
root.config(bg='black')

#variable
selected_alg = StringVar()
data = []
data2 = []
dataMin = 0
dataMax = 0


def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 1
    spacing = 1
    normalizeData = [i / max(data) for i in data]
    for i, height in enumerate(normalizeData):
        #top
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #botton
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        #canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()


def drawData2(data2, colorArray):
    canvas2.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data2) + 1)
    offset = 1
    spacing = 1
    normalizeData = [i / max(data2) for i in data2]
    for i, height in enumerate(normalizeData):
        #top
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #botton
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas2.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        #canvas2.create_text(x0+2, y0, anchor=SW, text=str(data2[i]))
    root.update_idletasks()


def buat():
    global data
    global data2
    global dataMin, dataMax

    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 100
    try:
        size = int(sizeEntry.get())
    except:
        size = 50

    if minVal < 0:
        minVal = 0
    if maxVal > 100:
        maxVal = 100
    if size > 1000 or size < 3:
        size = 25
    if minVal > maxVal:
        minVal, maxVal = maxVal, minVal

    data = []
    data2 = []
    dataMin = minVal
    dataMax = maxVal
    

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    data2 = data.copy()

    drawData(data, ['black' for x in range(len(data))])
    drawData2(data2, ['black' for x in range(len(data2))])


def shellSort(array, drawData2):
    start_time2 = time.time()
    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            drawData2(data, ['red' if x == j or x == j-interval else 'black' for x in range(len(array))])
            time.sleep(0.001)
            array[j] = temp
        interval //= 2
        drawData2(data, ['red' if x == j or x == j-interval else 'black' for x in range(len(array))])
    Label(text=("%s seconds" % (time.time() - start_time2))).grid(row=1, column=2, padx=5, pady=5)



def partition(data, low, high, drawData):
    i = (low-1)        
    pivot = data[high]     
 
    for j in range(low, high):
 
        if data[j] <= pivot:
            
            i = i+1
            drawData(data, ['red' if x == i or x == j else 'black' for x in range(len(data))])
            time.sleep(0.001)
            data[i], data[j] = data[j], data[i]
            

    data[i+1], data[high] = data[high], data[i+1]
    drawData(data, ['red' if x == i or x == j else 'black' for x in range(len(data))])
    return (i+1)

def Insertionsort(data, low, high, drawData):
    start_time2 = time.time()
    quickSort(data, low, high, drawData)
    Label(text=("%s seconds" % (time.time() - start_time2))).grid(row=1, column=0, padx=5, pady=5)

def InsertionSort(data, low, high, drawData):
    
    if len(data) == 1:
        return data
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(data, low, high, drawData)
 
        
        quickSort(data, low, pi-1, drawData)
        quickSort(data, pi+1, high, drawData)
    

def startAlgorithm():
    global data
    global data2
    global dataMin, dataMax
    buat()
    threading.Thread(target=shellSort, args=(data2, drawData2)).start()
    threading.Thread(target=quickSortMaster, args=(data, 0, len(data)-1, drawData)).start()


Label(text="").grid(row=1, column=0, padx=5, pady=5)
Label(text="").grid(row=1, column=2, padx=5, pady=5)


#frame

Label(text="Quick Sort").grid(row=5, column=0, padx=5, pady=5)
canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=4, column=0, padx=10, pady=5)

Label(text="Shell Sort").grid(row=5, column=2, padx=5, pady=5)
canvas2 = Canvas(root, width=600, height=380, bg='white')
canvas2.grid(row=4, column=2, padx=10, pady=5)
Button(text="Start", command=startAlgorithm, bg="white").grid(row=4, column=1, padx=5, pady=5)


#UI
#row[1]


root.mainloop()


 
