from flask import Flask, render_template, request, jsonify
import json
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the EPF calculation function
from epf_simple_calculator import calculate_epf_maturity

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/epf-calculator')
def epf_calculator():
    return render_template('epf_calculator.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calculate-epf', methods=['POST'])
def calculate_epf():
    try:
        data = request.get_json()
        
        monthly_salary = float(data['monthly_salary'])
        current_age = int(data['current_age'])
        epf_contribution = float(data['epf_contribution'])
        annual_increase = float(data['annual_increase'])
        interest_rate = float(data['interest_rate'])
        retirement_age = int(data['retirement_age'])
        
        result = calculate_epf_maturity(
            monthly_salary=monthly_salary,
            current_age=current_age,
            epf_contribution_rate=epf_contribution,
            annual_salary_increase=annual_increase,
            annual_interest_rate=interest_rate,
            retirement_age=retirement_age
        )
        
        # Add year-wise data for bar chart
        result['yearly_data'] = []
        current_salary = monthly_salary
        epf_balance = 0
        
        for year in range(1, retirement_age - current_age + 1):
            yearly_contribution = current_salary * 12 * (epf_contribution / 100)
            interest_earned = epf_balance * (interest_rate / 100)
            epf_balance += yearly_contribution + interest_earned
            
            result['yearly_data'].append({
                'year': year,
                'age': current_age + year,
                'contribution': yearly_contribution,
                'interest': interest_earned,
                'balance': epf_balance
            })
            
            current_salary *= (1 + annual_increase / 100)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# This is required for Vercel
handler = app

if __name__ == '__main__':
    app.run(debug=True) 