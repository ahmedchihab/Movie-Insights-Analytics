import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Recréer la matrice de corrélation depuis ta table
corr = pd.DataFrame({
    'box_office': [1.00, 0.74, 0.24, 0.18, 0.01],
    'budget': [0.74, 1.00, 0.32, 0.08, -0.02],
    'duration': [0.24, 0.32, 1.00, 0.40, 0.28],
    'score': [0.18, 0.08, 0.40, 1.00, 0.40],
    'votes': [0.01, -0.02, 0.28, 0.40, 1.00]
}, index=['box_office', 'budget', 'duration', 'score', 'votes'])

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, linewidths=0.5, fmt=".2f")
plt.title('Heatmap de la matrice de corrélation')
# Sauvegarder l'image dans le même dossier que le script
plt.savefig(r"C:\Users\Galaxy\Downloads\Correlation movie\heatmap_correlation.png", dpi=300, bbox_inches='tight')

# Afficher l'image
plt.show()

# ===== 2) BUBBLE CHART =====
corr_long = corr.reset_index().melt(id_vars='index')
corr_long.columns = ['Var1', 'Var2', 'Correlation']

# Taille des bulles proportionnelle à la corrélation
corr_long['Size'] = corr_long['Correlation'].abs() * 1000

plt.figure(figsize=(8,6))
bubble = plt.scatter(
    x=corr_long['Var1'],
    y=corr_long['Var2'],
    s=corr_long['Size'],
    c=corr_long['Correlation'],
    cmap='coolwarm',
    alpha=0.7,
    edgecolors='black'
)

plt.colorbar(bubble, label='Correlation')
plt.title("Bubble Chart - Corrélation entre les variables")
plt.xticks(rotation=45)
plt.gca().set_aspect('equal')
plt.tight_layout()

# Enregistrer le bubble chart
plt.savefig(r"C:\Users\Galaxy\Downloads\Correlation movie\bubble_chart_correlation.png", dpi=300, bbox_inches='tight')
plt.show()
