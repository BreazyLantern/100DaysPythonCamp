word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Using print to debug a problem
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
"""The reason for why this program is not functioning properly is because the way an input
is being placed into word per page is an evaluation instead of a modifier and the variable 
was also created without usage which results in a warning after fixing the evaluation"""