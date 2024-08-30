# paulowk

O projeto envolve no desenvolvimento de uma API, onde ele recebe como input uma query e devolve documentos relevantes à query. Neste contexto, foi feito um web scrapper que extraiu abstracts de artigos cintíficos no Consensus, um site dedicado para artigos científicos. Os abstracts extraídos foram de artigos relacionados a `health quality`. Informações sobre o scrapper podem ser encontradas (aqui)[scripts/consensus_scrapper.ipynb].  

## Running the Project with Docker

```bash
docker build -t pk-api .
docker run -d -p 8353:8888 pk-api
```

## Authors

Paulo Kim
