import warnings
import pickle
import numpy as np
import pandas as pd
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)


data = pd.read_csv("Training.csv").dropna(axis = 1)
Sym_desc = pd.read_csv("Symptom_Description.csv")
Sym_pre = pd.read_csv("Symptom_Precaution.csv")

disease_counts = data["prognosis"].value_counts()
temp_df = pd.DataFrame({
	"Disease": disease_counts.index,
	"Counts": disease_counts.values
})


encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

X = data.iloc[:,:-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test =train_test_split(
X, y, test_size = 0.2, random_state = 24)

models = {
	"SVC":SVC(),
	"Gaussian NB":GaussianNB(),
	"Random Forest":RandomForestClassifier(random_state=18)
}

svm_model = SVC()
svm_model.fit(X_train.values, y_train)
preds = svm_model.predict(X_test.values)


nb_model = GaussianNB()
nb_model.fit(X_train.values, y_train)
preds = nb_model.predict(X_test.values)

rf_model = RandomForestClassifier(random_state=18)
rf_model.fit(X_train.values, y_train)
preds = rf_model.predict(X_test.values)


final_svm_model = SVC()
final_nb_model = GaussianNB()
final_rf_model = RandomForestClassifier(random_state=18)
final_svm_model.fit(X.values, y)
final_nb_model.fit(X.values, y)
final_rf_model.fit(X.values, y)

test_data = pd.read_csv("Testing.csv").dropna(axis=1)

test_X = test_data.iloc[:, :-1]
test_Y = encoder.transform(test_data.iloc[:, -1])

svm_preds = final_svm_model.predict(test_X.values)
nb_preds = final_nb_model.predict(test_X.values)
rf_preds = final_rf_model.predict(test_X.values)

final_preds = [mode([i,j,k])[0][0] for i,j,k in zip(svm_preds, nb_preds, rf_preds)]



symptoms = X.columns.values


symptom_index = {}
for index, value in enumerate(symptoms):
	symptom = " ".join([i.capitalize() for i in value.split("_")])
	symptom_index[symptom] = index

data_dict = {
	"symptom_index":symptom_index,
	"predictions_classes":encoder.classes_
}


def predictDisease(symptoms):
	symptoms = symptoms.split(",")
	input_data = [0] * len(data_dict["symptom_index"])
	for symptom in symptoms:
		index = data_dict["symptom_index"][symptom]
		input_data[index] = 1
		

	input_data = np.array(input_data).reshape(1,-1)
	
	
	rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
	nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
	svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]
	
	final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]
	
	if final_prediction in Sym_desc['Disease'].values:
		b = Sym_desc.loc[Sym_desc['Disease'] == final_prediction, 'description'].iloc[0]
	else:
		b = "No description found for predicted disease." 

	if final_prediction in Sym_pre['Disease'].values:
		c = Sym_pre.loc[Sym_pre['Disease'] == final_prediction, ['1', '2', '3', '4']].iloc[0]
	else:
		c = "No Precautions found for predicted disease."
	
	predictions = {"Disease": final_prediction,"Description": b,"Precaution": c.to_string()}
	
    
	return predictions



a = input("Enter the symptoms: ")
 
result = predictDisease(a)
print(result["Disease"])
print(result["Description"])
print(result["Precaution"])

