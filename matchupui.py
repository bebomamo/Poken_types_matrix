import customtkinter as ctk
from PIL import Image
from type_effectiveness_matrix import generateTypeEffects
import numpy as np

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Type Buttons")
app.geometry("350x680")

# List of types
types = [
    "normal", "bug", "dark", "dragon", "electric", "fairy", "fighting",
    "fire", "flying", "ghost", "grass", "ground", "ice", "poison",
    "psychic", "rock", "steel", "water"
]

# Store references (important so images don’t get garbage-collected)
images = []
buttons = []
outcome_buttons = []
selected = []

# type matrix
matrix, type_effects = generateTypeEffects()

# instantiate ctk image objects and make the west anchored objects
for i, t in enumerate(types):
    raw_img = Image.open(f"assets/{t}.png")
    ctk_img = ctk.CTkImage(
        light_image=raw_img,
        dark_image=raw_img,
        size=(raw_img.width, raw_img.height)  # natural size
    )
    images.append(ctk_img)

    btn = ctk.CTkButton(
        app,
        image=ctk_img,
        text="",
        width=raw_img.width,
        height=raw_img.height,
        fg_color="transparent",  # optional: pure image look
        hover_color="gray70",
        command=lambda t=t: (print(f"{t.capitalize()} button clicked!"), typeSelect(t))
    )
    btn.grid(row=i, column=0, padx=50, pady=5, sticky="w")
    buttons.append(btn)

    out_btn = ctk.CTkButton(
        app,
        image=ctk_img,
        text="",
        width=raw_img.width,
        height=raw_img.height,
        fg_color="transparent",  # optional: pure image look
        hover_color="gray70",
        command=lambda t=t: (print(f"{t.capitalize()} button clicked!"), typeSelect(t))
    )
    out_btn.grid(row=i, column=1, padx=50, pady=5, sticky="e")
    outcome_buttons.append(out_btn)

def typeSelect(t):
    index = 0
    for i in range(0, len(types)):
        if t == types[i]:
            index = i
            break
    # now index is the index of the type to reference the other lists...
    if t in selected:
        buttons[index].configure(fg_color="transparent")
        selected.remove(t)
    else:   
        buttons[index].configure(fg_color="blue")
        selected.append(t)
    
    updateEffects()
    return

def updateEffects():
    effectivenesses = np.zeros((1, 18))
    for type in selected:
        effectivenesses = effectivenesses - matrix[types.index(type)]
    print(effectivenesses)
    for i in range(0, len(effectivenesses[0])):
        if effectivenesses[0][i] > 4: #defender immune to this types attack
            outcome_buttons[i].configure(fg_color='white')
        elif effectivenesses[0][i] > 2: #defender 4x strongly defensive to this type
            outcome_buttons[i].configure(fg_color="#00FF00")
        elif effectivenesses[0][i] > 0: #defender 2x defensive to this type
            outcome_buttons[i].configure(fg_color="#087C08")
        elif effectivenesses[0][i] > -2: #defender is neutral to this type
            outcome_buttons[i].configure(fg_color='transparent')
        elif effectivenesses[0][i] > -4: #defender 2x weak to this type
            outcome_buttons[i].configure(fg_color="#701507")
        else: #defender 4x weak to this type
            outcome_buttons[i].configure(fg_color="#FF2200")
    return

app.mainloop()