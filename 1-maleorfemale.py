from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

#[height,weight,shoe size]
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],
	[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],
	[171,75,42],[181,85,43]]

#label for each data point
Y = ['male','female','female','female','male','male',
	'male', 'female', 'male', 'female', 'male']

#split the data into test and training (30% for test)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)

def tree_model():
	#Initialize the decision tree model variable
	clf_tree = tree.DecisionTreeClassifier()

	#Train the algo with the data set
	clf_tree = clf_tree.fit(X_train,Y_train)

	#Validate the classifier
	accuracy = clf_tree.score(X_test,Y_test)

	# prediction = clf_tree.predict([[190,70,43]])
	
	return(str(accuracy))

def logistic():
	#Initialize the decision logistic regression model variable
	clf_log = LogisticRegression()

	#Train the algo with the data set
	clf_log = clf_log.fit(X_train,Y_train)

	#Validate the classifier
	accuracy = clf_log.score(X_test,Y_test)

	return(str(accuracy))

def gaussian():
	#Initialize the decision naive-bayes model variable
	clf_gauss = GaussianNB()

	#Train the algo with the data set
	clf_gauss = clf_gauss.fit(X_train,Y_train)

	#Validate the classifier
	accuracy = clf_gauss.score(X_test,Y_test)

	return(str(accuracy))

#Get the accuracy for all the models
acgaussian = float(gaussian())
aclogistic = float(logistic())
actree = float(tree_model())
ac = [actree,aclogistic,acgaussian]
models = ['tree_map','logistic','gaussian']

#Find the best module
max_accuracy = max(ac)
best_model = models[ac.index(max_accuracy)]

print('Accuracy for the tree model was: {:.0%}.'.format(actree))
print('Accuracy for the logistic regression model was: {:.0%}.'.format(aclogistic))
print('Accuracy for the naive-bayes model was: {:.0%}.'.format(acgaussian))
print('So, the best model was.... the {}!'.format(best_model))
