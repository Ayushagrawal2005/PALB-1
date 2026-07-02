questions = [
    ["What is the capital of India?", "A.Delhi", "B.Jabalpur", "C.Jaipur", "D.Dehradun", 1],
    ["What is the national bird of India?", "A.Hen", "B.Peacock", "C.Sparrow", "D.Ostrich", 2],
    ["Who is the Prime Minister of India?", "A.Rahul Gandhi", "B.HD Gowda", "C.Narendra Modi", "D.Arvind Kejriwal", 3],
    ["Who founded Microsoft?", "A.Tim Lee", "B.Mark Zuckerberg", "C.Bill Gates", "D.Larry Brothers", 3]
]
levels = [5000,10000,120000,360000]
money = 0
i = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Questions for {levels[i]}:")
    print(f" {question[1]}        {question[2]}")
    print(f" {question[3]}        {question[4]}")
    reply = int(input("Enter your answer (1-4):"))
    if reply ==question[-1]:
        print("Correct Answer")
        if i==1:
            money = 10000
        elif i==3:
            money=360000
    else:
        print("Wrong Answer Thanks For playing")
        break
print(f"You have won Rs.{money}")