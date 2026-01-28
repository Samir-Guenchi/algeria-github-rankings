# How to Run Algeria GitHub Rankings

## For Users Who Want to View Rankings

### Option 1: View Online (Easiest - No Setup Required)

Once deployed, rankings will be available at:
**https://samir-guenchi.github.io/algeria-github-rankings/**

Just open the link in your browser!

### Option 2: View on GitHub

Go to: https://github.com/Samir-Guenchi/algeria-github-rankings/tree/master/rankings

Browse markdown files directly on GitHub.

---

## For Developers Who Want to Run Locally

### Quick Start (Windows)

1. **Download the project:**
```cmd
git clone https://github.com/Samir-Guenchi/algeria-github-rankings.git
cd algeria-github-rankings
```

2. **Get GitHub Token:**
   - Go to https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select: `read:user` and `public_repo`
   - Copy the token

3. **Configure:**
```cmd
copy .env.example .env
notepad .env
```
Add your token: `GITHUB_TOKEN=ghp_your_token_here`

4. **Run deployment script:**
```cmd
deploy.bat
```

5. **Choose option 4** to start web server

6. **Open browser:** http://localhost:8000

### Quick Start (Linux/Mac)

1. **Download the project:**
```bash
git clone https://github.com/Samir-Guenchi/algeria-github-rankings.git
cd algeria-github-rankings
```

2. **Get GitHub Token** (same as Windows above)

3. **Configure:**
```bash
cp .env.example .env
nano .env
```
Add your token: `GITHUB_TOKEN=ghp_your_token_here`

4. **Run deployment script:**
```bash
chmod +x deploy.sh
./deploy.sh
```

5. **Choose option 4** to start web server

6. **Open browser:** http://localhost:8000

---

## Deployment Options

### Option 1: GitHub Pages (Recommended for Public Access)

1. **Enable GitHub Pages:**
   - Go to repository Settings
   - Scroll to "Pages" section
   - Source: Deploy from branch
   - Branch: `master`
   - Folder: `/rankings`
   - Click Save

2. **Generate and push rankings:**
```bash
# Collect data (choose one wilaya for testing)
python src/main.py --collect --wilaya "Algiers"

# Generate rankings
python src/main.py --generate-all

# Push to GitHub
git add rankings/
git commit -m "Add rankings"
git push origin master
```

3. **Access at:** https://samir-guenchi.github.io/algeria-github-rankings/

### Option 2: Local Web Server

```bash
cd rankings
python -m http.server 8000
```
Open: http://localhost:8000

### Option 3: Automated Updates with GitHub Actions

1. **Add GitHub Token as Secret:**
   - Go to repository Settings
   - Secrets and variables > Actions
   - New repository secret
   - Name: `GH_TOKEN`
   - Value: Your GitHub token
   - Save

2. **Enable Actions:**
   - Go to Actions tab
   - Enable workflows

3. **Rankings update automatically every day at midnight UTC**

4. **Manual trigger:**
   - Go to Actions tab
   - Select "Update Algeria GitHub Rankings"
   - Click "Run workflow"

---

## Step-by-Step Collection Process

### Test with One Wilaya (5 minutes)

```bash
# 1. Check rate limit
python src/main.py --check-rate-limit

# 2. Collect data for Algiers (most users)
python src/main.py --collect --wilaya "Algiers"

# 3. Generate rankings
python src/main.py --generate-all

# 4. View results
cd rankings
python -m http.server 8000
```

### Collect All Wilayas (Several Hours)

```bash
# This takes time due to GitHub API rate limits
python src/main.py --collect-all

# Generate rankings
python src/main.py --generate-all
```

---

## Understanding the Output

### Directory Structure After Running:

```
algeria-github-rankings/
├── data/
│   └── raw/
│       ├── wilaya_01.json    # Raw data for Adrar
│       ├── wilaya_16.json    # Raw data for Algiers
│       └── ...               # Data for all wilayas
├── rankings/
│   ├── index.html            # Main web interface
│   ├── README.md             # Rankings overview
│   ├── by-category/
│   │   ├── public_contributions.md
│   │   ├── followers.md
│   │   └── ...
│   ├── by-wilaya/
│   │   ├── wilaya_01.md      # Rankings for Adrar
│   │   ├── wilaya_16.md      # Rankings for Algiers
│   │   └── ...
│   └── national/
│       └── README.md         # National rankings
```

### Viewing Rankings:

1. **Web Interface:** Open `rankings/index.html` in browser
2. **Markdown Files:** Open `.md` files in VS Code or text editor
3. **GitHub:** View directly on GitHub repository

---

## Troubleshooting

### "Rate limit exceeded"
```bash
# Check remaining requests
python src/main.py --check-rate-limit

# Wait 1 hour for reset, or use multiple tokens
```

### "No module named 'requests'"
```bash
# Install dependencies
pip install -r requirements.txt
```

### "GITHUB_TOKEN not found"
```bash
# Create .env file
cp .env.example .env

# Edit and add your token
notepad .env  # Windows
nano .env     # Linux/Mac
```

### "No data collected"
- Check if location names match in `config/wilayas.json`
- Some users use different location formats
- Try adding more search terms to config

### Port 8000 already in use
```bash
# Use different port
python -m http.server 8080
```

---

## API Rate Limits

- **Authenticated:** 5,000 requests/hour
- **Unauthenticated:** 60 requests/hour
- **Search API:** 30 requests/minute

**Tips:**
- Always use authentication token
- Add delays between requests (already implemented)
- Collect data for one wilaya at a time for testing
- Use GitHub Actions for automated collection

---

## Customization

### Add More Search Terms

Edit `config/wilayas.json`:
```json
{
  "code": "16",
  "name_en": "Algiers",
  "search_terms": ["Algiers", "Alger", "الجزائر", "Bab Ezzouar", "Hydra"]
}
```

### Adjust Minimum Thresholds

Edit `config/wilayas.json`:
```json
"minimum_thresholds": {
  "followers": 5,
  "public_contributions": 10,
  "repositories": 1
}
```

### Add New Ranking Categories

Edit `config/wilayas.json` and `src/processors/ranking_processor.py`

---

## Support

- **Issues:** https://github.com/Samir-Guenchi/algeria-github-rankings/issues
- **Email:** samir.guenchi@ensia.edu.dz
- **Documentation:** See README.md and CONTRIBUTING.md

---

## Quick Reference Commands

```bash
# Check rate limit
python src/main.py --check-rate-limit

# Collect specific wilaya
python src/main.py --collect --wilaya "Algiers"

# Collect all wilayas
python src/main.py --collect-all

# Generate rankings
python src/main.py --generate-all

# Start web server
cd rankings && python -m http.server 8000

# Deploy to GitHub
git add rankings/ && git commit -m "Update rankings" && git push
```

---

**Last Updated:** January 2025
