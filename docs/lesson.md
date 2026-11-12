# Python — Fiche de révision des fondamentaux

**École 42 — Python for Data Science / Python 0**

Cette fiche couvre les notions rencontrées dans les exercices `Hello.py`, `whatis.py`, `building.py`, `filterstring.py`, `ft_filter.py`, l'encodeur Morse, ainsi que les notions complémentaires étudiées.

---

# 1. Syntaxe et conventions Python

## 1.1 Indentation et blocs de code

Python utilise l'**indentation** (*indentation*) pour délimiter les blocs, contrairement aux accolades `{}` du C et de JavaScript.

```python
if True:
    print("Dans le bloc")
    print("Toujours dans le bloc")

print("Hors du bloc")
```

Convention **PEP 8** : quatre espaces par niveau d'indentation, plutôt que des tabulations.

## 1.2 Conventions de nommage (*naming conventions*)

| Élément | Convention | Exemple |
|---|---|---|
| Fonction | `snake_case` | `count_characters()` |
| Variable | `snake_case` | `word_count` |
| Méthode | `snake_case` | `get_name()` |
| Classe | `PascalCase` | `UserAccount` |
| Constante | `UPPER_SNAKE_CASE` | `MAX_SIZE` |
| Module | `snake_case` | `my_module.py` |

Le `camelCase` est valide mais déconseillé pour les nouvelles fonctions Python.

## 1.3 Commentaires et docstrings

Un commentaire commence par `#`.

```python
# Calculate the square
result = number ** 2
```

Une **docstring** (*documentation string*) documente une fonction, une classe ou un module. Elle se place au début de son corps.

```python
def divide(a: float, b: float) -> float:
    """
    Divide two numbers.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: Result of the division.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b
```

Conventions importantes :

- **PEP 257** : conventions relatives aux docstrings.
- **PEP 8** : conventions de style du code.
- `Args` : paramètres.
- `Returns` : valeur retournée.
- `Raises` : exceptions pouvant se propager à l'appelant.

On évite les sections `Args: None` ou `Returns: None` lorsqu'elles n'apportent aucune information.

### Consulter une docstring

```python
help(divide)
print(divide.__doc__)
```

`help()` fournit une documentation formatée avec la signature ; `__doc__` contient le texte brut de la docstring.

Pour une fonction native :

```bash
python3 -c "help(filter)"
```

## 1.4 Annotations de type (*type hints*)

Python permet d'annoter les paramètres et les valeurs de retour.

```python
def greet(name: str) -> str:
    return "Hello " + name

def main() -> None:
    print("Hello")
```

Les annotations ne sont **pas vérifiées automatiquement à l'exécution**.

```python
def double(x: int) -> int:
    return x * 2

double("Hi")  # "HiHi", malgré l'annotation int
```

Elles servent à la documentation, à l'autocomplétion et à l'analyse statique (*static type checking*).

## 1.5 Le point d'entrée d'un programme

```python
def main() -> None:
    print("Hello")

if __name__ == "__main__":
    main()
```

`__name__` est une variable spéciale définie par Python.

- Si le fichier est exécuté directement, `__name__ == "__main__"`.
- S'il est importé comme module, `__name__` correspond au nom du module.

Cette convention évite d'exécuter `main()` lors d'un import.

---

# 2. Types et valeurs fondamentales

## 2.1 Types natifs (*built-in types*)

```python
a = 42           # int
b = 3.14         # float
c = "Hello"      # str
d = True         # bool
e = None         # NoneType
```

Python est un langage à **typage dynamique** (*dynamic typing*) : les variables sont des noms liés à des objets, et non des emplacements de type fixé à la déclaration.

```python
value = 42
value = "Hello"  # Valide
```

## 2.2 `type()` et `isinstance()`

`type()` retourne le type exact d'un objet.

```python
type(42)          # <class 'int'>
type("Hello")     # <class 'str'>
```

`isinstance()` vérifie l'appartenance à une classe ou à ses sous-classes.

```python
isinstance(42, int)       # True
isinstance("42", int)     # False
isinstance(True, int)     # True
```

Particularité : `bool` est une sous-classe de `int`.

```python
type(True) is int         # False
isinstance(True, int)     # True
```

Pour tester plusieurs types :

```python
isinstance(value, (int, float))
```

On peut également utiliser `numbers.Number` pour tester une famille de types numériques.

## 2.3 `None`

`None` représente l'absence de valeur, proche de `null` en JavaScript.

```python
result = None

if result is None:
    print("No result")
```

On utilise de préférence `is None` plutôt que `== None`, car `None` est un **singleton** : il n'en existe qu'un seul objet.

## 2.4 NaN (*Not a Number*)

NaN représente une valeur numérique indéfinie dans les calculs à virgule flottante.

```python
import math

value = float("nan")

print(math.isnan(value))  # True
```

Attention :

```python
value == value  # False pour NaN
```

Il faut donc utiliser `math.isnan()` plutôt qu'une comparaison d'égalité.

## 2.5 Valeurs truthy et falsy

En Python, une condition ne nécessite pas forcément un booléen.

Une valeur est dite **truthy** lorsqu'elle est considérée comme vraie dans un contexte booléen ; **falsy** dans le cas contraire.

Valeurs falsy courantes :

