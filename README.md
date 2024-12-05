# venv steps:
PS C:\Git\dododo-public> cd .\azure_functions\

PS C:\Git\dododo-public\azure_functions> c:\Users\USER_NAME\AppData\Local\Programs\Python\Python311\python.exe -m venv .venv

PS C:\Git\dododo-public\azure_functions> .venv\Scripts\activate   
(.venv) PS C:\Git\dododo-public\azure_functions> pip.exe install -r .\requirements.txt
Collecting azure-functions
  Using cached azure_functions-1.21.3-py3-none-any.whl (185 kB)
Installing collected packages: azure-functions
Successfully installed azure-functions-1.21.3

[notice] A new release of pip available: 22.3 -> 24.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) PS C:\Git\dododo-public\azure_functions> pip.exe install -r .\..\requirements.txt
Collecting openai==1.55.3
  Using cached openai-1.55.3-py3-none-any.whl (389 kB)
Collecting python-dotenv==1.0.1
  Using cached python_dotenv-1.0.1-py3-none-any.whl (19 kB)
Collecting langchain==0.0.338
  Using cached langchain-0.0.338-py3-none-any.whl (2.0 MB)
Collecting anyio<5,>=3.5.0
  Using cached anyio-4.7.0-py3-none-any.whl (93 kB)
Collecting distro<2,>=1.7.0
  Using cached distro-1.9.0-py3-none-any.whl (20 kB)
Collecting httpx<1,>=0.23.0
  Using cached httpx-0.28.0-py3-none-any.whl (73 kB)
Collecting jiter<1,>=0.4.0
  Using cached jiter-0.8.0-cp311-none-win_amd64.whl (208 kB)
Collecting pydantic<3,>=1.9.0
  Using cached pydantic-2.10.3-py3-none-any.whl (456 kB)
Collecting sniffio
  Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Collecting tqdm>4
  Using cached tqdm-4.67.1-py3-none-any.whl (78 kB)
Collecting typing-extensions<5,>=4.11
  Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Collecting PyYAML>=5.3
  Using cached PyYAML-6.0.2-cp311-cp311-win_amd64.whl (161 kB)
Collecting SQLAlchemy<3,>=1.4
  Using cached SQLAlchemy-2.0.36-cp311-cp311-win_amd64.whl (2.1 MB)
Collecting aiohttp<4.0.0,>=3.8.3
  Using cached aiohttp-3.11.9-cp311-cp311-win_amd64.whl (441 kB)
Collecting anyio<5,>=3.5.0
  Using cached anyio-3.7.1-py3-none-any.whl (80 kB)
Collecting dataclasses-json<0.7,>=0.5.7
  Using cached dataclasses_json-0.6.7-py3-none-any.whl (28 kB)
Collecting jsonpatch<2.0,>=1.33
  Using cached jsonpatch-1.33-py2.py3-none-any.whl (12 kB)
Collecting langsmith<0.1.0,>=0.0.63
  Using cached langsmith-0.0.92-py3-none-any.whl (56 kB)
Collecting numpy<2,>=1
  Using cached numpy-1.26.4-cp311-cp311-win_amd64.whl (15.8 MB)
Collecting requests<3,>=2
  Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Collecting tenacity<9.0.0,>=8.1.0
  Using cached tenacity-8.5.0-py3-none-any.whl (28 kB)
Collecting aiohappyeyeballs>=2.3.0
  Using cached aiohappyeyeballs-2.4.4-py3-none-any.whl (14 kB)
Collecting aiosignal>=1.1.2
  Using cached aiosignal-1.3.1-py3-none-any.whl (7.6 kB)
Collecting attrs>=17.3.0
  Using cached attrs-24.2.0-py3-none-any.whl (63 kB)
Collecting frozenlist>=1.1.1
  Using cached frozenlist-1.5.0-cp311-cp311-win_amd64.whl (51 kB)
Collecting multidict<7.0,>=4.5
  Using cached multidict-6.1.0-cp311-cp311-win_amd64.whl (28 kB)
Collecting propcache>=0.2.0
  Using cached propcache-0.2.1-cp311-cp311-win_amd64.whl (44 kB)
