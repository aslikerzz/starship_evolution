import os
import time
import subprocess
import math
import winsound

# ci-dessous, je définis la fonction "stack", qui va me permettre de créer un log des fonctions utilisées (quand le joueur tape 'back', ça pourra le ramener dans le menu précédent)
function_stack = []

# lignes prog : 105/205  =>  100 lignes vides/commentaires (en comptant celle-ci)

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
    function_stack.append(menu)
    print(f"""{MAGENTA}
          
        --------------------------[ {RESET}{HIGH_BLUE}MENU{MAGENTA} ]--------------------------{RESET}
        
        Je vous souhaite la bienvenue dans {YELLOW}Starship{RESET} {CYAN}Evolution{RESET}, jeune pilote !
        
        Votre {HIGH_RED}mission{RESET}, si vous l'acceptez, sera de concevoir une {YELLOW}fusée{RESET} capable de vous envoler toujours plus {HIGH_RED}haut{RESET}, 
        afin de permettre à la {UNDERLINE}{HIGH_BLUE}JAVA{RESET}{RED}*{RESET} de découvrir des zones inexplorées de notre galaxie !
        
        
        Vous contrôlerez le montage de fusée depuis l'ordinateur de contrôle, des instructions vous seront fournies.
        
        
        Bon courage, jeune pilote, la {UNDERLINE}{HIGH_BLUE}JAVA{RESET}{RED}*{RESET} compte sur votre savoir faire !
        
        '{HIGH_GREEN}rules{RESET}' pour accéder aux règles et commencer à jouer.
        
        
        {RED}*{RESET}JAVA {GREEN}=>{RESET} {RED}J{RESET}ubilation pour l'{RED}A{RESET}éronautique et le {RED}V{RESET}ol vers l'{RED}A{RESET}venture
        
        
        https://github.com/aslikerzz/starship_evolution  <= lien cliquable (ctrl+clic)
        {MAGENTA}--------------------------------------------------------------{RESET}
        
        """)

menu()

# je définis ci-dessous le 'start', y seront indiqués : les règles, les instructions de jeu

def rules():
    function_stack.append(rules)
    clear()
    print(f"""{MAGENTA}
        --------------------------[{RESET}{HIGH_BLUE} JAVA{RESET}{MAGENTA} ]--------------------------{RESET}
        
        Comme annoncé dans le menu, votre {HIGH_RED}mission{RESET} sera de faire un choix entre -- configurations.
        
        
        Étudiez bien les configurations, utilisez le {HIGH_RED}manuel{RESET}, et veillez à ce qu'il n'y est pas de pièces 
        trop puissantes, ou inversement.
        
        Votre fusée doit voler, pas s'écraser !
        
        Vos {HIGH_GREEN}contrôles{RESET} se limitent des commandes, tapez '{HIGH_GREEN}help{RESET}' pour obtenir la liste de celles-ci.
        
        {CYAN}Prêt(e) à devenir le génie de demain ?{RESET}{HIGH_GREEN}  y: lancer la partie{RESET}  //  {HIGH_RED}n: retour au menu principal{RESET}
        
        
        '{HIGH_GREEN}back{RESET}' => retour au menu précédent
        
        {MAGENTA}--------------------------------------------------------------{RESET}
        
        """)

# listes commandes ci-dessous

def h():
    function_stack.append(h)
    print(f"""{MAGENTA}
        --------------------------[{RESET}{HIGH_BLUE} JAVA{RESET}{HIGH_YELLOW} HELP{RESET}{MAGENTA} ]--------------------------{RESET}
        
        {UNDERLINE}{BOLD}{HIGH_RED}Commandes config/informatives :{RESET}
        
        {HIGH_CYAN}home{RESET}{HIGH_YELLOW}-{RESET} accéder au menu principal
        {HIGH_CYAN}rules{RESET}{HIGH_YELLOW}-{RESET} obtenir les règles
        {HIGH_CYAN}help{RESET}{HIGH_YELLOW}-{RESET} accéder au menu d'aide
        
        {UNDERLINE}{BOLD}{HIGH_RED}Commandes de jeu :{RESET}
        {RED} PAS ENCORE DEV{RESET}
        
        
        '{HIGH_GREEN}back{RESET}' => retour au menu précédent
        
        {MAGENTA}{MAGENTA}-----------------------------------------------------------------{RESET}{RESET}
        
        """)
    
