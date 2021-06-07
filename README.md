# My personal website
[![Streamlit App Pipeline](https://github.com/RafaelAMello/rafaelathaydemello-website/actions/workflows/pipeline.yml/badge.svg?branch=main)](https://github.com/RafaelAMello/rafaelathaydemello-website/actions/workflows/pipeline.yml)

For fun and profit
## Tech stack
- 🖥️ Webapp with python & [Streamlit](https://streamlit.io/)
- 🗺️ Mapping with [Pydeck](https://deckgl.readthedocs.io/en/latest/) & [Mapbox](https://www.mapbox.com/)
- 📈 Graphing with [Altair](https://altair-viz.github.io/)
- 🔨 Packaged with [Docker](https://www.docker.com/)
- 👷 CD with [Github Actions](https://github.com/features/actions)
- ☁️ Running on [AWS Fargate](https://aws.amazon.com/fargate/)
- 🚢 Deployed with [cdk](https://docs.aws.amazon.com/cdk/latest/guide/home.html) on typescript
## Get me up and running
```bash
docker-compose up
```

## Registering domain names
This deployment included everything you need to deploy the app except for the domain name.
The domain name is managed by route53 and needs to be [provisioned via here](https://console.aws.amazon.com/route53/v2/home#Dashboard)
