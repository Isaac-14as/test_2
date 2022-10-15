
class Matrix():
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def print_m(self):
        answer = ''
        for i in range(len(self.matrix_list)):
            answer += '|' + '\t'
            for j in range(len(self.matrix_list[i])):
                answer += str(self.matrix_list[i][j]) + '\t'
            answer = answer[:-1:]
            answer += '\t' + '|'
            answer += '\n'
        return answer
    
    def transposition(self):
        # answer = [[self.matrix_list[i][j] for j in range(len(self.matrix_list))] for i in range(len(self.matrix_list[0]))]
        answer = [[self.matrix_list[i][j] for j in range(len(self.matrix_list))] for i in range(len(self.matrix_list[0]))]
        print(answer)

        # return Matrix(answer)
    


b = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

a = Matrix(b)

print(a.print_m())
print(a)
a.transposition()
# print(a.transposition().print_m())
    

        

    