from datetime import datetime
import multiprocessing

def create(queue):
            n1 = queue.get()
            n2 = queue.get()
            npow = n1**n2
            sum = 0
            daten = datetime.now()
            for i in range(npow+1):
                sum+=i
            with open("answer.txt", "a") as file:
                file.write(str(daten) + " >> " + str(n1) + " ^ " + str(n2) + " = " + str(npow) + "\n")

if __name__ == '__main__':  
    queue = multiprocessing.Queue()
    list_process = []
    for i in range(5):
        try:
            x,y = map(int,input("Числа и степень: ").split())
        except:
            print("неверный ввод")
        queue.put(x)
        queue.put(y)
        con = multiprocessing.Process(target=create, args=(queue,))
        con.start()
        list_process.append(con)
        
    
    [con.join() for con in list_process]
s
