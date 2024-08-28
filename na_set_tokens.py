import sys
allsokenbangames = []
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
n = 0
while n < 128:
    allsokenbangames.append(letters[int(n / 10)] + (str(n))[len(str(n)) - 1])
    n += 1

    
def na_set_tokens(filename, newvalue):
    # try:
        f = open(filename, "r")
        save_data = str(f.read())
        f.close()

        gamesdone = []
        while len(gamesdone) < len(allsokenbangames):
            gamesdone.append(0)


        n = 16 + len(gamesdone)
        # Load inventory
        # print (save_data[n:n+2])
        SAVEinventorytokens = str(newvalue)
        while len(SAVEinventorytokens) < 2:
            SAVEinventorytokens = "0" + SAVEinventorytokens
        save_data = save_data[:n] + SAVEinventorytokens + save_data[n + 2:]

        f = open(filename, 'w')
        f.write(save_data)
        f.close()
    # except:
    #     print("Could not load save file")




if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            na_set_tokens(sys.argv[1], sys.argv[2])
        elif len(sys.argv) > 1:
            tokens = input("How many tokens would you like to have? ")
            na_set_tokens(sys.argv[1], tokens)
        else:
            print('Format is na_set_tokens <filename> <token value>')
    except:
         print('Error Running program Correct format is na_set_tokens <filename> <token value>')
    input("application finished running press ENTER to close")