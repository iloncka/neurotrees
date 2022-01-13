import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

from sklearn.tree import _tree


def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    feature_names = [f.replace(" ", "_") for f in feature_names]
    result_code = "def predict({}):".format(", ".join(feature_names)) + "\n"

    def recurse(node, depth):
        recurse_code = ''
        indent = "    " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            recurse_code += ("{}if {} <= {}:".format(indent, name, np.round(threshold, 2))) + "\n"
            recurse_code += recurse(tree_.children_left[node], depth + 1) + "\n"
            recurse_code += ("{}else:  # if {} > {}".format(indent, name, np.round(threshold, 2))) + "\n"
            recurse_code += recurse(tree_.children_right[node], depth + 1)
            return recurse_code
        else:
            recurse_code += ("{}return {}".format(indent, str(tree_.value[node].tolist())))
            return recurse_code

    recurse_code = recurse(0, 1)
    return result_code + recurse_code


# Example of use
dataset_name = 'blood_transfusion'
data = pd.read_csv(f"datasets/numerical/{dataset_name}.csv")
label_col = "Class"
data_X = data.drop([label_col], axis=1)
data_y = data[label_col]
dtree = DecisionTreeClassifier()
dtree.fit(data_X, data_y)
print(export_text(dtree, feature_names=data_X.columns.to_list()))  # as text
fout = open(f'tree_code_{dataset_name}.py', 'w')
fout.write(tree_to_code(dtree, data_X.columns.to_list()))  # as python code
fout.close()
