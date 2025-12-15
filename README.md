# Rule-Based Chatbot (Python + NLTK)

## 📌 Description
Ce projet présente un **chatbot basé sur des règles (Rule-Based Chatbot)** implémenté en **Python** à l’aide de la bibliothèque **NLTK**.  
Le chatbot analyse les messages de l’utilisateur, détecte des **mots-clés**, identifie l’**intention (intent)** correspondante, puis retourne une **réponse prédéfinie**.  
Ce type de chatbot est simple, rapide et efficace pour des cas bien définis comme les **FAQ** ou le **support basique**.

---

## ⚙️ Principe de fonctionnement
Le chatbot fonctionne en **trois étapes principales** :

### 1️⃣ Définition des intents et des réponses
- Un **intent** représente l’objectif de la question de l’utilisateur (salutation, horaires, prix, etc.).
- Chaque intent est associé à une liste de **mots-clés**.
- Une **réponse fixe** est définie pour chaque intent.

**Exemple** :
- Intent : `opening_hours`  
- Mots-clés : `open`, `opening`, `hours`  
- Réponse : *We are open from 9 AM to 6 PM, Monday to Friday.*

---

### 2️⃣ Analyse du message utilisateur
- Le message est converti en minuscules.
- Il est découpé en mots (**tokenization**) à l’aide de `word_tokenize` de NLTK.
- Le chatbot vérifie si l’un des mots-clés correspond à un intent.

---

### 3️⃣ Génération de la réponse
- Si un intent est reconnu → le chatbot renvoie la réponse associée.
- Si aucun intent ne correspond → une réponse par défaut est affichée.

---

## 🧠 Structure du code

### Définition des intents
```python
intents = {
    "greeting": ["hello", "hi", "hey"],
    "opening_hours": ["open", "opening", "hours"],
    "pricing": ["price", "cost", "how much"]
}


### Définition des réponses
```python
responses = {
    "greeting": "Hello! How can I help you today?",
    "opening_hours": "We are open from 9 AM to 6 PM, Monday to Friday.",
    "pricing": "Our pricing starts at $10 per month.",
    "default": "Sorry, I didn't understand that. Can you please rephrase?"
}