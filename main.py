import os
import time
import subprocess
import math
import winsound

# ci-dessous, la variable des fusées

starship1 = [
    r"                                        ^",
    r"                                       / \\",
    r"                                       |-|",
    r"                                       |||",
    r"                                       | |",
    r"                                       |_|",
    r"                                      //=\\"
    r"                                        |",
    r"                                          ",
    r"                                        |",
    r"                                          ",
    r"                                        |",
]

starship2 = [
    r"                                        |",
    r"                                       / \\",
    r"                                       |-|",
    r"                                      /|||\\",
    r"                                     //| |\\",
    r"                                       |_|",
    r"                                      //=\\"
    r"                                        |",
    r"                                          ",
    r"                                        |",
    r"                                          ",
    r"                                        |",
]

starship3 = [
    r"                                        o",
    r"                                       / \\",
    r"                                       |-|",
    r"                                      /|u|\\",
    r"                                     //|s|\\",
    r"                                       |a|"
    r"                                       |_|",
    r"                                      //@\\"
    r"                                        |",
    r"                                         ",
    r"                                        |",
    r"                                         ",
    r"                                        |",
]

starship4 = [
    r"                                         ^",
    r"                                       // \\",
    r"                                       |-|-|",
    r"                                      //|||\\",
    r"                                       | | |",
    r"                                      //_|_\\",
    r"                                         |",
    r"                                         ",
    r"                                         |",
    r"                                         ",
    r"                                         |",
]

# ci-dessous, je définis la variable "stack", qui va me permettre de créer un log des fonctions utilisées (quand le joueur tape 'back', ça pourra le ramener dans le menu précédent)
function_stack = []

