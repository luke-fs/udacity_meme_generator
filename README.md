# Udacity Meme Generator

The final project for udacity python nanodegree


## Installation

Create an virtual environment and use
```bash
pip install -r requirements.txt
```
to install all dependencies.

After it, use
```bash
python3 app.py
```
to start the app.

## run meme.py
To run meme.py, install the requirements.txt files in your virtual environment and type

```bash
python3 meme.py
```
It will create a meme with random quote in the static folder.

## (Sub)Models
The project constists of a MemeEngine which is responsible for all image processing and of a QuoteEngine which is responsible for reading in quotes from PDF, Doc, Txt or CSV files. 