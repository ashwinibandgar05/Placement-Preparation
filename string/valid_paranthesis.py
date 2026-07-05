def valid_paranthesis(s):
    output=[]
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            output.append(s[i])
        
        else:
            if len(output) == 0:
                return False
            if (s[i]==")" and output[-1]=="(") or (s[i]=="}" and output[-1]=="{") or (s[i]=="]" and output[-1]=="[") :
                output.pop()

            else:
                return False
     
    return len(output)==0

print(valid_paranthesis("({{}})"))        

