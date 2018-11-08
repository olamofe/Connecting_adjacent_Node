
# Complete the 'countMatches' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid1
#  2. STRING_ARRAY grid2
#

def countMatchesX(grid1, grid2):
    visited_grid1 = {}
    visited_grid2 = {}
    stack_grid1 = []
    stack_grid2 = []
    grid1_Ones = getOnesPos(grid1)
    grid2_Ones = getOnesPos(grid2)
    region1 = []
    region2 = []
    for pos in grid1_Ones:
        if visited_grid1.get(tuple(pos)) == True:
            pass
        else:
            visited_grid1[tuple(pos)] = True
            if(iCanFormEdges(pos, grid1)):
                stack_grid1.insert(0, pos)
                set_grid1 = set()
                set_grid1.add(tuple(pos))
                region1.insert(0, set_grid1)
                neighbour_grid1 = getNeighbors(pos, grid1)
                depthFirstSearch(grid1, visited_grid1, neighbour_grid1, stack_grid1, set_grid1)
                    

                
            
    for pos in grid2_Ones:
        if visited_grid2.get(tuple(pos)) == True:
            pass
        else:
            visited_grid2[tuple(pos)] = True
            if(iCanFormEdges(pos, grid2)):
                set_grid2 = set()
                set_grid2.add(tuple(pos))
                stack_grid2.insert(0, pos)
                region2.insert(0, set_grid2)
                neighbour_grid2 = getNeighbors(pos, grid2)
                print("from main", set_grid2, "gridNeibor ", neighbour_grid2, "pos ", pos)
                depthFirstSearch(grid2, visited_grid2, neighbour_grid2, stack_grid2, set_grid2)


#                 
                
#     count = 0
#     for reg in region1:
#         if reg in region2:
#             count += 1
#     return count
            
    return [region1, region2]
        

def depthFirstSearch(grid, visited, neigbourList, stack_grid1, set_grid1):
    print("I am neibourlist ", neigbourList)
    for neigbour in neigbourList:
        if visited.get(tuple(neigbour)) != True:
            visited[tuple(neigbour)] = True
            neighbour_grid1 = getNeighbors(neigbour, grid)
            if(iCanFormEdges(neigbour, grid)) and (validLink(visited, neighbour_grid1)):
                stack_grid1.insert(0, neigbour)
                set_grid1.add(tuple(neigbour))
                print("data Entered here ",tuple(neigbour), " ", set_grid1 )
                depthFirstSearch(grid, visited, neighbour_grid1, stack_grid1, set_grid1)
                
#                 neighbour_grid1 = getNeighbors(neigbour, grid)
#                 print("depth called", set_grid1)
                
                
            if(iCanFormEdges(neigbour, grid)) and (not validLink(visited, neighbour_grid1)):
                stack_grid1.pop(0)
                set_grid1.add(tuple(neigbour))
                print("Medata Entered here ",tuple(neigbour), " ", set_grid1 )
            

        
    
def validLink(visited, neigbourList):
    neigbourList = set([tuple(data) for data in neigbourList])
    visited = set([tuple(data) for data in visited.keys()])
    if(len(neigbourList - visited) != 0):
        return True
    else:
        return False
        
        

def getOnesPos(grid1):
    oneList = []
    for row in range(len(grid1)):
        for col in range(len(grid1[0])):
            if(iCanFormEdges):
                oneList.insert(0,[row, col])
    return oneList
            
            
    # Write your code here
def getNeighbors(node, grid):
    #node is a position list [row, col]
    rowSize = len(grid)-1
    colSize = len(grid[0])-1
    row = node[0]
    col = node[1]
    neighbouList = []
    #selecting neighbours at array egdes 
    if row == 0 and col == 0:
        neighbouList = [[row,col+1], [row+1, col]]
    if row == 0 and col == colSize:
        neighbouList = [[row, col-1], [row+1, col]]
        
    if row == rowSize and col == 0:
        neighbouList = [[row-1, col], [row, col+1]]
    if row == rowSize and col == colSize:
        neighbouList = [[row, col-1], [row-1, col]]
        
        # neighbour at boundary left and right of array where col is 0 or colSize
    if (row != 0 and row != rowSize) and col == 0:
        neighbouList = [[row-1, col], [row+1, col], [row, col+1]]
    
    if (row != 0 and row != rowSize) and col == colSize:
        neighbouList = [[row-1, col], [row+1, col], [row, col-1]]
       
        # neighbour at boundary top and bottom of array where row is 0 or rowSize
    if (col != 0 and col != colSize) and row == 0:
        neighbouList = [[row, col-1], [row+1, col], [row, col+1]]
    
    if (col != 0 and col != colSize) and row == rowSize:
        neighbouList = [[row, col-1], [row-1, col], [row, col+1]]
        
        #neighbour at any other position
    if (col != 0 and col != colSize) and (row != 0 and row != rowSize):
        neighbouList = [[row, col-1], [row-1, col], [row, col+1], [row+1, col]]
        
    return neighbouList
    
    
def checkEdges(myList, grid):
    for node in myList:
        if(iCanFormEdges(node, grid)):
            return True
        else:
            return False
        
def iCanFormEdges(pos, grid):
    if int(grid[pos[0]][pos[1]]) == 1:
        return True
    else:
        return False