with open('modules/scanner.py', 'r') as f:
    content = f.read()

import re
replacement = """
        emit('')
        sev_counts = {s: 0 for s in ('Critical', 'High', 'Medium', 'Low', 'Info')}
        for f in findings:
            sev_counts[f['severity']] = sev_counts.get(f['severity'], 0) + 1
        return {
            'logs': logs,
            'findings': findings,
            'summary': {
                'total': len(findings),
                'critical': sev_counts['Critical'],
                'high': sev_counts['High'],
                'medium': sev_counts['Medium']
            }
        }
"""
content = content.replace("        emit('')\n        pass\n        # ── Phase 0:", replacement + "\n        # ── Phase 0:")
with open('modules/scanner.py', 'w') as f:
    f.write(content)

