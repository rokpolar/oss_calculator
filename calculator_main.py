import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_new_operation = QHBoxLayout() # 새 연산들 자리 추가
        layout_new_operation_2 = QHBoxLayout() # 새 연산 두번째 줄 추가
        layout_operation = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("Equation: ")
        label_solution = QLabel("Number: ")
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")

        self.number_display = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        # layout_equation_solution.addRow(label_equation, self.equation)
        # layout_equation_solution.addRow(label_solution, self.solution)
        layout_equation_solution.addRow(self.number_display)

        ### 사칙연상 버튼 생성
        button_percent = QPushButton("%")
        button_CE = QPushButton("CE")
        button_C = QPushButton("C")
        button_backspace = QPushButton("Bsp")
        
        button_1x = QPushButton("1/x")
        button_pow2 = QPushButton("x^2")
        button_sqrt = QPushButton("x^(1/2)")
        button_division = QPushButton("/")

        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_equal = QPushButton("=")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        
                ## 새 연산 버튼을 layout_new_operation에 추가하자 <<<<<<<<<
        layout_new_operation.addWidget(button_percent)
        layout_new_operation.addWidget(button_CE)
        layout_new_operation.addWidget(button_C)
        layout_new_operation.addWidget(button_backspace)

        ## 새 연산 버튼을 layout_new_operation에 추가하자 <<<<<<<<<
        layout_new_operation_2.addWidget(button_1x)
        layout_new_operation_2.addWidget(button_pow2)
        layout_new_operation_2.addWidget(button_sqrt)
        layout_new_operation_2.addWidget(button_division)
        
        ### =, clear, backspace 버튼 클릭 시 시그널 설정 > num_diplay 초기화
        button_equal.clicked.connect(self.button_equal_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        
        button_CE.clicked.connect(self.button_CE_clicked)
        button_C.clicked.connect(self.button_C_clicked)
        button_1x.clicked.connect(self.button_1x_clicked)
        button_pow2.clicked.connect(self.button_pow2_clicked)
        button_sqrt.clicked.connect(self.button_sqrt_clicked)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], 2-x, y) #2-x로 숫자 순서 반전
            elif number == 0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        layout_number.addWidget(button_product,0,3)
        layout_number.addWidget(button_minus,1,3)
        layout_number.addWidget(button_plus,2,3)
        layout_number.addWidget(button_equal,3,3)

        ### 소숫점 버튼과 +/- 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_pmn = QPushButton("+/-") # + / - 버튼 추가
        layout_number.addWidget(button_pmn,3, 0)
        button_pmn.clicked.connect(self.button_pmn_clicked)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_new_operation) # <<<<<<<<새 연산 추가
        main_layout.addLayout(layout_new_operation_2) # <<<<<<<<새 연산 추가
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
