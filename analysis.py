import pandas
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

files = ['results_orig.csv', 'results_f3.csv', 'results_2c.csv', 'results_ev.csv', 'results_all.csv']
labels = ['Baseline', 'Flip 3', '2nd chance', 'EV', 'All combined']
var_win_rates = []
baseline_win_rates = []

for i in range(len(files)):
    df = pandas.read_csv(files[i], skipfooter = 1, engine = 'python')
    print(f'-----Baseline vs. {labels[i]}-----')
    print()
    
    var_win_rates.append((df['Winner'] == 'variant').sum() / 10)
    baseline_win_rates.append((df['Winner'] == 'baseline').sum() / 10)

    print('Total wins (%):')
    print(df['Winner'].value_counts())
    print()

    print('Average scores:')
    print(df[['Baseline score', 'Variant score']].mean())
    print()

    print('Standard deviation:')
    print(df[['Baseline score', 'Variant score']].std())
    print()

    print('Winning margins:') # how much you win by on average if you win
    baseline_wins_df = df[df['Winner'] == 'baseline']
    print('Baseline:')
    print(baseline_wins_df['Baseline score'].mean() - baseline_wins_df['Variant score'].mean())
    variant_wins_df = df[df['Winner'] == 'variant']
    print('Variant:')
    print(variant_wins_df['Variant score'].mean() - variant_wins_df['Baseline score'].mean())
    print()
    
    
#----------------------------------------------------------


plt.bar(labels, var_win_rates)
plt.title('Variant win rate by strategy')
plt.xlabel('Variant strategey')
plt.ylabel('Variant win rate (%)')
plt.show()
plt.bar(labels, baseline_win_rates)
plt.title('Baseline win rate by variant strategy')
plt.xlabel('Variant strategey')
plt.ylabel('Baseline win rate (%)')
plt.show()

for i in range(len(files)):
    df = pandas.read_csv(files[i], skipfooter = 1, engine = 'python')
    df['margins'] = df['Variant score'] - df['Baseline score']
    plt.hist(df['margins'], bins=50)
    plt.title(f'Baseline vs. {labels[i]} Margin Distribution')
    plt.xlabel("Variant's winning margin")
    plt.ylabel('Frequency')
    plt.axvline(x=0, color = 'red')
    plt.show()
    
    
#----------------------------------------------------------


var_wins = []
for i in range(len(var_win_rates)):
    var_wins.append(var_win_rates[i]*10)
for i in range(1, len(var_wins)):
    table = [[var_wins[0], 1000-var_wins[0]], [var_wins[i], 1000-var_wins[i]]]
    chi2_stat, p_value, degrees_of_freedom, expected_table = chi2_contingency(table)
    print(p_value)