```python
False
None
0
0.0
""
[]
()
{}
set()
```

Valeurs truthy :

```python
1
-5
"Hello"
[1, 2]
{"a": 1}
```

Exemple :

```python
if "Hello":
    print("Truthy")
```

`bool()` permet d'obtenir explicitement la valeur de vérité :

```python
bool(0)        # False
bool(42)       # True
bool("")       # False
bool("False")  # True
```

Attention : NaN est truthy.

## 2.6 Égalité et identité

- `==` : compare les valeurs (*equality*).
- `is` : compare l'identité des objets (*identity*).

```python
a = [1, 2]
b = [1, 2]

a == b  # True
a is b  # False
```

Ne pas confondre :

```python
value = 1

value == True  # True
value is True  # False
```

---

# 3. Les collections Python

## 3.1 `list` — Liste

Une liste est une séquence **ordonnée et mutable**.

```python
numbers = [10, 20, 30]

numbers[0] = 99
numbers.append(40)

print(numbers)  # [99, 20, 30, 40]
```

Caractéristiques :

- Indexation à partir de zéro.
- Doublons autorisés.
- Éléments de types différents autorisés.
- Taille dynamique.

Par rapport au C, une liste Python est davantage comparable à un tableau dynamique de références vers des objets qu'à un tableau contigu d'entiers.

## 3.2 `tuple` — N-uplet

Un tuple est une séquence **ordonnée et immutable**.

```python
coordinates = (10, 20)

print(coordinates[0])  # 10
```

Un tuple ne permet pas de réaffecter directement ses éléments.

```python
coordinates[0] = 5  # TypeError
```

Tuple à un élément :

```python
single = (42,)
```

La virgule est indispensable pour distinguer le tuple de `(42)`, qui est simplement l'entier `42`.

Un tuple est immutable, mais peut contenir un objet mutable :

```python
data = ([1, 2], 3)
data[0].append(4)  # Autorisé
```

## 3.3 `set` — Ensemble

Un set est une collection **non ordonnée**, sans doublons, fondée sur le hachage (*hashing*).

```python
numbers = {1, 2, 2, 3}

print(numbers)  # Contient 1, 2 et 3
```

Il permet notamment des tests d'appartenance efficaces.

```python
3 in numbers  # True
```

Créer un ensemble vide :

```python
empty_set = set()
```

Attention :

```python
empty = {}  # Dictionnaire, pas set
```

Les éléments d'un set doivent être **hashables**.

## 3.4 `dict` — Dictionnaire

Un dictionnaire est une structure de correspondance **clé-valeur** (*mapping*), reposant sur une table de hachage (*hash table*).

```python
person = {
    "name": "Alice",
    "age": 25
}
```

Accès direct :

```python
person["name"]  # "Alice"
```

Si la clé n'existe pas, une `KeyError` est levée.

Accès avec valeur par défaut :

```python
person.get("city")           # None
person.get("city", "Paris")  # "Paris"
```

Vérification de présence :

```python
if "name" in person:
    print(person["name"])
```

Modification :

```python
person["age"] = 26
```

Les dictionnaires préservent l'ordre d'insertion dans les versions modernes de Python.

## 3.5 Comparaison des collections

| Structure | Ordonnée | Mutable | Doublons |
|---|---|---|---|
| `list` | Oui | Oui | Oui |
| `tuple` | Oui | Non | Oui |
| `set` | Non | Oui | Non |
| `dict` | Ordre d'insertion | Oui | Clés uniques |

Dans un dictionnaire, les valeurs peuvent être dupliquées, mais pas les clés.

---

# 4. Chaînes de caractères (*strings*)

## 4.1 Immutabilité

Les chaînes Python sont **immutables**.

```python
text = "Hello"
text = text + " World"
```

La concaténation crée une nouvelle chaîne : elle ne modifie pas l'objet initial.

## 4.2 Indexation et slicing

Le **slicing** permet d'extraire une sous-séquence.

Syntaxe :

```python
sequence[start:stop:step]
```

`stop` est exclu.

```python
text = "Python"

text[0]    # "P"
text[-1]   # "n"
text[:3]   # "Pyt"
text[2:]   # "thon"
text[:-1]  # "Pyth"
text[-2:]  # "on"
text[::-1] # "nohtyP"
```

Sur une chaîne vide :

```python
""[:-1]  # ""
```

Contrairement à l'indexation directe, un slicing hors limites ne provoque généralement pas d'erreur.

## 4.3 Longueur avec `len()`

```python
len("Hello")  # 5
len("")       # 0
```

`len()` fonctionne également avec les listes, tuples, dictionnaires et ensembles.

## 4.4 Méthodes de classification des caractères

| Méthode | Signification |
|---|---|
| `.isalpha()` | Lettres uniquement |
| `.isdigit()` | Chiffres |
| `.isalnum()` | Lettres ou chiffres |
| `.isspace()` | Espaces blancs |
| `.isupper()` | Majuscules |
| `.islower()` | Minuscules |
| `.isprintable()` | Caractères imprimables |

Exemples :

```python
"Hello".isalpha()       # True
"Hello42".isalnum()     # True
"Hello World".isalnum() # False
"123".isdigit()         # True
"\n".isspace()          # True
"\t".isprintable()      # False
```

