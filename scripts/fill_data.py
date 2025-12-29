#!/usr/bin/env python3
"""
Script to fill in missing company data
Mengisi data yang masih kosong untuk perusahaan-perusahaan populer
"""

import json
from typing import Dict

# Data perusahaan yang akan diisi
COMPANY_DATA = {
    # BIG START-UP
    "Alami": {
        "website": "https://www.alami.id/",
        "linkedin": "https://www.linkedin.com/company/alami-sharia/",
        "careerPage": "https://www.alami.id/careers"
    },
    "Amartha": {
        "website": "https://www.amartha.com/",
        "linkedin": "https://www.linkedin.com/company/amartha/",
        "careerPage": "https://www.amartha.com/careers"
    },
    "Anteraja": {
        "category": "Logistics",
        "website": "https://anteraja.id/",
        "linkedin": "https://www.linkedin.com/company/anteraja/",
        "careerPage": "https://anteraja.id/careers"
    },
    "Bibit": {
        "category": "Investment",
        "website": "https://bibit.id/",
        "linkedin": "https://www.linkedin.com/company/bibit-id/",
        "careerPage": "https://bibit.id/careers"
    },
    "Cicil": {
        "category": "Fintech",
        "website": "https://www.cicil.co.id/",
        "linkedin": "https://www.linkedin.com/company/cicil/",
        "careerPage": ""
    },
    "Dagangan": {
        "category": "Ecommerce",
        "website": "https://dagangan.com/",
        "linkedin": "https://www.linkedin.com/company/dagangan/",
        "careerPage": ""
    },
    "eFishery": {
        "category": "Agritech",
        "website": "https://efishery.com/",
        "linkedin": "https://www.linkedin.com/company/efishery/",
        "careerPage": "https://efishery.com/careers"
    },
    "EdenFarm": {
        "category": "Agritech",
        "website": "https://edenfarm.id/",
        "linkedin": "https://www.linkedin.com/company/edenfarm/",
        "careerPage": ""
    },
    "Flip": {
        "category": "Fintech",
        "website": "https://flip.id/",
        "linkedin": "https://www.linkedin.com/company/flip-id/",
        "careerPage": "https://flip.id/careers"
    },
    "Fazz": {
        "category": "Fintech",
        "website": "https://fazz.com/",
        "linkedin": "https://www.linkedin.com/company/fazz/",
        "careerPage": "https://fazz.com/careers"
    },
    "GudangAda": {
        "website": "https://www.gudangada.com/",
        "linkedin": "https://www.linkedin.com/company/gudangada/",
        "careerPage": "https://www.gudangada.com/careers"
    },
    "Glints": {
        "category": "HR Tech",
        "website": "https://glints.com/id",
        "linkedin": "https://www.linkedin.com/company/glints/",
        "careerPage": "https://glints.com/id/careers"
    },
    "Home Credit Indonesia": {
        "category": "Fintech",
        "website": "https://www.homecredit.co.id/",
        "linkedin": "https://www.linkedin.com/company/home-credit-indonesia/",
        "careerPage": "https://www.homecredit.co.id/careers"
    },
    "Harian Kompas": {
        "website": "https://www.kompas.com/",
        "linkedin": "https://www.linkedin.com/company/kompas-gramedia/",
        "careerPage": ""
    },
    "INDODAX": {
        "website": "https://indodax.com/",
        "linkedin": "https://www.linkedin.com/company/indodax/",
        "careerPage": "https://indodax.com/careers"
    },
    "JULO": {
        "website": "https://www.julo.co.id/",
        "linkedin": "https://www.linkedin.com/company/julo/",
        "careerPage": ""
    },
    "kumparan": {
        "website": "https://kumparan.com/",
        "linkedin": "https://www.linkedin.com/company/kumparan/",
        "careerPage": "https://kumparan.com/careers"
    },
    "KreditPlus": {
        "website": "https://www.kreditplus.com/",
        "linkedin": "https://www.linkedin.com/company/kreditplus/",
        "careerPage": ""
    },
    "Kargo Technologies": {
        "website": "https://kargo.tech/",
        "linkedin": "https://www.linkedin.com/company/kargo-technologies/",
        "careerPage": "https://kargo.tech/careers"
    },
    "Logisly": {
        "website": "https://logisly.com/",
        "linkedin": "https://www.linkedin.com/company/logisly/",
        "careerPage": ""
    },
    "majoo Indonesia": {
        "category": "SaaS",
        "website": "https://majoo.id/",
        "linkedin": "https://www.linkedin.com/company/majoo/",
        "careerPage": ""
    },
    "Moladin": {
        "category": "Automotive",
        "website": "https://moladin.com/",
        "linkedin": "https://www.linkedin.com/company/moladin/",
        "careerPage": "https://moladin.com/careers"
    },
    "Mapan": {
        "category": "Ecommerce",
        "website": "https://mapan.com/",
        "linkedin": "https://www.linkedin.com/company/mapan/",
        "careerPage": ""
    },
    "Ninja Xpress": {
        "category": "Logistics",
        "website": "https://www.ninjaxpress.co/",
        "linkedin": "https://www.linkedin.com/company/ninja-xpress/",
        "careerPage": ""
    },
    "Pinhome": {
        "category": "PropTech",
        "website": "https://pinhome.id/",
        "linkedin": "https://www.linkedin.com/company/pinhome/",
        "careerPage": "https://pinhome.id/careers"
    },
    "Quipper": {
        "category": "EdTech",
        "website": "https://www.quipper.com/id/",
        "linkedin": "https://www.linkedin.com/company/quipper/",
        "careerPage": "https://www.quipper.com/id/careers"
    },
    "Sekolah.mu": {
        "category": "EdTech",
        "website": "https://www.sekolah.mu/",
        "linkedin": "https://www.linkedin.com/company/sekolahmu/",
        "careerPage": ""
    },
    "Stockbit": {
        "category": "Investment",
        "website": "https://stockbit.com/",
        "linkedin": "https://www.linkedin.com/company/stockbit/",
        "careerPage": "https://stockbit.com/careers"
    },
    "Sirclo": {
        "category": "Ecommerce",
        "website": "https://www.sirclo.com/",
        "linkedin": "https://www.linkedin.com/company/sirclo/",
        "careerPage": "https://www.sirclo.com/careers"
    },
    "Ula": {
        "category": "B2B Ecommerce",
        "website": "https://ula.id/",
        "linkedin": "https://www.linkedin.com/company/ula-id/",
        "careerPage": ""
    },
    "Vidio": {
        "category": "Media",
        "website": "https://www.vidio.com/",
        "linkedin": "https://www.linkedin.com/company/vidio/",
        "careerPage": ""
    },
    "Warung Pintar": {
        "category": "Retail Tech",
        "website": "https://warungpintar.co.id/",
        "linkedin": "https://www.linkedin.com/company/warungpintar/",
        "careerPage": ""
    },
    "Akulaku": {
        "careerPage": "https://www.akulaku.com/careers"
    },
    "Aruna": {
        "careerPage": "https://aruna.id/careers"
    },
    "Alodokter": {
        "careerPage": "https://www.alodokter.com/careers"
    },
    "IDN Media": {
        "careerPage": "https://www.idnmedia.com/careers"
    },
    "SiCepat": {
        "careerPage": "https://www.sicepat.com/careers"
    }
}

