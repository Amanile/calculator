from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder='../templates')

# Embedded EPF calculation function
def calculate_epf_balance(monthly_salary=50000, current_age=30, retirement_age=60,
                         epf_contribution_rate=24, annual_salary_increase=5, annual_interest_rate=8.25):
    """
    Calculate EPF balance at retirement with year-wise breakdown
    """
    
    # Convert percentages to decimals
    epf_rate = epf_contribution_rate / 100
    salary_increase_rate = annual_salary_increase / 100
    interest_rate = annual_interest_rate / 100
    
    # Initialize variables
    current_salary = monthly_salary
    epf_balance = 0
    total_contribution = 0
    total_interest = 0
    yearly_breakdown = []
    
    # Calculate for each year until retirement
    years_to_retirement = retirement_age - current_age
    
    for year in range(1, years_to_retirement + 1):
        # Calculate annual contribution
        annual_contribution = current_salary * 12 * epf_rate
        
        # Calculate interest earned on previous balance
        interest_earned = epf_balance * interest_rate
        
        # Update EPF balance
        epf_balance += annual_contribution + interest_earned
        
        # Update totals
        total_contribution += annual_contribution
        total_interest += interest_earned
        
        # Store yearly data
        yearly_breakdown.append({
            'year': year,
            'age': current_age + year,
            'annual_salary': current_salary * 12,
            'monthly_salary': current_salary,
            'annual_contribution': annual_contribution,
            'interest_earned': interest_earned,
            'epf_balance': epf_balance
        })
        
        # Increase salary for next year
        current_salary *= (1 + salary_increase_rate)
    
    # Calculate final amounts
    final_epf_amount = epf_balance
    
    return {
        'final_epf_amount': final_epf_amount,
        'total_contribution': total_contribution,
        'total_interest': total_interest,
        'total_years': years_to_retirement,
        'yearly_breakdown': yearly_breakdown,
        'summary': {
            'monthly_salary': monthly_salary,
            'current_age': current_age,
            'retirement_age': retirement_age,
            'epf_contribution_rate': epf_contribution_rate,
            'annual_salary_increase': annual_salary_increase,
            'annual_interest_rate': annual_interest_rate
        }
    }

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
        
        result = calculate_epf_balance(
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

# Vercel entry point - Flask app will be automatically detected
if __name__ == '__main__':
    app.run(debug=True) 