Ces méthodes sont compatibles avec Unicode.

```python
"école".isalpha()  # True
```

Pour tester une chaîne vide :

```python
"".isalnum()  # False
```

## 4.5 Espaces et caractères invisibles

`.isspace()` reconnaît notamment :

```python
" "   # Espace
"\t"  # Tabulation
"\n"  # Retour à la ligne
```

Si l'on souhaite autoriser uniquement les espaces classiques :

```python
char == " "
```

Cela exclut les tabulations et retours à la ligne.

## 4.6 Majuscules et minuscules

```python
"Hello".upper()  # "HELLO"
"HELLO".lower()  # "hello"
```

Ces méthodes sont utiles pour normaliser des clés de dictionnaire, notamment dans un encodeur Morse.

```python
code = NESTED_MORSE.get(char.upper())
```

Le Morse ne distingue pas majuscules et minuscules.

## 4.7 Ponctuation

Le module `string` fournit une constante contenant les signes de ponctuation ASCII.

```python
import string

"!" in string.punctuation  # True
"A" in string.punctuation  # False
```

Attention : cette constante ne contient pas toute la ponctuation Unicode.

## 4.8 `split()` — Découpage

```python
text = "Hello wonderful world"

words = text.split()

# ["Hello", "wonderful", "world"]
```

Sans argument, `.split()` découpe sur les séquences d'espaces blancs.

Avec un séparateur :

```python
"a,b,c".split(",")  # ["a", "b", "c"]
```

## 4.9 `join()` — Assemblage

`join()` est une méthode de `str`, et non de `list`.

```python
words = ["Hello", "World"]

" ".join(words)  # "Hello World"
"".join(words)   # "HelloWorld"
"-".join(words)  # "Hello-World"
```

Les éléments doivent être des chaînes.

```python
" ".join(["A", 42])  # TypeError
```

Pour une conversion Morse, `join()` évite souvent les concaténations répétées.

## 4.10 `strip()`, `rstrip()` et `lstrip()`

```python
"  Hello  ".strip()   # "Hello"
"Hello  ".rstrip()    # "Hello"
"  Hello".lstrip()    # "Hello"
```

Par défaut, elles retirent les espaces blancs.

Différence :

```python
text[:-1]     # Retire exactement un caractère
text.rstrip() # Retire tous les espaces blancs finaux
```

## 4.11 Chaînes multilignes et f-strings

Les triples guillemets permettent les chaînes multilignes.

```python
text = """First line
Second line"""
```

Une **f-string** (*formatted string literal*) permet d'intégrer des expressions.

```python
name = "Alice"
age = 25

print(f"{name} is {age} years old")
```

Une f-string peut être multiligne :

```python
result = f"""Name: {name}
Age: {age}"""
```

Attention : les retours à la ligne font partie de la chaîne.

---

# 5. Fonctions Python

## 5.1 Définition avec `def`

```python
def add(a: int, b: int) -> int:
    return a + b
```

`def` crée un objet fonction et lui associe un nom.

Les fonctions Python sont des **objets de première classe** (*first-class objects*) : elles peuvent être stockées dans des variables, passées en argument et retournées par d'autres fonctions.

## 5.2 `return`

`return` termine l'exécution de la fonction et renvoie une valeur.

```python
def square(x):
    return x * x
```

Une fonction sans `return` explicite retourne `None`.

```python
def greet():
    print("Hello")

print(greet())  # Affiche Hello puis None
```

## 5.3 Paramètres et arguments

Les **paramètres** (*parameters*) sont définis dans la signature.

Les **arguments** (*arguments*) sont les valeurs transmises lors de l'appel.

```python
def greet(name):  # name = paramètre
    print(name)

greet("Alice")    # "Alice" = argument
```

Python vérifie automatiquement le nombre d'arguments obligatoires.

```python
greet()  # TypeError
```

## 5.4 Portée des variables (*scope*)

Python utilise la règle **LEGB** pour résoudre les noms :

1. **Local** : portée de la fonction.
2. **Enclosing** : fonctions englobantes.
3. **Global** : module.
4. **Built-in** : noms intégrés au langage.

```python
value = 10

def show():
    value = 20
    print(value)  # 20

show()
print(value)      # 10
```

Contrairement à C ou à JavaScript avec `let`, les blocs `if`, `for`, `while` et `try` ne créent pas une nouvelle portée locale.

```python
if True:
    x = 42

print(x)  # 42
```

## 5.5 `global` et `nonlocal`

`global` permet de réaffecter un nom au niveau du module.

```python
count = 0

def increment():
    global count
    count += 1
```

`nonlocal` permet de réaffecter un nom défini dans une fonction englobante.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    return count
```

Modifier le contenu d'un objet mutable ne nécessite pas forcément `global`.

```python
items = []

def add_item():
    items.append(42)
```

---

# 6. Arguments de ligne de commande et entrées

## 6.1 `sys.argv`

Le module `sys` donne accès aux arguments de ligne de commande.

```python
import sys

