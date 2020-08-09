# ensure that we dont cross the borders of the matrix
def accessible(plateau, i, j):
    if i >= 0 and i < len(plateau) and j >= 0 and j < len(plateau[0]):
        return True
    else:
        return False

# verify if the destination is one step ahead
def arrive(icurrent,jcurrent,fin):
    if (icurrent + 1,jcurrent) == fin or (icurrent - 1,jcurrent) == fin or (icurrent,jcurrent + 1) == fin or (icurrent,jcurrent - 1) == fin :
        return True
    return False


def chemin(plateau, deb, fin,visited):
    # if the source is the distination!
    if deb == fin :
        return True
    ideb,jdeb = deb
    #look in the next step
    if arrive(ideb,jdeb,fin):
        return True
    passed = False
    # all possible moves
    if (accessible(plateau, ideb + 1, jdeb) and plateau[ideb + 1][jdeb] == False and (ideb + 1,jdeb) not in visited):
        passed = True
        visited.append((ideb + 1,jdeb))
        if chemin(plateau, (ideb + 1, jdeb), fin,visited) == True :
            return True
    if (accessible(plateau, ideb - 1, jdeb) and plateau[ideb - 1][jdeb] == False and (ideb - 1,jdeb) not in visited):
        passed = True
        visited.append((ideb - 1,jdeb))
        if chemin(plateau, (ideb - 1, jdeb), fin,visited) == True :
            return True
    if (accessible(plateau, ideb, jdeb + 1) and plateau[ideb][jdeb + 1] == False and (ideb,jdeb + 1) not in visited):
        passed = True
        visited.append((ideb,jdeb + 1))
        if chemin(plateau, (ideb, jdeb + 1), fin,visited) == True :
            return True
    if (accessible(plateau, ideb, jdeb - 1) and plateau[ideb][jdeb -1] == False and (ideb,jdeb -1) not in visited):
        passed = True
        visited.append((ideb,jdeb - 1))
        if chemin(plateau, (ideb, jdeb -1), fin,visited) == True :
            return True
    if passed == False:
        return False




plateau = [ [True , False , False , False ],
            [ False , True , True , False ] ]

if chemin(plateau, (1,3), (1,0), [(1,3)]) == True :
    print("True")
else:
    print("False")
