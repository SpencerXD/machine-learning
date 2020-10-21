    def clear_below(self, row_index):
        new_matrix = self.copy()
        col_index = new_matrix.check_value(row_index)
        col_value = new_matrix.check_value(col_index)
        for pivot_row in new_matrix.elements[row_index + 1:]:
            while pivot_row[int(col_index)] != 0:
                for value in range(col_value):
                    pivot_row[value] -= new_matrix.elements[row_index][value] 
        return new_matrix

    def clear_above(self, row_index):
        new_matrix = self.copy()
        col_index = new_matrix.check_value(row_index)
        col_value = new_matrix.check_value(col_index)
        for pivot_row in sel.elements[:row_index]:
            while row[col_index] != 0:
                for value in range(new_matrix.col_value):
                    pivot_row[value] -= new_matrix.elements[row_index][value] 
        return new_matrix