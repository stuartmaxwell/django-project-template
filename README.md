# Django Project Template

## Instructions

1. [Download the zip file](https://github.com/stuartmaxwell/django-project-template/archive/refs/heads/main.zip) and extract to a folder.
2. Create a virtual environment inside the folder:

   ```bash
   python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip wheel setuptools > /dev/null
   ```

3. Install requirements:

   ```bash
   pip install -r requirements/dev.txt
   ```

4. When required, create an `.env` file in the root directory to over-ride any default settings:

   ```bash
   DEBUG=False
   SECRET_KEY=xxx
   ```
