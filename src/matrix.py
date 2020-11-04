class Matrix():

    def __init__(self, elements):
        self.elements = elements
        self.num_rows = len(self.elements)
        self.num_cols = len(self.elements[0])


    def copy(self): 
        return Matrix(self.elements)

    def add(self, c):
        result = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        for row_index in range(self.num_cols):
            for col_index in range(self.num_rows):
                sum_of_elements = self.elements[row_index][col_index] + c.elements[row_index][col_index]
                result[row_index][col_index] = sum_of_elements
        return Matrix(result)

    def subtract(self, c):
        result = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        for row_index in range(self.num_cols):
            for col_index in range(self.num_rows):
                sum_of_elements = self.elements[row_index][col_index] - c.elements[row_index][col_index]
                result[row_index][col_index] = sum_of_elements
        return Matrix(result)

    def scalar_multiply(self, scalar):
        final_matrix = [[0 for a in range(self.num_rows)] for b in range(self.num_cols)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                final_matrix[i][j] = round(self.elements[i][j] * scalar, 5)
        return Matrix(final_matrix)

    def matrix_multiply(self, matrix2):
        final_matrix = [[0 for x in range(matrix2.num_cols)] for y in range(self.num_rows)]
        new_matrix = matrix2.elements
        for i in range(len(final_matrix)):
            for j in range(len(final_matrix[i])):
                element_sum = 0  
                for k in range(self.num_cols):
                    element_sum += self.elements[i][k]*new_matrix[k][j]
                final_matrix[i][j] = element_sum 
        return Matrix(final_matrix)

    def transpose(self):
        result = [[0 for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for row_index in range(self.num_rows):
            for col_index in range(self.num_cols):
                element = self.elements[row_index][col_index]
                result[col_index][row_index] = element
        return Matrix(result)

    def is_equal(self, matrix2):
        new_matrix = matrix2.elements
        equal = True
        for i in range(len(self.elements)):
            for j in range(len(self.elements[i])):
                if self.elements[i][j] != new_matrix[i][j]:
                    equal = False
        return equal

    def get_pivot_row(self, column_index):
        for pivot_row in range(len(self.elements)):
            none = False
            for x in range(column_index):
                if self.elements[pivot_row][x] != 0:
                    none = True
            if none == False and self.elements[pivot_row][column_index] != 0:
                return pivot_row

    def swap_rows(self, row_index1, row_index2):
        new_matrix = self.copy()
        new_matrix.elements[row_index1], new_matrix.elements[row_index2] = new_matrix.elements[row_index2], new_matrix.elements[row_index1]
        return new_matrix

    def check_value(self, row_index):
        for value in range(self.num_cols):
            if self.elements[row_index][value] != 0:
                return self.elements[row_index][value]


    def check_index(self, row_index):
        for index in range(self.num_cols):
            if self.elements[row_index][index] != 0:
                return index


    def normalize_row(self, row_index):
        new_matrix = self.copy()
        col_value = new_matrix.check_value(row_index)
        for value in range(len(new_matrix.elements[row_index])):
            new_matrix.elements[row_index][value] = int(abs(new_matrix.elements[row_index][value]/col_value))
        return new_matrix

    def clear_below(self, row_index):
        new_matrix = self.copy()
        col_index = new_matrix.check_index(row_index)
        col_num = new_matrix.check_value(col_index)
        for row in new_matrix.elements[row_index+1:]:
            x = row[col_index]/new_matrix.elements[row_index][col_index]
            for value in range(new_matrix.num_cols):
                row[value] -= int(x*new_matrix.elements[row_index][value])
        return new_matrix


    def clear_above(self, row_index):
        new_matrix = self.copy()
        col_index = new_matrix.check_index(row_index)
        col_num = new_matrix.check_value(col_index)
        for row in new_matrix.elements[:row_index]:
            x = row[col_index]/new_matrix.elements[row_index][col_index]
            for value in range(new_matrix.num_cols):
                row[value] -= int(x*new_matrix.elements[row_index][value])
        return new_matrix

    def rref(self):
        reduced_matrix = self.copy()
        row_index = 0
        print('1', reduced_matrix.elements)
        for col_index in range(reduced_matrix.num_cols):
            print('column index', col_index)
            pivot_row = reduced_matrix.get_pivot_row(col_index)
            #print('2', reduced_matrix.elements)
            if pivot_row != None:
                print('current matrix', reduced_matrix.elements)
                if pivot_row != row_index:
                    reduced_matrix = reduced_matrix.swap_rows(pivot_row, row_index)
                    print('swap rows', reduced_matrix.elements)
                reduced_matrix = reduced_matrix.normalize_row(row_index)
                print('normalize', reduced_matrix.elements)
                reduced_matrix = reduced_matrix.clear_below(row_index)
                print('clear below', reduced_matrix.elements)
                reduced_matrix = reduced_matrix.clear_above(row_index)
                print('clear above', reduced_matrix.elements)
                row_index += 1
                print('row index', row_index)
        return reduced_matrix

    def augment(self, other_matrix):
        result = self.copy()
        for row_index in range(result.num_rows):
            result.elements[row_index] += other_matrix.elements[row_index]
        return result

    def get_rows(self, row_nums):
        final_list = []
        result = self.copy()
        for index in row_nums:
            for element in range(self.num_rows):
                if index == element:
                    final_list.append(result.elements[element])
        return Matrix(final_list)

    def get_rows(self, row_nums):
        final_list = []
        result = self.copy()
        for index in row_nums:
            for element in range(self.num_rows):
                if index == element:
                    final_list.append(result.elements[element])
        return Matrix(final_list)

    # def inverse(self):
    #     identity = Matrix([[int(x == y) for x in range(self.num_cols)] for y in range(self.num_rows)])
    #     mat1 = self.augment(identity)
    #     mat1 = mat1.rref()
    #     left_mat = mat1.get_columns([num for num in range(self.num_cols)])
    #     inverse_mat = mat1.get_columns([num for num in range(self.num_cols, 2*self.num_cols)])
    #     if self.num_cols != self.num_rows:
    #     return 'Error: cannot invert a non-square matrix'
    #     if left_mat.elements != identity.elements:
    #     return 'Error: cannot invert a singular matrix'
    #     return inverse_mat



    def determinant(self):
        reduced_matrix = self.copy()
        row_index = 0
        scalar_nums = 1
        swap_count = 0
        for col_index in range(reduced_matrix.num_cols):
            pivot_row = reduced_matrix.get_pivot_row(col_index)
            if pivot_row != None:
                if pivot_row != row_index:
                    reduced_matrix = reduced_matrix.swap_rows(pivot_row, row_index)
                    swap_count += 1
                new_matrix = self.copy()
                col_value = new_matrix.check_value(row_index)
                for value in range(len(new_matrix.elements[row_index])):
                    new_matrix.elements[row_index][value] = int(abs(new_matrix.elements[row_index][value]/col_value))
                    scalar_nums *= new_matrix.elements[row_index][value]
                reduced_matrix = reduced_matrix.clear_below(row_index)
                reduced_matrix = reduced_matrix.clear_above(row_index)
                row_index += 1
        return reduced_matrix

    def exponent(self, num):
        final_matrix = self.copy()
        initial_matrix = self.copy()
        for i in range(num - 1):
            final_matrix = final_matrix.matrix_multiply(initial_matrix)
        return final_matrix
    
    def __add__(self, c):
        return self.add(c)
    def __sub__(self, c):
        return self.subtract(c)
    def __mul__(self, scalar):
        return self.scalar_multiply(scalar)
    def __matmul__(self, matrix2):
        return self.matrix_multiply(matrix2)
    def __eq__(self, matrix2):
        return self.is_equal(matrix2)
    