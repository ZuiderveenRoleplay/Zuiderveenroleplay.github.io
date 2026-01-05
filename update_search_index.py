import json
import re

# Lees de search_index.json
with open('search/search_index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Mapping van oude naar nieuwe artikelnummers
# Format: (oude_pattern, nieuwe_nummer)
replacements = [
    # Artikel 18-27 blijven hetzelfde
    # Artikel 27.1 -> 28
    (r'Artikel 27\.1', 'Artikel 28'),
    (r'artikel-271', 'artikel-28'),
    # Artikel 28 -> 29
    (r'Artikel 28:', 'Artikel 29:'),
    (r'artikel-28-', 'artikel-29-'),
    # Artikel 29 -> 30
    (r'Artikel 29:', 'Artikel 30:'),
    (r'artikel-29-', 'artikel-30-'),
    # Artikel 29.1 -> 31
    (r'Artikel 29\.1', 'Artikel 31'),
    (r'artikel-291', 'artikel-31'),
    # Artikel 30 -> 32
    (r'Artikel 30:', 'Artikel 32:'),
    (r'artikel-30-', 'artikel-32-'),
    # Artikel 31 -> 33
    (r'Artikel 31:', 'Artikel 33:'),
    (r'artikel-31-', 'artikel-33-'),
    # Artikel 32 -> 34
    (r'Artikel 32:', 'Artikel 34:'),
    (r'artikel-32-', 'artikel-34-'),
    # Artikel 32.1 -> 35
    (r'Artikel 32\.1', 'Artikel 35'),
    (r'artikel-321', 'artikel-35'),
    # Artikel 32.2 -> 36
    (r'Artikel 32\.2', 'Artikel 36'),
    (r'artikel-322', 'artikel-36'),
    # Artikel 32.3 -> 37
    (r'Artikel 32\.3', 'Artikel 37'),
    (r'artikel-323', 'artikel-37'),
    # Artikel 33 -> 38
    (r'Artikel 33:', 'Artikel 38:'),
    (r'artikel-33-', 'artikel-38-'),
    # Artikel 34 -> 39
    (r'Artikel 34:', 'Artikel 39:'),
    (r'artikel-34-', 'artikel-39-'),
    # Artikel 35 -> 40
    (r'Artikel 35:', 'Artikel 40:'),
    (r'artikel-35-', 'artikel-40-'),
    # Artikel 35.1 -> 41
    (r'Artikel 35\.1', 'Artikel 41'),
    (r'artikel-351', 'artikel-41'),
    # Artikel 36A -> 42
    (r'Artikel 36A', 'Artikel 42'),
    (r'artikel-36a', 'artikel-42'),
    # Artikel 36B -> verwijderd (samengevoegd met 42)
    # Artikel 37 -> 43
    (r'Artikel 37:', 'Artikel 43:'),
    (r'artikel-37-', 'artikel-43-'),
    # Artikel 38 -> 44
    (r'Artikel 38:', 'Artikel 44:'),
    (r'artikel-38-', 'artikel-44-'),
    # Artikel 38.1 -> verwijderd
    # Artikel 38.2 -> 45
    (r'Artikel 38\.2', 'Artikel 45'),
    (r'artikel-382', 'artikel-45'),
    # Artikel 39 -> 46
    (r'Artikel 39:', 'Artikel 46:'),
    (r'artikel-39-', 'artikel-46-'),
    # Artikel 40 -> 47
    (r'Artikel 40:', 'Artikel 47:'),
    (r'artikel-40-', 'artikel-47-'),
    # Artikel 41 -> 48
    (r'Artikel 41:', 'Artikel 48:'),
    (r'artikel-41-', 'artikel-48-'),
    # Artikel 42 -> 49
    (r'Artikel 42:', 'Artikel 49:'),
    (r'artikel-42-', 'artikel-49-'),
    # Artikel 43 -> 50
    (r'Artikel 43:', 'Artikel 50:'),
    (r'artikel-43-', 'artikel-50-'),
    # Artikel 44 -> 51
    (r'Artikel 44:', 'Artikel 51:'),
    (r'artikel-44-', 'artikel-51-'),
    # Artikel 44.1 -> verwijderd
    # Artikel 45 -> 52
    (r'Artikel 45:', 'Artikel 52:'),
    (r'artikel-45-', 'artikel-52-'),
    # Artikel 46 -> 53
    (r'Artikel 46:', 'Artikel 53:'),
    (r'artikel-46', 'artikel-53'),
    # Artikel 47 -> 54
    (r'Artikel 47:', 'Artikel 54:'),
    (r'artikel-47-', 'artikel-54-'),
    # Artikel 47.1 -> verwijderd (samengevoegd)
    # Artikel 47.2 -> verwijderd (samengevoegd)
    # Artikel 48 -> 55
    (r'Artikel 48:', 'Artikel 55:'),
    (r'artikel-48-', 'artikel-55-'),
    # Artikel 49 -> 56
    (r'Artikel 49:', 'Artikel 56:'),
    (r'artikel-49-', 'artikel-56-'),
    # Artikel 50 -> 57
    (r'Artikel 50:', 'Artikel 57:'),
    (r'artikel-50-', 'artikel-57-'),
    # Artikel 51 -> 58
    (r'Artikel 51:', 'Artikel 58:'),
    (r'artikel-51-', 'artikel-58-'),
    # Artikel 51A -> 59
    (r'Artikel 51A', 'Artikel 59'),
    (r'artikel-51a', 'artikel-59'),
    # Artikel 100 -> 60
    (r'Artikel 100:', 'Artikel 60:'),
    (r'artikel-100', 'artikel-60'),
]

# Converteer data naar string voor makkelijker vervangen
json_str = json.dumps(data, ensure_ascii=False)

# Voer alle vervangingen uit
for pattern, replacement in replacements:
    json_str = re.sub(pattern, replacement, json_str, flags=re.IGNORECASE)

# Parse terug naar JSON
updated_data = json.loads(json_str)

# Schrijf terug naar bestand
with open('search/search_index.json', 'w', encoding='utf-8') as f:
    json.dump(updated_data, f, ensure_ascii=False)

print("Search index succesvol bijgewerkt!")
