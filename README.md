# scraping-wikipedia-tokens

This is a project that seeks to obtain corpus from wikipedia and from there generate tokens and a vocabulary. 
Our team members are:
- Sebastián Galindo 15452
- Jose Antonio Ramirez 15441
- Diego Castañeda 15151

## Installation

It is recommended to use a virtual environment before installing the libraries used in the project. To install the libraries, use the following command:

```bash
pip install -r requirements.txt
```

## Usage

Si quiere ejecutar el scraper, primero asegúrese de navegar a la carpeta del proyecto ".\wiki_scraper" para ejecutar los comandos . Para hacer que la araña realice el rastreo, use el siguiente comando:

```bash
scrapy crawl article -O article.json
```

Otherwise you can download the generated corpus from the following link:
[articles.json](https://drive.google.com/file/d/1puUyiOuzXvTVgfShOYsL8HVhqriDiH17/view?usp=sharing)


After obtaining the corpus (article.json), we worked in a jupyter notebook (./notebook.ipynb) where the cleaning and manipulation of the corpus was done to generate the tokens and vocabulary.

## Output

This crawl generate a .json file

## Team contributions

Our team contributions are divided as follow:

- Diego Castañeda: Corpus cleaning, creation of tokens and vocabulary from the corpus.
- Jose Antonio Ramirez: Creation of the project template, cleaning process and graphs with matplotlib.
- Sebastián Galindo: made the scraper on Wikipedia.
