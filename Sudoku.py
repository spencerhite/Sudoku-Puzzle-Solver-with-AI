import time
from csp import backtracking_search, Sudoku, forward_checking
#import necessary libraries

easy = ".3..8...65..29471....3..5....5.1.8.442.8.5.391.8.3.6....3..7....41653..22...4..6."
"""Added the easy sudoku problem to test both
    simple and smart backtracking.
 """

#...26.7.168..7..9.19...45..82.1...4...46.29...5...3.28..93...74.4..5..367.3.18...

game = Sudoku(easy) #initializes the Sudoku class
search = backtracking_search(game,inference=forward_checking) #initializes the smart backtracking alogirthm as search

e = Sudoku(easy)
print("\nInitial board for smart backtracking search: \n")
e.display(e.infer_assignment()) #displays the initial board
print("\nFinished board for smart backtracking search: \n")
start_time = time.perf_counter() #begins counting timer for runt time
backtracking_search(e, inference=forward_checking) #runs the smart backtrack search
end_time = time.perf_counter() #ends run time counter
e.display(e.infer_assignment()) #displays the finished board
smart = search[1] #assigns number of assigned variables to smaart
print("\nTime taken (seconds): ", end_time - start_time) #displays the runtime
print("\nNumber of trials of assigning values to the variables", smart) #displays the number of assigned variables

#I have these just for my sake. Deletes values of game and search because I'm not entirely sure how python works.
del game
del search

game = Sudoku(easy) #initializes the Sudoku class
search = backtracking_search(game) #initializes the smart backtracking alogirthm as search

f = Sudoku(easy)
print("\nInitial board for simple backtracking search: \n")
f.display(f.infer_assignment()) #displays the initial board
print("\nFinished board for simple backtracking search: \n")
start_time = time.perf_counter()#begins counting timer for runt time
backtracking_search(f) #runs the simple backtrack search
end_time = time.perf_counter() #ends run time counter
f.display(f.infer_assignment()) #displays the finished board
simple = search[1] #assigns number of assigned variables to simple
print("\nTime taken (seconds): ", end_time - start_time) #displays the runtime
print("\nNumber of trials of assigning values to the variables", simple) #displays the number of assigned variables













