import requests
import tkinter as tk
import random

def get_questions():
    response = requests.get("https://opentdb.com/api.php?amount=10&type=multiple")
    data = response.json()
    return data["results"]

questions = get_questions()
window = tk.Tk()
window.title("Welcome to Rizzzo Quizzo")
window.geometry("600x400")
window.current_question = 0
window.score = 0
question_label = tk.Label(window, text="", wraplength=550, font=("Arial", 14))
question_label.pack(pady=20)
buttons = []
for i in range(4):
    button = tk.Button(window, text="", width=40, font=("Arial", 12))
    button.pack(pady=5)
    buttons.append(button)

def create_question():
    if window.current_question >= len(questions):
        question_label.config(text=f"Game Over\nScore: {window.score} / {len(questions)}")
        return
    q = questions[window.current_question]
    answers = q["incorrect_answers"] + [q["correct_answer"]]
    random.shuffle(answers)
    question_label.config(text=q["question"])
    for i in range(4):
        buttons[i].config(text=answers[i])

def check_answer(selected):
    correct = questions[window.current_question]["correct_answer"]
    if selected == correct:
        window.score += 1
    window.current_question += 1
    create_question()
def answer1():
    check_answer(buttons[0]["text"])
def answer2():
    check_answer(buttons[1]["text"])
def answer3():
    check_answer(buttons[2]["text"])
def answer4():
    check_answer(buttons[3]["text"])

buttons[0].config(command=answer1)
buttons[1].config(command=answer2)
buttons[2].config(command=answer3)
buttons[3].config(command=answer4)

create_question()
window.mainloop()

# import tkinter as tk
# cookies = 0
# cookies_per_click = 1
# upgrade_cost = 10
# def click_cookie():
#     cookies +=1
#     cookies += cookies_per_click
#     update_labels()

# def buy_upgrade():
#     cookies, cookies_per_click, upgrade_cost
#     if cookies >= upgrade_cost:
#         cookies -= upgrade_cost
#         cookies_per_click += 1
#         upgrade_cost += 10
#         update_labels()

# def update_labels():
#     cookie_label.config(text=f"Cookies: {cookies}")
#     cpc_label.config(text=f"Cookies per click: {cookies_per_click}")
#     upgrade_button.config(text=f"Upgrade (+1 CPC)\nCost: {upgrade_cost}")


# root = tk.Tk()
# root.title("Cookie Clicker")
# root.geometry("300x300")


# cookie_label = tk.Label(root, text="Cookies: 0", font=("Arial", 16))
# cookie_label.pack(pady=10)

# cpc_label = tk.Label(root, text="Cookies per click: 1")
# cpc_label.pack()

# cookie_button = tk.Button(
#     root,
#     text="Press To Click",
#     width=15,
#     command=click_cookie
# )
# cookie_button.pack(pady=10)

# upgrade_button = tk.Button(
#     root,
#     text="Upgrade (+1 CPC)\nCost: 10",
#     command=buy_upgrade
# )


# root.mainloop()

# import requests

# def getPoke(poke):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
#     if response.status_code != 200:
#         print("Error fetching data!")
#         return None
    
#     data = response.json()
#     return {
#         "name": data["name"],
#         "height": data["height"],
#         "weight": data["weight"],
#         "types": [t["type"]["name"] for t in data["types"]]
#     }

# pokemon = getPoke("Bulbasaur")
# print(pokemon)

