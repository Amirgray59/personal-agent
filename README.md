# A personal agent for basic daily use 

### programming, article & report writing , ... 

### recommended model: deepseek-v4.1-flash 
### recommended ai provider : gapgpt.app 


# Features : 
* system prompt 
* conversation memory 
* basic commands (exit, reset memory)
* tool calling : 
    - calculator 


#Run : 
```
touch .env
```

### add .env contents : 
```
OPENAI_API_KEY=
OPENAI_BASE_URL=
OPENAI_MODEL=
```


``` bash 

python -m venv .venv 

source .venv/bin/activate 

pip install -r requirements.txt 

python main.py
```
