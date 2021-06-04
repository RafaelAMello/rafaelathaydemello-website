FROM python:3.8

WORKDIR /app
# USER streamlit #TODO: run as non root user

# Install App requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose Streamlit port
EXPOSE 8501

CMD streamlit run app.py
