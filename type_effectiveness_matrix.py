import numpy as np

class State:
    def __init__(self, balance: bool = False, coverage: bool = False):
        self.balance = balance  # binary field (True/False)
        self.coverage = coverage

    def toggle_balance(self):
        """Flip the balance state."""
        self.balance = not self.balance

    def toggle_coverage(self):
        """Flip the coverage state."""
        self.coverage = not self.coverage

    def __repr__(self):
        return f"State(balance={self.balance})"
    
# List of types
types = [
    "normal", "bug", "dark", "dragon", "electric", "fairy", "fighting",
    "fire", "flying", "ghost", "grass", "ground", "ice", "poison",
    "psychic", "rock", "steel", "water"
]

# [attacker][defender]
def generateTypeEffects():
    type_effects = {
        "normal":   {"normal": 0, "bug": 0, "dark": 0, "dragon": 0, "electric": 0, "fairy": 0, "fighting": 0, "fire": 0, "flying": 0, "ghost": -10, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 0, "rock": -2, "steel": -2, "water": 0},
        "bug":      {"normal": 0, "bug": 0, "dark": 2, "dragon": 0, "electric": 0, "fairy": -2, "fighting": -2, "fire": -2, "flying": -2, "ghost": -2, "grass": 2, "ground": 0, "ice": 0, "poison": -2, "psychic": 2, "rock": 0, "steel": -2, "water": 0},
        "dark":     {"normal": 0, "bug": 0, "dark": -2, "dragon": 0, "electric": 0, "fairy": -2, "fighting": -2, "fire": 0, "flying": 0, "ghost": 2, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 2, "rock": 0, "steel": 0, "water": 0},
        "dragon":   {"normal": 0, "bug": 0, "dark": 0, "dragon": 2, "electric": 0, "fairy": -10, "fighting": 0, "fire": 0, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 0, "rock": 0, "steel": -2, "water": 0},
        "electric": {"normal": 0, "bug": 0, "dark": 0, "dragon": -2, "electric": -2, "fairy": 0, "fighting": 0, "fire": 0, "flying": 2, "ghost": 0, "grass": -2, "ground": -10, "ice": 0, "poison": 0, "psychic": 0, "rock": 0, "steel": 0, "water": 2},
        "fairy":    {"normal": 0, "bug": 0, "dark": 2, "dragon": 2, "electric": 0, "fairy": 0, "fighting": 2, "fire": -2, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 0, "poison": -2, "psychic": 0, "rock": 0, "steel": -2, "water": 0},
        "fighting": {"normal": 2, "bug": -2, "dark": 2, "dragon": 0, "electric": 0, "fairy": -2, "fighting": 0, "fire": 0, "flying": -2, "ghost": -10, "grass": 0, "ground": 0, "ice": 2, "poison": -2, "psychic": -2, "rock": 2, "steel": 2, "water": 0},
        "fire":     {"normal": 0, "bug": 2, "dark": 0, "dragon": -2, "electric": 0, "fairy": 0, "fighting": 0, "fire": -2, "flying": 0, "ghost": 0, "grass": 2, "ground": 0, "ice": 2, "poison": 0, "psychic": 0, "rock": -2, "steel": 2, "water": -2},
        "flying":   {"normal": 0, "bug": 2, "dark": 0, "dragon": 0, "electric": -2, "fairy": 0, "fighting": 2, "fire": 0, "flying": 0, "ghost": 0, "grass": 2, "ground": 0, "ice": 0, "poison": 0, "psychic": 0, "rock": -2, "steel": -2, "water": 0},
        "ghost":    {"normal": -10, "bug": 0, "dark": -2, "dragon": 0, "electric": 0, "fairy": 0, "fighting": 0, "fire": 0, "flying": 0, "ghost": 2, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 2, "rock": 0, "steel": 0, "water": 0},
        "grass":    {"normal": 0, "bug": -2, "dark": 0, "dragon": -2, "electric": 0, "fairy": 0, "fighting": 0, "fire": -2, "flying": -2, "ghost": 0, "grass": -2, "ground": 2, "ice": 0, "poison": -2, "psychic": 0, "rock": 2, "steel": -2, "water": 2},
        "ground":   {"normal": 0, "bug": -2, "dark": 0, "dragon": 0, "electric": 2, "fairy": 0, "fighting": 0, "fire": 2, "flying": -10, "ghost": 0, "grass": -2, "ground": 0, "ice": 0, "poison": 2, "psychic": 0, "rock": 2, "steel": 2, "water": 0},
        "ice":      {"normal": 0, "bug": 0, "dark": 0, "dragon": 2, "electric": 0, "fairy": 0, "fighting": 0, "fire": -2, "flying": 2, "ghost": 0, "grass": 2, "ground": 2, "ice": -2, "poison": 0, "psychic": 0, "rock": 0, "steel": -2, "water": -2},
        "poison":   {"normal": 0, "bug": 0, "dark": 0, "dragon": 0, "electric": 0, "fairy": 2, "fighting": 0, "fire": 0, "flying": 0, "ghost": -2, "grass": 2, "ground": -2, "ice": 0, "poison": -2, "psychic": 0, "rock": -2, "steel": -10, "water": 0},
        "psychic":  {"normal": 0, "bug": 0, "dark": -10, "dragon": 0, "electric": 0, "fairy": 0, "fighting": 2, "fire": 0, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 0, "poison": 2, "psychic": -2, "rock": 0, "steel": -2, "water": 0},
        "rock":     {"normal": 0, "bug": 2, "dark": 0, "dragon": 0, "electric": 0, "fairy": 0, "fighting": -2, "fire": 2, "flying": 2, "ghost": 0, "grass": 0, "ground": -2, "ice": 2, "poison": 0, "psychic": 0, "rock": 0, "steel": -2, "water": 0},
        "steel":    {"normal": 0, "bug": 0, "dark": 0, "dragon": 0, "electric": -2, "fairy": 2, "fighting": 0, "fire": -2, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 2, "poison": 0, "psychic": 0, "rock": 2, "steel": -2, "water": -2},
        "water":    {"normal": 0, "bug": 0, "dark": 0, "dragon": -2, "electric": 0, "fairy": 0, "fighting": 0, "fire": 2, "flying": 0, "ghost": 0, "grass": -2, "ground": 2, "ice": 0, "poison": 0, "psychic": 0, "rock": 2, "steel": 0, "water": -2}
    }

    matrix = np.array([[type_effects[attacker][defender] for attacker in types] for defender in types])
    return matrix, type_effects

