# + tags=["parameters"]
upstream = list('raw')
product = NULL
# -


df = read.csv(upstream$raw$data)

write.csv(df, product$data)