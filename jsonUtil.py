from json import dump, load

def read_keys():
    with open("notestorage.json", "r", encoding="utf-8") as file:
        storage = load(file)
    return list(storage.keys())

def create_note(name_new, note_text=""):
    with open("notestorage.json", "r", encoding="utf-8") as file:
        origdata = load(file)
    origdata[name_new] = {"text": note_text, "tags": []}
    with open("notestorage.json", "w", encoding="utf-8") as file:
        dump(origdata, file, indent=4)

def note_fetch(name_note):
    with open("notestorage.json", "r", encoding="utf-8") as file:
        storage = load(file)
    return storage[name_note]["text"]

def write_json(storage):
    with open("notestorage.json", "w", encoding="utf-8") as file:
        storage = dump(storage, file)

# Debug test routines

print(read_keys())
with open("notestorage.json", "r") as json_FLE:
    storage = load(json_FLE)
    print(storage)