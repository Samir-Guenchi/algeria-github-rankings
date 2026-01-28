# 🚀 START HERE - Get Real Rankings in 10 Minutes

## Step 1: Get Your GitHub Token (2 minutes)

1. Open: https://github.com/settings/tokens
2. Click **"Generate new token (classic)"**
3. Give it a name: `Algeria Rankings`
4. Check these boxes:
   - ✅ `read:user`
   - ✅ `public_repo`
5. Click **"Generate token"** at the bottom
6. **COPY THE TOKEN** (you won't see it again!)

## Step 2: Add Your Token (1 minute)

Open the `.env` file in this folder and replace `your_token_here` with your token:

```
GITHUB_TOKEN=ghp_your_actual_token_here
```

Save the file.

## Step 3: Install Dependencies (2 minutes)

Open terminal in this folder and run:

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 4: Collect Real Data (5 minutes)

Run this command:

```bash
python collect_real_data.py
```

This will:
- Collect data from 10 major Algerian wilayas
- Find real GitHub developers
- Generate rankings automatically
- Create beautiful web pages

## Step 5: View Your Rankings

After collection completes:

```bash
cd rankings
python -m http.server 8000
```

Open your browser: **http://localhost:8000**

## Step 6: Deploy to GitHub Pages (Share on LinkedIn!)

```bash
git add .
git commit -m "Add real Algeria GitHub rankings"
git push origin master
```

Then:
1. Go to your repository on GitHub
2. Click **Settings** > **Pages**
3. Source: **Deploy from branch**
4. Branch: **master**
5. Folder: **/rankings**
6. Click **Save**

Your site will be live at:
**https://samir-guenchi.github.io/algeria-github-rankings/**

---

## Troubleshooting

### "Rate limit exceeded"
Wait 1 hour or the script will automatically handle it.

### "No developers found"
Some wilayas have few developers. The script focuses on major cities first.

### "Token invalid"
Make sure you copied the entire token including `ghp_` prefix.

### Need help?
- Check: HOW_TO_RUN.md
- Email: samir.guenchi@ensia.edu.dz

---

## What You'll Get

✅ Real GitHub developer rankings  
✅ Data from 10 major Algerian wilayas  
✅ Professional web interface  
✅ Ready to share on LinkedIn  
✅ Automatic daily updates (via GitHub Actions)  

---

**Time to complete: ~10 minutes**  
**Result: Professional portfolio project ready to share!**
