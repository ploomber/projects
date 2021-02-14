def run_in_env(c, command, env):
    commands = ['eval "$(conda shell.bash hook)"', f'conda activate {env}']
    commands.append(command)
    c.run(' && '.join(commands))
