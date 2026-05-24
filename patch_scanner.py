with open('modules/scanner.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for idx, line in enumerate(lines):
    if "else:" in line and "# ── Phase 0: Resolve host list" in lines[idx+1]:
        # we found the else block
        new_lines.append("        pass\n") # keep valid syntax
        continue
    new_lines.append(line)

with open('modules/scanner.py', 'w') as f:
    f.writelines(new_lines)

