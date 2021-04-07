# for random number generation 
import random as r


def otp_gen():
    otp=""
    for i in range(4):
        otp += str(r.randint(1, 9))
    print('Your one time password is ')
    print(otp)


otp_gen()
