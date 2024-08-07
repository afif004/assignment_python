def is_substr(main_str, substr):
    if substr in main_str:
        return "Yes"
    else:
        return "No"
main_str = input("Main string: ")
substr = input("Substring: ")
print(is_substr(main_str, substr))