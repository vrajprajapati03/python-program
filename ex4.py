def function(s):

    a={"UPPERCASE":0,"LOWERCASE":0}

    for i in s:
        if i.isupper():
            a["UPPERCASE"] +=1
        elif i.islower():
            a["LOWERCASE"] +=1
        '''else:
            pass'''

    print("ORIGINAL STRING IS : ",s)
    print("-----------------------------------------------------------------------")
    print("NO.OF UPPERCASE CHARCTER :",a["UPPERCASE"])
    print("NO.OF LOWERCASE CHARACTER :",a["LOWERCASE"])

function('The Quick Brown Fox')
            
