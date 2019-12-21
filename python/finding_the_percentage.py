student=[]
mark=[]
s=[]
r=[]
n=int(input())
for _ in range(n):
    n_m=input().split(" ")
    student.append(n_m)
p=input()
print(student)
for i in range(n):
    if p == student[i][0]:
        su=0
        for j in range(1,len(n_m)):
            s=int(student[i][j])
            su+=s
            a=su/3
        mark.append(a)
print(mark[0])
