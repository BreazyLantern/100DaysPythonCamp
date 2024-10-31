
# Start learning about creating functions with outputs!!
# first example
def a_funtion():
    return 3*5

print(a_funtion())
# title function will modify a string value into a formated name value
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name("jake", "LOGan")

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2((function_1("Hello")))
print(output)