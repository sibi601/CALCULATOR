class Calculator:

    def operation(self):

        num1 = self.get_input()
        num2 = self.get_input()

        print("Select the operator:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")

        try:
            ch=int(input("Enter the option:"))
        except ValueError:
            print("You have entered an alphabet or a null value")
            quit()     

        if ch in(1,2,3,4):
             
            if ch==1:
                result = self.add(num1,num2)
                self.print_result(result)
                self.append_result(result)
            
            elif ch==2:
                result = self.sub(num1,num2)
                self.print_result(result)
                self.append_result(result)
            
            elif ch==3:
                result = self.multi(num1,num2)
                self.print_result(result)
                self.append_result(result)

            elif ch==4:
                result = self.divide(num1,num2)
                self.print_result(result)
                self.append_result(result)
        else:
            print("Invalid Option")

    def get_input(self):
        
        try:
            return float(input("Enter the number: "))
        except ValueError:
            print("You have entered an alphabet or a null value")
            quit()     

    def add(self, num1, num2):
        return num1 + num2
        
    def sub(self, num1, num2):
        return num1 - num2

    def multi(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def print_result(self, result):
        print(result)

    def append_result(self,result):
        f=open("calc_msp_file.txt","a")
        f.write(str(result)+"\n")
        f.close()

calc = Calculator()

calc.operation()
        





