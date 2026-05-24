with open('templates/lab_sqli_medium.html', 'r') as f:
    text = f.read()

text = text.replace('SQLi Lab (Low) — ThreatMapper', 'SQLi Lab (Medium) — ThreatMapper')
text = text.replace('<span>Level: Low</span>', '<span>Level: Medium</span>')

old_source = """      <div class="source-block">
        // Vulnerable backend logic simulation:<br>
        $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
      </div>"""

new_source = """      <div class="source-block">
        // Escaped input, without quotes:<br>
        $id = mysqli_real_escape_string($GLOBALS["___mysqli_ston"], $id);<br>
        $query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
      </div>"""
text = text.replace(old_source, new_source)

text = text.replace('placeholder="Enter User ID (e.g. 1 or 1\' OR 1=1 #)"', 'placeholder="Enter User ID (e.g. 1 or 1 OR 1=1)"')

with open('templates/lab_sqli_medium.html', 'w') as f:
    f.write(text)
print("lab_sqli_medium.html patched successfully.")
