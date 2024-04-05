# Queue Exercise

### 0. Testing Environment
```
OS:       Ubuntu 22.04
Python:   3.7.16
```

### 1. Quick Start

```shell
$ make test   # test queue 
$ make        # execute main.py -p & non -p 
```  


### 2. Makefile Configuration

```makefile
all: use_priority dont_use_priority

use_priority:
	python3 main.py -p

dont_use_priority:
	python3 main.py

test:
	python3 -m pytest ./tests

clean:
	rm -rf __pycache__	rm -rf .pytest_cache
	rm -rf ./tests/__pycache__
	rm -rf ./utils/__pycache__
```


### 3. Set Config
```python
# $PROJECT/config.py

CUSTOMERS_DATA = "./src/customer.txt" # 데이터 파일
PRODUCER_DELAY = 0.2   # 생성자 큐 추가 딜레이
CONSUMER_DELAY = 1.0   # 소비자 큐 로드 딜레이
```

### 4. File Tree
```shell
.
├── config.py
├── main.py
├── makefile
├── readme.md
├── src
│   └── customer.txt
├── tests
│   ├── test_container.py
│   └── test_customer.py
└── utils
    ├── container.py
    └── wrapper.py
```

### 5. Dockerfile
```
WIP
```