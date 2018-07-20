#%%
from sklearn.datasets import make_moons

X,Y = make_moons(n_samples=10000,noise=0.4,random_state=42)
print(X)
print(Y)

#%%
from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test= train_test_split(
    X,Y,test_size=0.2,random_state=42)
print(X_train)
print(Y_train)

#%%
def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())
    
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier


param_grid = [
    {'max_depth':[2,5,10,20],
    'max_leaf_nodes':[5,10,15,20,50],
    'min_impurity_split':[0.2,0.3,0.4]}
]
decision_tree_cls = DecisionTreeClassifier()
_search = GridSearchCV(decision_tree_cls, param_grid, cv=10,
scoring='neg_mean_squared_error')
_search.fit(X_train, Y_train)
_search.best_params_

#%%
# from sklearn.model_selection import RandomizedSearchCV
# _search = RandomizedSearchCV(decision_tree_cls, 
#             param_distributions=param_grid,
#             n_iter=50, cv=5, scoring='neg_mean_squared_error',
#             verbose=2, n_jobs=4, random_state=42)
# _search.fit(X_train, Y_train)
# _search.best_params_


#%%
from sklearn.metrics import mean_squared_error
import numpy as np
final_model = _search.best_estimator_
prediction = final_model.predict(X_test)
mse = mean_squared_error(Y_test,prediction)
rmse = np.sqrt(mse)
rmse
# scores_forest = cross_val_score(grid_search)
#  cv=10)

