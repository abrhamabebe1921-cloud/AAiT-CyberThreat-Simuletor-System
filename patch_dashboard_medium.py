with open('templates/dashboard.html', 'r') as f:
    text = f.read()

target = """      if (activeVulnLab === 'SQL Injection' && difficulty === 'Low') {
          window.location.href = '/aau/threatmapper/aaulab/sqli/low';
          return;
      }"""

new_code = """      if (activeVulnLab === 'SQL Injection' && difficulty === 'Low') {
          window.location.href = '/aau/threatmapper/aaulab/sqli/low';
          return;
      }
      if (activeVulnLab === 'SQL Injection' && difficulty === 'Medium') {
          window.location.href = '/aau/threatmapper/aaulab/sqli/medium';
          return;
      }"""

if target in text:
    text = text.replace(target, new_code)
    with open('templates/dashboard.html', 'w') as f:
        f.write(text)
    print("dashboard.html patched for Medium difficulty.")
else:
    print("Target block not found in dashboard.html")
