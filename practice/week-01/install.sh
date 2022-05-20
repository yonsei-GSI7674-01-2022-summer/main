sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.8 -y
sudo apt install python3.8-venv -y
python3.8 -m venv venv
. venv/bin/activate
pip install -U pip
pip install -r requirements.txt