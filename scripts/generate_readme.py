#!/usr/bin/env python3
"""
Script to generate README.md from companies.json
This allows for easier data management via JSON
"""

import json
from typing import Dict, List

def format_markdown_link(text: str, url: str) -> str:
    """Format markdown link"""
    if not url:
        return '[-]()'
    if not text:
        text = url
    return f'[{text}]({url})'

def generate_table(companies: List[Dict], is_big_startup: bool = False) -> str:
    """Generate markdown table from company list"""
    if is_big_startup:
        header = "| Company | Category | Headcount | Website | Linkedin | Career Page |"
        separator = "| --------------------- | ------------- | --------- | -------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------- |"
    else:
        header = "| Company | Category | Headcount | Website | Linkedin | Career Page |"
        separator = "| ------------------------- | -------- | --------- | ------- | -------- | ----------- |"
    
    rows = [header, separator]
    
    for company in companies:
        name = company.get('name', '-')
        category = company.get('category', '-') or '-'
        headcount = company.get('headcount', '-') or '-'
        website = company.get('website', '') or '-'
        linkedin = company.get('linkedin', '') or '-'
        career = company.get('careerPage', '') or '-'
        
        # Format links
        website_link = format_markdown_link(company.get('name', ''), website) if website != '-' else '[-]()'
        linkedin_link = format_markdown_link(company.get('name', ''), linkedin) if linkedin != '-' else '[-](-)'
        career_link = format_markdown_link(company.get('name', ''), career) if career != '-' else '[-]()'
        
        if is_big_startup:
            row = f"| {name:<22} | {category:<12} | {headcount:<9} | {website:<32} | {linkedin_link:<85} | {career_link:<51} |"
        else:
            row = f"| {name:<25} | {category:<8} | {headcount:<9} | {website:<7} | {linkedin_link:<9} | {career_link:<12} |"
        
        rows.append(row)
    
    return '\n'.join(rows)

def main():
    """Main function to generate README"""
    try:
        with open('companies.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ companies.json not found.")
        return
    
    readme_content = """# ID Tech List

List of tech companies in Indonesia. Useful when looking for a new job.

> **Warning**
> Categories are highly subjective and potentially biased. Relative positions within a category are arbitrary.

> **Warning**
> The list is not meant to be exhaustive. I am not affiliated to any companies listed.

| Level  | Headcount |
| ------ | --------- |
| Big    | 500+      |
| Medium | 300~500   |
| Small  | 30~300    |

"""
    
    category_order = [
        ('big_startup', 'BIG START-UP'),
        ('medium_startup', 'MEDIUM START-UP'),
        ('small_startup', 'SMALL START-UP'),
        ('big_it_consulting', 'BIG IT CONSULTING'),
        ('medium_it_consulting', 'MEDIUM IT CONSULTING'),
        ('small_it_consulting', 'SMALL IT CONSULTING'),
        ('bank_other_big_company', 'BANK / OTHER BIG COMPANY')
    ]
    
    for category_key, category_title in category_order:
        if category_key in data['categories']:
            category_data = data['categories'][category_key]
            companies = category_data.get('companies', [])
            
            readme_content += f"## {category_title}\n\n"
            readme_content += generate_table(companies, is_big_startup=(category_key == 'big_startup'))
            readme_content += "\n\n"
    
    # Write README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✅ README.md generated successfully!")

if __name__ == '__main__':
    main()

