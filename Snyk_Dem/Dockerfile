FROM python:3.10.9-slim-buster
 
# Create non-root user
RUN adduser --disabled-password --gecos '' appuser
 
# Set working directory
WORKDIR /app
 
# Copy source code to working directory
COPY . app.py /app/
 
# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
 
# Switch to non-root user
USER appuser
 
# Expose port
EXPOSE 8080
 
# Add health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s CMD curl --fail http://localhost:8080/ || exit 1
 
# Start the app
ENTRYPOINT ["python"]
CMD ["app.py"]

 
 