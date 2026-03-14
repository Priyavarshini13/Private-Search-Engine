# Private Search Engine

A simple privacy-focused search engine prototype built using Python, Scrapy, Elasticsearch, and FastAPI.

## Features

- Web crawling using Scrapy
- Indexing documents using Elasticsearch
- FastAPI search backend
- REST API endpoint for searching indexed pages

## Tech Stack

- Python
- Scrapy
- Elasticsearch
- FastAPI
- Uvicorn

## Architecture

Crawler → JSON Dataset → Elasticsearch Index → FastAPI API → Search Results

## Project Structure

Private-Search-Engine
│
├ crawler/
├ indexer.py
├ search_api.py
├ .gitignore
└ README.md

## Run the Project

Start Elasticsearch
