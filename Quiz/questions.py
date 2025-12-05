import random

# ---------------------- CATEGORIES ----------------------
categories = {
    "Science": [],
    "Math": [],
    "General Knowledge": []
}

# ---------------------- SCIENCE QUESTIONS ----------------------
categories["Science"] = [
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "HO"], "answer": 0},
    {"question": "The human heart has how many chambers?", "options": ["2", "3", "4", "5"], "answer": 2},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": 1},
    {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": 1},
    {"question": "What is the speed of light?", "options": ["3x10^8 m/s", "3x10^6 m/s", "3x10^5 km/s", "300 m/s"], "answer": 0},
    {"question": "What is the basic unit of life?", "options": ["Cell", "Atom", "Molecule", "Organ"], "answer": 0},
    {"question": "What part of the cell contains DNA?", "options": ["Nucleus", "Cytoplasm", "Ribosome", "Mitochondria"], "answer": 0},
    {"question": "What is the chemical formula of table salt?", "options": ["NaCl", "KCl", "Na2CO3", "HCl"], "answer": 0},
    {"question": "Which vitamin is produced when a person is exposed to sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": 3},
    {"question": "What is the main gas found in the Earth's atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": 1},
    {"question": "Which organ purifies blood in human body?", "options": ["Liver", "Kidney", "Heart", "Lungs"], "answer": 1},
    {"question": "What is the powerhouse of the cell?", "options": ["Ribosome", "Mitochondria", "Nucleus", "Chloroplast"], "answer": 1},
    {"question": "Water freezes at 0 degrees on which scale?", "options": ["Celsius", "Fahrenheit", "Kelvin", "Rankine"], "answer": 0},
    {"question": "Which planet has the most moons?", "options": ["Jupiter", "Saturn", "Mars", "Earth"], "answer": 1},
    {"question": "The boiling point of water is?", "options": ["90°C", "100°C", "120°C", "80°C"], "answer": 1}
]

# ---------------------- MATH QUESTIONS ----------------------
categories["Math"] = [
    {"question": "What is 12 + 15?", "options": ["25", "27", "26", "28"], "answer": 1},
    {"question": "What is 7 x 8?", "options": ["54", "56", "58", "64"], "answer": 1},
    {"question": "Square root of 144?", "options": ["11", "12", "13", "14"], "answer": 1},
    {"question": "10^3 equals?", "options": ["100", "1000", "10000", "10"], "answer": 1},
    {"question": "5! (factorial) equals?", "options": ["120", "60", "24", "720"], "answer": 0},
    {"question": "What is 15% of 200?", "options": ["20", "25", "30", "35"], "answer": 2},
    {"question": "Value of pi (approx)?", "options": ["3.14", "3.15", "3.12", "3.41"], "answer": 0},
    {"question": "Solve: 3x + 5 = 14", "options": ["3", "4", "5", "6"], "answer": 0},
    {"question": "7^2 equals?", "options": ["42", "49", "56", "36"], "answer": 1},
    {"question": "What is 45 / 5?", "options": ["8", "9", "10", "7"], "answer": 1},
    {"question": "What is 2^5?", "options": ["16", "32", "64", "25"], "answer": 1},
    {"question": "If angle A = 90°, triangle type?", "options": ["Acute", "Right", "Obtuse", "Equilateral"], "answer": 1},
    {"question": "Sum of interior angles of triangle?", "options": ["180°", "360°", "90°", "270°"], "answer": 0},
    {"question": "Next prime after 7?", "options": ["9", "11", "13", "17"], "answer": 1},
    {"question": "2 + 2 x 2 = ?", "options": ["6", "8", "4", "2"], "answer": 0}
]

# ---------------------- GENERAL KNOWLEDGE QUESTIONS ----------------------
categories["General Knowledge"] = [
    {"question": "Capital of France?", "options": ["Berlin", "Paris", "Rome", "Madrid"], "answer": 1},
    {"question": "Largest ocean?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": 2},
    {"question": "Who wrote Hamlet?", "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"], "answer": 0},
    {"question": "Fastest land animal?", "options": ["Cheetah", "Lion", "Tiger", "Horse"], "answer": 0},
    {"question": "Which country is known as Land of Rising Sun?", "options": ["China", "Japan", "Korea", "Thailand"], "answer": 1},
    {"question": "Currency of USA?", "options": ["Dollar", "Euro", "Yen", "Pound"], "answer": 0},
    {"question": "Mount Everest is in?", "options": ["Nepal", "India", "China", "Bhutan"], "answer": 0},
    {"question": "Who invented telephone?", "options": ["Bell", "Edison", "Tesla", "Newton"], "answer": 0},
    {"question": "Longest river?", "options": ["Amazon", "Nile", "Ganges", "Yangtze"], "answer": 1},
    {"question": "Olympics held every?", "options": ["2 years", "3 years", "4 years", "5 years"], "answer": 2},
    {"question": "Largest desert?", "options": ["Sahara", "Gobi", "Kalahari", "Arabian"], "answer": 0},
    {"question": "Who painted Mona Lisa?", "options": ["Da Vinci", "Picasso", "Van Gogh", "Michelangelo"], "answer": 0},
    {"question": "First man on the moon?", "options": ["Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "John Glenn"], "answer": 1},
    {"question": "Biggest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": 1},
    {"question": "Which planet is closest to Sun?", "options": ["Venus", "Earth", "Mercury", "Mars"], "answer": 2}
]

# ---------------------- GET SHUFFLED QUESTIONS ----------------------
def get_shuffled_questions(category):
    q_list = categories.get(category, [])
    random.shuffle(q_list)
    return q_list