print(sys.argv)
```

Commande :

```bash
python3 script.py Hello 42
```

Valeur :

```python
["script.py", "Hello", "42"]
```

Important : **tous les éléments de `sys.argv` sont des chaînes**.

`sys.argv[0]` représente le chemin ou nom utilisé pour lancer le script.

## 6.2 Vérifier le nombre d'arguments

```python
assert len(sys.argv) == 3, "Bad arguments"
```

L'accès à `sys.argv[2]` sans vérifier la longueur peut provoquer une `IndexError`.

## 6.3 Conversion avec `int()`

```python
number = int("42")  # 42
```

Conversion invalide :

```python
int("Hello")  # ValueError
```

On utilise donc généralement `try/except` pour les arguments numériques.

## 6.4 `input()` et `sys.stdin.readline()`

```python
text = input("Enter text: ")
```

`input()` retourne une chaîne sans le retour à la ligne final.

```python
text = sys.stdin.readline()
```

`readline()` conserve le `\n` final s'il est présent.

Exemple :

```python
len("Hello")    # 5
len("Hello\n")  # 6
```

Cette différence est importante pour un programme qui compte les caractères.

## 6.5 Valeur de retour de `append()`

`list.append()` modifie la liste en place et retourne `None`.

```python
items = []
result = items.append(42)

print(items)   # [42]
print(result)  # None
```

Il ne faut donc pas écrire :

```python
text = sys.argv.append("Hello")
```

en espérant récupérer la liste modifiée.

---

# 7. Conditions et expressions booléennes

## 7.1 `if`, `elif`, `else`

```python
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

## 7.2 Opérateurs logiques

```python
a and b
a or b
not a
```

Les opérateurs `and` et `or` effectuent une **évaluation court-circuitée** (*short-circuit evaluation*).

```python
value = None

if value is not None and value > 0:
    print("Positive")
```

La seconde condition n'est pas évaluée si la première est fausse.

Autre subtilité : `and` et `or` ne retournent pas forcément des booléens.

```python
0 or 42        # 42
"Hello" and 5  # 5
```

## 7.3 Expression conditionnelle (*ternary expression*)

Python utilise :

```python
result = value_if_true if condition else value_if_false
```

Exemple :

```python
parity = "Even" if number % 2 == 0 else "Odd"
```

Équivalent conceptuel du `condition ? a : b` en JavaScript et en C.

## 7.4 Incrémentation

Python ne possède pas les opérateurs `++` et `--`.

```python
count += 1
count -= 1
```

---

# 8. Exceptions et gestion des erreurs

## 8.1 Principe

Une **exception** (*exception*) interrompt le flux normal d'exécution lorsqu'une erreur survient.

Exemples :

| Exception | Situation |
|---|---|
| `TypeError` | Type ou appel incorrect |
| `ValueError` | Valeur invalide |
| `IndexError` | Indice hors limites |
| `KeyError` | Clé absente |
| `AssertionError` | Assertion échouée |
| `StopIteration` | Itérateur épuisé |
| `ZeroDivisionError` | Division par zéro |
| `UnboundLocalError` | Variable locale utilisée avant affectation |

## 8.2 `try` / `except`

```python
try:
    number = int(text)
except ValueError:
    print("Invalid number")
```

Équivalent conceptuel du `try/catch` JavaScript.

## 8.3 Intercepter plusieurs exceptions

```python
try:
    ...
except (ValueError, AssertionError) as error:
    print(error)
```

On peut aussi utiliser plusieurs clauses `except` pour différencier les traitements.

## 8.4 `raise`

`raise` permet de lever explicitement une exception.

```python
raise AssertionError("Bad arguments")
```

On peut convertir une exception :

```python
try:
    number = int(text)
except ValueError:
    raise AssertionError("Bad arguments") from None
```

`from None` supprime l'affichage du contexte de l'exception précédente, mais pas la traceback de la nouvelle exception.

## 8.5 `assert`

Syntaxe :

```python
assert condition, message
```

Équivalent approximatif :

```python
if not condition:
    raise AssertionError(message)
```

Exemple :

```python
assert len(sys.argv) == 3, "Bad arguments"
```

Attention : les assertions peuvent être désactivées avec `python -O`.

En production, il ne faut donc pas s'appuyer sur `assert` pour valider les entrées utilisateur.

## 8.6 Lever ou afficher une erreur

Ces deux opérations sont différentes :

```python
raise AssertionError("Bad arguments")
```

et :

```python
print("AssertionError: Bad arguments")
```

La première lève une véritable exception.

La seconde affiche simplement du texte.

Pour reproduire fidèlement le comportement d'une fonction, il faut distinguer les deux.

## 8.7 Portée d'un bloc `try`

```python
assert len(sys.argv) == 3

try:
    ...
except AssertionError:
    ...
```

L'assertion située avant `try` ne sera pas interceptée par ce bloc.

Il faut placer dans le `try` les instructions dont on souhaite intercepter les exceptions.

---

# 9. Boucles et parcours

## 9.1 Boucle `for`

```python
for char in "Hello":
    print(char)
```

La boucle `for` parcourt un **itérable** (*iterable*).

## 9.2 `range()`

```python
for i in range(5):
    print(i)
```

Produit les valeurs de 0 à 4.

```python
range(2, 10, 2)
```

Produit successivement 2, 4, 6 et 8.

`range()` n'est pas une liste ; c'est un objet itérable spécialisé.

## 9.3 `enumerate()`

`enumerate()` fournit simultanément un indice et une valeur.

```python
for index, char in enumerate("ABC"):
    print(index, char)
```

