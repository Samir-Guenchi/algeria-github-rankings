# Contributing to Algeria GitHub Rankings

Thank you for your interest in contributing to this project!

## How to Contribute

### Reporting Issues

- Check existing issues before creating a new one
- Provide clear description and steps to reproduce
- Include system information and error messages

### Adding New Features

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write tests for new functionality
5. Ensure all tests pass
6. Commit with clear messages (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Write comments for complex logic

### Testing

```bash
# Run tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

### Documentation

- Update README.md for user-facing changes
- Add docstrings for new functions/classes
- Update API documentation if applicable

## Development Setup

```bash
# Clone repository
git clone https://github.com/Samir-Guenchi/algeria-github-rankings.git
cd algeria-github-rankings

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Set up pre-commit hooks
pre-commit install
```

## Adding New Wilayas or Cities

Edit `config/wilayas.json`:

```json
{
  "code": "XX",
  "name_ar": "Arabic Name",
  "name_fr": "French Name",
  "name_en": "English Name",
  "cities": ["City1", "City2"],
  "search_terms": ["Term1", "Term2"]
}
```

## Questions?

Feel free to open an issue or contact:
- Email: samir.guenchi@ensia.edu.dz
- GitHub: @Samir-Guenchi

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Maintain professional communication

Thank you for contributing!
