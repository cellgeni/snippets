# Create R-kernel
```
conda create -n R422 r-base=4.2.2 r-essentials
conda activate R422
conda install r-irkernel
R -e 'IRkernel::installspec()'
```

# Create python kernel
```
python -m ipykernel install --user --name=<NAME>
```

# Start jupyter lab
```
jupyter lab --no-browser --ip="0.0.0.0"
```

# Compile notebook using papermill
```
papermill input.ipynb  out.ipynb
```
