class Matrix():

    def __init__(self, elements):
        self.elements = elements
        self.num_rows = len(elements)
        self.num_cols = len(elements[0])


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
        final_matrix = [[self.elements[0][0]*scalar, self.elements[0][1]*scalar], [self.elements[1][0]*scalar, self.elements[1][1]*scalar]]
        return Matrix(final_matrix)

    def matrix_multiply(self, c):
        result = [[0 for _ in range(self.num_rows)] for _ in range(self.num_cols)]

        for row_index in range(self.num_rows):
            for col_index in range(self.num_cols):

                row = self.elements[row_index]
                col = [c.elements[k][col_index] for k in range(self.num_rows)]

                dot_product = 0

                for i in range(len(row)):
                    dot_product += row_item*column_item

                result[row_index][col_index] = dot_product

        return Matrix(result)

    def transpose(self):
        result = [[0 for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for row_index in range(self.num_rows):
            for col_index in range(self.num_cols):
                element = self.elements[row_index][col_index]
                result[col_index][row_index] = element
        return Matrix(result)

    def get_pivot_row(self, column_index):
        for pivot_row in range(len(self.elements):
            none = False
            for x in range(col_index):
                if self.elements[pivot_row][x] != 0:
                    none = True
            if none == False and self.elements[pivot_row][column_index] != 0:
                return pivot_row

    def swap_rows(self, row_index1, row_index2):
        self.elements[row_index1], self.elements[row_index2] = self.elements[row_index2], self.elements[row_index1]

    def check_value(self, row_index):
        for value in range(len(self.elements)):
            if self.elements[row_index][value] != 0:
                return value 

    def normalize_row(self, row_index):
        col_value = self.check_value(row_index)
        for value in range(len(self.elements[row_index])):
            self.elements[row_index][value] = self.elements[row_index][value]/col_value

    def clear_below(self, row_index):
            col_index = self.check_value(row_index)
        col_value = self.check_value(col_index)
        for pivot_row in sel.elements[row_index + 1:]:
            while row[col_index] != 0:
                for value in range(self.col_value):
                    pivot_row[value] -= self.elements[row_index][value] 

    def clear_above(self, row_index):
            col_index = self.check_value(row_index)
        col_value = self.check_value(col_index)
        for pivot_row in sel.elements[:row_index]:
            while row[col_index] != 0:
                for value in range(self.col_value):
                    pivot_row[value] -= self.elements[row_index][value] 