Résultat :

```text
0 A
1 B
2 C
```

## 9.4 `break`

`break` interrompt immédiatement une boucle.

```python
for n in range(10):
    if n == 5:
        break
```

## 9.5 `continue`

`continue` passe directement à l'itération suivante.

```python
for n in range(5):
    if n == 2:
        continue
    print(n)
```

---

# 10. List comprehensions

## 10.1 Définition

Une **compréhension de liste** (*list comprehension*) construit une nouvelle liste à partir d'un itérable.

Syntaxe :

```python
[expression for element in iterable]
```

Exemple :

```python
squares = [n ** 2 for n in range(5)]
# [0, 1, 4, 9, 16]
```

Équivalent avec une boucle :

```python
squares = []

for n in range(5):
    squares.append(n ** 2)
```

## 10.2 Filtrage avec `if`

```python
numbers = [1, 2, 3, 4, 5]

evens = [n for n in numbers if n % 2 == 0]
# [2, 4]
```

## 10.3 Transformation et filtrage

```python
squares = [n ** 2 for n in range(10) if n % 2 == 0]
```

La condition sélectionne les éléments, puis l'expression produit les valeurs de la nouvelle liste.

## 10.4 Application à `filterstring.py`

```python
text = "Hello the wonderful world"
number = 4

result = [
    word for word in text.split()
    if len(word) > number
]

# ["Hello", "wonderful", "world"]
```

## 10.5 Portée de la variable

Une list comprehension possède sa propre portée pour sa variable d'itération.

```python
x = 10

values = [x for x in range(3)]

print(x)  # 10
```

C'est différent d'une boucle `for` classique.

---

# 11. Fonctions lambda

## 11.1 Définition

Une **lambda** (*lambda expression / anonymous function*) permet de créer une fonction anonyme.

Syntaxe :

```python
lambda parameters: expression
```

Exemple :

```python
lambda x: x * 2
```

Elle peut recevoir plusieurs paramètres :

```python
lambda a, b: a + b
```

## 11.2 Comparaison avec `def`

```python
def double(x):
    return x * 2
```

Une lambda équivalente :

```python
lambda x: x * 2
```

Une lambda est limitée à une expression, dont le résultat est retourné implicitement.

Elle ne permet pas d'écrire directement une suite d'instructions comme une fonction `def`.

## 11.3 Une lambda n'est pas nécessairement imbriquée

Une fonction définie dans une autre fonction est une **fonction imbriquée** (*nested function*).

```python
def outer():
    def inner():
        return 42
    return inner()
```

Une lambda est simplement une autre syntaxe pour créer une fonction.

Elle peut être utilisée dans une fonction ou au niveau du module.

## 11.4 Usage avec `sort()`

```python
people = [("Alice", 25), ("Bob", 18)]

people.sort(key=lambda person: person[1])
```

La lambda retourne la clé de tri pour chaque élément.

## 11.5 Flake8 E731

Flake8 déconseille d'affecter directement une lambda à une variable.

Déconseillé :

```python
double = lambda x: x * 2
```

Préféré :

```python
def double(x):
    return x * 2
```

La règle **E731** recommande `def` lorsqu'une fonction possède un nom.

Les lambdas sont surtout utiles lorsqu'elles sont passées directement à une autre fonction.

---

# 12. `all()` et `any()`

## 12.1 `all()`

`all()` retourne `True` si tous les éléments de l'itérable sont truthy.

```python
all([True, True, True])   # True
all([True, False, True])  # False
```

Elle s'arrête dès qu'un élément est falsy.

Sur un itérable vide :

```python
all([])  # True
```

## 12.2 `any()`

`any()` retourne `True` si au moins un élément est truthy.

```python
any([False, True, False])  # True
any([False, False])        # False
any([])                    # False
```

Elle s'arrête dès qu'un élément est truthy.

## 12.3 Validation des caractères

```python
valid = all(
    char.isalnum() or char == " "
    for char in text
)
```

Cette expression vérifie que chaque caractère est une lettre, un chiffre ou un espace classique.

Elle combine `all()` et une **expression génératrice** (*generator expression*).

---

# 13. Generator expressions

## 13.1 Définition

Une expression génératrice produit des valeurs **à la demande** (*lazy evaluation*), sans construire immédiatement une liste.

```python
generator = (n * n for n in range(5))
```

Comparaison :

```python
[n * n for n in range(5)]  # Liste
(n * n for n in range(5))  # Générateur
```

## 13.2 Avec une fonction

Lorsque l'expression génératrice est l'unique argument d'une fonction, les parenthèses supplémentaires sont facultatives.

```python
all(n > 0 for n in numbers)
```

Équivalent :

```python
all((n > 0 for n in numbers))
```

## 13.3 Évaluation paresseuse

Une liste calcule et stocke immédiatement ses éléments.

Un générateur calcule ses éléments au fur et à mesure de leur consommation.

Cela peut réduire considérablement l'utilisation de mémoire.

---

# 14. Itérables et itérateurs

## 14.1 Iterable — Objet itérable

Un **itérable** (*iterable*) est un objet capable de fournir un itérateur.

Exemples :

```python
[1, 2, 3]     # list
(1, 2, 3)     # tuple
"Hello"       # str
range(10)     # range
```

