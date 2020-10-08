# exit if any command fails
set -e

# initialize conda in the shell process
eval "$(conda shell.bash hook)"
conda activate base

# move to the project_root
cd /Users/Edu/dev/projects-ploomber/testing

# install the env, the user might name it differently so we force it to be
# installed as "ploomber-env"
conda env create --file /Users/Edu/dev/projects-ploomber/testing/environment.yml --name ploomber-env --force
conda activate ploomber-env

# verify ploomber is installed
python -c "import ploomber" || PLOOMBER_INSTALLED=$?

if [[ $PLOOMBER_INSTALLED -ne 0 ]];
then
    echo "ploomber is not installed, consider adding it to your environment.yml file. Installing..."
    pip install ploomber
fi



if [ -f "setup.py" ]; then
    echo "Found setup.py, installing package..."
    pip install .
fi


# run pipeline
ploomber build

