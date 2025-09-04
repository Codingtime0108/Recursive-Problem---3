keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def Combination(combination,curr,output,n):
    if(curr == n):
        print(*output,sep=",")
        return
    for i in range(len(keypad[combination[curr]])):

        output.append(keypad[combination[curr]][i])

        Combination(combination, curr +1, output, n)
        output.pop()
        if(combination[curr]==0 or combination[curr]==1):
            return
        
combination = [2,3,2]
n = len(combination)
Combination(combination,0,[],n)