# -*- coding: utf-8 -*-
"""Copy of Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uKS99LnfszpuweXcLJ5BbRG8z9ZVXkrQ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('conversion_data.csv')

df.head(2)

df.describe()

df['country'].value_counts()

df['source'].value_counts()

df['total_pages_visited'].hist()

df['country'].value_counts()

df.isnull().any()

df_onehot = pd.get_dummies(df, drop_first=True)
df_onehot.head()

y = df_onehot['converted']

x = df_onehot.drop(columns =['converted'])

from sklearn.model_selection import train_test_split

# Train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.25,
                                                    random_state=0)

# Normalize with Scikit Learn 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier()

classifier.fit(X_train, y_train)

classifier.predict(X_test)

classifier.score(X_test,y_test)

classifier.feature_importances_

from sklearn.metrics import roc_auc_score, roc_curve
y_predicted = classifier.predict_proba(X_test)[:, 1]

# Evaluate model
roc_auc = roc_auc_score(y_test, y_predicted.round(4))
print('Random Forest roc_auc_score metric: {}'.format(roc_auc))
                        
fpr, tpr, thresholds = roc_curve(y_test, y_predicted, pos_label=1)

plt.plot(fpr, tpr, lw=1, alpha=0.8, label='ROC {}'.format(roc_auc))
plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Random', alpha=.8)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show();

import seaborn as sns
### Plot the feature importances of the forest
rf_importances = pd.DataFrame(zip(x.columns, classifier.feature_importances_), columns= ['Variables', 'Importance']).sort_values( 'Importance', ascending=False)
plt.figure(figsize=(10,10))
plt.title("Feature importances")
ax = sns.barplot(x="Importance", y="Variables", data=rf_importances)
plt.show()

