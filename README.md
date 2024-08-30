This project focuses on developing an API that receives a query as input and returns relevant documents related to that query. In this context, a web scraper was created to extract abstracts from scientific articles on Consensus, a site dedicated to scientific literature. The extracted abstracts pertain to articles related to `health quality`. More information about the scraper can be found [here](scripts/consensus_scrapper.ipynb).

## Running the Project with Docker

```bash
docker build -t pk-api .
docker run -d -p 8353:8888 pk-api
```

## Execute a Query
```bash
curl --location 'localhost:8353/query?query=medical'
```

## Authors

Paulo Kim
