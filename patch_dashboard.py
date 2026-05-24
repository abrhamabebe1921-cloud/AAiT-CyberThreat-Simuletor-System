with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacement = """
                  <div style="display:flex;gap:6px;margin-bottom:10px;">
                    <button id="tabDomain" onclick="setScanTab('domain')" style="flex:1;padding:6px 10px;border-radius:7px;border:1px solid rgba(0,255,200,0.45);
                             background:rgba(0,255,200,0.12);color:#00ffcc;font-family:monospace;
                             font-size:11px;font-weight:700;cursor:pointer;transition:0.2s;">
                      🌐 Domain
                    </button>
                    <button id="tabFile" onclick="setScanTab('file')" style="flex:1;padding:6px 10px;border-radius:7px;border:1px solid rgba(255,255,255,0.1);
                             background:rgba(255,255,255,0.04);color:#888;font-family:monospace;
                             font-size:11px;font-weight:700;cursor:pointer;transition:0.2s;">
                      📄 Subdomains
                    </button>
                    <button id="tabSource" onclick="setScanTab('source')" style="flex:1;padding:6px 10px;border-radius:7px;border:1px solid rgba(255,255,255,0.1);
                             background:rgba(255,255,255,0.04);color:#888;font-family:monospace;
                             font-size:11px;font-weight:700;cursor:pointer;transition:0.2s;">
                      💻 Source Code
                    </button>
                  </div>

                  <!-- Mode 1: Domain / wildcard -->
                  <div id="modeDomain">
                    <input type="text" id="scanTarget" placeholder="e.g.  *.aau.edu.et  or  aau.edu.et"
                      style="width:100%;margin-bottom:8px;font-family:monospace;font-size:12px;">
                    <div style="font-size:10px;color:#555;font-family:monospace;margin-top:-4px;margin-bottom:8px;">
                      Use <code style="color:#00ffcc;">*.domain.com</code> to scan all subdomains automatically.
                    </div>
                  </div>

                  <!-- Mode 2: .txt file upload -->
                  <div id="modeFile" style="display:none;">
                    <label style="display:block;margin-bottom:5px;font-size:11px;color:#aaa;font-family:monospace;">
                      Upload a <code style="color:#00ffcc;">.txt</code> file — one subdomain per line:
                    </label>
                    <input type="file" id="subdomainFile" accept=".txt" onchange="previewSubdomainFile(this)" style="width:100%;padding:6px 8px;background:rgba(0,255,200,0.06);
                             border:1px dashed rgba(0,255,200,0.35);border-radius:7px;
                             color:#ccc;font-family:monospace;font-size:11px;cursor:pointer;
                             margin-bottom:6px;">
                    <div id="subdomainFilePreview"
                      style="font-size:10px;color:#555;font-family:monospace;min-height:16px;"></div>
                  </div>

                  <!-- Mode 3: Source Code SAST -->
                  <div id="modeSource" style="display:none; margin-bottom:8px;">
                    <textarea id="sourceCodeInput" placeholder="Paste PHP/Python source code here for SAST analysis..."
                      style="width:100%;height:80px;background:rgba(0,0,0,0.5);border:1px solid #444;color:#00ffcc;font-family:monospace;font-size:11px;padding:8px;border-radius:6px;resize:vertical;"></textarea>
                  </div>
"""

import re

# Match the old target mode tabs block and mode sections up to <!-- Controls row -->
pattern = re.compile(r'<!-- ── Target Mode Tabs ── -->.*?<!-- Controls row -->', re.DOTALL)
text = pattern.sub(f'<!-- ── Target Mode Tabs ── -->\n{replacement}\n                  <!-- Controls row -->', text)

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(text)

