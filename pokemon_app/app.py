import tkinter as tk
import requests

class PokemonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Data App")
        self.root.geometry("400x400")

        self.label = tk.Label(root, text="Enter Pokémon Name or ID")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Search", command=self.fetch_pokemon)
        self.button.pack(pady=5)

        self.result = tk.Label(root, text="", justify="left")
        self.result.pack(pady=10)

    def fetch_pokemon(self):
        name = self.entry.get().lower()
        if not name:
            self.result.config(text="Please enter a Pokémon name or ID")
            return

        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.update_ui(data)
        else:
            self.result.config(text="Pokémon not found")

    def update_ui(self, data):
        name = data['name'].title()
        height = data['height']
        weight = data['weight']
        types = ', '.join([t['type']['name'] for t in data['types']])

        info = (
            f"Name: {name}\n"
            f"Height: {height}\n"
            f"Weight: {weight}\n"
            f"Types: {types}"
        )
        self.result.config(text=info)

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonApp(root)
    root.mainloop()

