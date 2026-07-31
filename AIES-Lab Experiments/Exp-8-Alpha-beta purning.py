scores = [3,5,2,9]

def alphabeta(depth,index,maxPlayer,alpha,beta):
    if depth==2:
        return scores[index]

    if maxPlayer:
        value=-999
        for i in range(2):
            value=max(value,alphabeta(depth+1,index*2+i,False,alpha,beta))
            alpha=max(alpha,value)
            if alpha>=beta:
                break
        return value
    else:
        value=999
        for i in range(2):
            value=min(value,alphabeta(depth+1,index*2+i,True,alpha,beta))
            beta=min(beta,value)
            if beta<=alpha:
                break
        return value

print("Optimal Value:", alphabeta(0,0,True,-999,999))
