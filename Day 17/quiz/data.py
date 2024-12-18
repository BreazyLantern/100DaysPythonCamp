question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

# make a data set using trivia from https://opentdb.com/
# select api from the site and choose your categories. Then generate questions and
# copy and place into search bar for json list

my_data = [
    {"type": "boolean", "difficulty": "easy",
     "category": "General Knowledge",
     "question": "Slovakia is a member of European Union-",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "The color orange is named after the fruit.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "The Great Wall of China is visible from the moon.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "One of Donald Trump&#039;s 2016 Presidential Campaign promises was to build a border wall between the United States and Mexico.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "The mitochondria is the powerhouse of the cell.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "Adolf Hitler was born in Australia. ", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "Scotland voted to become an independent country during the referendum from September 2014.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "Jingle Bells was originally meant for Thanksgiving",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "Ping-Pong originated in England", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "A scientific study on peanuts in bars found traces of over 100 unique specimens of urine.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "In 2010, Twitter and the United States Library of Congress partnered together to archive every tweet by American citizens.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "You can legally drink alcohol while driving in Mississippi.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
     "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.",
     "correct_answer": "False", "incorrect_answers": ["True"]}
]
