with open('app.py', 'r') as f:
    text = f.read()

target = r"if not found and re.search(r'('|\-\-|;|\s|or|and)', user_id, re.IGNORECASE):"
fixed = r"if not found and re.search(r'(\'|--|;|\s|or|and)', user_id, re.IGNORECASE):"

if target in text:
    text = text.replace(target, fixed)
    with open('app.py', 'w') as f:
        f.write(text)
    print("Fixed regex in app.py")
else:
    print("Not found! Let's search line by line...")
