# + tags=["parameters"]
upstream = NULL
product = NULL
# -


data(iris)
colnames(iris) = list('sepal_length', 'sepal_width','petal_length', 'petal_width', 'class')
dir.create('output')
write.csv(iris, product$data)