# CO2 emissions (metric tons per capita)

Contributed by [Henrique Oliveira](https://www.linkedin.com/in/henrique-meira-de-oliveira-4b381232/)

Animated plot using pandas, matplotlib and moviepy.

Output (compressed, actual output is in high-resolution):

![final-compressed](final-compressed.gif)

Data source: [World Bank](https://data.worldbank.org/indicator/EN.ATM.CO2E.PC?end=2014&start=2014&view=bar)

## Build project

Requirements: [miniconda](https://docs.conda.io/en/latest/miniconda.html)


```sh
# clone repo
git clone https://github.com/ploomber/projects

# move to co2-emissions folder
cd projects/contrib/co2-emissions

# install dependencies
conda env create --file environment.yml
conda activate co2-emissions

# build (takes around 1 minute to finish)
ploomber build
```

Final gif will be stored in `output/final.gif`

(Optional) Compress gif using [gifsicle](https://www.lcdf.org/gifsicle/):

```sh
gifsicle --colors=256 --optimize=10 -i output/final.gif -o final-compressed.gif --scale 0.2
```

(Optional) Convert to mp4:

```sh
ffmpeg -r 4 -i output/final.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" output/final.mp4
```
