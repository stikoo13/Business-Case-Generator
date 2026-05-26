# financial_model.py
# This file does all the financial calculations for the business case

def calculate_financials(cost, annual_benefit, years, discount_rate=0.10):
    
    results = {}

    # ROI calculation
    # Formula: ((Total benefit - Cost) / Cost) x 100
    total_benefit = annual_benefit * years
    results['roi_percent'] = round(((total_benefit - cost) / cost) * 100, 1)

    # Payback period calculation
    # Formula: Cost / Annual benefit
    results['payback_years'] = round(cost / annual_benefit, 1)

    # NPV calculation
    # Formula: Add up discounted benefits each year, then subtract cost
    npv = -cost
    for year in range(1, years + 1):
        npv += annual_benefit / ((1 + discount_rate) ** year)
    results['npv'] = round(npv, 0)

    # Year by year data for the chart
    cumulative = -cost
    results['yearly_data'] = []
    for year in range(1, years + 1):
        cumulative += annual_benefit
        results['yearly_data'].append({
            'year': f'Year {year}',
            'cumulative_net': round(cumulative, 0),
            'annual_benefit': annual_benefit,
            'cost_line': cost
        })

    return results