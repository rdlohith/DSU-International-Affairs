import os

directory = r'c:\Users\Lohith-IA\Documents\www.dsu.edu.in'
analytics_script = '<script src="https://analytics.ahrefs.com/analytics.js" data-key="EHffXp0LApw/17YqguRLbw" async></script>'
target_tag = '</head>'

count = 0
skipped = 0

print(f"Scanning directory: {directory}")

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if analytics_script in content:
                print(f"Skipping {filename} (already present)")
                skipped += 1
                continue
            
            if target_tag in content:
                print(f"Updating {filename}")
                new_content = content.replace(target_tag, f"{analytics_script}\n{target_tag}")
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
            else:
                print(f"Warning: {target_tag} not found in {filename}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"\nSummary: Updated {count} files. Skipped {skipped} files.")
