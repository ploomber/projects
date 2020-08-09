# + tags=["parameters"]

# -

df = read.csv(upstream[['upvotes-dump']])
head(df)

hist(df$mean_upvotes)


