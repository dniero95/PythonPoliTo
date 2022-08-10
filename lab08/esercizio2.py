# Scrivete la funzione neighbor_average(values, row, column)che, in una tabella values, calcoli il valore medio dei vicini di un elemento nelle otto direzioni, come si può vedere nella figura sotto. Se, però, l’elemento si trova su un bordo della tabella, la media va calcolata considerando soltanto i vicini che appartengono effettivamente alla tabella. Ad esempio, se row e column valgono entrambe 0, ci sono soltanto tre vicini.


def neighbor_average(values, row, column):
    average = 0


    if row == 0 and column == 0:
        average = (values[row][1] + values[1][1] + values[1][column])/3
    elif row == len(values)-1 and column == 0:
        average = (values[row][1] + values[row-1][1] + values[row-1][column])/3
    elif row == len(values)-1 and column == len(values[0])-1:
        average = (values[row][column-1] + values[row-1][column-1] + values[row-1][column])/3
    elif row == 0 and column == len(values[0])-1:
        average = (values[row][column-1] + values[1][column-1] + values[1][column])/3
    elif row == 0:
        average = (values[row][column-1] + values[1][column-1] + values[1][column] + values[1][column+1] + values[row][column+1])/5
    elif row == len(values)-1:
        average = (values[row][column-1] + values[row-1][column-1] + values[row-1][column] + values[row-1][column+1] + values[row][column+1])/5
    elif column == 0:
        average = (values[row-1][column] + values[row-1][1] + values[row][column+1] + values[row+1][column+1] + values[row][column+1])/5
    elif column == len(values[0])-1:
        average = (values[row-1][column] + values[row-1][1] + values[row][column+1] + values[row+1][column+1] + values[row][column+1])/5
    else:
        average = (values[row-1][column-1]+ values[row-1][column] +values[row-1][column+1] + values[row][column-1]+ values[row][column+1] + values[row+1][column-1]+ values[row+1][column] +values[row+1][column+1])/8

    return average



table = [[2,2,2],[2,2,2],[2,2,2]]

print(neighbor_average(table, 2, 0))