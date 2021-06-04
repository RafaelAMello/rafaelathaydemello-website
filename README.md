# My personal website

## Get me up and running
Build docker image:
```bash
docker build . -t streamlit
```
Run Docker image / interactively
```bash
docker run -p 8051:8051 -it -v $(pwd):/usr/app --rm streamlit
```

Run image interactively
```bash
docker run -p 8051:8051 -it -v $(pwd):/usr/app --rm streamlit /bin/bash
```
