# Cryptography Web UI
A web-based user interface for encrypting and decrypting text to and from AES-256

## Instalation
1. Install python 3.10+
2. Download the code and extract into a folder on your desktop
3. Open the folder in a terminal of choice
4. Create a new python virtual environment using:
```sh
python -m venv venv
```
5. Activate the virtual environment using the activate script found in:
```sh
./venv/Scripts/activate
```
6. Install the required python packages using:
```sh
pip install -r requirements.txt
```
7. Create a new .env file with the items shown in the .env.example file (NOTE: password requirements is 16 characters minimum)
8. Run the application using:
```sh
fastapi run app.py
```
9. The application should now be running and can be visited at:
```
http://0.0.0.0:8000
```