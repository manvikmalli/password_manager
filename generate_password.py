import string
import secrets
def generate_password():
    pass_gen=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    password=[]
    for i in range(16):
        password.append(secrets.choice(pass_gen))
    password="".join(password)
    return password

def check_strength(password):
    score=0
    length=len(password)>=12
    if length:
        score+=1
    upper=any(char.isupper() for char in password)
    if upper is True:
        score+=1
    lower=any(char.islower() for char in password)
    if lower is True:
        score+=1
    digit=any(char.isdigit() for char in password)
    if digit is True:
        score+=1
    punct=any(char in string.punctuation for char in password)
    if punct is True:
        score+=1
    if score==1:
        return "Very Weak!"
    if score==2:
        return "Weak!"
    if score==3:
        return "Average!"
    if score==4:
        return "Strong!"
    if score==5:
        return "Very Strong!"   