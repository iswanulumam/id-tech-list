#!/usr/bin/env python3
"""
Script to generate README.md from companies.json
This allows for easier data management via JSON
"""

import json
from typing import Dict, List

# Category emoji mapping
CATEGORY_EMOJI = {
    'Fintech': '💳',
    'Ecommerce': '🛒',
    'Investment': '📈',
    'Health Care': '🏥',
    'EdTech': '📚',
    'Logistics': '🚚',
    'logistics': '🚚',  # lowercase variant
    'Travel': '✈️',
    'Media': '📺',
    'Ride Hailing': '🚗',
    'B2B Ecommerce': '🏢',
    'HR Tech': '👥',
    'Publishing': '📰',
    'Web3': '🌐',
    'web3': '🌐',  # lowercase variant
    'Maritime Tech': '⚓',
    'Digital Identity': '🔐',
    'SaaS': '☁️',
    'Automotive': '🚙',
    'PropTech': '🏠',
    'Agritech': '🌾',
    'Retail Tech': '🏪',
}

def get_category_display(category: str) -> str:
    """Get category with emoji"""
    if not category or category == '-':
        return '—'
    # Normalize category (capitalize first letter)
    normalized = category.strip()
    if normalized:
        normalized = normalized[0].upper() + normalized[1:] if len(normalized) > 1 else normalized.upper()
    emoji = CATEGORY_EMOJI.get(category, CATEGORY_EMOJI.get(normalized, '💼'))
    return f"{emoji} {normalized}"

def format_markdown_link(text: str, url: str, icon: str = '🔗') -> str:
    """Format markdown link with icon"""
    if not url or url == '-':
        return '<sub>—</sub>'
    if not text:
        text = url
    return f'{icon} [{text}]({url})'

def format_empty(value: str) -> str:
    """Format empty values nicely"""
    if not value or value == '-':
        return '<sub>—</sub>'
    return value

def generate_table(companies: List[Dict]) -> str:
    """Generate markdown table from company list"""
    header = "| Company | Category | Headcount | Website | LinkedIn | Career Page |"
    separator = "| :--- | :--- | :---: | :--- | :--- | :--- |"
    
    rows = [header, separator]
    
    for company in companies:
        name = company.get('name', '').strip()
        if not name or name == '-' or name.startswith('-'):
            continue
            
        category = get_category_display(company.get('category', ''))
        headcount = format_empty(company.get('headcount', ''))
        
        website = company.get('website', '').strip()
        linkedin = company.get('linkedin', '').strip()
        career = company.get('careerPage', '').strip()
        
        # Format links with icons
        website_link = format_markdown_link(name, website, '🌐') if website and website != '-' else '<sub>—</sub>'
        linkedin_link = format_markdown_link(name, linkedin, '💼') if linkedin and linkedin != '-' else '<sub>—</sub>'
        career_link = format_markdown_link(name, career, '💼') if career and career != '-' else '<sub>—</sub>'
        
        row = f"| **{name}** | {category} | {headcount} | {website_link} | {linkedin_link} | {career_link} |"
        rows.append(row)
    
    return '\n'.join(rows)

def calculate_stats(data: Dict) -> Dict:
    """Calculate statistics from data"""
    stats = {
        'total': 0,
        'with_website': 0,
        'with_linkedin': 0,
        'with_career': 0,
        'categories': {}
    }
    
    for category_key, category_data in data['categories'].items():
        companies = category_data.get('companies', [])
        category_count = len([c for c in companies if c.get('name', '').strip() and not c.get('name', '').startswith('-')])
        stats['categories'][category_key] = category_count
        stats['total'] += category_count
        
        for company in companies:
            if company.get('name', '').strip() and not company.get('name', '').startswith('-'):
                if company.get('website', '').strip() and company.get('website', '') != '-':
                    stats['with_website'] += 1
                if company.get('linkedin', '').strip() and company.get('linkedin', '') != '-':
                    stats['with_linkedin'] += 1
                if company.get('careerPage', '').strip() and company.get('careerPage', '') != '-':
                    stats['with_career'] += 1
    
    return stats

