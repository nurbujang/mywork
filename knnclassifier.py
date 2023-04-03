# trimmed from project

from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from sklearn.inspection import DecisionBoundaryDisplay

ir = datasets.load_iris() # load dataset from sklearn
k = 7 # decide on the number of neighbor (k)
X = ir.data[:,:2] # use the first 2 columns (sepal length and sepal width) as a 2 dimensional dataset
y = ir.target
targets = ir.target_names# define target name (species name)
print(targets) # print target name (species name)

# Create color maps
cmap_light = ListedColormap(["mediumorchid", "orange", "steelblue"]) # define boundary area color
cmap_bold = ["fuchsia", "darkorange", "navy"] # define 

for weights in ["uniform", "distance"]: # (distance=closer neighbor weighted more than farther ones and uniform=all points are weighted equally
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(k, weights=weights) # define classifier
    clf.fit(X, y)
    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(clf, X, cmap=cmap_light, ax=ax, response_method="predict", plot_method="pcolormesh", xlabel=ir.feature_names[0], ylabel=ir.feature_names[1], shading="auto")
# clf =
# X =
# cmap=cmap_light =
# ax=ax =
# response_method="predict" =
# plot_method="pcolormesh" =
# xlabel=ir.feature_names[0] =
# ylabel=ir.feature_names[1] =
# shading="auto" =

    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=ir.target_names[y], palette=cmap_bold, alpha=1.0, edgecolor="black") # Plot the Training plots (points)
    plt.title("3-Class classification (k = %i, weights = '%s')" % (k, weights))
# x=X[:, 0] =
# y=X[:, 1] =
# hue =
# palette=cmap_bold =
# alpha=1.0 =
# edgecolor="black" =
# %i =
# %s =
plt.show() # show plot
# outputs 2 plots (distance and uniform), and Iris setosa is distinctly different from others based on sepal attribute