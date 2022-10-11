
def knapsack01(item_amount_in, limit_in, item_list_in, item_value_list_in, items_name_in):

    item_amount = int(item_amount_in)
    limit = int(limit_in)

    item_list = item_list_in.split(',')
    item_value_list = item_value_list_in.split(',')
    
    item_list = list(map(int, item_list))    
    item_value_list = list(map(int, item_value_list))

    items_name = items_name_in.split(',')  
    
    #return item_value_list, limit

    c = [[0 for x in range(limit+1)] for y in range(item_amount+1)] 

    for i in range(1, item_amount+1):
        for j in range(1, limit+1):
            if item_value_list[i-1] > j:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = max(c[i - 1][j], c[i - 1][j - item_value_list[i - 1]] + item_list[i - 1])

    w = limit
    res = c[item_amount][limit]

    res_item_list = []
    res_item_name = []
    i = item_amount
    while(i > 0 and res > 0):
        if res == c[i-1][w]:
            continue
        else:
            res_item_list.append(item_list[i-1])
            res_item_name.append(items_name[i-1])
            res -= item_list[i-1]
            w -= item_value_list[i-1]
        i -= 1
    return res_item_list, res_item_name, c[item_amount][limit]