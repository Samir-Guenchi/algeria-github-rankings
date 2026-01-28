# Algeria GitHub Rankings

**Comprehensive GitHub user rankings for all 69 Algerian wilayas**

A data-driven platform to discover and rank the most active GitHub developers across Algeria, organized by wilaya (province) with advanced filtering and search capabilities.

---

## Overview

This project provides detailed rankings of GitHub users in Algeria, covering all 69 wilayas with multiple ranking criteria:

- Public contributions
- Total contributions
- Followers count
- Repository stars
- Active repositories

**Key Features:**
- Complete coverage of all 69 Algerian wilayas
- Multiple ranking categories
- Clean, accessible interface following HCI principles
- Automated daily updates
- RESTful API for data access
- Interactive visualizations

---

## Project Structure

```
algeria-github-rankings/
├── src/
│   ├── collectors/          # GitHub API data collection
│   ├── processors/          # Data processing and ranking
│   ├── generators/          # Markdown and HTML generation
│   └── api/                 # REST API endpoints
├── data/
│   ├── raw/                 # Raw GitHub API responses
│   ├── processed/           # Processed ranking data
│   └── cache/               # API response cache
├── rankings/
│   ├── by-wilaya/           # Rankings per wilaya
│   ├── by-category/         # Rankings by contribution type
│   └── national/            # National rankings
├── web/
│   ├── static/              # CSS, JS, images
│   └── templates/           # HTML templates
├── config/
│   └── wilayas.json         # All 69 wilayas configuration
└── tests/                   # Unit and integration tests
```

---

## HCI Design Principles Applied

### 1. Visibility of System Status
- Real-time update timestamps
- Loading indicators during data fetch
- Clear status messages

### 2. Match Between System and Real World
- Algerian wilaya names in Arabic and French
- Familiar geographic organization
- Natural ranking categories

### 3. User Control and Freedom
- Multiple filtering options
- Search functionality
- Easy navigation between wilayas
- Export data capabilities

### 4. Consistency and Standards
- Uniform table layouts
- Consistent color schemes
- Standard GitHub terminology

### 5. Error Prevention
- Input validation
- Clear error messages
- Graceful API failure handling

### 6. Recognition Rather Than Recall
- Visual indicators for rankings
- Clear labels and headers
- Breadcrumb navigation

### 7. Flexibility and Efficiency
- Quick filters
- Keyboard shortcuts
- API for programmatic access

### 8. Aesthetic and Minimalist Design
- Clean tables without clutter
- Essential information only
- Professional color palette

### 9. Error Recovery
- Helpful error messages
- Suggestions for corrections
- Fallback data sources

### 10. Help and Documentation
- Clear README
- API documentation
- Usage examples

---

## Installation

```bash
# Clone repository
git clone https://github.com/Samir-Guenchi/algeria-github-rankings.git
cd algeria-github-rankings

# Install dependencies
pip install -r requirements.txt

# Configure GitHub token
cp .env.example .env
# Edit .env and add your GitHub token
```

---

## Usage

### Collect Data

```bash
# Collect data for all wilayas
python src/main.py --collect-all

# Collect data for specific wilaya
python src/main.py --collect --wilaya "Algiers"

# Update existing data
python src/main.py --update
```

### Generate Rankings

```bash
# Generate all rankings
python src/main.py --generate-all

# Generate specific category
python src/main.py --generate --category "public-contributions"
```

### Start Web Interface

```bash
# Start local server
python src/main.py --serve

# Access at http://localhost:8000
```

---

## Configuration

### GitHub Token

Create a GitHub Personal Access Token with `read:user` and `public_repo` permissions.

Add to `.env`:
```
GITHUB_TOKEN=your_token_here
```

### Wilaya Configuration

All 69 wilayas are configured in `config/wilayas.json` with:
- Wilaya code (01-69)
- Arabic name
- French name
- Major cities
- Search terms

---

## API Endpoints

```
GET /api/v1/rankings/national
GET /api/v1/rankings/wilaya/{code}
GET /api/v1/rankings/category/{category}
GET /api/v1/user/{username}
GET /api/v1/stats/overview
```

---

## Ranking Categories

1. **Public Contributions** - Open source contributions
2. **Total Contributions** - All contributions including private
3. **Followers** - Community influence
4. **Stars** - Repository quality
5. **Active Repositories** - Project maintenance

---

## All 69 Wilayas Covered

01. Adrar | 02. Chlef | 03. Laghouat | 04. Oum El Bouaghi | 05. Batna
06. Béjaïa | 07. Biskra | 08. Béchar | 09. Blida | 10. Bouira
11. Tamanrasset | 12. Tébessa | 13. Tlemcen | 14. Tiaret | 15. Tizi Ouzou
16. Alger | 17. Djelfa | 18. Jijel | 19. Sétif | 20. Saïda
21. Skikda | 22. Sidi Bel Abbès | 23. Annaba | 24. Guelma | 25. Constantine
26. Médéa | 27. Mostaganem | 28. M'Sila | 29. Mascara | 30. Ouargla
31. Oran | 32. El Bayadh | 33. Illizi | 34. Bordj Bou Arréridj | 35. Boumerdès
36. El Tarf | 37. Tindouf | 38. Tissemsilt | 39. El Oued | 40. Khenchela
41. Souk Ahras | 42. Tipaza | 43. Mila | 44. Aïn Defla | 45. Naâma
46. Aïn Témouchent | 47. Ghardaïa | 48. Relizane | 49. Timimoun | 50. Bordj Badji Mokhtar
51. Ouled Djellal | 52. Béni Abbès | 53. In Salah | 54. In Guezzam | 55. Touggourt
56. Djanet | 57. El M'Ghair | 58. El Meniaa | 59. Ouargla | 60. Timimoun
61. Bordj Badji Mokhtar | 62. Ouled Djellal | 63. Béni Abbès | 64. In Salah | 65. In Guezzam
66. Touggourt | 67. Djanet | 68. El M'Ghair | 69. El Meniaa

---

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT License - See [LICENSE](LICENSE) for details

---

## Acknowledgments

- GitHub API for data access
- Algerian developer community
- Inspired by gayanvoice/top-github-users

---

## Contact

**Samir Guenchi**  
AI Engineer & Arabic NLP Researcher  
ENSIA - Algeria

- GitHub: [@Samir-Guenchi](https://github.com/Samir-Guenchi)
- Email: samir.guenchi@ensia.edu.dz
- LinkedIn: [guenchi-samir](https://linkedin.com/in/guenchi-samir)

---

**Last Updated:** January 2025
