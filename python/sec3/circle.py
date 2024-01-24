def circle():
    num = int(input())

    for i in range(num):
        word = str(input()) # str 안해도 됐음.
        word = word.lower() # lower()는 원본을 변형 x, 원본은 두고 변형된 객체를 반환
        re_word = "".join(reversed(word))
        if word == re_word:
            print(f'#{i+1} YES')
        else:
            print(f'#{i+1} NO')

def circle_best():
    num = int(input())

    for i in range(num):
        s=input()
        s = s.upper()
        if s == s[::-1]:
            print("#%d YES" % (i+1))
        else:
            print("#%d NO" % (i+1))