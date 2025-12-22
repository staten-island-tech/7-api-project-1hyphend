import tkinter as tk
cookies = 0
cookies_per_click = 1
upgrade_cost = 10
def click_cookie():
    cookies +=1
    cookies += cookies_per_click
    update_labels()

def buy_upgrade():
    cookies, cookies_per_click, upgrade_cost
    if cookies >= upgrade_cost:
        cookies -= upgrade_cost
        cookies_per_click += 1
        upgrade_cost += 10
        update_labels()

def update_labels():
    cookie_label.config(text=f"Cookies: {cookies}")
    cpc_label.config(text=f"Cookies per click: {cookies_per_click}")
    upgrade_button.config(text=f"Upgrade (+1 CPC)\nCost: {upgrade_cost}")


root = tk.Tk()
root.title("Cookie Clicker 🍪")
root.geometry("300x300")


cookie_label = tk.Label(root, text="Cookies: 0", font=("Arial", 16))
cookie_label.pack(pady=10)

cpc_label = tk.Label(root, text="Cookies per click: 1")
cpc_label.pack()

cookie_button = tk.Button(
    root,
    text="🍪 Click Me!",
    font=("Arial", 14),
    width=15,
    command=click_cookie
)
cookie_button.pack(pady=10)

upgrade_button = tk.Button(
    root,
    text="Upgrade (+1 CPC)\nCost: 10",
    command=buy_upgrade
)
upgrade_button.pack(pady=10)

root.mainloop()