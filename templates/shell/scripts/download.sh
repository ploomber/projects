# use product (inside curly brackets) as a placeholder. When executing your
# script, ploomber replaces this with the value declared in the pipeline.yaml
# file. If your task generates more than one product use product[product_key]
mkdir -p output
curl https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv -o {{product}}