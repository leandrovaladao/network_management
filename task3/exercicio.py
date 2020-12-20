import warnings

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from pandas import read_csv


def extract_file_x():
    return read_csv('../X.csv')


def extract_file_y():
    return read_csv('../Y.csv')


BASE_DIRECTORY = '../plots/task2/'


def do_logistic_regression():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        #Task 3
        #Execicio 1
        x = extract_file_x()
        y = extract_file_y()

        normalized_dispframes = []
        for i in y['DispFrames']:
            normalized_dispframes.append(1 if i >= 18 else 0)

        train_x, test_x, train_y, test_y = train_test_split(x, normalized_dispframes, test_size=0.3)

        classifier = LogisticRegression()

        tmp_train_x = train_x.iloc[:, 2:10]
        tmp_test_x = test_x.iloc[:, 2:10]

        classifier.fit(tmp_train_x, train_y)

        print("Coeficients: ", classifier.coef_)

        #Exercicio 2
        predict_y = classifier.predict(tmp_test_x)

        calculated_confusion_matrix = confusion_matrix(test_y, predict_y)

        tn, tp = calculated_confusion_matrix[0][0], calculated_confusion_matrix[1][1]

        print("\nConfusion matrix:\n", calculated_confusion_matrix)

        err = 1-((tp+tn)/len(tmp_test_x))

        print("\nErr: ", err)

        #Exercicio 3
        amount_true = sum(normalized_dispframes)
        naive_true_p = amount_true/len(normalized_dispframes)
        naive_false_p = 1-naive_true_p

        amount_true_predict_y = sum(predict_y)
        predict_true = amount_true_predict_y / len(predict_y)
        predict_false = 1 - predict_true

        print("\nNaive True: {}\nNaive False: {}\nPredict True: {}\nPredict False: {}\n".format(naive_true_p, naive_false_p, predict_true, predict_false))

        #Exercicio 4
        x['DispFrames'] = y['DispFrames']

        train_x, test_x = train_test_split(x, test_size=0.3)

        tmp_train_x = train_x.iloc[:, 2:10]
        tmp_test_x = test_x.iloc[:, 2:10]

        model = LinearRegression()

        model.fit(tmp_train_x, train_x['DispFrames'])

        predict_results = model.predict(tmp_test_x)

        predicted_linear_regression = []
        normalized_linear_regression = []
        for predict_result in predict_results:
            predicted_linear_regression.append('conformance' if predict_result >= 18 else 'violation')
            normalized_linear_regression.append(1 if predict_result >= 18 else 0)

        new_classifier = LogisticRegression()

        new_classifier.fit(tmp_test_x, predicted_linear_regression)

        print("Coeficients new classifier: ", new_classifier.coef_)

        new_predict_y = classifier.predict(tmp_test_x)

        new_calculated_confusion_matrix = confusion_matrix(test_y, new_predict_y)

        tn, tp = new_calculated_confusion_matrix[0][0], new_calculated_confusion_matrix[1][1]

        print("\nConfusion matrix new classifier:\n", new_calculated_confusion_matrix)

        err = 1 - ((tp + tn) / len(tmp_test_x))

        print("\nErr new classifier: ", err)


do_logistic_regression()
