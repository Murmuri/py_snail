def getValue(name):
    value = input('Input ' + name + ': ')
    
    try:
        value = int(value)
    except:
        value = getValue(name)
    
    if value < 1:
        value = getValue(name)
           
    return value


def getEmptyMatrix(height, width):
    matrix = []
    
    for i in range(0, height):
        matrix.append(list(range(0, width)))
        
    return matrix


def printSnail(matrix):
    i  = 0
    
    while i < len(matrix):
        j = 0
        
        while j < len(matrix[i]):  
            print(matrix[i][j], end="\t")
            j += 1 
            
        i += 1
        print("\n")


def main():
    widthMatrix = getValue('width')
    heightMatrix = getValue('height')
    
    lengthMatrix = widthMatrix * heightMatrix
    matrix = getEmptyMatrix(heightMatrix, widthMatrix)
    
    i = 1
    w = 0 
    h = 0
    isHeight = True
    isPlus = True
    side = 2
    changePosition = 0
        
    while i <= lengthMatrix:
        matrix[h][w] = i
        
        if i < widthMatrix:
            w += 1
            i += 1
            continue
        
        if isHeight:
            
            if isPlus:
                h += 1
            else:
                h -= 1    
                
            changePosition += 1
                    
            if changePosition == heightMatrix - 1:
                isHeight = not isHeight
                changePosition = 0
                side += 1
                heightMatrix -= 1
                
                if side % 2:
                    isPlus = not isPlus 
        else: 
            
            if isPlus:
                w += 1
            else:
                w -= 1
                
            changePosition += 1
            
            if changePosition == widthMatrix - 1:
                isHeight = not isHeight
                changePosition = 0
                side += 1
                widthMatrix -=1
                
                if side % 2:
                    isPlus = not isPlus 
                
        i += 1
       
    printSnail(matrix)  
    

main()