def fill_company_data():
    """Fill in missing company data"""
    # Load JSON
    with open('companies.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated_count = 0
    
    # Iterate through all categories
    for category_key, category_data in data['categories'].items():
        companies = category_data.get('companies', [])
        
        for company in companies:
            name = company.get('name', '').strip()
            
            # Skip separator rows
            if not name or name.startswith('-'):
                continue
            
            # Check if we have data for this company
            if name in COMPANY_DATA:
                company_data = COMPANY_DATA[name]
                updated = False
                
                # Update category if provided and empty
                if 'category' in company_data and not company.get('category'):
                    company['category'] = company_data['category']
                    updated = True
                
                # Update website if provided and empty
                if 'website' in company_data and not company.get('website'):
                    company['website'] = company_data['website']
                    updated = True
                
                # Update LinkedIn if provided and empty
                if 'linkedin' in company_data and not company.get('linkedin'):
                    company['linkedin'] = company_data['linkedin']
                    updated = True
                
                # Update career page if provided and empty
                if 'careerPage' in company_data and not company.get('careerPage'):
                    company['careerPage'] = company_data['careerPage']
                    updated = True
                
                if updated:
                    updated_count += 1
                    print(f"✅ Updated: {name}")
    
    # Save updated JSON
    with open('companies.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n🎉 Successfully updated {updated_count} companies!")
    print("💡 Run 'python3 scripts/generate_readme.py' to update README.md")

if __name__ == '__main__':
    fill_company_data()

