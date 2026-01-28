"""
Check data collection progress
"""

import json
from pathlib import Path

def check_progress():
    data_dir = Path("data/raw")
    
    if not data_dir.exists():
        print("❌ No data collected yet")
        return
    
    json_files = list(data_dir.glob("wilaya_*.json"))
    
    if not json_files:
        print("⏳ Collection in progress...")
        return
    
    print(f"✅ Data collected for {len(json_files)} wilayas")
    print()
    
    total_users = 0
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            users = json.load(f)
            wilaya_code = file.stem.split('_')[1]
            print(f"   Wilaya {wilaya_code}: {len(users)} developers")
            total_users += len(users)
    
    print()
    print(f"📊 Total developers: {total_users}")
    print()
    
    if total_users > 0:
        print("✅ Ready to generate rankings!")
        print("Run: python collect_real_data.py")

if __name__ == "__main__":
    check_progress()