## 14.2 Iterator — Itérateur

Un **itérateur** (*iterator*) est un objet qui fournit les éléments successivement et conserve sa position de parcours.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

next(iterator)  # 10
next(iterator)  # 20
next(iterator)  # 30
```

L'appel suivant lève `StopIteration`.

## 14.3 `iter()`

`iter()` demande un itérateur à un objet itérable.

```python
iterator = iter([1, 2, 3])
```

## 14.4 `next()`

`next()` demande la prochaine valeur.

```python
next(iterator)
```

Lorsqu'il n'y a plus de valeur, l'itérateur lève `StopIteration`.

On peut fournir une valeur par défaut :

```python
next(iterator, None)
```

Dans ce cas, `None` est retourné à l'épuisement au lieu de lever l'exception.

## 14.5 Comment fonctionne `for` ?

Une boucle `for` utilise implicitement le protocole d'itération.

```python
for item in numbers:
    print(item)
```

Fonctionnement conceptuel :

```python
iterator = iter(numbers)

while True:
    try:
        item = next(iterator)
    except StopIteration:
        break

    print(item)
```

## 14.6 Protocole d'itération (*iterator protocol*)

Un itérateur implémente deux méthodes spéciales :

- `__iter__()` : retourne l'itérateur.
- `__next__()` : produit la valeur suivante ou lève `StopIteration`.

Exemple :

```python
class Counter:
    def __init__(self, maximum):
        self.current = 0
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.maximum:
            raise StopIteration

        self.current += 1
        return self.current
```

Utilisation :

```python
for n in Counter(3):
    print(n)
```

## 14.7 Consommation d'un itérateur

Un itérateur conserve sa position et est généralement consommable une seule fois.

```python
iterator = iter([1, 2, 3])

print(list(iterator))  # [1, 2, 3]
print(list(iterator))  # []
```

La liste d'origine reste disponible, mais cet itérateur est épuisé.

---

# 15. `yield` et les générateurs

## 15.1 `yield` vs `return`

`return` termine une fonction.

`yield` produit une valeur et suspend son exécution.

```python
def counter():
    yield 1
    yield 2
    yield 3
```

## 15.2 Fonction génératrice (*generator function*)

Une fonction contenant `yield` est une fonction génératrice.

Son appel retourne un objet générateur (*generator object*).

```python
gen = counter()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

Le corps de la fonction n'est pas exécuté lors de la création du générateur, mais lors de son itération.

## 15.3 Suspension et reprise

```python
def example():
    print("Start")
    yield 10

    print("Continue")
    yield 20
```

```python
gen = example()

next(gen)  # Affiche Start, retourne 10
next(gen)  # Affiche Continue, retourne 20
```

Python conserve l'état local et la position d'exécution entre deux `yield`.

## 15.4 Avantage mémoire

Avec une liste :

```python
numbers = [n for n in range(1_000_000)]
```

Tous les éléments sont construits.

Avec un générateur :

```python
numbers = (n for n in range(1_000_000))
```

Les éléments sont produits à la demande.

## 15.5 Épuisement

```python
gen = (n for n in range(3))

print(list(gen))  # [0, 1, 2]
print(list(gen))  # []
```

Un générateur épuisé ne redémarre pas automatiquement.

---

# 16. `filter()` et `ft_filter()`

## 16.1 Fonction native `filter()`

Signature :

```python
filter(function, iterable)
```

Elle retourne un **itérateur** contenant les éléments pour lesquels `function(item)` est truthy.

```python
numbers = [1, 2, 3, 4, 5]

result = filter(lambda n: n % 2 == 0, numbers)

print(list(result))  # [2, 4]
```

## 16.2 `filter(None, iterable)`

Lorsque `function` vaut `None`, `filter()` conserve tous les éléments truthy.

```python
values = [False, "Hello", True, 0, 3]

print(list(filter(None, values)))
# ['Hello', True, 3]
```

Il ne faut pas confondre :

```python
value is True
```

avec :

```python
bool(value)
```

Par exemple, `3` est truthy mais `3 is True` est faux.

## 16.3 Réimplémentation avec `yield`

```python
def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        function = bool

    for item in iterable:
        if function(item):
            yield item
```

Cette version reproduit le comportement de filtrage et retourne un générateur.

## 16.4 Consommer le résultat

Avec `list()` :

```python
result = list(ft_filter(None, values))
```

Avec une boucle :

```python
for item in ft_filter(None, values):
    print(item)
```

Attention :

```python
print(ft_filter(None, values))
```

affiche une représentation de l'objet générateur, et non les valeurs produites.

## 16.5 `filter()` vs list comprehension

```python
result = list(filter(lambda x: x > 2, numbers))
```

Équivalent :

```python
result = [x for x in numbers if x > 2]
```

La différence principale :

- `filter()` retourne un itérateur.
- Une list comprehension construit immédiatement une liste.

## 16.6 Évaluation des erreurs

La fonction native `filter()` vérifie certains arguments dès l'appel.

Une fonction génératrice avec `yield` exécute son corps seulement au moment de l'itération.

```python
gen = ft_filter(None, 42)  # Création possible

next(gen)  # TypeError
```

Ce comportement est une conséquence de l'exécution différée (*lazy execution*).

---

# 17. Validation des entrées

