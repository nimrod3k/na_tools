import sys
from areainfo import areainfo
allsokenbangames = []
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
n = 0
while n < 128:
    allsokenbangames.append(letters[int(n / 10)] + (str(n))[len(str(n)) - 1])
    n += 1





def checksokobanmachines(filename):
    try:
        f = open(filename, "r")
        save_data = str(f.read())
        f.close()

        gamesdone = []
        while len(gamesdone) < len(allsokenbangames):
            gamesdone.append(0)

        n = 15
        i = 0
        count_unfound = 0
        count_optimized = 0
        count_done = 0
        print('Machines left to optimize:')
        while i < len(gamesdone):
            if areainfo[i]['moves'] != 0:
                if int(save_data[n]) == 1:
                    count_done += 1
                    print(f'Machine #{i} ({allsokenbangames[i]}): {areainfo[i]["loc"]}')
                elif int(save_data[n]) == 0:
                    count_unfound += 1
                else:
                    count_optimized += 1
            n += 1
            i += 1
        if count_unfound + count_optimized + count_done != 100:
            print ("Something went wrong")
        print (f'You have {count_unfound} machine(s) left to find')

        

    except:
        print("Could not load save file")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        checksokobanmachines(sys.argv[1])
    else:
        print('Format is na_machinechecker.py <filename>')
    input("application finished running press ENTER to close")