with open('templates/lab_sqli_high.html', 'r') as f:
    text = f.read()

text = text.replace('SQLi Lab (Medium)', 'SQLi Lab (High)')
text = text.replace('<span>Level: Medium</span>', '<span>Level: High</span>')

old_source = """      <div class="source-block">
        // Escaped input, without quotes:<br>
        $id = mysqli_real_escape_string($GLOBALS["___mysqli_ston"], $id);<br>
        $query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
      </div>"""

new_source = """      <div class="source-block">
        // Session-based input, with quotes and LIMIT 1:<br>
        $id = $_SESSION['id'];<br>
        $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";
      </div>"""
text = text.replace(old_source, new_source)

text = text.replace('Submit Query', 'Update Session & Submit')
text = text.replace('placeholder="Enter User ID (e.g. 1 or 1 OR 1=1)"', 'placeholder="Enter your Session ID (e.g. 1 or 1\' OR 1=1 #)"')

with open('templates/lab_sqli_high.html', 'w') as f:
    f.write(text)
print("lab_sqli_high.html patched successfully.")