## 17.1 Vérifier une chaîne alphanumérique

```python
text.isalnum()
```

Cette méthode retourne `False` si la chaîne contient des espaces.

## 17.2 Autoriser les espaces

```python
all(char.isalnum() or char == " " for char in text)
```

Cela rejette la ponctuation et les caractères invisibles.

La vérification `.isprintable()` est alors généralement redondante.

## 17.3 Conversion numérique

```python
try:
    number = int(sys.argv[2])
except ValueError:
    raise AssertionError("Bad arguments") from None
```

`int()` valide implicitement la possibilité de conversion.

## 17.4 Validation de plusieurs conditions

```python
assert len(sys.argv) == 3, ARG_ERROR

text = sys.argv[1]

assert all(
    char.isalnum() or char == " "
    for char in text
), ARG_ERROR
```

L'ordre des vérifications est important : on vérifie la présence des arguments avant de les utiliser.

---

# 18. Exemple complet : encodeur Morse

## 18.1 Dictionnaire de correspondance

```python
MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    " ": "/",
}
```

Chaque caractère est une clé, et son code Morse est la valeur associée.

## 18.2 Recherche et validation

```python
def text_to_morse(text: str) -> str:
    codes = []

    for char in text.upper():
        code = MORSE.get(char)

        if code is None:
            raise AssertionError("Unsupported character")

        codes.append(code)

    return " ".join(codes)
```

Cette fonction mobilise plusieurs notions :

- `dict` et recherche par clé.
- `.get()` et `None`.
- `.upper()` pour normaliser.
- `for` pour parcourir une chaîne.
- `raise` pour les caractères invalides.
- `.append()` pour construire une liste.
- `.join()` pour construire la chaîne finale.

## 18.3 Pourquoi une liste plutôt que `+=` ?

Cette approche :

```python
result = ""

for code in codes:
    result += code
```

effectue des concaténations successives de chaînes immutables.

Pour de nombreuses opérations, accumuler les morceaux dans une liste puis appeler `join()` est généralement plus efficace.

---

# 19. Outils de qualité du code

## 19.1 PEP 8

La **PEP 8** définit les principales conventions de style Python :

- Indentation de quatre espaces.
- Fonctions et variables en `snake_case`.
- Classes en `PascalCase`.
- Constantes en majuscules.
- Deux lignes vides entre les fonctions de premier niveau.
- Espaces autour des opérateurs.

## 19.2 PEP 257

La **PEP 257** décrit les conventions des docstrings.

Exemple :

```python
def main() -> None:
    """
    Validate command-line arguments.

    Print the filtered result.
    """
```

## 19.3 Flake8 — Linter

Un **linter** analyse statiquement le code pour signaler des problèmes de style et certaines erreurs potentielles.

Commande :

```bash
flake8 filterstring.py
```

Flake8 regroupe notamment des vérifications issues de `pycodestyle` et `Pyflakes`.

Exemple de règle :

```text
E731: do not assign a lambda expression, use a def
```

Le Flake8 standard ne vérifie pas toutes les conventions de docstrings. Des extensions comme `flake8-docstrings` peuvent ajouter ces contrôles.

## 19.4 `pip` et `pipx`

- `pip` : gestionnaire de paquets Python.
- `pipx` : installe des applications Python dans des environnements isolés, tout en exposant leurs commandes.

Exemple :

```bash
pipx install flake8
```

Sur Ubuntu récent, `pipx` peut éviter les restrictions d'installation dans l'environnement Python système (PEP 668).

---

# 20. Comparaison rapide avec C et JavaScript

| Concept | Python | JavaScript | C |
|---|---|---|---|
| Fonction | `def f():` | `function f() {}` | `void f(void) {}` |
| Fonction anonyme | `lambda x: x * 2` | `x => x * 2` | Pas d'équivalent standard direct |
| Liste dynamique | `list` | `Array` | Allocation manuelle / bibliothèque |
| Dictionnaire | `dict` | `Map` / objet | Table de hachage à implémenter ou bibliothèque |
| Ensemble | `set` | `Set` | Bibliothèque / implémentation |
| Valeur absente | `None` | `null` / `undefined` | `NULL` pour un pointeur |
| Test de type | `isinstance()` | `typeof` / `instanceof` | Types statiques |
| Exception | `try/except` | `try/catch` | Gestion par codes de retour, etc. |
| Transformation | List comprehension | `.map()` | Boucle |
| Filtrage | `filter()` / comprehension | `.filter()` | Boucle |
| Tous vrais | `all()` | `.every()` | Boucle |
| Au moins un vrai | `any()` | `.some()` | Boucle |
| Itération | `for ... in` | `for ... of` | Boucle / itérateur personnalisé |
| Générateur | `yield` | `function*` / `yield` | Pas d'équivalent natif |
| Longueur | `len(x)` | `x.length` | Selon le type |
| Conversion entière | `int(x)` | `Number()` / `parseInt()` | `strtol()`, etc. |

---

# 21. Les distinctions essentielles à mémoriser

