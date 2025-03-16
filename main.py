import os
import time
import subprocess
import math
import winsound

# lignes prog : 29/77

# j'appelle ici les codes ANSI pour les couleurs 
# d'abord, je mets les effets et le reset

RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# puis, j'appelle les codes couleurs basiques

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
BLACK = "\033[30m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE_LIGHT_GREY = "\033[37m"

# afin de mieux texturer l'ensemble, j'appelle les codes de couleurs brillantes, je veux essayer de créer quelque chose de beau mdrr

HIGH_RED = "\033[91m"
HIGH_GREEN = "\033[92m"
HIGH_YELLOW = "\033[93m"
HIGH_BLUE = "\033[94m"
HIGH_MAGENTA = "\033[95m"
HIGH_CYAN = "\033[96m"
HIGH_WHITE = "\033[97m"

# le code ANSI a été l'une de mes meilleures découvertes à travers ce projet, merci aux ingés de l'époque de nos grands parents

# plus tard, j'ajouterai peut-être des couleurs de fond, j'ai un peu imaginé mon Starship Evolution de rêve, donc why not

# note à moi-même, la syntaxe pour utiliser ANSI => f"{CODE_ANSI}<mon texte>{CODE_RESET}"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(f"""{MAGENTA}
          
        --------------------------[ MENU ]--------------------------{RESET}
        
        Je vous souhaite la bienvenue dans {YELLOW}Starship{RESET} {CYAN}Evolution{RESET}, jeune pilote !
        
        Votre {HIGH_RED}mission{RESET}, si vous l'acceptez, sera de concevoir une {YELLOW}fusée{RESET} capable de vous envoler toujours plus {HIGH_RED}haut{RESET}, 
        afin de permettre à la {UNDERLINE}{HIGH_BLUE}JAVA{RESET}{RED}*{RESET} de découvrir des zones inexplorées de notre galaxie !
        
        
        Vous contrôlerez le montage de fusée depuis l'ordinateur de contrôle, des instructions vous seront fournies.
        
        
        Bon courage, jeune pilote, la {UNDERLINE}{HIGH_BLUE}JAVA{RESET}{RED}*{RESET} compte sur votre savoir faire !
        
        'start' pour commencer à jouer.
        
        
        {RED}*{RESET}JAVA {GREEN}=>{RESET} {RED}J{RESET}ubilation pour l'{RED}A{RESET}éronautique et le {RED}V{RESET}ol vers l'{RED}A{RESET}venture
        
        
        https://github.com/aslikerzz/starship_evolution
        {MAGENTA}--------------------------------------------------------------{RESET}
        
        """)

menu()

# user input

while True:
    user_input = input(f"{BLUE}~JAVA@st4rship+:{RESET} ")