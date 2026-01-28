"""
Generate demo data for Algeria GitHub Rankings
Creates realistic sample data for demonstration purposes
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Sample users data for demonstration
DEMO_USERS = [
    {
        "username": "demo_user_1",
        "name": "Ahmed Benali",
        "location": "Algiers, Algeria",
        "followers": 245,
        "public_repos": 42,
        "total_stars": 1250,
        "wilaya_code": "16",
        "wilaya_name": "Algiers",
        "bio": "Full Stack Developer | Open Source Contributor",
        "company": "Tech Startup"
    },
    {
        "username": "demo_user_2",
        "name": "Fatima Khelifi",
        "location": "Oran, Algeria",
        "followers": 189,
        "public_repos": 35,
        "total_stars": 890,
        "wilaya_code": "31",
        "wilaya_name": "Oran",
        "bio": "AI/ML Engineer | Python Developer",
        "company": "ENSIA"
    },
    {
        "username": "demo_user_3",
        "name": "Youcef Mansouri",
        "location": "Constantine, Algeria",
        "followers": 167,
        "public_repos": 28,
        "total_stars": 720,
        "wilaya_code": "25",
        "wilaya_name": "Constantine",
        "bio": "Backend Developer | DevOps Enthusiast",
        "company": "Freelance"
    },
    {
        "username": "demo_user_4",
        "name": "Amina Boudiaf",
        "location": "Tlemcen, Algeria",
        "followers": 143,
        "public_repos": 31,
        "total_stars": 650,
        "wilaya_code": "13",
        "wilaya_name": "Tlemcen",
        "bio": "Frontend Developer | UI/UX Designer",
        "company": "Digital Agency"
    },
    {
        "username": "demo_user_5",
        "name": "Karim Zerrouki",
        "location": "Sétif, Algeria",
        "followers": 128,
        "public_repos": 25,
        "total_stars": 580,
        "wilaya_code": "19",
        "wilaya_name": "Setif",
        "bio": "Mobile Developer | Flutter Expert",
        "company": "Startup"
    }
]

def generate_demo_rankings():
    """Generate demo ranking markdown files"""
    
    rankings_dir = Path("rankings")
    rankings_dir.mkdir(exist_ok=True)
    
    # Generate national ranking
    national_dir = rankings_dir / "national"
    national_dir.mkdir(exist_ok=True)
    
    national_content = f"""# Algeria GitHub Rankings - National

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

---

## Top GitHub Developers in Algeria

