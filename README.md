# Live Map with Django

## Description

This is just a super simple demo I made just for fun. The idea is a website which shows locations of places for rent, sell, ect. on a map, with some filter features.

### What this project does:

1. saves LAT, and LONG of the place in db, along with the rent, or sell status
2. shows the saved, and available locations on a map.
3. filter the places by type, township, etc.
4. Currently only availabe for **Yangon/Myanmar**.

### Stacks Used:

    - Backend:
      - Django
    - Frontend:
      - HTML, CSS, Vanilla JS
    - DB:
      - Postgres
      - redis (for caches)
    - Docker

## How to install

  1. clone this repo
  2. run `docker-compose up`
  3. go to this link: `localhost:8000/hello`
