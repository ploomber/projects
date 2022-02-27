set -e

# activate virtual environment
source venv-cron/bin/activate

# use env.cron.yaml env file
export PLOOMBER_ENV_FILENAME=env.cron.yaml

# get current timestamp
DATE=$(date +'%Y-%m-%dT%H:%M:%S%z')

# make sure logs/ exists
mkdir -p logs

# execute pipeline and store logs
ploomber build --log-file logs/$DATE.log
