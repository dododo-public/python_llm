# venv steps:
PS C:\Git\dododo-public> cd .\azure_functions\
PS C:\Git\dododo-public\azure_functions> c:\Users\USER_NAME\AppData\Local\Programs\Python\Python311\python.exe -m venv .venv
PS C:\Git\dododo-public\azure_functions> .venv\Scripts\activate                  
(.venv) PS C:\Git\dododo-public\azure_functions> pip.exe install -r .\requirements.txt   
Collecting azure-functions
  Using cached azure_functions-1.21.3-py3-none-any.whl (185 kB)
Installing collected packages: azure-functions
Successfully installed azure-functions-1.21.3
PS C:\Git\dododo-public> cd .\azure_functions\
PS C:\Git\dododo-public\azure_functions> c:\Users\USER_NAME\AppData\Local\Programs\Python\Python311\python.exe -m venv .venv
PS C:\Git\dododo-public\azure_functions> .venv\Scripts\activate
(.venv) PS C:\Git\dododo-public\azure_functions> pip.exe install -r .\requirements.txt
Collecting azure-functions
  Using cached azure_functions-1.21.3-py3-none-any.whl (185 kB)
Installing collected packages: azure-functions
Successfully installed azure-functions-1.21.3

[notice] A new release of pip available: 22.3 -> 24.3.1
PS C:\Git\dododo-public\azure_functions> c:\Users\USER_NAME\AppData\Local\Programs\Python\Python311\python.exe -m venv .venv
PS C:\Git\dododo-public\azure_functions> .venv\Scripts\activate
(.venv) PS C:\Git\dododo-public\azure_functions> pip.exe install -r .\requirements.txt
Collecting azure-functions
  Using cached azure_functions-1.21.3-py3-none-any.whl (185 kB)
Installing collected packages: azure-functions
Successfully installed azure-functions-1.21.3
(.venv) PS C:\Git\dododo-public\azure_functions> pip.exe install -r .\requirements.txt
Collecting azure-functions
  Using cached azure_functions-1.21.3-py3-none-any.whl (185 kB)
Installing collected packages: azure-functions
Successfully installed azure-functions-1.21.3

Installing collected packages: azure-functions
Successfully installed azure-functions-1.21.3

Successfully installed azure-functions-1.21.3


[notice] A new release of pip available: 22.3 -> 24.3.1
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
(.venv) PS C:\Git\dododo-public\azure_functions> pip install -e .\..\
Obtaining file:///C:/Git/dododo-public
  Preparing metadata (setup.py) ... done
Installing collected packages: main
  Attempting uninstall: main
    Found existing installation: main 1.0
    Uninstalling main-1.0:
      Successfully uninstalled main-1.0
  Running setup.py develop for main
Successfully installed main-1.0

[notice] A new release of pip available: 22.3 -> 24.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip


# Then deployment happens via azure extension for VS Code