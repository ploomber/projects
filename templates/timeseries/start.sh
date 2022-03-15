# Install miniconda (to get a Python environment ready, not needed if
# There's already a Python environment up and running)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ~/Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda

# Init conda
eval "$($HOME/miniconda/bin/conda shell.bash hook)"

# Create and activate env
conda create --name myenv python=3.9 -y
conda activate myenv

# install ploomber and soopervisor in the base environment
pip install ploomber soopervisor
pip install -r requirements.txt
