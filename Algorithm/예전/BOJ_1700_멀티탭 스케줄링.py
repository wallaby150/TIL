holes, usages = map(int, input().split())    # 멀티탭 구멍의 개수, 전기 용품의 총 사용횟수
use_orders = list(map(int, input().split()))
plugs = [0] * holes
count = 0

# 사용 순서를 쭉 훑어본다.
for now_order in range(usages):
    now_tool = use_orders[now_order]

    # 지금 꽂혀있는 놈이면 넘어가
    if now_tool in plugs:
        continue
    
    # 아직 빈 구멍이 있으면
    if 0 in plugs:
        # 해당 구멍의 인덱스에 지금 순서의 전기 용품의 번호를 넣는다.
        idx = plugs.index(0)
        plugs[idx] = now_tool

    # 꽉 찼다면
    else:
        count += 1
        # 쭉 훑어보면서 다시 안 쓸 녀석 찾음
        for hole in range(holes):
            plug = plugs[hole]
            if plug not in use_orders[now_order+1:]:
                plugs[hole] = now_tool
                break

        # 전부 다 뒤에서 다시 쓸 예정이라면
        else:
            for order in range(now_order+holes-1, usages):
                if use_orders[order] in plugs:
                    idx = plugs.index(use_orders[order])
                    plugs[idx] = now_tool
                    break
            # for order in range(usages-1, now_order+holes, -1):
            #     if use_orders[order] in plugs:
            #         idx = plugs.index(use_orders[order])
            #         plugs[idx] = now_tool
            #         break

print(count)