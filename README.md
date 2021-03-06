# My personal website
[![Streamlit App Pipeline](https://github.com/RafaelAMello/rafaelathaydemello-website/actions/workflows/pipeline.yml/badge.svg?branch=main)](https://github.com/RafaelAMello/rafaelathaydemello-website/actions/workflows/pipeline.yml)

For fun and profit
## Tech stack
- π₯οΈ Webapp with python & [Streamlit](https://streamlit.io/)
- πΊοΈ Mapping with [Pydeck](https://deckgl.readthedocs.io/en/latest/) & [Mapbox](https://www.mapbox.com/)
- π Graphing with [Altair](https://altair-viz.github.io/) and [plotly](https://plotly.com/python/)
- π¨ Packaged with [Docker](https://www.docker.com/)
- π· CD with [Github Actions](https://github.com/features/actions)
- βοΈ Running on [AWS Fargate](https://aws.amazon.com/fargate/)
- π’ Deployed with [cdk](https://docs.aws.amazon.com/cdk/latest/guide/home.html) on typescript
## Get me up and running
```bash
docker-compose up
```

## Registering domain names
This deployment included everything you need to deploy the app except for the domain name.
The domain name is managed by route53 and needs to be [provisioned via here](https://console.aws.amazon.com/route53/v2/home#Dashboard)
