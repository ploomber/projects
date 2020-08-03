# CO2 emissions (metric tons per capita)

Animated plot using pandas, matplotlib and moviepy.

![example](example.png)

Data source: [World Bank](https://data.worldbank.org/indicator/EN.ATM.CO2E.PC?end=2014&start=2014&view=bar)

Requirements: [miniconda](https://docs.conda.io/en/latest/miniconda.html)

To build:

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
gifsicle --colors=256 --optimize=10 -i output/final.gif -o output/final-small.gif --scale 0.5
```

(Optional) Convert to mp4:

```sh
ffmpeg -r 4 -i output/final.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" output/final.mp4
```
