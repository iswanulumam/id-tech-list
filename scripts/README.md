# Scripts

Scripts untuk mengelola data perusahaan teknologi Indonesia.

## Scripts Available

### 1. `parse_readme.py`
Mengkonversi README.md ke format JSON (`companies.json`) untuk lebih mudah dikelola.

**Usage:**
```bash
python scripts/parse_readme.py
```

### 2. `validate_data.py`
Memvalidasi data perusahaan dan mengecek inkonsistensi seperti:
- URL yang tidak valid
- Data yang hilang
- Duplikasi nama perusahaan

**Usage:**
```bash
python scripts/validate_data.py
```

### 3. `generate_readme.py`
Generate README.md dari `companies.json`. Berguna setelah mengupdate data di JSON.

**Usage:**
```bash
python scripts/generate_readme.py
```

## Workflow

1. Edit data di `companies.json` (lebih mudah daripada edit markdown)
2. Run `generate_readme.py` untuk update README.md
3. Run `validate_data.py` untuk memastikan tidak ada error

## Requirements

- Python 3.6+
- No external dependencies required (uses only standard library)

