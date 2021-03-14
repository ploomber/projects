# + tags=["parameters"]
upstream = NULL
product = NULL
# -


df = read.csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
header=FALSE)
colnames(df) = list('sepal_length', 'sepal_width','petal_length', 'petal_width', 'class')

write.csv(df, product$data)