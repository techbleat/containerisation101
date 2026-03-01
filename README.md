# Flask “Hello World” Container Example

This small sample repo contains a minimal Flask application and a
Dockerfile that builds a container image running it with **gunicorn**.

## Contents

- `app.py` – A tiny Flask app with two endpoints (`/` and `/health`).
- `requirements.txt` – Lists dependencies (Flask).
- `containerisation101/dockerfile` – Builds an image from `python:3.11-slim`
  and runs the app on port 8000.

> **Note:** the base app is the same as in the parent directory; the
Dockerfile references it and the top‑level `requirements.txt`.

---

## Running locally

```bash
python -m venv venv# Flask “Hello World” Container Example

This small sample repo contains a minimal Flask application and a
Dockerfile that builds a container image running it with **gunicorn**.

## Contents

- `app.py` – A tiny Flask app with two endpoints (`/` and `/health`).
- `requirements.txt` – Lists dependencies (Flask).
- `containerisation101/dockerfile` – Builds an image from `python:3.11-slim`
  and runs the app on port 8000.

> **Note:** the base app is the same as in the parent directory; the
Dockerfile references it and the top‑level `requirements.txt`.

---

## Running locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python [app.py](http://_vscodecontentref_/1)
source venv/bin/activate
pip install -r requirements.txt
python [app.py](http://_vscodecontentref_/1)
```

## BUILD a docker image
docker build -t my-flask-app .

## run image
docker run --rm -p 8000:8000 my-flask-app

# or, using your Docker Hub name:
docker build -t shegoj/python-helloworld:1.0 .


docker login
docker tag my-flask-app shegoj/python-helloworld:1.0
docker push shegoj/python-helloworld:1.0