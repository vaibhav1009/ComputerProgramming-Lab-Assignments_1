#  **********************************************************************
#   Author - Vaibhav Kagathara
#   Date :- 20th September 2019
#   Language :- Python
#   About :- To Check The Greater Number From Two User Inputed Values
#  **********************************************************************


a = input("Enter First Number: ")
b = input("Enter Second Number: ")

if a>b:
    print("{} is greater than {}".format(a, b))
elif a==b:
    print("Both Numbers are Equal.")
else:
    print("{} is greater than {}".format(b, a))
