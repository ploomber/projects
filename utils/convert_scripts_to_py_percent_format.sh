for dir in ../**/
do
    jupytext ${dir}*.py --to py:percent
done