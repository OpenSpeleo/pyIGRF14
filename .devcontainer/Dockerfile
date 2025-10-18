FROM python:3.14.0-bookworm

RUN apt update && apt install -y --no-install-recommends \
    git \
    curl \
    wget \
    unzip \
    vim \
    nano \
    zsh \
    tmux \
    # cleaning up unused files
    && apt clean \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

ENV UV_CACHE_DIR="/workspace/.uv/cache"
