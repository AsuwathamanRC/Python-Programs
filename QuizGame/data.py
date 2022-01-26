import requests

parameters = { "amount" : "10", "type" : "boolean" }
response = requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()  # Throw error when the response code is not OK
question_data_api = response.json()["results"]

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


# Use the below website and it's API feature to generate random questions like below
# https://opentdb.com/api_config.php
# https://opentdb.com/api.php?amount=25&type=boolean
question_data_2 = [
    {
      "category": "Entertainment: Music",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The music group Daft Punk got their name from a negative review they recieved.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Film",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Han Solo's co-pilot and best friend, 'Chewbacca', is an Ewok.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Music",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The cover of The Beatles album 'Abbey Road' featured a Volkswagen Beetle in the background.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Science: Computers",
      "type": "boolean",
      "difficulty": "medium",
      "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The longest place named in the United States is Lake Chargoggagoggmanchauggagoggchaubunagungamaugg, located near Webster, MA.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Politics",
      "type": "boolean",
      "difficulty": "easy",
      "question": "In 2016, the United Kingdom voted to stay in the EU.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Science & Nature",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Type 1 diabetes is a result of the liver working improperly.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Luigi is taller than Mario?",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Science: Gadgets",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The communication protocol NFC stands for Near-Field Control.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "medium",
      "question": "In 'Overwatch,' an allied McCree will say 'Step right up' upon using his ultimate ability Deadeye.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Science: Mathematics",
      "type": "boolean",
      "difficulty": "hard",
      "question": "If you could fold a piece of paper in half 50 times, its' thickness will be 3/4th the distance from the Earth to the Sun.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Film",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Ewan McGregor did not know the name of the second prequel film of Star Wars during and after filming.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Rebecca Chambers does not appear in any Resident Evil except for the original Resident Evil and the Gamecube remake.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Pluto is a planet.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Science: Computers",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Early RAM was directly seated onto the motherboard and could not be easily removed.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Pistons were added to Minecraft in Beta 1.5.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Film",
      "type": "boolean",
      "difficulty": "easy",
      "question": "George Lucas directed the entire original Star Wars trilogy.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "medium",
      "question": "'Return to Castle Wolfenstein' was the only game of the Wolfenstein series where you don't play as William 'B.J.' Blazkowicz.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Television",
      "type": "boolean",
      "difficulty": "medium",
      "question": "In 'Star Trek: The Next Generation', Data is the only android in existence.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The scrapped Sonic the Hedgehog 2 level 'Hidden Palace Zone' was later reused in the iOS port of the game. ",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Cartoon & Animations",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Night on Bald Mountain was one of the musical pieces featured in Disney's 1940's film Fantasia.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Sports",
      "type": "boolean",
      "difficulty": "medium",
      "question": "In 2008, Usain Bolt set the world record for the 100 meters with one shoelace untied.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The internet browser Firefox is named after the Red Panda.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Minecraft wasn't the original name to Minecraft.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Musicals & Theatres",
      "type": "boolean",
      "difficulty": "hard",
      "question": "The protagonist's names in 'Who's Afraid of Virginia Woolf', George and Martha, were derived from George Washington and his wife.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    }
]