def generateTypeEffectsBalanceD():
    type_effects = {
        "normal":   {"normal": 0, "bug": 0, "dark": 0, "dragon": 0, "electric": 0, "fairy": 0, "fighting": 0, "fire": 0, "flying": 0, "ghost": -10, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 0, "rock": -2, "steel": -2, "water": 0},
        "bug":      {"normal": 0, "bug": 0, "dark": 2, "dragon": 0, "electric": 0, "fairy": -2, "fighting": -2, "fire": -2, "flying": -2, "ghost": -2, "grass": 2, "ground": 0, "ice": 0, "poison": -2, "psychic": 2, "rock": 0, "steel": -2, "water": 0},
        "dark":     {"normal": 0, "bug": 0, "dark": -2, "dragon": 0, "electric": 0, "fairy": -2, "fighting": -2, "fire": 0, "flying": 0, "ghost": 2, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 2, "rock": 0, "steel": 0, "water": 0},
        "dragon":   {"normal": 0, "bug": 0, "dark": 0, "dragon": 2, "electric": 0, "fairy": -10, "fighting": 0, "fire": 0, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 0, "rock": 0, "steel": -2, "water": 0},
        "electric": {"normal": 0, "bug": 0, "dark": 0, "dragon": -2, "electric": -2, "fairy": 0, "fighting": 0, "fire": 0, "flying": 2, "ghost": 0, "grass": -2, "ground": -10, "ice": 0, "poison": 0, "psychic": 0, "rock": 0, "steel": 0, "water": 2},
        "fairy":    {"normal": 0, "bug": 0, "dark": 2, "dragon": 2, "electric": 0, "fairy": 0, "fighting": 2, "fire": -2, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 0, "poison": -2, "psychic": 0, "rock": 0, "steel": -2, "water": 0},
        "fighting": {"normal": 2, "bug": -2, "dark": 2, "dragon": 0, "electric": 0, "fairy": -2, "fighting": 0, "fire": 0, "flying": -2, "ghost": -10, "grass": 0, "ground": 0, "ice": 2, "poison": -2, "psychic": -2, "rock": 2, "steel": 2, "water": 0},
        "fire":     {"normal": 0, "bug": 2, "dark": 0, "dragon": -2, "electric": 0, "fairy": 0, "fighting": 0, "fire": -2, "flying": 0, "ghost": 0, "grass": 2, "ground": 0, "ice": 2, "poison": 0, "psychic": 0, "rock": -2, "steel": 2, "water": -2},
        "flying":   {"normal": 0, "bug": 2, "dark": 0, "dragon": 0, "electric": -2, "fairy": 0, "fighting": 2, "fire": 0, "flying": 0, "ghost": 0, "grass": 2, "ground": 0, "ice": 0, "poison": 0, "psychic": 0, "rock": -2, "steel": -2, "water": 0},
        "ghost":    {"normal": -10, "bug": 0, "dark": -2, "dragon": 0, "electric": 0, "fairy": 0, "fighting": 0, "fire": 0, "flying": 0, "ghost": 2, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 2, "rock": 0, "steel": 0, "water": 0},
        "grass":    {"normal": 0, "bug": -2, "dark": 0, "dragon": -2, "electric": 0, "fairy": 0, "fighting": 0, "fire": -2, "flying": -2, "ghost": 0, "grass": -2, "ground": 2, "ice": 0, "poison": -2, "psychic": 0, "rock": 2, "steel": -2, "water": 2},
        "ground":   {"normal": 0, "bug": -2, "dark": 0, "dragon": 0, "electric": 2, "fairy": 0, "fighting": 0, "fire": 2, "flying": -10, "ghost": 0, "grass": -2, "ground": 0, "ice": 0, "poison": 2, "psychic": 0, "rock": 2, "steel": 2, "water": 0},
        "ice":      {"normal": 0, "bug": 0, "dark": 0, "dragon": 2, "electric": 0, "fairy": 0, "fighting": 0, "fire": -2, "flying": 2, "ghost": 0, "grass": 2, "ground": 2, "ice": -2, "poison": 0, "psychic": 0, "rock": 0, "steel": -2, "water": -2},
        "poison":   {"normal": 0, "bug": 0, "dark": 0, "dragon": 0, "electric": 0, "fairy": 2, "fighting": 0, "fire": 0, "flying": 0, "ghost": -2, "grass": 2, "ground": -2, "ice": 0, "poison": -2, "psychic": 0, "rock": -2, "steel": -10, "water": 0},
        "psychic":  {"normal": 0, "bug": 0, "dark": -10, "dragon": 0, "electric": 0, "fairy": 0, "fighting": 2, "fire": 0, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 0, "poison": 2, "psychic": -2, "rock": 0, "steel": -2, "water": 0},
        "rock":     {"normal": 0, "bug": 2, "dark": 0, "dragon": 0, "electric": 0, "fairy": 0, "fighting": -2, "fire": 2, "flying": 2, "ghost": 0, "grass": 0, "ground": -2, "ice": 2, "poison": 0, "psychic": 0, "rock": 0, "steel": -2, "water": 0},
        "steel":    {"normal": 0, "bug": 0, "dark": 0, "dragon": 0, "electric": -2, "fairy": 2, "fighting": 0, "fire": -2, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 2, "poison": 0, "psychic": 0, "rock": 2, "steel": -2, "water": -2},
        "water":    {"normal": 0, "bug": 0, "dark": 0, "dragon": -2, "electric": 0, "fairy": 0, "fighting": 0, "fire": 2, "flying": 0, "ghost": 0, "grass": -2, "ground": 2, "ice": 0, "poison": 0, "psychic": 0, "rock": 2, "steel": 0, "water": -2}
    }

    matrix = np.array([[type_effects[attacker][defender] for attacker in types] for defender in types])
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] > 0:
                matrix[i][j] = 0

    return matrix, type_effects

