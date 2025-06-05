# select operating system
FROM redhat/ubi9-minimal:latest

# Install Required Packages...
RUN microdnf install -y --nodocs python3 python3-pip && \
    pip3 install --no-cache-dir requests && \
    microdnf clean all


# Set WORKDIR
WORKDIR /opt/app

# Copy entry.py over to WORKDIR
COPY entry.py /opt/app/

# Starting python script.
ENTRYPOINT ["python3", "./entry.py"]