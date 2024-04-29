cc_number = input('Please enter your credit card number')

bank_number = cc_number[1:6]
acc_number = cc_number[6:-2]
check_digit = cc_number[-1]

if cc_number[0] == '4' and (len(cc_number) == 13 or len(cc_number) ==16):
    print('This is a valid Visa card')
    print('Bank number = ' + bank_number)
    print('Account number = ' + acc_number)
else:
    print('This is not a valid Visa card number')