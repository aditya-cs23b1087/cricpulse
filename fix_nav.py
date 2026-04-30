import os, glob, re

top_bar_html = '''<div class="top-bar" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; padding: 8px 32px;">
  <div>🏏 Welcome to CricPulse! Your #1 Cricket Destination</div>
  <div style="display:flex; gap:16px; flex-wrap:wrap; justify-content:center;">
    <a href="search.html" style="color:#fff; text-decoration:none;"><i class="fas fa-search"></i> Search</a>
    <a href="fanzone.html" style="color:#fff; text-decoration:none;"><i class="fas fa-users"></i> Fan Zone</a>
    <a href="store.html" style="color:#fff; text-decoration:none;"><i class="fas fa-shopping-cart"></i> Store</a>
    <a href="tickets.html" style="color:#fff; text-decoration:none;"><i class="fas fa-ticket-alt"></i> Tickets</a>
    <a href="rankings.html" style="color:#fff; text-decoration:none;"><i class="fas fa-chart-bar"></i> Rankings</a>
    <a href="archive.html" style="color:#fff; text-decoration:none;"><i class="fas fa-history"></i> Archives</a>
    <a href="team.html" style="color:#fff; text-decoration:none;"><i class="fas fa-flag"></i> Teams</a>
    <a href="premium.html" style="color:var(--primary); background:var(--gold); padding:2px 8px; border-radius:4px; text-decoration:none; font-weight:bold;"><i class="fas fa-crown"></i> Premium</a>
    <a href="auth.html" style="color:#fff; text-decoration:none;"><i class="fas fa-user"></i> Login</a>
  </div>
</div>'''

count = 0
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 1. Replace top-bar
    # We will use regex to find the <div class="top-bar">...</div>
    new_content = re.sub(r'<div class="top-bar".*?</div>', top_bar_html, content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        modified = True

    # 2. Remove the nav-dropdown we added earlier
    # It starts with <div class="nav-dropdown" and ends with </div></div> right before </div></nav> or similar.
    # Actually, let's just find <div class="nav-dropdown" ... </div>  </div>
    # Using regex to remove the specific dropdown HTML
    dropdown_pattern = r'<div class="nav-dropdown".*?</div>\s*</div>'
    new_content2 = re.sub(dropdown_pattern, '', content, flags=re.DOTALL)
    if new_content2 != content:
        content = new_content2
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Fixed top-bar navigation in {count} HTML files.')
