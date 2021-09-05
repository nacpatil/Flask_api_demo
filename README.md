Requirements: Install python3 and python package - Flask

To run:  
python3 app.py  
To open web page: copy paste in browser: http://localhost:5000/

To build Docker image :

```
sudo docker build -t app-student .
```

Run Docker :

```
sudo docker run -p 80:80 app-student .
```


