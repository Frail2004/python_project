try:
      n = int(input("enter   :"))
      sum = 0


      for i in range(n):
            number = int(input(f"enter numbers { i + 1} : "))
            sum += number
     

      average = sum / n 
      print(f"the average is {average}")

except  ZeroDivisionError:
      
      print("fuck")