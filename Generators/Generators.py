# def countdown(num):
#     yield "A"
#     yield "B"
#     yield "C"
#     yield "D"
#
# test = countdown(4)
#
# for i in test:
#     print(i)


# Input: abcde$gh
# Output: hgedc$ba
input = "abcde$gh"
output=[]
index=-1
input = list(input)
print("",input)
for i in range(len(input)-1,int(len(input)/2),-1):
    if input[i]!="$":
        temp=input[i]
        while True:
            index+=1
            if input[index]!="$":
                input[i] = input[index]
                input[index] = temp
                break

print(input)