import os, glob

dropdown_html = '''<a href="fantasy.html" class="nav-link">Fantasy</a>
  <div class="nav-dropdown" style="position:relative; display:inline-block;">
    <a href="#" class="nav-link" onclick="document.getElementById('more-menu').style.display = document.getElementById('more-menu').style.display === 'none' ? 'block' : 'none'; event.preventDefault();">More <i class="fas fa-chevron-down" style="font-size:10px;"></i></a>
    <div id="more-menu" style="display:none; position:absolute; top:100%; right:0; background:var(--card); box-shadow:var(--shadow); border-radius:var(--radius); padding:8px 0; min-width:180px; z-index:1000; border:1px solid var(--border); text-align:left;">
      <a href="search.html" style="display:block; padding:10px 16px; color:var(--text); text-decoration:none; font-size:14px;"><i class="fas fa-search" style="width:20px; color:var(--primary);"></i> Search</a>
      <a href="fanzone.html" style="display:block; padding:10px 16px; color:var(--text); text-decoration:none; font-size:14px;"><i class="fas fa-users" style="width:20px; color:var(--primary);"></i> Fan Zone</a>
      <a href="store.html" style="display:block; padding:10px 16px; color:var(--text); text-decoration:none; font-size:14px;"><i class="fas fa-shopping-cart" style="width:20px; color:var(--primary);"></i> Store</a>
      <a href="tickets.html" style="display:block; padding:10px 16px; color:var(--text); text-decoration:none; font-size:14px;"><i class="fas fa-ticket-alt" style="width:20px; color:var(--primary);"></i> Tickets</a>
      <a href="rankings.html" style="display:block; padding:10px 16px; color:var(--text); text-decoration:none; font-size:14px;"><i class="fas fa-chart-bar" style="width:20px; color:var(--primary);"></i> Rankings</a>
      <a href="archive.html" style="display:block; padding:10px 16px; color:var(--text); text-decoration:none; font-size:14px;"><i class="fas fa-history" style="width:20px; color:var(--primary);"></i> Archives</a>
      <a href="team.html" style="display:block; padding:10px 16px; color:var(--text); text-decoration:none; font-size:14px;"><i class="fas fa-flag" style="width:20px; color:var(--primary);"></i> Teams</a>
      <div style="height:1px; background:var(--border); margin:8px 0;"></div>
      <a href="premium.html" style="display:block; padding:10px 16px; color:#D4AF37; text-decoration:none; font-size:14px; font-weight:bold;"><i class="fas fa-crown" style="width:20px;"></i> Premium</a>
      <a href="auth.html" style="display:block; padding:10px 16px; color:var(--text); text-decoration:none; font-size:14px;"><i class="fas fa-user" style="width:20px; color:var(--primary);"></i> Login</a>
    </div>
  </div>'''

count = 0
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try different variations of the fantasy link
    targets = [
        '<a href="fantasy.html" class="nav-link" role="menuitem">Fantasy</a>',
        '<a href="fantasy.html" class="nav-link active">Fantasy</a>',
        '<a href="fantasy.html" class="nav-link">Fantasy</a>'
    ]
    
    modified = False
    for target in targets:
        if target in content:
            new_target = dropdown_html
            if 'active' in target:
                new_target = dropdown_html.replace('class="nav-link"', 'class="nav-link active"', 1)
            elif 'role="menuitem"' in target:
                 new_target = dropdown_html.replace('class="nav-link"', 'class="nav-link" role="menuitem"', 1)
                 
            content = content.replace(target, new_target)
            modified = True
            break
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Updated {count} HTML files with the More dropdown menu.')
