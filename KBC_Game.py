
def KBC_Game(Ques,Prize):
    print("Welcome to Koun Banega Crorepati")
    name=input("Enter your name: ")
    print("Welcome",name)
    print("All the best!")
    print()
    
    money=0
    
    for i in range(len(Ques)):
        print()
        print(f"Your Question for Rs.{Prize[i]}")
        print(f"Q{i+1}.{Ques[i][0]}")
        print(f"1.{Ques[i][1]}")
        print(f"2.{Ques[i][2]}")
        print(f"3.{Ques[i][3]}")
        print(f"4.{Ques[i][4]}")
        try:
            ans=int(input("Enter your answer(1-4)): "))
        except ValueError:
            print("Invalid input! Please enter valid input between 1-4")
            break
        
        if ans==Ques[i][5]:
            print(f"Congratulations! Your answer is correct. You won Rs.{Prize[i]}")
            money=Prize[i]
        else:
            print("Sorry! Your answer is wrong")
            break
    
    print()
     
    if money<40000:
        print("You won Total Money from kbc is  Rs.0")
    elif money<640000:
        print("You won Total Money from kbc is  Rs.40000")
    elif money<10000000:
        print("You won Total Money from kbc is  Rs.640000")
    else:
        print("You won Total Money from kbc is  Rs.10000000")
        
    print("\nThank you for playing KBC")

Ques=[["Who creted the Python Programming Language?","Tim Berners-Lee","Guido van Rossum","ames Gosling","Bjarne Stroustrup",2],
      ["Which of the following is not a valid data type in Python?","List","Tuple","Dictionary","Class",4],
      ["Which of the following is not a keyword in Python?","eval","assert","nonlocal","pass",1],
      ["Which of the following is not a valid keyword in Python?","raise","try","with","finally",3],
      ["Which of the following is not a valid keyword in Python?","native","nonlocal","lambda","continue",1],
      ["Which is not OOPs concept in Python?","Encapsulation","Inheritance","Polymorphism","Compilation",4],
      ["who is prime minister of India?","Narendra Modi","Rahul Gandhi","Amit Shah","Manmohan Singh",1],
      ["who is first president of America?","George Washington","Abraham Lincoln","John F. Kennedy","Thomas Jefferson",1],
      ["who is first president of India?","Rajendra Prasad","Jawaharlal Nehru","Indira Gandhi","Sardar Patel",1],
      ["when India won first world cup?","1987","1975","1983","1992",3],
      ["Who is Captain of Indian Team in T20 World Cup 2024?","Virat Kohli","Rohit Sharma","KL Rahul","Shreyas Iyer",2],
      ["Who is Captain of Indian Team in ODI World Cup 2023?","Virat Kohli","Rohit Sharma","KL Rahul","Shreyas Iyer",1],
      ["where Rio Olympics 2016 held?","USA","Brazil","India","Russia",2]
]
Prize=[1000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
KBC_Game(Ques,Prize)