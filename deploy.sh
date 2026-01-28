#!/bin/bash

# Algeria GitHub Rankings - Deployment Script

echo "========================================="
echo "Algeria GitHub Rankings - Deployment"
echo "========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "ERROR: .env file not found!"
    echo "Please create .env file with your GITHUB_TOKEN"
    echo "Example: cp .env.example .env"
    exit 1
fi

# Check rate limit
echo ""
echo "Checking GitHub API rate limit..."
python src/main.py --check-rate-limit

# Ask user what to do
echo ""
echo "What would you like to do?"
echo "1) Collect data for specific wilaya (fast test)"
echo "2) Collect data for all wilayas (takes hours)"
echo "3) Generate rankings from existing data"
echo "4) Start web server to view rankings"
echo "5) Deploy to GitHub Pages"
read -p "Enter choice [1-5]: " choice

case $choice in
    1)
        read -p "Enter wilaya name (e.g., Algiers): " wilaya
        echo "Collecting data for $wilaya..."
        python src/main.py --collect --wilaya "$wilaya"
        echo "Generating rankings..."
        python src/main.py --generate-all
        echo "Done! View rankings in rankings/ folder"
        ;;
    2)
        echo "Collecting data for all 69 wilayas..."
        echo "This will take several hours due to API rate limits"
        read -p "Continue? (y/n): " confirm
        if [ "$confirm" = "y" ]; then
            python src/main.py --collect-all
            echo "Generating rankings..."
            python src/main.py --generate-all
            echo "Done!"
        fi
        ;;
    3)
        echo "Generating rankings..."
        python src/main.py --generate-all
        echo "Done! View rankings in rankings/ folder"
        ;;
    4)
        echo "Starting web server..."
        echo "Open http://localhost:8000 in your browser"
        cd rankings
        python -m http.server 8000
        ;;
    5)
        echo "Deploying to GitHub Pages..."
        git add rankings/
        git commit -m "Update rankings - $(date +'%Y-%m-%d %H:%M')"
        git push origin master
        echo ""
        echo "Done! Your rankings will be available at:"
        echo "https://samir-guenchi.github.io/algeria-github-rankings/"
        echo ""
        echo "Note: Enable GitHub Pages in repository settings if not already enabled"
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "========================================="
echo "Deployment complete!"
echo "========================================="
