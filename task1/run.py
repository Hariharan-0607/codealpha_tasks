def isemail(word):
            if '@gmail.com' in word:
                if len(word)>len('@gmail.com'):
                    return True
                return False

n=input("Enter your text file")
with open(n,'r') as file:
    content=file.read()
words=content.replace('\n',' ').split(' ')
email=[]
for word in words:
    if isemail(word):
        if word not in email:
            email.append(word)

with open('email_output.txt','w') as ofile:
    for i in email:
        ofile.write(i+'\n')
print("Emails extracted from file and saved to email_output")