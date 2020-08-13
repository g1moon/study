n,c = map(int,input().split())
lst = sorted([int(input()) for _ in range(n)])
print(n,c)
print(lst)


def install(gap):
    idx, ret = 0, 1
    while True:
        if idx > len(lst)-1:
            return ret 
        if idx+1 > len(lst)-1:
            return ret 
        
        elif gap <= lst[idx+1] - lst[idx]:
            ret += 1
            idx = idx+1
            continue  
        elif gap > lst[idx+1] - lst[idx]:
            base = idx+2
            while True:#1.cnt설치할떄까지 돌거나,  #2.#base가 len(lst)-1 보다 클떄까지 돌아(걍꺼버려)
                if base > len(lst)-1:
                    return ret 
                if gap <= lst[base] - lst[idx]:#설치
                    ret += 1
                    idx = base 
                    break
                else:
                    base += 1
    return ret 

gap = lst[-1] - lst[0]

while True:
    if install(gap) < c: #적게설치헀어... 갭이 조금 줄어야겠어
        print(1, install(gap), gap)
        gap = gap // 2
        
    elif install(gap) > c: #많이 설치해버렸어... 갭이 조금 늘어나야겠어 
        print(2, install(gap), gap)
        gap += 1
        
    elif install(gap) == c:
        print(3, install(gap), gap)
        av = [gap]
        tr = gap
        while True:
            tr +=  1
            if install(tr) == c:
                av.append(tr)
                continue
            else:
                print(max(av))
                break
        break
        
        