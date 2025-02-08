'''
This is used to judge to keep, buy, or sell stock
Buy signal: when stock goes up for 3 consecutive days --> show 1
Sell signal: when stock goes down for 3 consecutive days --> show -1
Keep signal: not buy or sell --> show 0
Given example data = [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368]
FUnction will show [0, 0, 0, 1, 1, 0, 0, -1]
'''
data = [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368]


def three_days(data):
    decision = None
    decision_keep = 0
    decision_buy = 1
    decision_sell = -1

    # To make first 3 numbers judgable
    add_items = [data[0], data[0], data[0]]
    
    new_data = add_items + data
    judge_data = []
    decision_list = []
    
    # To make a 4-number group to judge 3 day status 
    for num in range(8):
        judge_data.append(new_data[num:num+4])

    for gp in judge_data:
        if gp[3] > gp[2]:
            if gp[2] > gp[1]:
                if gp[1] > gp[0]:
                    decision = decision_buy
                    decision_list.append(decision)
                else:
                    decision = decision_keep
                    decision_list.append(decision)                
            else:
                decision = decision_keep
                decision_list.append(decision)

        elif gp[3] < gp[2]:
            if gp[2] < gp[1]:
                if gp[1] < gp[0]:
                    decision = decision_sell
                    decision_list.append(decision)
                else:
                    decision = decision_keep
                    decision_list.append(decision)

            else:
                decision = decision_keep
                decision_list.append(decision)

        elif gp[3] == gp[2]:
            decision = decision_keep
            decision_list.append(decision)
    print(decision_list)

three_days(data)



