a, b, c = map(int, input().split())
d = (a + b + c) / 3
print("과제 :",a, sep=' ')
print("중간 :",b, sep=' ')
print("기말 :",c, sep=' ')
print("평균 :",d,sep=' ')
if d >= 90:
    print("A"+"학점 입니다.")
elif d >= 80:
    print("B"+"학점 입니다.")
elif d >= 70:
    print("C"+"학점 입니다.")
elif d >= 60:
    print("D"+"학점 입니다.")
elif d<60:
    print("F"+"학점 입니다.")
print("계속하려면 아무 키나 누르십시오 . . .")






