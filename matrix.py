import copy
class matrix:
    """
    Defines the matrix object
    rows: number of rows
    cols: number of columns
    elements: 2d list containing the matrix entries Ex. elements[2][4] is the entry at row 2 column 4
    identity: 2d list containing the identity matrix corresponding to elements.

    """



    def __init__(self,r,c):
        """
        Builds the matrix object
        :param r: rows
        :param c: columns
        """
        self.rows = r
        self.cols = c
        self.elements = [[0]*self.cols for i in range(self.rows)]
        self.identity = [[0]*self.cols for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if(i == j):
                    self.identity[i][j] = 1
                else:
                    self.identity[i][j] = 0



    def setElements(self, arr):
        self.elements = arr
    def setElement(self,i,j,value):
        self.elements[i][j] = value
    def getElements(self):
        return self.elements
    def getElement(self,i,j):
        return self.elements[i][j]
    def swapRows(self,a,b):
        temp = self.getElements()[a]
        self.getElements()[a] = self.getElements()[b]
        self.getElements()[b] = temp
    def multiply(self,other):
        if(self.cols != other.rows):
            print("The two matricies are not multiplicable")
            return
        result = matrix(self.rows,other.cols)

        for i in range(0,len(self.elements)):
            for j in range(0,len(other.elements[0])):
                sum = 0
                for k in range(0,len(self.elements[0])):
                    sum += self.elements[i][k] * other.elements[k][j]
                    #print(i," ", j," ",k," ",sum)
                result.elements[i][j] = sum

        return result


    def concat(self,b):
        result = matrix(self.rows,self.cols + b.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.setElement(i,j,self.elements[i][j])
        for k in range(b.rows):
            for l in range(b.cols):
                result.setElement(k,l+self.cols,b.getElement(k,l))
        return result

    def gaussJordan(self,b):
        result = self.concat(b) #augment the matrix
        e =1


        for j in range(self.cols):
            maxVal = 0
            p=-1
            for i in range(j,self.rows):
                if(abs(result.getElement(i,j)) > maxVal): #find the largest value in each row
                    maxVal = abs(result.getElement(i,j))
                    p = i

            if(maxVal == 0):
                e = 0
                return "no solution"
            if(p>j):
                result.swapRows(p,j) #perform a row swap for the row with the largest value in the column


            pivVal = result.getElement(j, j)
            for k in range(result.cols):

                result.setElement(j,k,result.getElement(j,k)/pivVal) #divide the row by the pivot value



            for l in range(result.rows):
                c = result.getElement(l,j)
                if(l != j):
                    for m in range(result.cols):

                        result.setElement(l,m,(result.getElement(l,m) - result.getElement(j,m)*c)) #subtract rows to get the identity matrix

            solution = matrix(result.rows,1)
            for n in range(result.rows):
                solution.setElement(n,0,result.getElement(n,result.cols-1))
            print(result)
            print(solution)
        return result

    def Inverse(self):
        self.identityMatrix = matrix(self.rows,self.cols)
        self.identityMatrix.setElements(self.identity)

        inverse = matrix(self.rows,self.cols)
        result = self.gaussJordan(self.identityMatrix)


        for i in range(self.rows):
            for j in range(self.cols,result.cols):
                inverse.setElement(i,j-self.cols,result.getElement(i,j))
        print(inverse)

    def gaussianElimSolution(self,b):
        result = self.concat(b)
        e = 1


        for j in range(self.cols):
            maxVal = 0
            p = -1
            for i in range(j, self.rows):
                if (abs(result.getElement(i, j)) > maxVal): #find the largest value in each column
                    maxVal = abs(result.getElement(i, j))
                    p = i
            if (p > j):
                result.swapRows(p, j) #swap rows


            for l in range(result.rows):
                c = result.getElement(l,j)
                d = result.getElement(j,j)
                f = c/d
                if(l > j):
                    for m in range(result.cols):

                        result.setElement(l,m,(result.getElement(l,m) - result.getElement(j,m)*f)) #build the lower triangle matirx

            solution = matrix(result.rows,1)


            print(result)

        return result


    def gaussianElim(self):
        result = copy.deepcopy(self) #same as gaussianElimSolution except there is no matrix to augment
        e = 1
        r = 0


        for j in range(self.cols):
            maxVal = 0
            p = -1
            for i in range(j, self.rows):
                if (abs(result.getElement(i, j)) > maxVal):
                    maxVal = abs(result.getElement(i, j))
                    p = i
            if (p > j):
                result.swapRows(p, j)
                r+=1


            for l in range(result.rows):
                c = result.getElement(l,j)
                d = result.getElement(j,j)
                f = c/d
                if(l > j):
                    for m in range(result.cols):

                        result.setElement(l,m,(result.getElement(l,m) - result.getElement(j,m)*f))
            print(result)


        return result,r

    def determinant(self):
        result,r = self.gaussianElim() #finds the determinant by using the matrix trace
        product = 1

        for i in range(result.rows):
            product*=result.getElement(i,i)
        if(r%2==1):
            product *= -1

        print(product)
















































    def __str__(self):
        self.elems = ""
        for i in range(0,len(self.elements)):

            for j in range(0,len(self.elements[i])):

                self.elems += str(self.elements[i][j]) + " "
            self.elems += "\n"

        return self.elems



