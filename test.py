import requests
import random

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "hp": data["stats"][0]["base_stat"],       
        "attack": data["stats"][1]["base_stat"],   
    }
pikachu = getPoke("pikachu")
for key, value in pikachu.items():
    print(f"{key.title()}: {value}")
def battle(pokemon1, pokemon2):
    print(f" {pokemon1['name']} VS {pokemon2['name']} ")
    
    hp1 = pokemon1["hp"]
    hp2 = pokemon2["hp"]
    
    while hp1 > 0 and hp2 > 0:
       
        dmg1 = random.randint(pokemon1["attack"]//2, pokemon1["attack"])
        dmg2 = random.randint(pokemon2["attack"]//2, pokemon2["attack"])
        
        hp2 -= dmg1
        hp1 -= dmg2
        
        print(f"{pokemon1['name']} hits {pokemon2['name']} for {dmg1} damage! ({max(hp2, 0)} HP left)")
        print(f"{pokemon2['name']} hits {pokemon1['name']} for {dmg2} damage! ({max(hp1, 0)} HP left)\n")
    
    if hp1 <= 0 and hp2 <= 0:
        print("It's a tie!")
    elif hp1 <= 0:
        print(f"{pokemon2['name']} wins")
    else:
        print(f"{pokemon1['name']} wins")
poke1_name = input("chose the name for ur pokemon: ")
poke2_name = input("choose the name for yur second pokemon: ")

poke1 = getPoke(poke1_name)
poke2 = getPoke(poke2_name)

if poke1 and poke2:
    battle(poke1, poke2)


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
# upgrade_button.pack(pady=10)

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

