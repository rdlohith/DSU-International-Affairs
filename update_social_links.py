
import os
import re

# Configuration
target_dir = r"c:\Users\Lohith-IA\Documents\www.dsu.edu.in"

replacements = [
    {
        "name": "Instagram",
        "regex": r'https://www\.instagram\.com/dsu_int_affairs/[^"\']*',
        "new": "https://www.instagram.com/dayanandasagaruniversityblr/"
    },
    {
        "name": "Facebook",
        "regex": r'https://www\.facebook\.com/DSUint[^"\']*',
        "new": "https://www.facebook.com/Dayanandasagaruniversitybangalore"
    },
    {
        "name": "Twitter/X",
        "regex": r'https://x\.com/dsu_media[^"\']*',
        "new": "https://x.com/dsubangalore?s=21"
    },
    {
        "name": "LinkedIn",
        "regex": r'https://www\.linkedin\.com/company/96291393[^"\']*',
        "new": "https://www.linkedin.com/school/dayananda-sagar-university-bangalore/posts/?feedView=all"
    },
    {
        "name": "YouTube",
        "regex": r'https://www\.youtube\.com/@Dayanandasagaruniversityint[^"\']*',
        "new": "https://www.youtube.com/@dayanandasagaruniversity"
    }
]

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for item in replacements:
            content = re.sub(item["regex"], item["new"], content)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath}")
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    count = 0
    print(f"Scanning {target_dir}...")
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                if update_file(filepath):
                    count += 1
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    main()
