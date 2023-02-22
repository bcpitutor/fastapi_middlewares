# Run development server for the project

## Create a virtual environment

```bash
python3 -m venv venv
```

## Activate the virtual environment

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -e .
```

## Create config file

```bash
cp local_config.example.py local_config.py
```
Then replace the exaple values with actual values.

## Run the development server

```bash
uvicorn dev.google_sso:app --reload --host 0.0.0.0 --port 8765
```

## The app will be running in the port 8765, you can now manipulate the code and see the changes in real time.
