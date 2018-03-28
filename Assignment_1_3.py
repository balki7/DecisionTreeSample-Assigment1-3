data = [[True, True, True],
        [True, True, False],
        [True, False, True],
        [True, False, False],
        [False, True, True],
        [False, True, False],
        [False, False, True],
        [False, False, False]]
result = ['No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No']
print(data)
print(result)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(data, result)
from sklearn import tree
with open("tree_representation.dot","w") as f:
    f = tree.export_graphviz(clf,feature_names=['A','B','C'],out_file=f)