# Quick Start Guide

## Setup (5 minutes)

### 1. Install Dependencies

```bash
# Clone the repository
git clone https://github.com/Samir-Guenchi/algeria-github-rankings.git
cd algeria-github-rankings

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Get GitHub Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name: "Algeria Rankings"
4. Select scopes: `read:user` and `public_repo`
5. Click "Generate token"
6. Copy the token

### 3. Configure Token

```bash
# Copy example env file
cp .env.example .env

# Edit .env file and add your token
# On Windows:
notepad .env
# On Linux/Mac:
nano .env
```

Add your token:
```
GITHUB_TOKEN=ghp_your_token_here
```

## Running the Project

### Option 1: Collect Data for Specific Wilaya (Fast Test)

```bash
# Test with Algiers (has most users)
python src/main.py --collect --wilaya "Algiers"

# Check collected data
dir data\raw\  # Windows
ls data/raw/   # Linux/Mac
```

### Option 2: Collect Data for All Wilayas (Takes Time)

```bash
# This will take several hours due to API rate limits
python src/main.py --collect-all
```

### Option 3: Generate Rankings from Collected Data

```bash
# Generate all rankings
python src/main.py --generate-all

# View generated rankings
dir rankings\  # Windows
ls rankings/   # Linux/Mac
```

### Option 4: Check Your API Rate Limit

```bash
python src/main.py --check-rate-limit
```

## Viewing Rankings

### Method 1: GitHub Pages (Recommended)

1. Push rankings to GitHub:
```bash
git add rankings/
git commit -m "Add rankings data"
git push origin master
```

2. Enable GitHub Pages:
   - Go to repository Settings
   - Scroll to "Pages"
   - Source: Deploy from branch
   - Branch: master, folder: /rankings
   - Save

3. View at: `https://samir-guenchi.github.io/algeria-github-rankings/`

### Method 2: Local Web Server

```bash
# Start simple HTTP server
cd rankings
python -m http.server 8000

# Open browser to:
# http://localhost:8000
```

### Method 3: View Markdown Files Directly

```bash
# Open in VS Code
code rankings/README.md

# Or view on GitHub
# https://github.com/Samir-Guenchi/algeria-github-rankings/tree/master/rankings
```

## Example Workflow

```bash
# 1. Check rate limit
python src/main.py --check-rate-limit

# 2. Collect data for test wilaya
python src/main.py --collect --wilaya "Algiers"

# 3. Generate rankings
python src/main.py --generate-all

# 4. View results
cd rankings
python -m http.server 8000
# Open http://localhost:8000 in browser

# 5. Push to GitHub
git add .
git commit -m "Update rankings"
git push origin master
```

## Automated Updates (GitHub Actions)

The project includes GitHub Actions workflow that:
- Runs daily at midnight
- Collects data for all wilayas
- Generates rankings
- Commits and pushes automatically

To enable:
1. Add `GITHUB_TOKEN` as repository secret
2. Push `.github/workflows/update-rankings.yml`
3. Rankings update automatically every day

## Troubleshooting

### Rate Limit Exceeded
```bash
# Check remaining requests
python src/main.py --check-rate-limit

# Wait 1 hour or use multiple tokens
```

### No Data Collected
```bash
# Check if location names are correct
# Some users might use different location formats
# Example: "Alger" vs "Algiers" vs "Algeria"
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## Next Steps

1. Customize `config/wilayas.json` to add more search terms
2. Adjust `minimum_thresholds` in config
3. Add more ranking categories
4. Create custom visualizations
5. Build REST API endpoints

## Support

- Issues: https://github.com/Samir-Guenchi/algeria-github-rankings/issues
- Email: samir.guenchi@ensia.edu.dz
