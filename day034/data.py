import requests
from random import shuffle
API_PARAM= {"amount":10,
            # "category":12,
            "difficulty":"medium",
            "type":"boolean"}
# API_PARAM= {"apiKey":"YOUR_API_KEY",
#            "category":"html",
#            "difficulty":"Medium",
#            "Limit":20}

# question_trivia = requests.get("https://quizapi.io/api/v1/questions", params=API_PARAM)
question_trivia = requests.get("https://opentdb.com/api.php", params=API_PARAM)
data = question_trivia.json()
question_data = [
    {"question":e['question'],
    "answer":e['correct_answer']}
     for e in data['results']]
