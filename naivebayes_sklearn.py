from sklearn import datasets
news = datasets.fetch_20newsgroups(subset='all')
print(len(news.data))
print(news.data[0])


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=44)

vec = CountVectorizer()
X_train = vec.fit_transform(X_train)
X_test = vec.transform(X_test)

mnb = MultinomialNB()
mnb.fit(X_train, y_train)
y_predict = mnb.predict(X_test)

print('The Accuracy of Naive Bayes:', mnb.score(X_test, y_test))
print(classification_report(y_test, y_predict,target_names=news.target_names))