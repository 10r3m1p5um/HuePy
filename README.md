# HuePy

HuePy is a programm desinged to save energy and money therefore supporting the planet. It was part of a schoolproject about the enviroment.
## Installation

To install the programm first you need to download the files.
```bash
git clone https://gitlab.iet-gibb.ch/jba116404/huepy.git
```
After that you will have to install all python packages
```bash
pip install -r requirements.txt
```
To run the programm sucessfully you will need to configure the conf.yaml.example
```bash
mv conf.yaml.example conf.yaml
```
now change the values "ip" and "cords"

ip:
* Log into account.meethue.com.
* Select "Bridge".
* Your bridge's IP address is listed under "internal ip address".
* Copy the IP address to your conf.yaml file right after "ip" (ip: 0.0.0.0)

cords:
* Go to google maps
* search for your location
* right click and select the first row (coordinates looking like "46.95608813294073, 7.444088258203987")
* copy the cords to the conf.yaml files right after "cords:" (cords: 46.95608813294073, 7.444088258203987)

## Usage

```python
python main.yp
```