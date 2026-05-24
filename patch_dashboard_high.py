with open('templates/dashboard.html', 'r') as f:
    text = f.read()

target = """      if (activeVulnLab === 'SQL Injection' && difficulty === 'Medium') {
          window.location.href = '/aau/threatmapper/aaulab/sqli/medium';
          return;
      }"""

new_code = """      if (activeVulnLab === 'SQL Injection' && difficulty === 'Medium') {
          window.location.href = '/aau/threatmapper/aaulab/sqli/medium';
          return;
      }
      if (activeVulnLab === 'SQL Injection' && difficulty === 'High') {
          window.location.href = '/aau/threatmapper/aaulab/sqli/high';
          return;
      }"""

if target in text:
    text = text.replace(target, new_code)
    with open('templates/dashboard.html', 'w') as f:
        f.write(text)
    print("dashboard.html patched for High difficulty.")
else:
    print("Target block not found in dashboard.html")
