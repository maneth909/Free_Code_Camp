def verify(translated_card_number):
    reversed_card_number = translated_card_number[::-1]

    #select odd number from reversed card num
    odd_digits = reversed_card_number[0::2]
    sum_odd_digits = 0
    for i in odd_digits:
        sum_odd_digits += int(i)

    #select even numbers from revesrsed card num
    even_digits = reversed_card_number[1::2]
    sum_even_digits = 0
    for j in even_digits:
        num = int(j)*2
        if num >= 10:
            num = num//10 + num%10
        sum_even_digits += num
    
    total = sum_even_digits+sum_odd_digits
    return 0 == total %10

def main():
    card_number = '4111-1111-4555-1811'
    card_translation = str.maketrans({'-':'', ' ':''})
    translated_card_number = card_number.translate(card_translation)
    
    if verify(translated_card_number):
        print('Valid!')
    else:
        print('Invalid!')

main()