# choix des configs
def y():
    function_stack.append(y)
    clear()
    print(f"""
     {MAGENTA}——————————[{RESET}{HIGH_YELLOW}CONFIG 1{RESET}{MAGENTA}]—————————————                              ——————————[CONFIG 2]—————————————        
    ‖{RESET}{HIGH_RED} {UNDERLINE}Puissance :{RESET}{MAGENTA}                      ‖                           ‖ {UNDERLINE}Puissance :{RESET}                      ‖
    {MAGENTA}‖{HIGH_BLUE} Chambre combustion :{RESET} 19{MAGENTA}          ‖                           ‖ Chambre combustion : 72          ‖
    {MAGENTA}‖{HIGH_BLUE} Turbopompe :{RESET} 12{MAGENTA}                  ‖                           ‖ Turbopompe : 46                  ‖
    {MAGENTA}‖{HIGH_BLUE} Air comprimé :{RESET} 34{MAGENTA}                ‖                           ‖ Air comprimé : 119               ‖
    {MAGENTA}‖{HIGH_BLUE} Réservoir :{RESET} 40{MAGENTA}                   ‖                           ‖ Réservoir : 210                  ‖
    {MAGENTA}‖                                  ‖                           ‖                                  ‖
    ‖ {HIGH_RED}{UNDERLINE}Équipements :{RESET}{MAGENTA}                    ‖                           ‖  {UNDERLINE}Équipements :{RESET}                   ‖
    {MAGENTA}‖{HIGH_BLUE} Fuselage :{RESET} 11{MAGENTA}                    ‖                           ‖ Fuselage : 29                    ‖
    {MAGENTA}‖{HIGH_BLUE} Empennage :{RESET} 29{MAGENTA}                   ‖                           ‖ Empennage : 52                   ‖
    {MAGENTA}‖{HIGH_BLUE} Déflecteur de jet :{RESET} 30{MAGENTA}           ‖                           ‖ Déflecteur de jet : 90           ‖
    {MAGENTA}‖{HIGH_BLUE} Gouverne aerodynamique :{RESET} 22{MAGENTA}      ‖                           ‖ Gouverne aerodynamique : 11      ‖
    {MAGENTA}‖{HIGH_BLUE} Plateforme gyroscopique:{RESET} 16{MAGENTA}      ‖                           ‖ Plateforme gyroscopique: 76      ‖
    {MAGENTA}‖                                  {MAGENTA}‖                           ‖                                  ‖
     —————————————————————————————————{RESET}                               —————————————————————————————————
     
     
     ——————————[CONFIG 3]—————————————                              ——————————[CONFIG 4]—————————————         
    ‖  {UNDERLINE} Puissance :{RESET}                    ‖                           ‖  {UNDERLINE} Puissance :{RESET}                    ‖
    ‖ Chambre combustion : 103         ‖                           ‖ Chambre combustion : 193         ‖
    ‖ Turbopompe : 79                  ‖                           ‖ Turbopompe : 68                  ‖
    ‖ Air comprimé : 89                ‖                           ‖ Air comprimé : 74                ‖
    ‖ Réservoir : 220                  ‖                           ‖ Réservoir : 802                  ‖
    ‖                                  ‖                           ‖                                  ‖ 
    ‖  {UNDERLINE} Équipements :{RESET}                  ‖                           ‖   {UNDERLINE} Équipements :{RESET}                 ‖ 
    ‖ Fuselage : 105                   ‖                           ‖ Fuselage : 308                   ‖   
    ‖ Empennage : 90                   ‖                           ‖ Empennage : 212                  ‖  
    ‖ Déflecteur de jet : 65           ‖                           ‖ Déflecteur de jet : 172          ‖ 
    ‖ Gouverne aerodynamique : 67      ‖                           ‖ Gouverne aerodynamique : 420     ‖ 
    ‖ Plateforme gyroscopique: 99      ‖                           ‖ Plateforme gyroscopique: 192     ‖  
    ‖                                  ‖                           ‖                                  ‖  
     —————————————————————————————————                              —————————————————————————————————                
     
     """)
    
def go_back():
    if len(function_stack) > 1:
        function_stack.pop()
        previous_function = function_stack.pop()
        previous_function()

# gestionnaire des commandes

while True:
    user_input = input(f"{BLUE}~JAVA@st4rship+:{RESET} ")
    
    if user_input == 'rules':
        rules()
    elif user_input == 'home':
        clear()
        menu()
    elif user_input == 'bye':
        break
    elif user_input == 'help':
        clear()
        h()
    elif user_input == 'n':
        clear()
        menu()
    elif user_input == 'back':
        clear()
        go_back()
    elif user_input == 'y':
        clear()
        y()



# source schéma fusée :
# https://static.techno-science.net/illustration/Definitions/1200px/v/v-2-rocket-diagram-with-french-labels.svg_481431405adecddfbbb13033a0a3871a.png
