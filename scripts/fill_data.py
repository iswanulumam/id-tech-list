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
    },
    
    # MEDIUM START-UP
    "Mekari": {
        "category": "SaaS",
        "website": "https://www.mekari.com/",
        "linkedin": "https://www.linkedin.com/company/mekari/",
        "careerPage": "https://www.mekari.com/careers"
    },
    "Pluang": {
        "category": "Investment",
        "website": "https://pluang.com/",
        "linkedin": "https://www.linkedin.com/company/pluang/",
        "careerPage": "https://pluang.com/careers"
    },
    "Qoala": {
        "category": "Fintech",
        "website": "https://www.qoala.id/",
        "linkedin": "https://www.linkedin.com/company/qoala/",
        "careerPage": "https://www.qoala.id/careers"
    },
    "SehatQ": {
        "category": "Health Care",
        "website": "https://www.sehatq.com/",
        "linkedin": "https://www.linkedin.com/company/sehatq/",
        "careerPage": "https://www.sehatq.com/careers"
    },
    "TaniHub": {
        "category": "Agritech",
        "website": "https://tanihub.com/",
        "linkedin": "https://www.linkedin.com/company/tanihub/",
        "careerPage": "https://tanihub.com/careers"
    },
    "Tokocrypto": {
        "category": "Web3",
        "website": "https://www.tokocrypto.com/",
        "linkedin": "https://www.linkedin.com/company/tokocrypto/",
        "careerPage": "https://www.tokocrypto.com/careers"
    },
    "Waresix": {
        "category": "Logistics",
        "website": "https://waresix.com/",
        "linkedin": "https://www.linkedin.com/company/waresix/",
        "careerPage": "https://waresix.com/careers"
    },
    "Pintu": {
        "category": "Web3",
        "website": "https://pintu.co.id/",
        "linkedin": "https://www.linkedin.com/company/pintu/",
        "careerPage": "https://pintu.co.id/careers"
    },
    "Modalku": {
        "category": "Fintech",
        "website": "https://www.modalku.com/",
        "linkedin": "https://www.linkedin.com/company/modalku/",
        "careerPage": "https://www.modalku.com/careers"
    },
    "Investree": {
        "category": "Fintech",
        "website": "https://investree.id/",
        "linkedin": "https://www.linkedin.com/company/investree/",
        "careerPage": "https://investree.id/careers"
    },
    "Kitabisa": {
        "category": "Social Impact",
        "website": "https://kitabisa.com/",
        "linkedin": "https://www.linkedin.com/company/kitabisa/",
        "careerPage": "https://kitabisa.com/careers"
    },
    "Lemonilo": {
        "category": "Ecommerce",
        "website": "https://www.lemonilo.com/",
        "linkedin": "https://www.linkedin.com/company/lemonilo/",
        "careerPage": "https://www.lemonilo.com/careers"
    },
    "Mamikos": {
        "category": "PropTech",
        "website": "https://mamikos.com/",
        "linkedin": "https://www.linkedin.com/company/mamikos/",
        "careerPage": "https://mamikos.com/careers"
    },
    "Kopi Kenangan": {
        "category": "F&B Tech",
        "website": "https://kopikenangan.com/",
        "linkedin": "https://www.linkedin.com/company/kopi-kenangan/",
        "careerPage": ""
    },
    "Fore Coffee": {
        "category": "F&B Tech",
        "website": "https://fore.coffee/",
        "linkedin": "https://www.linkedin.com/company/fore-coffee/",
        "careerPage": ""
    },
    "HappyFresh": {
        "category": "Ecommerce",
        "website": "https://www.happyfresh.com/",
        "linkedin": "https://www.linkedin.com/company/happyfresh/",
        "careerPage": "https://www.happyfresh.com/careers"
    },
    "Bobobox": {
        "category": "Travel",
        "website": "https://www.bobobox.co.id/",
        "linkedin": "https://www.linkedin.com/company/bobobox/",
        "careerPage": ""
    },
    "Cermati.com": {
        "category": "Fintech",
        "website": "https://www.cermati.com/",
        "linkedin": "https://www.linkedin.com/company/cermati/",
        "careerPage": ""
    },
    "DOKU": {
        "category": "Fintech",
        "website": "https://www.doku.com/",
        "linkedin": "https://www.linkedin.com/company/doku/",
        "careerPage": "https://www.doku.com/careers"
    },
    "Evermos": {
        "category": "Ecommerce",
        "website": "https://evermos.com/",
        "linkedin": "https://www.linkedin.com/company/evermos/",
        "careerPage": "https://evermos.com/careers"
    },
    "Female Daily Network": {
        "category": "Media",
        "website": "https://www.femaledaily.com/",
        "linkedin": "https://www.linkedin.com/company/female-daily-network/",
        "careerPage": ""
    },
    "Koinworks": {
        "category": "Fintech",
        "website": "https://koinworks.com/",
        "linkedin": "https://www.linkedin.com/company/koinworks/",
        "careerPage": "https://koinworks.com/careers"
    },
    "KlikDokter": {
        "category": "Health Care",
        "website": "https://www.klikdokter.com/",
        "linkedin": "https://www.linkedin.com/company/klikdokter/",
        "careerPage": ""
    },
    "Niagahoster": {
        "category": "SaaS",
        "website": "https://www.niagahoster.co.id/",
        "linkedin": "https://www.linkedin.com/company/niagahoster/",
        "careerPage": "https://www.niagahoster.co.id/careers"
    },
    "UniPin": {
        "category": "Gaming",
        "website": "https://www.unipin.com/",
        "linkedin": "https://www.linkedin.com/company/unipin/",
        "careerPage": ""
    },
    
    # SMALL START-UP
    "Kata.ai": {
        "category": "AI",
        "website": "https://kata.ai/",
        "linkedin": "https://www.linkedin.com/company/kata-ai/",
        "careerPage": "https://kata.ai/careers"
    },
    "Qiscus": {
        "category": "SaaS",
        "website": "https://www.qiscus.com/",
        "linkedin": "https://www.linkedin.com/company/qiscus/",
        "careerPage": "https://www.qiscus.com/careers"
    },
    "Reku": {
        "category": "Fintech",
        "website": "https://reku.id/",
        "linkedin": "https://www.linkedin.com/company/reku/",
        "careerPage": ""
    },
    "SoftwareSeni Indonesia": {
        "category": "IT Consulting",
        "website": "https://softwareseni.com/",
        "linkedin": "https://www.linkedin.com/company/softwareseni/",
        "careerPage": "https://softwareseni.com/careers"
    },
    "Suitmedia Digital Agency": {
        "category": "Digital Agency",
        "website": "https://suitmedia.com/",
        "linkedin": "https://www.linkedin.com/company/suitmedia/",
        "careerPage": "https://suitmedia.com/careers"
    },
    
    # BIG IT CONSULTING
    "Accenture": {
        "category": "IT Consulting",
        "website": "https://www.accenture.com/id-en",
        "linkedin": "https://www.linkedin.com/company/accenture/",
        "careerPage": "https://www.accenture.com/id-en/careers"
    },
    "Binar Academy": {
        "category": "EdTech",
        "website": "https://www.binaracademy.com/",
        "linkedin": "https://www.linkedin.com/company/binar-academy/",
        "careerPage": "https://www.binaracademy.com/careers"
    },
    "Xtremax": {
        "category": "IT Consulting",
        "website": "https://www.xtremax.com/",
        "linkedin": "https://www.linkedin.com/company/xtremax/",
        "careerPage": "https://www.xtremax.com/careers"
    },
    "Anabatic Technologies": {
        "category": "IT Consulting",
        "website": "https://www.anabatic.com/",
        "linkedin": "https://www.linkedin.com/company/anabatic-technologies/",
        "careerPage": "https://www.anabatic.com/careers"
    },
    "Mitra Integrasi Informatika": {
        "category": "IT Consulting",
        "website": "https://www.mii.co.id/",
        "linkedin": "https://www.linkedin.com/company/mitra-integrasi-informatika/",
        "careerPage": "https://www.mii.co.id/careers"
    },
    "Indocyber Global Teknologi": {
        "category": "IT Consulting",
        "website": "https://www.indocyber.co.id/",
        "linkedin": "https://www.linkedin.com/company/indocyber/",
        "careerPage": ""
    },
    
    # MEDIUM IT CONSULTING
    "CODE.ID": {
        "category": "IT Consulting",
        "website": "https://code.id/",
        "linkedin": "https://www.linkedin.com/company/code-id/",
        "careerPage": "https://code.id/careers"
    },
    
    # BANK / OTHER BIG COMPANY
    "BCA": {
        "category": "Banking",
        "website": "https://www.bca.co.id/",
        "linkedin": "https://www.linkedin.com/company/bank-central-asia/",
        "careerPage": "https://www.bca.co.id/id/tentang-bca/karir"
    },
    "BRI": {
        "category": "Banking",
        "website": "https://www.bri.co.id/",
        "linkedin": "https://www.linkedin.com/company/bank-rakyat-indonesia/",
        "careerPage": "https://www.bri.co.id/id/tentang-bri/karir"
    },
    "BNI": {
        "category": "Banking",
        "website": "https://www.bni.co.id/",
        "linkedin": "https://www.linkedin.com/company/bank-negara-indonesia/",
        "careerPage": "https://www.bni.co.id/id-id/tentang-bni/karir"
    },
    "Bank Mandiri": {
        "category": "Banking",
        "website": "https://www.bankmandiri.co.id/",
        "linkedin": "https://www.linkedin.com/company/bank-mandiri/",
        "careerPage": "https://www.bankmandiri.co.id/id/karir"
    },
    "Bank Jago": {
        "category": "Banking",
        "website": "https://www.jago.com/",
        "linkedin": "https://www.linkedin.com/company/bank-jago/",
        "careerPage": "https://www.jago.com/careers"
    },
    "Bank Neo Commerce": {
        "category": "Banking",
        "website": "https://www.neocommerce.co.id/",
        "linkedin": "https://www.linkedin.com/company/bank-neo-commerce/",
        "careerPage": ""
    },
    "CIMB Niaga": {
        "category": "Banking",
        "website": "https://www.cimbniaga.co.id/",
        "linkedin": "https://www.linkedin.com/company/cimb-niaga/",
        "careerPage": "https://www.cimbniaga.co.id/id/personal/careers"
    },
    "Telkom": {
        "category": "Telecommunications",
        "website": "https://www.telkom.co.id/",
        "linkedin": "https://www.linkedin.com/company/telkom-indonesia/",
        "careerPage": "https://www.telkom.co.id/id/about-us/people/career"
    },
    "Indosat": {
        "category": "Telecommunications",
        "website": "https://www.indosat.com/",
        "linkedin": "https://www.linkedin.com/company/indosat/",
        "careerPage": "https://www.indosat.com/careers"
    },
    "XL Axiata": {
        "category": "Telecommunications",
        "website": "https://www.xl.co.id/",
        "linkedin": "https://www.linkedin.com/company/xl-axiata/",
        "careerPage": "https://www.xl.co.id/careers"
    },
    "Smartfren Telecom": {
        "category": "Telecommunications",
        "website": "https://www.smartfren.com/",
        "linkedin": "https://www.linkedin.com/company/smartfren/",
        "careerPage": ""
    },
    "Astra International": {
        "category": "Conglomerate",
        "website": "https://www.astra.co.id/",
        "linkedin": "https://www.linkedin.com/company/astra-international/",
        "careerPage": "https://www.astra.co.id/careers"
    },
    "Deloitte": {
        "category": "Consulting",
        "website": "https://www2.deloitte.com/id/en.html",
        "linkedin": "https://www.linkedin.com/company/deloitte/",
        "careerPage": "https://www2.deloitte.com/id/en/careers.html"
    },
    "Biznet": {
        "category": "Telecommunications",
        "website": "https://www.biznetnetworks.com/",
        "linkedin": "https://www.linkedin.com/company/biznet/",
        "careerPage": "https://www.biznetnetworks.com/careers"
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

