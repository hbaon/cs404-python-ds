t = int(input())

for _ in range(0, t):
    s = input()[::-1] # .reverse()
    news = ""
    for c in s:
        if c == "p":
            news += "q"
        elif c == "q":
            news += "p"
        else: news += "w"
    print(news)