#!/usr/bin/env python3
"""
Script to validate company data and check for inconsistencies
"""

import json
import re
from typing import Dict, List, Tuple

def validate_url(url: str) -> bool:
    """Validate URL format"""
    if not url:
        return True  # Empty is OK
    
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return bool(url_pattern.match(url))

def check_duplicates(companies: List[Dict]) -> List[Tuple[str, str]]:
    """Check for duplicate company names"""
    seen = {}
    duplicates = []
    
    for company in companies:
        name = company['name'].lower().strip()
        if name in seen:
            duplicates.append((company['name'], seen[name]))
        else:
            seen[name] = company['name']
    
    return duplicates

def validate_company(company: Dict, category: str) -> List[str]:
    """Validate a single company entry and return list of issues"""
    issues = []
    
    name = company.get('name', '').strip()
    if not name or name == '-':
        issues.append(f"❌ Empty company name")
    
    # Check URLs
    for url_field in ['website', 'linkedin', 'careerPage']:
        url = company.get(url_field, '')
        if url and not validate_url(url):
            issues.append(f"⚠️  Invalid {url_field} URL: {url}")
    
    # Check for common inconsistencies
    if company.get('category', '') == '-':
        issues.append(f"ℹ️  Missing category")
    
    if company.get('headcount', '') == '-':
        issues.append(f"ℹ️  Missing headcount")
    
    return issues

def main():
    """Main validation function"""
    try:
        with open('companies.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ companies.json not found. Run parse_readme.py first.")
        return
    
    print("🔍 Validating company data...\n")
    
    all_issues = []
    all_companies = []
    
    for category_key, category_data in data['categories'].items():
        companies = category_data.get('companies', [])
        all_companies.extend(companies)
        
        print(f"📊 {category_data['name']}: {len(companies)} companies")
        
        # Check duplicates within category
        duplicates = check_duplicates(companies)
        if duplicates:
            print(f"  ⚠️  Found duplicates: {duplicates}")
        
        # Validate each company
        for company in companies:
            issues = validate_company(company, category_key)
            if issues:
                all_issues.append({
                    'company': company.get('name', 'Unknown'),
                    'category': category_data['name'],
                    'issues': issues
                })
    
    # Check for duplicates across all categories
    all_duplicates = check_duplicates(all_companies)
    if all_duplicates:
        print(f"\n⚠️  Found duplicates across categories: {all_duplicates}")
    
    # Report issues
    if all_issues:
        print(f"\n📋 Found {len(all_issues)} companies with issues:")
        for item in all_issues[:10]:  # Show first 10
            print(f"\n  {item['company']} ({item['category']}):")
            for issue in item['issues']:
                print(f"    {issue}")
        if len(all_issues) > 10:
            print(f"\n  ... and {len(all_issues) - 10} more")
    else:
        print("\n✅ No issues found!")
    
    # Statistics
    total_companies = len(all_companies)
    companies_with_website = sum(1 for c in all_companies if c.get('website'))
    companies_with_linkedin = sum(1 for c in all_companies if c.get('linkedin'))
    companies_with_career = sum(1 for c in all_companies if c.get('careerPage'))
    
    print(f"\n📈 Statistics:")
    print(f"  Total companies: {total_companies}")
    print(f"  With website: {companies_with_website} ({companies_with_website/total_companies*100:.1f}%)")
    print(f"  With LinkedIn: {companies_with_linkedin} ({companies_with_linkedin/total_companies*100:.1f}%)")
    print(f"  With career page: {companies_with_career} ({companies_with_career/total_companies*100:.1f}%)")

if __name__ == '__main__':
    main()

