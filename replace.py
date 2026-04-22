import os

def replace_lines(filepath, start_idx, end_idx, replacement):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if start_idx < 1 or end_idx > len(lines):
        print(f"Index out of bounds for {filepath}")
        return
        
    new_lines = lines[:start_idx-1] + [replacement + "\n"] + lines[end_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"SUCCESS: {filepath} updated.")

files = [
    {
        "path": "project-04-tool-search.html",
        "start": 13,
        "end": 330,
        "repl": '  <link rel="stylesheet" href="assets/css/global.css">\n  <style>'
    }
]

for item in files:
    replace_lines(item["path"], item["start"], item["end"], item["repl"])
