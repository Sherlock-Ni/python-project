# 输入所需的数文本
grid = []
while True:
    a = input()
    b = list(str(a))
    if a == ' ':
        break
    grid = grid + b

# 转换输出数据
j = 0
i = 0
while j < 7:
    while i < 10:
        print(grid[i][j])
        i = i+1
        if i == 9:
            break
    j = j+1
    if j == 6:
        break


           
        
        



