import numpy as np

flag = 0
# To print matrix without brackets
def printf(mat):
    print(str(mat).replace(' [', '').replace('[', '').replace(']', ''),end="\n\n")

# Main Matrix
matrix = []
# First Element
row = list(map(int,input().split()))
columns = len(row)
rows = 1
matrix.append(row)

# Taking input of other rows and appending to main matrix
while True:
    row = list(map(int,input().split()))
    if(len(row)==columns):
        matrix.append(row)
        rows += 1
    # So that plain enter can end the input and get final matrix
    else:
        break

# Converting matrix to numpy matrix
matrix = np.array(matrix)

for j in range(1,columns):
    for i in range(j,rows):
        # if flag==1:
        #     i -= 1
        #     flag -=1
        current = matrix[i][j-1]
        current_row = matrix[i]
        key = matrix[j-1][j-1]
        key_row = matrix[j-1]
        print(current,current_row,key,key_row)
        # Required condition of making zero is already satisfied
        if current == 0:
            continue
        # Case when key is zero
        if key == 0:
            # Operation such that key element won't be zero
            
            temp_var = 0
            # Checking that adjacent row isn't zero
            # Changing adjacent row if it is zero
            for temp_var in range(0,rows-i):
                adjacent_el = matrix[j][i]
                adjacent_row = matrix[j]
                if adjacent_el == 0:
                    adjacent_el = matrix[j+temp_var][i]
                    adjacent_row = matrix[j+temp_var]
            matrix[j-1] = key_row + adjacent_row
            print('R',j,' -> ','R',j,' + ','R',j+temp_var,sep="")
            printf(matrix)
            # Resetting loop iteration
            i-=1
            print(i,'`',sep="")
            continue
        # Case when current element is exactly divisible by key
        elif current%key==0:
            factor = current//key
            # Operation on current row
            matrix[i] = current_row - factor*key_row
            # Printing case of positive and negative case
            if key*current > 0:
                print('R',i+1,' -> ','R',i+1,'-',factor,'*R',j,sep="")
            else:
                print('R',i+1,' -> ','R',i+1,'-',abs(factor),'*R',j,sep="")
        # General Case scenario
        else:
            matrix[i] = current_row*key - key_row*current
            print('R',i+1,' -> ',key,'*R',i+1,' - ',current,'*R',j,sep="")
        printf(matrix)