| Notions | Différence fondamentale |
|---|---|
| `==` / `is` | Égalité de valeur / identité d'objet |
| `True` / truthy | Booléen exact / valeur considérée vraie |
| `None` / `False` | Absence de valeur / booléen faux |
| `type()` / `isinstance()` | Type exact / appartenance avec héritage |
| `list` / `tuple` | Mutable / immutable |
| `set` / `dict` | Ensemble de valeurs / correspondance clé-valeur |
| `[]` / `.get()` | Accès avec `KeyError` / accès avec défaut |
| `return` / `yield` | Terminaison / suspension |
| Iterable / iterator | Fournit un parcours / conserve l'état du parcours |
| Iterator / generator | Protocole général / implémentation particulière |
| List comprehension / generator expression | Liste immédiate / production différée |
| `def` / `lambda` | Définition nommée / expression fonctionnelle |
| `all()` / `any()` | Toutes les valeurs / au moins une valeur |
| `filter()` / list comprehension | Itérateur / liste |
| `print()` / `raise` | Affichage / déclenchement d'exception |
| `assert` / `if ... raise` | Assertion désactivable / validation explicite |
| `input()` / `readline()` | Retire le `\n` / le conserve |
| `[:-1]` / `.rstrip()` | Retire un caractère / retire les blancs finaux |
| `append()` / `join()` | Ajoute à une liste / assemble des chaînes |

---

# 22. Exercices pratiques de révision

## Exercice A — Collections

Créer une liste contenant des nombres, éliminer les doublons avec un `set`, puis construire un dictionnaire associant chaque nombre à son carré.

Notions : `list`, `set`, `dict`, compréhension de dictionnaire.

## Exercice B — Validation

Écrire une fonction qui vérifie qu'une chaîne contient uniquement des lettres, chiffres et espaces classiques.

Notions : `str`, `.isalnum()`, `all()`, generator expression.

## Exercice C — Filtrage

Extraire les mots d'une chaîne dont la longueur est strictement supérieure à un entier donné.

Notions : `.split()`, `len()`, list comprehension.

## Exercice D — Générateur

Créer un générateur qui produit tous les nombres pairs jusqu'à une limite.

```python
def even_numbers(limit):
    for n in range(limit):
        if n % 2 == 0:
            yield n
```

Notions : `yield`, iterator, lazy evaluation.

## Exercice E — Réimplémenter `filter()`

Créer une fonction qui reçoit un prédicat et un itérable, puis produit les éléments pour lesquels le prédicat est truthy.

Notions : fonction de première classe, `bool`, `yield`, protocole d'itération.

## Exercice F — Tester les erreurs

Comparer les comportements de :

```python
int("abc")
```

```python
raise AssertionError("Bad arguments")
```

```python
assert False, "Bad arguments"
```

Notions : exceptions, `raise`, `assert`, `try/except`.

---

# 23. Glossaire technique

| Terme anglais | Terme français | Définition |
|---|---|---|
| Built-in | Natif / intégré | Fourni directement par Python |
| Mutable | Mutable | Objet modifiable après création |
| Immutable | Immutable | Objet non modifiable après création |
| Hashable | Hachable | Objet possédant un hachage compatible avec l'égalité |
| Mapping | Correspondance | Structure associant clés et valeurs |
| Hash table | Table de hachage | Structure permettant une recherche par clé efficace |
| Iterable | Itérable | Objet capable de fournir un itérateur |
| Iterator | Itérateur | Objet produisant les éléments successivement |
| Generator | Générateur | Itérateur produit par une fonction génératrice ou une expression génératrice |
| Lazy evaluation | Évaluation paresseuse | Calcul effectué seulement lorsqu'il est nécessaire |
| Eager evaluation | Évaluation immédiate | Calcul effectué immédiatement |
| Generator expression | Expression génératrice | Expression produisant un générateur |
| List comprehension | Compréhension de liste | Expression construisant une liste |
| Lambda expression | Expression lambda | Expression créant une fonction anonyme |
| Predicate | Prédicat | Fonction utilisée pour tester une condition |
| Callback | Fonction de rappel | Fonction transmise à une autre fonction pour être appelée |
| First-class function | Fonction de première classe | Fonction manipulable comme une valeur |
| Scope | Portée | Zone dans laquelle un nom est accessible |
| Namespace | Espace de noms | Association entre noms et objets |
| Truthy / falsy | Vrai / faux en contexte booléen | Valeur de vérité implicite |
| Short-circuit evaluation | Évaluation court-circuitée | Arrêt anticipé d'une expression logique |
| Exception | Exception | Signalement d'une situation anormale |
| Traceback | Trace d'appels | Historique des appels ayant conduit à une exception |
| Docstring | Chaîne de documentation | Documentation intégrée à un objet Python |
| Type hint | Annotation de type | Indication du type attendu |
| Linter | Analyseur statique de style | Outil signalant certaines erreurs et violations de conventions |
| Slicing | Découpage | Extraction d'une sous-séquence |
| Unicode | Unicode | Standard de représentation des caractères |
| ASCII | ASCII | Jeu de caractères historique à 7 bits |
| Iterator protocol | Protocole d'itération | Contrat fondé sur `__iter__()` et `__next__()` |

---

**Synthèse :** les notions centrales de ces premiers exercices sont la manipulation des objets et collections Python, les fonctions, la validation des données, les expressions compréhensives, les fonctions de première classe et surtout le modèle d'itération (`iter`, `next`, `yield`). Ces mécanismes constituent une base essentielle pour la suite de Python for Data Science.