# docker build . -t collective.outpufilters.tinymce:latest -f Dockerfile
# docker run --rm -p 8080:8080 -it collective.outpufilters.tinymce:latest
# docker run --rm -p 8080:8080 -it collective.outpufilters.tinymce:latest /bin/sh
FROM plone/plone-backend:6.0

# Select the Plone Backend Type 'classic' or 'volto'
# 'classic' can run standalone
#
# Plone 6 Classic UI
ENV TYPE "classic"

# Site ID, dont use it in Production Mode
ENV SITE "Plone"

# Instance listen port, default 808ß
ENV LISTEN_PORT 8080

# Delete existing Site, dont use it in Production Mode
ENV DELETE_EXISTING "true"

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/sources/collective.outpufilters.tinymce

RUN /app/bin/pip install -e /app/sources/collective.outpufilters.tinymce
