const fs = require('fs');
let text = fs.readFileSync('templates/dashboard.html', 'utf-8');

const targetFunction = `    function launchLab(difficulty) {
      document.getElementById('labLevelModal').style.display = 'none';

      // Alert exactly what was built for now, routing logic can be expanded!
      showToast(\`Launch sequence initiated: \${activeVulnLab} [\${difficulty} Difficulty]\`, 'success');

      // Output to terminal for immersion
      const output = document.getElementById('scanOutput');
      const line = \`<span style="color:#00ffcc;">[SYSTEM] Initializing Custom Training Lab...</span><br>
                     <span style="color:#00ff88;">[MODULE] Target: \${activeVulnLab}</span><br>
                     <span style="color:#ffaa00;">[CONFIG] Difficulty Level: \${difficulty}</span><br>
                     <span style="color:#aaa;">[PROCESS] Provisioning virtual sandbox... standby.</span><br><br>\`;
      if (output) {
        output.innerHTML += line;
        output.closest('.terminal').scrollTop = output.closest('.terminal').scrollHeight;
      }
    }`;

const newFunction = `    function launchLab(difficulty) {
      document.getElementById('labLevelModal').style.display = 'none';
      
      if (activeVulnLab === 'SQL Injection' && difficulty === 'Low') {
          window.location.href = '/aau/threatmapper/aaulab/sqli/low';
          return;
      }

      // Alert exactly what was built for now, routing logic can be expanded!
      showToast(\`Launch sequence initiated: \${activeVulnLab} [\${difficulty} Difficulty]\`, 'success');

      // Output to terminal for immersion
      const output = document.getElementById('scanOutput');
      const line = \`<span style="color:#00ffcc;">[SYSTEM] Initializing Custom Training Lab...</span><br>
                     <span style="color:#00ff88;">[MODULE] Target: \${activeVulnLab}</span><br>
                     <span style="color:#ffaa00;">[CONFIG] Difficulty Level: \${difficulty}</span><br>
                     <span style="color:#aaa;">[PROCESS] Provisioning virtual sandbox... standby.</span><br><br>\`;
      if (output) {
        output.innerHTML += line;
        output.closest('.terminal').scrollTop = output.closest('.terminal').scrollHeight;
      }
    }`;

text = text.replace(targetFunction, newFunction);
fs.writeFileSync('templates/dashboard.html', text);
