This application consists of two components:

* A SOAP web-service for reading information of a student (XML-based)
* A REST web-service for registering (creating) information of a student (JSON-based)

## How to run

Install the requirements:

```bash
python3 -m venv venv/
source venv/bin/activate
pip3 install -r student_webservice/requirements.txt
```

Run the program:

```bash
source venv/bin/activate
python3 main.py
```

## How to use

Install the requirements:

```
sudo apt install curl tidy -y
```

Test registration API with a sample JSON data:

```bash
curl -s http://localhost:8000/ -d '{"register": {"std_id": 98443138, "name": "Masoud Sadrnezhaad", "major": "IT", "level": "MSc"}}'
```

Test get student information API with XML data: 

```bash
curl -s http://localhost:8001/ -d "<?xml version='1.0' encoding='UTF-8'?><soap11env:Envelope xmlns:soap11env=\"http://schemas.xmlsoap.org/soap/envelope/\"><soap11env:Body>  <get_student>  <std_id>98443138</std_id>  </get_student></soap11env:Body></soap11env:Envelope>" | tidy -q -xml -indent -wrap 0
```