# lignes prog : 205/394  =>  189 lignes vides/commentaires (en comptant celle-ci)

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
        
        
        Étudiez bien les configurations, utilisez le {HIGH_RED}manuel{RESET} pour pouvoir jouer, 
        et veillez à ce qu'il n'y est pas de pièces trop puissantes, ou inversement.
        
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
        --------------------------[{RESET}{HIGH_BLUE} JAVA{RESET}{HIGH_YELLOW} MANUEL{RESET}{MAGENTA} ]--------------------------{RESET}
        
        {UNDERLINE}{BOLD}{HIGH_RED}Commandes config/informatives :{RESET}
        
        {HIGH_CYAN}home{RESET}{HIGH_YELLOW} -{RESET} accéder au menu principal
        {HIGH_CYAN}rules{RESET}{HIGH_YELLOW} -{RESET} obtenir les règles
        {HIGH_CYAN}help{RESET}{HIGH_YELLOW} -{RESET} accéder au menu d'aide
        {HIGH_CYAN}back{RESET}{HIGH_YELLOW} -{RESET} retourner au menu précédent
        {HIGH_CYAN}bye{RESET}{HIGH_YELLOW} -{RESET} quitter le jeu
        
        {UNDERLINE}{BOLD}{HIGH_RED}Commandes de jeu :{RESET}
        {HIGH_CYAN}retry{RESET}{HIGH_YELLOW} -{RESET} relancer une partie
        {HIGH_CYAN}conf{RESET}{HIGH_YELLOW} -{RESET} afin de sélectionner une configuration, tapez '{HIGH_GREEN}conf1{RESET}' (pour la 2ème, 'conf2', etc)
        
        
        '{HIGH_GREEN}back{RESET}' => retour au menu précédent
        
        {MAGENTA}{MAGENTA}-----------------------------------------------------------------{RESET}{RESET}
        
        """)
    
# choix des configs
def y():
    function_stack.append(y)
    clear()
    print(f"""
     {MAGENTA}——————————[{RESET}{HIGH_YELLOW}CONFIG 1{RESET}{MAGENTA}]—————————————                              ——————————[{RESET}{HIGH_YELLOW}CONFIG 2{RESET}{MAGENTA}]—————————————        
    ‖{RESET}{HIGH_RED} {UNDERLINE}Puissance :{RESET}{MAGENTA}                      ‖                           ‖ {UNDERLINE}{HIGH_RED}Puissance :{RESET}{MAGENTA}                       ‖
    {MAGENTA}‖{HIGH_BLUE} Chambre combustion :{RESET} 19{MAGENTA}          ‖                           ‖{HIGH_BLUE} Chambre combustion :{RESET} 72{MAGENTA}           ‖
    {MAGENTA}‖{HIGH_BLUE} Turbopompe :{RESET} 12{MAGENTA}                  ‖                           ‖{HIGH_BLUE} Turbopompe :{RESET} 46{MAGENTA}                   ‖
    {MAGENTA}‖{HIGH_BLUE} Air comprimé :{RESET} 34{MAGENTA}                ‖                           ‖{HIGH_BLUE} Air comprimé :{RESET} 119{MAGENTA}                ‖
    {MAGENTA}‖{HIGH_BLUE} Réservoir :{RESET} 40{MAGENTA}                   ‖                           ‖{HIGH_BLUE} Réservoir :{RESET} 210{MAGENTA}                   ‖
    {MAGENTA}‖                                  ‖                           ‖                                   ‖  
    ‖ {HIGH_RED}{UNDERLINE}Équipements :{RESET}{MAGENTA}                    ‖                           ‖  {UNDERLINE}{HIGH_RED}Équipements :{RESET}{MAGENTA}                    ‖
    {MAGENTA}‖{HIGH_BLUE} Fuselage :{RESET} 11{MAGENTA}                    ‖                           ‖{HIGH_BLUE} Fuselage :{RESET} 29{MAGENTA}                     ‖
    {MAGENTA}‖{HIGH_BLUE} Empennage :{RESET} 29{MAGENTA}                   ‖                           ‖{HIGH_BLUE} Empennage :{RESET} 52{MAGENTA}                    ‖
    {MAGENTA}‖{HIGH_BLUE} Déflecteur de jet :{RESET} 30{MAGENTA}           ‖                           ‖{HIGH_BLUE} Déflecteur de jet :{RESET} 90{MAGENTA}            ‖
    {MAGENTA}‖{HIGH_BLUE} Gouverne aerodynamique :{RESET} 22{MAGENTA}      ‖                           ‖{HIGH_BLUE} Gouverne aerodynamique :{RESET} 11{MAGENTA}       ‖
    {MAGENTA}‖{HIGH_BLUE} Plateforme gyroscopique:{RESET} 16{MAGENTA}      ‖                           ‖{HIGH_BLUE} Plateforme gyroscopique:{RESET} 76{MAGENTA}       ‖
    {MAGENTA}‖                                  {MAGENTA}‖                           ‖                                   ‖
     —————————————————————————————————{RESET}                               {MAGENTA}—————————————————————————————————{RESET}
     
     
    {MAGENTA}  ——————————[{RESET}{HIGH_YELLOW}CONFIG 3{RESET}{MAGENTA}]—————————————                               ——————————[{RESET}{HIGH_YELLOW}CONFIG 4{RESET}{MAGENTA}]—————————————         
    {MAGENTA} ‖  {UNDERLINE}{HIGH_RED}Puissance :{RESET}{MAGENTA}                      ‖                           ‖  {UNDERLINE}{HIGH_RED}Puissance :{RESET}{MAGENTA}                      ‖
    {MAGENTA} ‖ {HIGH_BLUE}Chambre combustion :{RESET} 103{MAGENTA}          ‖                           ‖{HIGH_BLUE} Chambre combustion :{RESET} 193{MAGENTA}          ‖
    {MAGENTA} ‖{HIGH_BLUE} Turbopompe :{RESET} 79{MAGENTA}                   ‖                           ‖{HIGH_BLUE} Turbopompe :{RESET} 68{MAGENTA}                   ‖
    {MAGENTA} ‖{HIGH_BLUE} Air comprimé :{RESET} 89{MAGENTA}                 ‖                           ‖{HIGH_BLUE} Air comprimé :{RESET} 74{MAGENTA}                 ‖
    {MAGENTA} ‖{HIGH_BLUE} Réservoir :{RESET} 220{MAGENTA}                   ‖                           ‖{HIGH_BLUE} Réservoir :{RESET} 802{MAGENTA}                   ‖
    {MAGENTA} ‖                                   ‖                           ‖                                   ‖ 
    {MAGENTA} ‖  {UNDERLINE}{HIGH_RED}Équipements :{RESET}{MAGENTA}                    ‖                           ‖   {UNDERLINE}{HIGH_RED}Équipements :{RESET}{MAGENTA}                   ‖ 
    {MAGENTA} ‖{HIGH_BLUE} Fuselage :{RESET} 105{MAGENTA}                    ‖                           ‖{HIGH_BLUE} Fuselage :{RESET} 308{MAGENTA}                    ‖   
    {MAGENTA} ‖{HIGH_BLUE} Empennage :{RESET} 90{MAGENTA}                    ‖                           ‖{HIGH_BLUE} Empennage :{RESET} 212{MAGENTA}                   ‖  
    {MAGENTA} ‖{HIGH_BLUE} Déflecteur de jet :{RESET} 65{MAGENTA}            ‖                           ‖{HIGH_BLUE} Déflecteur de jet :{RESET} 172{MAGENTA}           ‖ 
   {MAGENTA}  ‖{HIGH_BLUE} Gouverne aerodynamique :{RESET} 67{MAGENTA}       ‖                           ‖{HIGH_BLUE} Gouverne aerodynamique :{RESET} 420{MAGENTA}      ‖ 
   {MAGENTA}  ‖{HIGH_BLUE} Plateforme gyroscopique:{RESET} 99{MAGENTA}       ‖                           ‖{HIGH_BLUE} Plateforme gyroscopique :{RESET} 192{MAGENTA}     ‖  
   {MAGENTA}  ‖                                   ‖                           ‖                                   ‖  
   {MAGENTA}   —————————————————————————————————                               —————————————————————————————————                
     
     """)

# ci-dessous l'animation des fusées

def star1():
    for i in range(20, -1, -1):
        clear()
        print("\n"*i)
        for line in starship1:
            print(line)
        time.sleep(0.1)

def star2():
    for i in range(20, -1, -1):
        clear()
        print("\n"*i)
        for line in starship2:
            print(line)
        time.sleep(0.1)
        
def star3():
    for i in range(20, -1, -1):
        clear()
        print("\n"*i)
        for line in starship3:
            print(line)
        time.sleep(0.1)

def star4():
    for i in range(20, -1, -1):
        clear()
        print("\n"*i)
        for line in starship4:
            print(line)
        time.sleep(0.1)

    
def credits():
    print("""
          Jeu python blabla bli blou""")
    
    
def game_over():
    clear()
    print("""
          Perdu ! Tapez 'retry' pour relancer une partie !
          """)
    

def win():
    clear()
    print("""
          Gagné ! Patientez pour accéder aux crédits et sources qui ont permis le développement du jeu.
          
          Une fois les crédits affichés, tapez 'home' si vous souhaitez retourner sur le manu principal.
          """)
    time.sleep(6)
    clear()
    credits()
    if user_input == 'menu':
        menu()

    

    
def conf1():
    print("Montage de la fusée en cours, veuillez patientez . . .")
    time.sleep(3)
    clear()
    star1()
    time.sleep(2)
    clear()
    game_over()
    # mettre un cls ici et un panneau GAME OVER! qui annonce l'explosion de la fusée, et la raison de l'explosion 
    # => mettre un message "ré-essayer ?" qui renvoie sur la fonction "y"

def conf2():
    print("La seconde configuration vous plaît ? Très bien, l'équipe technique se charge du montage !")
    time.sleep(3)
    clear()
    star2()
    time.sleep(2)
    clear()
    game_over()
    # mettre un cls ici et un panneau GAME OVER! qui annonce l'explosion de la fusée, et la raison de l'explosion 
    # => mettre un message "ré-essayer ?" qui renvoie sur la fonction "y"
    
def conf3():
    print("On m'a dit que la 3ème configuration vous faisait de l'oeil, mon équipe technique se charge de l'assemblage !")
    time.sleep(4)
    clear()
    star3()
    time.sleep(2)
    clear()
    game_over()
    # mettre un cls ici et un panneau GAME OVER! qui annonce l'explosion de la fusée, et la raison de l'explosion 
    # => mettre un message "ré-essayer ?" qui renvoie sur la fonction "y"

def conf4():
    print("La configuration 4, n'est-ce pas ? J'espère que votre instinct est bon !")
    time.sleep(5)
    clear()
    star4()
    time.sleep(2)
    clear()
    win()
    # mettre un cls ici et un panneau VICTOIRE! qui annonce que la fusée fonctionne correctement
    # => afficher les crédits (lien repo github, lien vers le schéma d'inspiration de la fusée)
    
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
    elif user_input == 'conf1':
        clear()
        conf1()
    elif user_input == 'conf2':
        clear()
        conf2()
    elif user_input == 'conf3':
        clear()
        conf3()
    elif user_input == 'conf4':
        clear()
        conf4()
    elif user_input == 'retry':
        clear()
        y()
    elif user_input == 'test':
        clear()
        star1()


# source schéma fusée :
# https://static.techno-science.net/illustration/Definitions/1200px/v/v-2-rocket-diagram-with-french-labels.svg_481431405adecddfbbb13033a0a3871a.png
