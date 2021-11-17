# use upstream[task_name] (inside curly brackets) to declare task dependencies,
# when executing the script they will be replaced by the output of such task,
# if the task generates more than one output,
# use upstream[task_name][product_key]
cp {{upstream['download']}} {{product}}