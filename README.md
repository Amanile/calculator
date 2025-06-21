# EPF Calculator Web Application

A responsive Employees' Provident Fund (EPF) Calculator built with Python Flask and Tailwind CSS, inspired by the design style of emicalculator.net.

## Features

- 🧮 **Accurate EPF Calculations**: Calculate your EPF maturity amount using compound interest
- 📊 **Interactive Charts**: Visual representation of EPF growth with line and bar charts
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- 💰 **Indian Currency Format**: All amounts displayed with Indian Rupee (₹) symbol
- 📈 **Year-wise Breakdown**: Detailed table showing annual contributions, interest, and balance
- 🎨 **Modern UI**: Clean and modern interface with smooth animations
- 📋 **Tab Navigation**: Easy navigation between Home, EPF Calculator, and About pages

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: Tailwind CSS
- **Charts**: Chart.js
- **Icons**: Heroicons (via Tailwind CSS)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd calculator
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv epf_calculator_env
   source epf_calculator_env/bin/activate  # On Windows: epf_calculator_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

## Usage

### EPF Calculator Inputs

- **Monthly Salary (Basic + DA)**: Your monthly basic salary plus dearness allowance
- **Current Age**: Your current age in years
- **Contribution to EPF (%)**: Total EPF contribution percentage (default: 24% - 12% employee + 12% employer)
- **Annual Salary Increase (%)**: Expected annual increment in salary
- **Rate of Interest (%)**: Current EPF interest rate (default: 8.25% for FY 2023-24)
- **Retirement Age**: Age at which you plan to retire

### Results

The calculator provides:

1. **Summary Cards**:
   - Final EPF maturity amount
   - Total contributions made
   - Total interest earned

2. **Interactive Charts**:
   - Line chart showing EPF growth over time
   - Bar chart for year-wise comparison
   - Toggle between chart types

3. **Detailed Table**:
   - Year-wise breakdown of contributions
   - Annual interest earned
   - Running EPF balance

## EPF Calculation Logic

The calculator uses the following formula for EPF calculation:

1. **Annual Contribution** = Monthly Salary × 12 × (EPF Contribution Rate / 100)
2. **Interest Earned** = Previous Year Balance × (Interest Rate / 100)
3. **New Balance** = Previous Balance + Annual Contribution + Interest Earned
4. **Salary Growth** = Previous Salary × (1 + Annual Increase Rate / 100)

## File Structure

```
calculator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    ├── base.html         # Base template with common layout
    ├── index.html        # Home page
    ├── epf_calculator.html # EPF calculator page
    └── about.html        # About page
```

## API Endpoints

- `GET /` - Home page
- `GET /epf-calculator` - EPF calculator page
- `GET /about` - About page
- `POST /calculate-epf` - API endpoint for EPF calculations (JSON)

## Browser Support

- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This calculator provides estimated calculations based on the inputs provided and current EPF rules. Actual EPF returns may vary due to changes in interest rates, government policies, and individual circumstances. Please consult with financial advisors or EPFO officials for personalized advice and accurate information about your EPF account.

## Support

If you encounter any issues or have questions, please:

1. Check the existing issues in the repository
2. Create a new issue with detailed information
3. Include steps to reproduce the problem

---

**Happy Calculating! 🎯** 