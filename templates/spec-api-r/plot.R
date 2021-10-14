# + tags=["parameters"]
upstream = list('clean')
product = NULL
# -

# +
df = read.csv(upstream$clean$data)
head(df)

# +
hist(df$sepal_length)