| Rank | User | Name | Location | Followers | Repos | Stars |
|------|------|------|----------|-----------|-------|-------|
| 1 | [@demo_user_1](https://github.com/demo_user_1) | Ahmed Benali | Algiers | 245 | 42 | 1250 |
| 2 | [@demo_user_2](https://github.com/demo_user_2) | Fatima Khelifi | Oran | 189 | 35 | 890 |
| 3 | [@demo_user_3](https://github.com/demo_user_3) | Youcef Mansouri | Constantine | 167 | 28 | 720 |
| 4 | [@demo_user_4](https://github.com/demo_user_4) | Amina Boudiaf | Tlemcen | 143 | 31 | 650 |
| 5 | [@demo_user_5](https://github.com/demo_user_5) | Karim Zerrouki | Sétif | 128 | 25 | 580 |

---

## Statistics

- Total Developers Tracked: 5
- Total Repositories: 161
- Total Stars: 4,090
- Total Followers: 872

---

**Note:** This is demo data. Run data collection to see real rankings.

[Back to Home](../index.html)
"""
    
    with open(national_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(national_content)
    
    # Generate by-category rankings
    category_dir = rankings_dir / "by-category"
    category_dir.mkdir(exist_ok=True)
    
    categories = [
        ("public_contributions", "Public Contributions"),
        ("followers", "Followers"),
        ("stars", "Repository Stars"),
        ("repositories", "Active Repositories")
    ]
    
    for cat_id, cat_name in categories:
        cat_content = f"""# Algeria GitHub Rankings - {cat_name}

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

---

## Top Developers by {cat_name}

| Rank | User | Name | Location | Followers | Repos | Stars |
|------|------|------|----------|-----------|-------|-------|
| 1 | [@demo_user_1](https://github.com/demo_user_1) | Ahmed Benali | Algiers | 245 | 42 | 1250 |
| 2 | [@demo_user_2](https://github.com/demo_user_2) | Fatima Khelifi | Oran | 189 | 35 | 890 |
| 3 | [@demo_user_3](https://github.com/demo_user_3) | Youcef Mansouri | Constantine | 167 | 28 | 720 |
| 4 | [@demo_user_4](https://github.com/demo_user_4) | Amina Boudiaf | Tlemcen | 143 | 31 | 650 |
| 5 | [@demo_user_5](https://github.com/demo_user_5) | Karim Zerrouki | Sétif | 128 | 25 | 580 |

---

**Note:** This is demo data. Run data collection to see real rankings.

[Back to Home](../index.html) | [All Categories](README.md)
"""
        
        with open(category_dir / f"{cat_id}.md", "w", encoding="utf-8") as f:
            f.write(cat_content)
    
    # Generate category index
    cat_index = f"""# Rankings by Category

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

---

## Available Categories

- [Public Contributions](public_contributions.md) - Open source contributions
- [Followers](followers.md) - Community influence
- [Repository Stars](stars.md) - Project quality
- [Active Repositories](repositories.md) - Project maintenance

---

[Back to Home](../index.html)
"""
    
    with open(category_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(cat_index)
    
    # Generate by-wilaya rankings (sample for major wilayas)
    wilaya_dir = rankings_dir / "by-wilaya"
    wilaya_dir.mkdir(exist_ok=True)
    
    major_wilayas = [
        ("16", "Algiers", "الجزائر", [DEMO_USERS[0]]),
        ("31", "Oran", "وهران", [DEMO_USERS[1]]),
        ("25", "Constantine", "قسنطينة", [DEMO_USERS[2]]),
        ("13", "Tlemcen", "تلمسان", [DEMO_USERS[3]]),
        ("19", "Sétif", "سطيف", [DEMO_USERS[4]])
    ]
    
    for code, name_en, name_ar, users in major_wilayas:
        wilaya_content = f"""# GitHub Rankings - {name_en} ({name_ar})

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

---

## Top Developers from {name_en}

| Rank | User | Name | Followers | Repos | Stars |
|------|------|------|-----------|-------|-------|
"""
        
        for i, user in enumerate(users, 1):
            wilaya_content += f"| {i} | [@{user['username']}](https://github.com/{user['username']}) | {user['name']} | {user['followers']} | {user['public_repos']} | {user['total_stars']} |\n"
        
        wilaya_content += f"""
---

**Note:** This is demo data. Run data collection to see real rankings.

[Back to Home](../index.html) | [All Wilayas](README.md)
"""
        
        with open(wilaya_dir / f"wilaya_{code}.md", "w", encoding="utf-8") as f:
            f.write(wilaya_content)
    
    # Generate wilaya index
    wilaya_index = f"""# Rankings by Wilaya

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

---

## Major Wilayas (Demo Data)

- [Algiers (16)](wilaya_16.md) - الجزائر
- [Oran (31)](wilaya_31.md) - وهران
- [Constantine (25)](wilaya_25.md) - قسنطينة
- [Tlemcen (13)](wilaya_13.md) - تلمسان
- [Sétif (19)](wilaya_19.md) - سطيف

---

**Note:** Run data collection to generate rankings for all 69 wilayas.

[Back to Home](../index.html)
"""
    
    with open(wilaya_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(wilaya_index)
    
    # Generate main README
    main_readme = f"""# Algeria GitHub Rankings

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

---

## Overview

Comprehensive rankings of GitHub developers across all 69 Algerian wilayas.

## Quick Links

- [National Rankings](national/README.md) - Top developers across Algeria
- [By Category](by-category/README.md) - Rankings by contribution type
- [By Wilaya](by-wilaya/README.md) - Regional rankings

## Statistics

- Developers Tracked: 5 (Demo)
- Wilayas Covered: 69
- Categories: 5
- Last Update: {datetime.now().strftime('%Y-%m-%d')}

---

**Note:** This is demo data for demonstration purposes. 

To generate real rankings:
1. Configure your GitHub token in `.env`
2. Run `python src/main.py --collect-all`
3. Run `python src/main.py --generate-all`

---

[View Web Interface](index.html) | [GitHub Repository](https://github.com/Samir-Guenchi/algeria-github-rankings)
"""
    
    with open(rankings_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(main_readme)
    
    print("✅ Demo rankings generated successfully!")
    print(f"📁 Location: {rankings_dir.absolute()}")
    print("🌐 Open rankings/index.html in your browser")

if __name__ == "__main__":
    generate_demo_rankings()
