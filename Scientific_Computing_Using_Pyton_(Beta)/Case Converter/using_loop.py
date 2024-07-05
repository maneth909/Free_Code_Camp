def case_converter(text):
    snake_cased_list = []
    for char in text:
        if char.isupper():
            lower_cased = '_' + char.lower()
            snake_cased_list.append(lower_cased)
        else:
            snake_cased_list.append(char)
    join_char = ''.join(snake_cased_list)
    cleaned_text = join_char.strip('_')
    return cleaned_text
def main():
    print(case_converter('aLongAndComplexString'))
main()