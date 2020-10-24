import requests

def api_data(item):
    question = item['question']
    global correct_ans 
    correct_ans = item['correct_answer']
    print(f'Question: {question}')

choices = '''
*****Welcome to the Quiz*****
Choose your topic:
1.General Knowlegde
2.Films
3.Computer
'''
try:
    usr_choice = int(input(choices))
except ValueError:
    print('Pleas enter a number!!')
    exit()

if usr_choice == 1:
    url = 'https://opentdb.com/api.php?amount=5&category=9&difficulty=medium&type=boolean'
elif usr_choice == 2:
    url = 'https://opentdb.com/api.php?amount=5&category=11&difficulty=medium&type=boolean'
elif usr_choice == 3:
    url = 'https://opentdb.com/api.php?amount=5&category=18&difficulty=medium&type=boolean'
else:
    print('Please choose between 1 to 4')
    exit()

response = requests.get(url)
text = response.json()
result = text['results']
score = 0
for item in result:
    api_data(item)
    usr_ans = input('True/False?: ').title()
    if usr_ans == correct_ans:
        score+=1
    elif usr_ans != 'True' or usr_ans != 'False':
        print('Enter True or False only!! Score discarded!!\n')
print(f'Your Score: {score}\n*Thanks For Playing*')
