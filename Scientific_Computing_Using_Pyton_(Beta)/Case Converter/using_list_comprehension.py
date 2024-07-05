def case_converter(text):
    snake_cased_list = ['_'+char.lower() if char.isupper() else char for char in text]
    return ''.join(snake_cased_list).strip('_')

def main():
    print(case_converter('aLongAndComplexString'))
main()