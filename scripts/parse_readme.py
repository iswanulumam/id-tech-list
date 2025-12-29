#!/usr/bin/env python3
"""
Script to parse README.md and convert to JSON format
Also validates and fixes inconsistencies in the data
"""

import json
import re
from typing import Dict, List, Any

def parse_markdown_table(content: str) -> List[Dict[str, str]]:
    """Parse markdown table and return list of dictionaries"""
    lines = content.strip().split('\n')
    companies = []
    
    for line in lines:
        if not line.startswith('|') or line.startswith('|---'):
            continue
        
        # Split by pipe and clean up
        parts = [p.strip() for p in line.split('|')[1:-1]]
        
        if len(parts) >= 3 and parts[0] != 'Company' and parts[0] != '-':
            company = {
                'name': parts[0],
                'category': parts[1] if len(parts) > 1 else '',
                'headcount': parts[2] if len(parts) > 2 else '',
                'website': parts[3] if len(parts) > 3 else '',
                'linkedin': parts[4] if len(parts) > 4 else '',
                'careerPage': parts[5] if len(parts) > 5 else ''
            }
            
            # Clean up empty values
            for key in company:
                if company[key] in ['-', '[-]()', '[-](-)']:
                    company[key] = ''
                # Extract URL from markdown links
                elif '[' in company[key] and '](' in company[key]:
                    match = re.search(r'\[.*?\]\((.*?)\)', company[key])
                    if match:
                        company[key] = match.group(1)
            
            companies.append(company)
    
    return companies

def extract_category_section(content: str, category_name: str) -> str:
    """Extract table content for a specific category"""
    pattern = f'## {category_name}.*?(?=##|$)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(0)
    return ''

def main():
    """Main function to parse README and generate JSON"""
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    categories = {
        'BIG START-UP': 'big_startup',
        'MEDIUM START-UP': 'medium_startup',
        'SMALL START-UP': 'small_startup',
        'BIG IT CONSULTING': 'big_it_consulting',
        'MEDIUM IT CONSULTING': 'medium_it_consulting',
        'SMALL IT CONSULTING': 'small_it_consulting',
        'BANK / OTHER BIG COMPANY': 'bank_other_big_company'
    }
    
    result = {
        'metadata': {
            'description': 'List of tech companies in Indonesia',
            'lastUpdated': '2024',
            'note': 'Categories are highly subjective and potentially biased. The list is not meant to be exhaustive.'
        },
        'categories': {}
    }
    
    for category_name, category_key in categories.items():
        section_content = extract_category_section(readme_content, category_name)
        if section_content:
            companies = parse_markdown_table(section_content)
            
            # Determine headcount range
            headcount_range = ''
            if 'BIG' in category_name:
                headcount_range = '500+'
            elif 'MEDIUM' in category_name:
                headcount_range = '300~500'
            elif 'SMALL' in category_name:
                headcount_range = '30~300'
            
            result['categories'][category_key] = {
                'name': category_name,
                'headcount': headcount_range,
                'companies': companies
            }
    
    # Write to JSON file
    with open('companies.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Successfully parsed {len(result['categories'])} categories")
    total_companies = sum(len(cat['companies']) for cat in result['categories'].values())
    print(f"✅ Total companies: {total_companies}")

if __name__ == '__main__':
    main()

