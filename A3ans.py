pip install Topsis-Akul-102103487
!topsis assignment3.csv "1,1,1" "+,+,+" output.csv
import matplotlib.pyplot as plt
import pandas as pd
ans = pd.read_csv('output.csv')
ans

#code to make bar graph
model_names = ans['Model Names']
topsis_scores = ans['TOPSIS_Score']
plt.figure(figsize=(10, 6))
colors = sns.color_palette('viridis', len(df[category_column]))
plt.bar(model_names, topsis_scores, color=colors)
plt.xlabel('Model Name')
plt.ylabel('Topsis Score')
plt.title('TOPSIS Evaluation for various text classification models - By Akul Vaishnavi (102103487)')
plt.tight_layout()
plt.show()
