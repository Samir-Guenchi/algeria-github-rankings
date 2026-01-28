@echo off
REM Algeria GitHub Rankings - Deployment Script for Windows

echo =========================================
echo Algeria GitHub Rankings - Deployment
echo =========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Check if .env exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please create .env file with your GITHUB_TOKEN
    echo Example: copy .env.example .env
    pause
    exit /b 1
)

REM Check rate limit
echo.
echo Checking GitHub API rate limit...
python src/main.py --check-rate-limit

REM Ask user what to do
echo.
echo What would you like to do?
echo 1) Collect data for specific wilaya (fast test)
echo 2) Collect data for all wilayas (takes hours)
echo 3) Generate rankings from existing data
echo 4) Start web server to view rankings
echo 5) Deploy to GitHub Pages
set /p choice="Enter choice [1-5]: "

if "%choice%"=="1" (
    set /p wilaya="Enter wilaya name (e.g., Algiers): "
    echo Collecting data for %wilaya%...
    python src/main.py --collect --wilaya "%wilaya%"
    echo Generating rankings...
    python src/main.py --generate-all
    echo Done! View rankings in rankings\ folder
    goto end
)

if "%choice%"=="2" (
    echo Collecting data for all 69 wilayas...
    echo This will take several hours due to API rate limits
    set /p confirm="Continue? (y/n): "
    if /i "%confirm%"=="y" (
        python src/main.py --collect-all
        echo Generating rankings...
        python src/main.py --generate-all
        echo Done!
    )
    goto end
)

if "%choice%"=="3" (
    echo Generating rankings...
    python src/main.py --generate-all
    echo Done! View rankings in rankings\ folder
    goto end
)

if "%choice%"=="4" (
    echo Starting web server...
    echo Open http://localhost:8000 in your browser
    cd rankings
    python -m http.server 8000
    goto end
)

if "%choice%"=="5" (
    echo Deploying to GitHub Pages...
    git add rankings/
    git commit -m "Update rankings - %date% %time%"
    git push origin master
    echo.
    echo Done! Your rankings will be available at:
    echo https://samir-guenchi.github.io/algeria-github-rankings/
    echo.
    echo Note: Enable GitHub Pages in repository settings if not already enabled
    goto end
)

echo Invalid choice
exit /b 1

:end
echo.
echo =========================================
echo Deployment complete!
echo =========================================
pause
