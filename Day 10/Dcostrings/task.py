def format_name(f_name, l_name):
    """This is an example of a doc string This function takes the first and last name and
    formats the name with aa title case version of the name then returns the modified value"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



