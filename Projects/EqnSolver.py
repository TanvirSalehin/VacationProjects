#     TODO for 31-08-2021
#     
#     1.   Make this such, so that it can go beyond the range.
#     2.   Reformat this to a much simpler and function based file.
#     3.   Make differForTwo()
#     4.   Implement differForOne() and differForTwo()


import math

def initialize():
    unknowns = int(input("How many unknowns: " ))
    if unknowns == 2:
        equal = input("Can the unknowns be equal?   y/n"
                    "\n==> ")
    else:
        equal = "y"
        
    lhs = input("Write the lhs:\n")
    rhs = input("Write the rhs:\n")
    
    return unknowns, equal, lhs, rhs

unknowns, equal, lhs, rhs = initialize()

def styleAssign(style):
    pstyle = 1
    if style == 2:
        pstyle = 2
    elif style == 3:
        pstyle = 3
    elif style == 4:
        pstyle = 4
    elif style == 1:
        pstyle = 1
    else:
        pstyle = 1
        
    return pstyle

def solPrinter(pstyle, List, Dict):
    if pstyle == 2:
        print(List)
    elif pstyle == 3:
        print(Dict)
    elif pstyle == 4:
        print(List)
        print(Dict)

def solveForOne(lhs, rhs, List, Dict, StyleName, solnum, range1, range2):
    for x in range(range1, range2):
        try:
            if evaluate(lhs, x) == evaluate(rhs, x):
                List.append(x)
                solnum += 1
                Dict[solnum] = x
                if StyleName == 1:
                	print("The unknown is: ", x)
        except ZeroDivisionError:
            continue

def differForOne(lhs, rhs, range1, range2):
    dlist = []
    xlist = []
    slist = []
    for x in range(range1, range2):
        try:
            if x == range1:
                xlist.append(x)
                dif = evaluate(lhs, x) - evaluate(rhs, x)
                dlist.append(dif)
            else:
                difference = evaluate(lhs, x) - evaluate(rhs, x)
                differ1 =  evaluate(lhs, x) - evaluate(rhs, x)
                differ2 =  evaluate(lhs, x-1) - evaluate(rhs, x-1)
                differ1, differ2 = (differ1 ** 2), (differ2 ** 2)
                differ1, differ2 = math.sqrt(differ1), math.sqrt(differ2)
                differ1, differ2 = int(differ1), int(differ2)
                if differ1 < differ2:
                    differ = differ1
                elif differ1 > differ2:
                    differ = differ2
                else:
                    differ = dlist[0]
                differ_ = dlist[0]
                if differ < differ_:
                    xlist[0] = x
                elif differ > differ_:
                    differ = differ_
                else:
                    pass
                dlist.append(differ)
                if difference == 0:
                    slist.append(x)
        except ZeroDivisionError:
                continue
    r1, r2 = dlist[0], xlist[0]
    return r1, r2, slist

def solveForTwo(lhs, rhs, List, Dict, StyleName, solnum, equal, range1, range2):
    for x in range(range1, range2):
            for y in range(-range1, range2):
                if x == y:
                    if not equal:
                        continue
                try:
                    if evaluate(lhs, x, y) == evaluate(rhs, x, y):
                        solnum += 1
                        li = [x, y]
                        List.append(li)
                        Dict[x] = y
                        if StyleName == 1:
                            print("The unknowns are: ", x, y)
                except ZeroDivisionError:
                    continue

def convertLiToStr(List):
	string = ''
	for element in List:
		string += str(element)
	return string

def convertStrToLi(string):
    list1=[]
    list1[:0]=string
    return list1

def evaluate(exp, a=0, b=0, c=0):
	exp1 = exp
	exp1 = convertStrToLi(exp1)
	for element in range(len(exp1)):
		if exp1[element] == 'x':
			exp1[element] = a
		elif exp1[element] == 'y':
			exp1[element] = b
		elif exp1[element] == 'z':
			exp1[element] = c
	exp1 = convertLiToStr(exp1)
	exp1 = eval(exp1)
	return exp1


def solve(lhs, rhs, Unknowns, equal = True, style = 1, prnt=True):
    print("Solving for the equation with ", Unknowns, " unknown(s):\n", lhs, "=", rhs)
    Solutions = []
    SolutionDict = {}
    
    range1 = -100
    range2 = 100
    
    pstyle = styleAssign(style)
    
    if Unknowns == 1:
        a = 0
        smallDiffer, smallDifferx, Solutions = differForOne(lhs, rhs, range1, range2)
        for i in range(1, len(Solutions) + 1):
            SolutionDict[i] = Solutions[i - 1]
            a += 1
        #solveForOne(lhs, rhs, Solutions, SolutionDict, pstyle, a, range1, range2)
        if prnt:
            solPrinter(pstyle, Solutions, SolutionDict)
        else:
            pass
        return Solutions, SolutionDict
        
            
                
    elif Unknowns == 2:
        a = 0
        solveForTwo(lhs, rhs, Solutions, SolutionDict, pstyle, a, equal, range1, range2)
        if prnt:
            solPrinter(pstyle, Solutions, SolutionDict)
        else:
            pass
        return Solutions, SolutionDict

    if a == 0:
        pass

run = True
while run:
    outputStyle = int(input("Write 1 for normal output."
                        "\nWrite 2 for Output in List."
                        "\nWrite 3 for output in Dictionary."
                        "\nWrite 4 for output in both Dictionary and List."
                        "\n"
                        "\n==> "))
    if equal == "y":
        if outputStyle == 1:
            solve(lhs, rhs, unknowns, True, 1)
            run = False
        elif outputStyle == 2:
            a, b = solve(lhs, rhs, unknowns, True, 2)
            run = False
        elif outputStyle == 3:
            a, b = solve(lhs, rhs, unknowns, True, 3)
            run = False
        elif outputStyle == 4:
            a, b = solve(lhs, rhs, unknowns, True, 4)
            run = False
        else:
            print("The input to see the style of output has to be a positive integer among 1, 2, 3, 4."
                  "\n")
            
    elif equal == "n":
        if outputStyle == 1:
            solve(lhs, rhs, unknowns, False, 1)
            run = False
        elif outputStyle == 2:
            a, b = solve(lhs, rhs, unknowns, False, 2)
            run = False
        elif outputStyle == 3:
            a, b = solve(lhs, rhs, unknowns, False, 3)
            run = False
        elif outputStyle == 4:
            a, b = solve(lhs, rhs, unknowns, False, 4)
            run = False
        else:
            print("The input to see the style of output has to be a positive integer among 1, 2, 3, 4.")

#                    Made By Tanvir
