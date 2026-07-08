import os
import re

directory = r"c:/Users/Lohith-IA/Documents/www.dsu.edu.in"

# Pattern to remove
# Used [^>]* to match any attributes including newlines
pattern = r'<div>\s*<p>\s*<a[^>]*href="Calendar\.html"[^>]*>Calendar</a>\s*<br\s*/>\s*<a[^>]*href="GlobalPartnerships\.html"[^>]*>Collaborations</a>\s*<br\s*/>\s*<a[^>]*href="newsletter\.html"[^>]*>News Release</a>\s*</p>\s*</div>\s*<div>\s*<p>\s*<a[^>]*href="Testimonials\.html"[^>]*>Alumni</a>\s*<br\s*/>\s*<a[^>]*href="Resources\.html"[^>]*>International &amp;\s*Resources</a>\s*<br\s*/>\s*<a[^>]*href="team\.html"[^>]*>Team</a>\s*</p>\s*</div>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if pattern exists
            new_content, n = re.subn(pattern, '', content, flags=re.DOTALL)
            
            if n > 0:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Modified: {filename}")
                count += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"Total files modified: {count}")
