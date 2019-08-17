#! /usr/bin/env python3
#by Yusdel Lima Lorenzo Prin Prog 2019
class dfa:
    def main():
        q = []
        symbols = []
        rules = []
        start = ''
        final = []
        dfa = {}
        stateItems = []
        while True:
            currentState = start
            try:
                inputlines = (input().split(' '))
            except EOFError:
                quit()
            if inputlines[0] == 'states:':
                for i in range(len(inputlines)-1):
                    q.append((inputlines[i+1]))
            elif inputlines[0] == 'symbols:':
                for i in range(len(inputlines)-1):
                    symbols.append((inputlines[i+1]))
            elif inputlines[0] == 'begin_rules':
                    try:
                        while inputlines[0] != 'end_rules':
                            inputlines = (input().split(' '))
                            if len(inputlines) != 1:
                                rules.append(inputlines)
                    except EOFError:
                        quit()
            elif inputlines[0] == 'start:':
                for i in range(len(inputlines)-1):
                    start= (inputlines[i+1])
                currentState = start

            elif inputlines[0] == 'final:':
                for i in range(len(inputlines)-1):
                    final.append((inputlines[i+1]))

                for i in range(len(q)):
                    dfa.update({q[i]:{}})

                for i in range(len(rules)):
                    dfa[rules[i][0]].update({rules[i][4]:rules[i][2]})

                #dfa ={q[0]:{'a':q[1], 'c':q[2], 'b':q[3]},
                #      q[1]:{'a':q[1], 'b':q[2]},
                #      q[2]:{},
                #      q[3]:{}}

            else:
                path = list(str(inputlines[0]))

                #keep track of what state we are on and then update that state until its a final one?
                #if it ends with a final one or doesnt have a way to get from s2 to a letter then fail

                #check if stateItems set contains the letter

                stateItems = list(dfa[currentState].items())

                for char in range(len(path)):
                    found = False
                    for x in range(len(stateItems)):
                        if stateItems[x][0] == path[char]:
                            currentState = stateItems[x][1]
                            stateItems = list(dfa[currentState].items())
                            found = True
                            break
                    if found == False:
                        print('rejected')
                        break

                if len(path) != 0:
                    if found != False:
                        if currentState in final:
                            print('accepted')
                        else:
                            print('rejected')


    main()