def main():
    """Main function to generate README"""
    try:
        with open('companies.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ companies.json not found.")
        return
    
    stats = calculate_stats(data)
    completeness = (stats['with_website'] / stats['total'] * 100) if stats['total'] > 0 else 0
    
    readme_content = """# 🇮🇩 ID Tech List

> **Daftar perusahaan teknologi di Indonesia. Berguna untuk mencari pekerjaan baru.**

<div align="center">

![Total Companies](https://img.shields.io/badge/Total%20Companies-{total}-blue)
![Completeness](https://img.shields.io/badge/Data%20Completeness-{completeness:.1f}%25-green)

</div>

---

## 📊 Statistik

| Metrik | Jumlah |
| :--- | :---: |
| **Total Perusahaan** | **{total}** |
| Dengan Website | {with_website} |
| Dengan LinkedIn | {with_linkedin} |
| Dengan Career Page | {with_career} |

---

## 📋 Kategori Perusahaan

| Level | Headcount | Jumlah |
| :--- | :--- | :---: |
| 🏢 **Big** | 500+ | {big_count} |
| 🏛️ **Medium** | 300~500 | {medium_count} |
| 🏠 **Small** | 30~300 | {small_count} |

---

> ⚠️ **Peringatan**  
> Kategori bersifat subjektif dan berpotensi bias. Posisi relatif dalam kategori bersifat arbitrer.  
> Daftar ini tidak dimaksudkan untuk lengkap. Saya tidak berafiliasi dengan perusahaan yang terdaftar.

---

""".format(
        total=stats['total'],
        completeness=completeness,
        with_website=stats['with_website'],
        with_linkedin=stats['with_linkedin'],
        with_career=stats['with_career'],
        big_count=stats['categories'].get('big_startup', 0) + stats['categories'].get('big_it_consulting', 0),
        medium_count=stats['categories'].get('medium_startup', 0) + stats['categories'].get('medium_it_consulting', 0),
        small_count=stats['categories'].get('small_startup', 0) + stats['categories'].get('small_it_consulting', 0)
    )
    
    category_order = [
        ('big_startup', '🚀 BIG START-UP', 'Perusahaan startup besar dengan 500+ karyawan'),
        ('medium_startup', '🏛️ MEDIUM START-UP', 'Perusahaan startup menengah dengan 300~500 karyawan'),
        ('small_startup', '🏠 SMALL START-UP', 'Perusahaan startup kecil dengan 30~300 karyawan'),
        ('big_it_consulting', '💼 BIG IT CONSULTING', 'Perusahaan konsultan IT besar'),
        ('medium_it_consulting', '🏢 MEDIUM IT CONSULTING', 'Perusahaan konsultan IT menengah'),
        ('small_it_consulting', '🏡 SMALL IT CONSULTING', 'Perusahaan konsultan IT kecil'),
        ('bank_other_big_company', '🏦 BANK / OTHER BIG COMPANY', 'Bank dan perusahaan besar lainnya')
    ]
    
    for category_key, category_title, category_desc in category_order:
        if category_key in data['categories']:
            category_data = data['categories'][category_key]
            companies = category_data.get('companies', [])
            count = len([c for c in companies if c.get('name', '').strip() and not c.get('name', '').startswith('-')])
            
            readme_content += f"## {category_title}\n\n"
            readme_content += f"*{category_desc}*\n\n"
            readme_content += f"**Total: {count} perusahaan**\n\n"
            readme_content += generate_table(companies)
            readme_content += "\n\n---\n\n"
    
    # Write README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✅ README.md generated successfully!")
    print(f"   📊 Total companies: {stats['total']}")
    print(f"   📈 Data completeness: {completeness:.1f}%")

if __name__ == '__main__':
    main()