def generateTypeEffectsBalanceO():
    type_effects = {
        "normal":   {"normal": 0, "bug": 0, "dark": 0, "dragon": 0, "electric": 0, "fairy": 0, "fighting": 0, "fire": 0, "flying": 0, "ghost": -10, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 0, "rock": -2, "steel": -2, "water": 0},
        "bug":      {"normal": 0, "bug": 0, "dark": 2, "dragon": 0, "electric": 0, "fairy": -2, "fighting": -2, "fire": -2, "flying": -2, "ghost": -2, "grass": 2, "ground": 0, "ice": 0, "poison": -2, "psychic": 2, "rock": 0, "steel": -2, "water": 0},
        "dark":     {"normal": 0, "bug": 0, "dark": -2, "dragon": 0, "electric": 0, "fairy": -2, "fighting": -2, "fire": 0, "flying": 0, "ghost": 2, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 2, "rock": 0, "steel": 0, "water": 0},
        "dragon":   {"normal": 0, "bug": 0, "dark": 0, "dragon": 2, "electric": 0, "fairy": -10, "fighting": 0, "fire": 0, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 0, "rock": 0, "steel": -2, "water": 0},
        "electric": {"normal": 0, "bug": 0, "dark": 0, "dragon": -2, "electric": -2, "fairy": 0, "fighting": 0, "fire": 0, "flying": 2, "ghost": 0, "grass": -2, "ground": -10, "ice": 0, "poison": 0, "psychic": 0, "rock": 0, "steel": 0, "water": 2},
        "fairy":    {"normal": 0, "bug": 0, "dark": 2, "dragon": 2, "electric": 0, "fairy": 0, "fighting": 2, "fire": -2, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 0, "poison": -2, "psychic": 0, "rock": 0, "steel": -2, "water": 0},
        "fighting": {"normal": 2, "bug": -2, "dark": 2, "dragon": 0, "electric": 0, "fairy": -2, "fighting": 0, "fire": 0, "flying": -2, "ghost": -10, "grass": 0, "ground": 0, "ice": 2, "poison": -2, "psychic": -2, "rock": 2, "steel": 2, "water": 0},
        "fire":     {"normal": 0, "bug": 2, "dark": 0, "dragon": -2, "electric": 0, "fairy": 0, "fighting": 0, "fire": -2, "flying": 0, "ghost": 0, "grass": 2, "ground": 0, "ice": 2, "poison": 0, "psychic": 0, "rock": -2, "steel": 2, "water": -2},
        "flying":   {"normal": 0, "bug": 2, "dark": 0, "dragon": 0, "electric": -2, "fairy": 0, "fighting": 2, "fire": 0, "flying": 0, "ghost": 0, "grass": 2, "ground": 0, "ice": 0, "poison": 0, "psychic": 0, "rock": -2, "steel": -2, "water": 0},
        "ghost":    {"normal": -10, "bug": 0, "dark": -2, "dragon": 0, "electric": 0, "fairy": 0, "fighting": 0, "fire": 0, "flying": 0, "ghost": 2, "grass": 0, "ground": 0, "ice": 0, "poison": 0, "psychic": 2, "rock": 0, "steel": 0, "water": 0},
        "grass":    {"normal": 0, "bug": -2, "dark": 0, "dragon": -2, "electric": 0, "fairy": 0, "fighting": 0, "fire": -2, "flying": -2, "ghost": 0, "grass": -2, "ground": 2, "ice": 0, "poison": -2, "psychic": 0, "rock": 2, "steel": -2, "water": 2},
        "ground":   {"normal": 0, "bug": -2, "dark": 0, "dragon": 0, "electric": 2, "fairy": 0, "fighting": 0, "fire": 2, "flying": -10, "ghost": 0, "grass": -2, "ground": 0, "ice": 0, "poison": 2, "psychic": 0, "rock": 2, "steel": 2, "water": 0},
        "ice":      {"normal": 0, "bug": 0, "dark": 0, "dragon": 2, "electric": 0, "fairy": 0, "fighting": 0, "fire": -2, "flying": 2, "ghost": 0, "grass": 2, "ground": 2, "ice": -2, "poison": 0, "psychic": 0, "rock": 0, "steel": -2, "water": -2},
        "poison":   {"normal": 0, "bug": 0, "dark": 0, "dragon": 0, "electric": 0, "fairy": 2, "fighting": 0, "fire": 0, "flying": 0, "ghost": -2, "grass": 2, "ground": -2, "ice": 0, "poison": -2, "psychic": 0, "rock": -2, "steel": -10, "water": 0},
        "psychic":  {"normal": 0, "bug": 0, "dark": -10, "dragon": 0, "electric": 0, "fairy": 0, "fighting": 2, "fire": 0, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 0, "poison": 2, "psychic": -2, "rock": 0, "steel": -2, "water": 0},
        "rock":     {"normal": 0, "bug": 2, "dark": 0, "dragon": 0, "electric": 0, "fairy": 0, "fighting": -2, "fire": 2, "flying": 2, "ghost": 0, "grass": 0, "ground": -2, "ice": 2, "poison": 0, "psychic": 0, "rock": 0, "steel": -2, "water": 0},
        "steel":    {"normal": 0, "bug": 0, "dark": 0, "dragon": 0, "electric": -2, "fairy": 2, "fighting": 0, "fire": -2, "flying": 0, "ghost": 0, "grass": 0, "ground": 0, "ice": 2, "poison": 0, "psychic": 0, "rock": 2, "steel": -2, "water": -2},
        "water":    {"normal": 0, "bug": 0, "dark": 0, "dragon": -2, "electric": 0, "fairy": 0, "fighting": 0, "fire": 2, "flying": 0, "ghost": 0, "grass": -2, "ground": 2, "ice": 0, "poison": 0, "psychic": 0, "rock": 2, "steel": 0, "water": -2}
    }

    matrix = np.array([[type_effects[attacker][defender] for defender in types] for attacker in types])
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] < 0:
                matrix[i][j] = 0

    return matrix, type_effects