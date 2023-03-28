import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def execute_ipybn(filename):
    with open(filename) as ff:
        nb_in = nbformat.read(ff, nbformat.NO_CONVERT)

    ep = ExecutePreprocessor(timeout=1000, kernel_name='python3')

    # The output is an ipython/jupyter notebook including the output of all cells
    nb_out = ep.preprocess(nb_in)

    return nb_out


if __name__ == '__main__':
    nb = execute_ipybn('Notebook_aily_case.ipynb')
    with open('executed_notebook.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

