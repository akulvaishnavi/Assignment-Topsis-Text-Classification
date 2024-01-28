pip install Topsis-Akul-102103487
!topsis assignment3.csv "1,1,1" "+,+,+" output.csv
import matplotlib.pyplot as plt
import pandas as pd
ans = pd.read_csv('output.csv')
ans

model_names = ans['Model Names']
topsis_scores = ans['TOPSIS_Score']