Collecting yarl<2.0,>=1.17.0
  Using cached yarl-1.18.3-cp311-cp311-win_amd64.whl (91 kB)
Collecting idna>=2.8
  Using cached idna-3.10-py3-none-any.whl (70 kB)
Collecting marshmallow<4.0.0,>=3.18.0
  Using cached marshmallow-3.23.1-py3-none-any.whl (49 kB)
Collecting typing-inspect<1,>=0.4.0
  Using cached typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
Collecting certifi
  Using cached certifi-2024.8.30-py3-none-any.whl (167 kB)
Collecting httpcore==1.*
  Using cached httpcore-1.0.7-py3-none-any.whl (78 kB)
Collecting h11<0.15,>=0.13
  Using cached h11-0.14.0-py3-none-any.whl (58 kB)
Collecting jsonpointer>=1.9
  Using cached jsonpointer-3.0.0-py2.py3-none-any.whl (7.6 kB)
Collecting annotated-types>=0.6.0
  Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Collecting pydantic-core==2.27.1
  Using cached pydantic_core-2.27.1-cp311-none-win_amd64.whl (2.0 MB)
Collecting charset-normalizer<4,>=2
  Using cached charset_normalizer-3.4.0-cp311-cp311-win_amd64.whl (101 kB)
Collecting urllib3<3,>=1.21.1
  Using cached urllib3-2.2.3-py3-none-any.whl (126 kB)
Collecting greenlet!=0.4.17
  Using cached greenlet-3.1.1-cp311-cp311-win_amd64.whl (298 kB)
Collecting colorama
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting packaging>=17.0
  Using cached packaging-24.2-py3-none-any.whl (65 kB)
Collecting mypy-extensions>=0.3.0
  Using cached mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
Installing collected packages: urllib3, typing-extensions, tenacity, sniffio, PyYAML, python-dotenv, propcache, packaging, numpy, mypy-extensions, multidict, jsonpointer, jiter, idna, h11, greenlet, frozenlist, distro, colorama, charset-normalizer, certifi, attrs, annotated-types, aiohappyeyeballs, yarl, typing-inspect, tqdm, SQLAlchemy, requests, pydantic-core, marshmallow, jsonpatch, httpcore, anyio, aiosignal, pydantic, httpx, dataclasses-json, aiohttp, openai, langsmith, langchain
Successfully installed PyYAML-6.0.2 SQLAlchemy-2.0.36 aiohappyeyeballs-2.4.4 aiohttp-3.11.9 aiosignal-1.3.1 annotated-types-0.7.0 anyio-3.7.1 attrs-24.2.0 certifi-2024.8.30 charset-normalizer-3.4.0 colorama-0.4.6 dataclasses-json-0.6.7 distro-1.9.0 frozenlist-1.5.0 greenlet-3.1.1 h11-0.14.0 httpcore-1.0.7 httpx-0.28.0 idna-3.10 jiter-0.8.0 jsonpatch-1.33 jsonpointer-3.0.0 langchain-0.0.338 langsmith-0.0.92 marshmallow-3.23.1 multidict-6.1.0 mypy-extensions-1.0.0 numpy-1.26.4 openai-1.55.3 packaging-24.2 propcache-0.2.1 pydantic-2.10.3 pydantic-core-2.27.1 python-dotenv-1.0.1 requests-2.32.3 sniffio-1.3.1 tenacity-8.5.0 tqdm-4.67.1 typing-extensions-4.12.2 typing-inspect-0.9.0 urllib3-2.2.3 yarl-1.18.3

[notice] A new release of pip available: 22.3 -> 24.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(.venv) PS C:\Git\dododo-public\azure_functions> pip install -e .\..\
Obtaining file:///C:/Git/dododo-public
  Preparing metadata (setup.py) ... done
Installing collected packages: main
  Running setup.py develop for main
Successfully installed main-1.0

[notice] A new release of pip available: 22.3 -> 24.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip


# Then deployment happens via azure extension for VS Code
where the result is dependent on this line https://github.com/dododo-public/python_llm/blob/main/azure_functions/function_app.py#L3-L4
