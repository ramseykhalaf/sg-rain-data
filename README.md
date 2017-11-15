# Dependencies

Anaconda for environment

`brew cask install miniconda`

Add miniconda to your path in your bashrc/zshrc

`export PATH=/usr/local/miniconda3/bin:"$PATH"`

then run the env setup

`setup_env.sh`

# Run tests!

```
pytest
```

# Download some rain data

Make a folder and then download some data to it (the first arg to the script is)

```
mkdir data
python download_sg_rain.py data
```
