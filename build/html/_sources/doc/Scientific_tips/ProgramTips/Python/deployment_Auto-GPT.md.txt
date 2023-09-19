

# 配置Auto-GPT

## 🚀 特征

- 🌐 用于搜索和信息收集的互联网接入
- 💾 长期和短期记忆管理
- 🧠 用于文本生成的 GPT-4 实例
- 🔗 访问热门网站和平台
- 🗃️ 使用 GPT-3.5 进行文件存储和摘要

## 📋 环境要求

- 环境（选择其中之一）
  - [VSCode + devcontainer](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers): 已在 .devcontainer 文件夹中配置，可直接使用
  - Docker
  - Python 3.10 或更高版本 (instructions: [for Windows](https://www.tutorialspoint.com/how-to-install-python-in-windows))
- [OpenAI API key](https://platform.openai.com/account/api-keys)

### 可选
- Memory backend (选择其中之一)
  - [Pinecone](https://www.pinecone.io/)
  - [Milvus](https://milvus.io/)
  - [Redis](https://redis.io)
  - [Weaviate](https://weaviate.io)
- ElevenLabs Key (如果你想AI说话)

## ⚠️ 配置 OpenAI API Keys ⚠️ 

从以下位置获取您的 OpenAI API 密钥: https://platform.openai.com/account/api-keys.

要将 OpenAI API 密钥用于自动 GPT，**您需要设置**结算信息（又名付费帐户）。

您可以在 https://platform.openai.com/account/billing/overview 设置付费帐户。

重要提示: 强烈建议您在 [使用情况](https://platform.openai.com/account/usage)页面上跟踪使用情况。
您还可以在 [使用情况限制](https://platform.openai.com/account/billing/limits)页面上设置支出限制。


#### **在继续之前，请确保您已完成此步骤。否则，什么都行不通！**

## 💾 安装

要安装自动 GPT，请按照以下步骤操作：

1. 确保您满足上面列出的所有**环境要求**。如果没有，请安装/获取它们。

_若要执行以下命令，请导航到计算机上的文件夹并在顶部的文件夹路径中键入 `CMD`， 然后按 Enter 键，从而打开 CMD、Bash 或 Powershell 窗口。_

2. 克隆存储库：对于此步骤，您需要安装 Git。 注意：如果您没有 Git，只需下载 [最新的稳定版本](https://github.com/Significant-Gravitas/Auto-GPT/releases/latest) 或者在页面底部 (`Source code (zip)`)。

    ```bash
    git clone -b stable https://github.com/Significant-Gravitas/Auto-GPT.git
    ```

3. 进入下载存储库的目录。

    ```bash
    cd Auto-GPT
    ```

4. 安装所需的依赖项。

    ```bash
    pip install -r requirements.txt
    ```
输出以下内容：
```
Collecting en_core_web_sm@ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.4.0/en_core_web_sm-3.4.0-py3-none-any.whl
  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.4.0/en_core_web_sm-3.4.0-py3-none-any.whl (12.8 MB)
     ---------------------------------------- 12.8/12.8 MB 6.4 MB/s eta 0:00:00
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.12.2-py3-none-any.whl (142 kB)
     ---------------------------------------- 143.0/143.0 kB 236.2 kB/s eta 0:00:00
Collecting colorama==0.4.6
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting openai==0.27.2
  Downloading openai-0.27.2-py3-none-any.whl (70 kB)
     ---------------------------------------- 70.1/70.1 kB 950.1 kB/s eta 0:00:00
Collecting playsound==1.2.2
  Downloading playsound-1.2.2-py2.py3-none-any.whl (6.0 kB)
Collecting python-dotenv==1.0.0
  Downloading python_dotenv-1.0.0-py3-none-any.whl (19 kB)
Collecting pyyaml==6.0
  Using cached PyYAML-6.0-cp311-cp311-win_amd64.whl (143 kB)
Collecting readability-lxml==0.8.1
  Downloading readability_lxml-0.8.1-py3-none-any.whl (20 kB)
Collecting requests
  Using cached requests-2.28.2-py3-none-any.whl (62 kB)
Collecting tiktoken==0.3.3
  Downloading tiktoken-0.3.3-cp311-cp311-win_amd64.whl (579 kB)
     ---------------------------------------- 579.4/579.4 kB 847.0 kB/s eta 0:00:00
Collecting gTTS==2.3.1
  Downloading gTTS-2.3.1-py3-none-any.whl (28 kB)
Collecting docker
  Downloading docker-6.0.1-py3-none-any.whl (147 kB)
     ---------------------------------------- 147.5/147.5 kB 2.9 MB/s eta 0:00:00
Collecting duckduckgo-search
  Downloading duckduckgo_search-2.8.6-py3-none-any.whl (30 kB)
Collecting google-api-python-client
  Downloading google_api_python_client-2.86.0-py2.py3-none-any.whl (11.3 MB)
     ---------------------------------------- 11.3/11.3 MB 7.6 MB/s eta 0:00:00
Collecting pinecone-client==2.2.1
  Downloading pinecone_client-2.2.1-py3-none-any.whl (177 kB)
     ---------------------------------------- 177.2/177.2 kB 10.4 MB/s eta 0:00:00
Collecting redis
  Downloading redis-4.5.4-py3-none-any.whl (238 kB)
     ---------------------------------------- 238.9/238.9 kB 14.3 MB/s eta 0:00:00
Collecting orjson
  Downloading orjson-3.8.10-cp311-none-win_amd64.whl (197 kB)
     ---------------------------------------- 197.1/197.1 kB 5.8 MB/s eta 0:00:00
Collecting Pillow
  Downloading Pillow-9.5.0-cp311-cp311-win_amd64.whl (2.5 MB)
     ---------------------------------------- 2.5/2.5 MB 8.9 MB/s eta 0:00:00
Collecting selenium
  Downloading selenium-4.9.0-py3-none-any.whl (6.5 MB)
     ---------------------------------------- 6.5/6.5 MB 7.9 MB/s eta 0:00:00
Collecting webdriver-manager
  Downloading webdriver_manager-3.8.6-py2.py3-none-any.whl (27 kB)
Collecting jsonschema
  Downloading jsonschema-4.17.3-py3-none-any.whl (90 kB)
     ---------------------------------------- 90.4/90.4 kB ? eta 0:00:00
Collecting tweepy
  Downloading tweepy-4.13.0-py3-none-any.whl (102 kB)
     ---------------------------------------- 102.8/102.8 kB ? eta 0:00:00
Collecting click
  Using cached click-8.1.3-py3-none-any.whl (96 kB)
Collecting spacy<4.0.0,>=3.0.0
  Downloading spacy-3.5.2-cp311-cp311-win_amd64.whl (12.2 MB)
     ---------------------------------------- 12.2/12.2 MB 6.5 MB/s eta 0:00:00
Collecting coverage
  Downloading coverage-7.2.3-cp311-cp311-win_amd64.whl (203 kB)
     ---------------------------------------- 203.5/203.5 kB 6.0 MB/s eta 0:00:00
Collecting flake8
  Using cached flake8-6.0.0-py2.py3-none-any.whl (57 kB)
Collecting numpy
  Using cached numpy-1.24.2-cp311-cp311-win_amd64.whl (14.8 MB)
Collecting pre-commit
  Downloading pre_commit-3.2.2-py2.py3-none-any.whl (202 kB)
     ---------------------------------------- 202.7/202.7 kB 6.2 MB/s eta 0:00:00
Collecting black
  Downloading black-23.3.0-cp311-cp311-win_amd64.whl (1.3 MB)
     ---------------------------------------- 1.3/1.3 MB 8.2 MB/s eta 0:00:00
Collecting isort
  Downloading isort-5.12.0-py3-none-any.whl (91 kB)
     ---------------------------------------- 91.2/91.2 kB ? eta 0:00:00
Collecting gitpython==3.1.31
  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)
     ---------------------------------------- 184.3/184.3 kB 10.9 MB/s eta 0:00:00
Collecting pytest
  Downloading pytest-7.3.1-py3-none-any.whl (320 kB)
     ---------------------------------------- 320.5/320.5 kB 9.7 MB/s eta 0:00:00
Collecting asynctest
  Downloading asynctest-0.13.0-py3-none-any.whl (26 kB)
Collecting pytest-asyncio
  Downloading pytest_asyncio-0.21.0-py3-none-any.whl (13 kB)
Collecting pytest-benchmark
  Downloading pytest_benchmark-4.0.0-py3-none-any.whl (43 kB)
     ---------------------------------------- 44.0/44.0 kB 2.1 MB/s eta 0:00:00
Collecting pytest-cov
  Downloading pytest_cov-4.0.0-py3-none-any.whl (21 kB)
Collecting pytest-integration
  Downloading pytest_integration-0.2.3-py3-none-any.whl (4.5 kB)
Collecting pytest-mock
  Downloading pytest_mock-3.10.0-py3-none-any.whl (9.3 kB)
Collecting tqdm
  Downloading tqdm-4.65.0-py3-none-any.whl (77 kB)
     ---------------------------------------- 77.1/77.1 kB 4.2 MB/s eta 0:00:00
Collecting aiohttp
  Downloading aiohttp-3.8.4-cp311-cp311-win_amd64.whl (317 kB)
     ---------------------------------------- 317.2/317.2 kB 4.9 MB/s eta 0:00:00
Collecting chardet
  Downloading chardet-5.1.0-py3-none-any.whl (199 kB)
     ---------------------------------------- 199.1/199.1 kB 6.1 MB/s eta 0:00:00
Collecting lxml
  Downloading lxml-4.9.2-cp311-cp311-win_amd64.whl (3.8 MB)
     ---------------------------------------- 3.8/3.8 MB 2.4 MB/s eta 0:00:00
Collecting cssselect
  Downloading cssselect-1.2.0-py2.py3-none-any.whl (18 kB)
Collecting regex>=2022.1.18
  Downloading regex-2023.3.23-cp311-cp311-win_amd64.whl (267 kB)
     ---------------------------------------- 267.9/267.9 kB 3.3 MB/s eta 0:00:00
Collecting loguru>=0.5.0
  Downloading loguru-0.7.0-py3-none-any.whl (59 kB)
     ---------------------------------------- 60.0/60.0 kB 789.1 kB/s eta 0:00:00
Collecting typing-extensions>=3.7.4
  Using cached typing_extensions-4.5.0-py3-none-any.whl (27 kB)
Collecting dnspython>=2.0.0
  Downloading dnspython-2.3.0-py3-none-any.whl (283 kB)
     ---------------------------------------- 283.7/283.7 kB 2.2 MB/s eta 0:00:00
Collecting python-dateutil>=2.5.3
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting urllib3>=1.21.1
  Using cached urllib3-1.26.15-py2.py3-none-any.whl (140 kB)
Collecting gitdb<5,>=4.0.1
  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)
     ---------------------------------------- 62.7/62.7 kB 3.5 MB/s eta 0:00:00
Collecting soupsieve>1.2
  Downloading soupsieve-2.4.1-py3-none-any.whl (36 kB)
Collecting charset-normalizer<4,>=2
  Using cached charset_normalizer-3.1.0-cp311-cp311-win_amd64.whl (96 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.4-py3-none-any.whl (61 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2022.12.7-py3-none-any.whl (155 kB)
     ---------------------------------------- 155.3/155.3 kB 3.1 MB/s eta 0:00:00
Collecting packaging>=14.0
  Using cached packaging-23.1-py3-none-any.whl (48 kB)
Collecting websocket-client>=0.32.0
  Downloading websocket_client-1.5.1-py3-none-any.whl (55 kB)
     ---------------------------------------- 55.9/55.9 kB 2.9 MB/s eta 0:00:00
Collecting pywin32>=304
  Downloading pywin32-306-cp311-cp311-win_amd64.whl (9.2 MB)
     ---------------------------------------- 9.2/9.2 MB 4.9 MB/s eta 0:00:00
Collecting httplib2<1dev,>=0.15.0
  Downloading httplib2-0.22.0-py3-none-any.whl (96 kB)
     ---------------------------------------- 96.9/96.9 kB 1.8 MB/s eta 0:00:00
Collecting google-auth<3.0.0dev,>=1.19.0
  Downloading google_auth-2.17.3-py2.py3-none-any.whl (178 kB)
     ---------------------------------------- 178.2/178.2 kB 3.6 MB/s eta 0:00:00
Collecting google-auth-httplib2>=0.1.0
  Downloading google_auth_httplib2-0.1.0-py2.py3-none-any.whl (9.3 kB)
Collecting google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5
  Downloading google_api_core-2.11.0-py3-none-any.whl (120 kB)
     ---------------------------------------- 120.3/120.3 kB 6.9 MB/s eta 0:00:00
Collecting uritemplate<5,>=3.0.1
  Downloading uritemplate-4.1.1-py2.py3-none-any.whl (10 kB)
Collecting async-timeout>=4.0.2
  Downloading async_timeout-4.0.2-py3-none-any.whl (5.8 kB)
Collecting trio~=0.17
  Downloading trio-0.22.0-py3-none-any.whl (384 kB)
     ---------------------------------------- 384.9/384.9 kB 4.0 MB/s eta 0:00:00
Collecting trio-websocket~=0.9
  Downloading trio_websocket-0.10.2-py3-none-any.whl (17 kB)
Collecting attrs>=17.4.0
  Downloading attrs-23.1.0-py3-none-any.whl (61 kB)
     ---------------------------------------- 61.2/61.2 kB 3.2 MB/s eta 0:00:00
Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0
  Downloading pyrsistent-0.19.3-cp311-cp311-win_amd64.whl (62 kB)
     ---------------------------------------- 62.7/62.7 kB 3.5 MB/s eta 0:00:00
Collecting oauthlib<4,>=3.2.0
  Downloading oauthlib-3.2.2-py3-none-any.whl (151 kB)
     ---------------------------------------- 151.7/151.7 kB 8.8 MB/s eta 0:00:00
Collecting requests-oauthlib<2,>=1.2.0
  Downloading requests_oauthlib-1.3.1-py2.py3-none-any.whl (23 kB)
Collecting spacy-legacy<3.1.0,>=3.0.11
  Downloading spacy_legacy-3.0.12-py2.py3-none-any.whl (29 kB)
Collecting spacy-loggers<2.0.0,>=1.0.0
  Downloading spacy_loggers-1.0.4-py3-none-any.whl (11 kB)
Collecting murmurhash<1.1.0,>=0.28.0
  Downloading murmurhash-1.0.9-cp311-cp311-win_amd64.whl (18 kB)
Collecting cymem<2.1.0,>=2.0.2
  Downloading cymem-2.0.7-cp311-cp311-win_amd64.whl (28 kB)
Collecting preshed<3.1.0,>=3.0.2
  Downloading preshed-3.0.8-cp311-cp311-win_amd64.whl (91 kB)
     ---------------------------------------- 91.9/91.9 kB 2.6 MB/s eta 0:00:00
Collecting thinc<8.2.0,>=8.1.8
  Downloading thinc-8.1.9-cp311-cp311-win_amd64.whl (1.5 MB)
     ---------------------------------------- 1.5/1.5 MB 4.6 MB/s eta 0:00:00
Collecting wasabi<1.2.0,>=0.9.1
  Downloading wasabi-1.1.1-py3-none-any.whl (27 kB)
Collecting srsly<3.0.0,>=2.4.3
  Downloading srsly-2.4.6-cp311-cp311-win_amd64.whl (478 kB)
     ---------------------------------------- 478.8/478.8 kB 5.0 MB/s eta 0:00:00
Collecting catalogue<2.1.0,>=2.0.6
  Downloading catalogue-2.0.8-py3-none-any.whl (17 kB)
Collecting typer<0.8.0,>=0.3.0
  Downloading typer-0.7.0-py3-none-any.whl (38 kB)
Collecting pathy>=0.10.0
  Downloading pathy-0.10.1-py3-none-any.whl (48 kB)
     ---------------------------------------- 48.9/48.9 kB 2.4 MB/s eta 0:00:00
Collecting smart-open<7.0.0,>=5.2.1
  Downloading smart_open-6.3.0-py3-none-any.whl (56 kB)
     ---------------------------------------- 56.8/56.8 kB 3.1 MB/s eta 0:00:00
Collecting pydantic!=1.8,!=1.8.1,<1.11.0,>=1.7.4
  Downloading pydantic-1.10.7-cp311-cp311-win_amd64.whl (2.1 MB)
     ---------------------------------------- 2.1/2.1 MB 5.6 MB/s eta 0:00:00
Collecting jinja2
  Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)
Requirement already satisfied: setuptools in c:\users\gn\anaconda3\envs\ai-copilot\lib\site-packages (from spacy<4.0.0,>=3.0.0->-r requirements.txt (line 23)) (66.0.0)
Collecting langcodes<4.0.0,>=3.2.0
  Downloading langcodes-3.3.0-py3-none-any.whl (181 kB)
     ---------------------------------------- 181.6/181.6 kB 5.5 MB/s eta 0:00:00
Collecting spacy<4.0.0,>=3.0.0
  Downloading spacy-3.4.4-cp311-cp311-win_amd64.whl (11.9 MB)
     ---------------------------------------- 11.9/11.9 MB 7.0 MB/s eta 0:00:00
Collecting wasabi<1.2.0,>=0.9.1
  Downloading wasabi-0.10.1-py3-none-any.whl (26 kB)
Collecting mccabe<0.8.0,>=0.7.0
  Using cached mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Collecting pycodestyle<2.11.0,>=2.10.0
  Using cached pycodestyle-2.10.0-py2.py3-none-any.whl (41 kB)
Collecting pyflakes<3.1.0,>=3.0.0
  Using cached pyflakes-3.0.1-py2.py3-none-any.whl (62 kB)
Collecting cfgv>=2.0.0
  Downloading cfgv-3.3.1-py2.py3-none-any.whl (7.3 kB)
Collecting identify>=1.0.0
  Downloading identify-2.5.22-py2.py3-none-any.whl (98 kB)
     ---------------------------------------- 98.8/98.8 kB 5.5 MB/s eta 0:00:00
Collecting nodeenv>=0.11.1
  Downloading nodeenv-1.7.0-py2.py3-none-any.whl (21 kB)
Collecting virtualenv>=20.10.0
  Downloading virtualenv-20.22.0-py3-none-any.whl (3.2 MB)
     ---------------------------------------- 3.2/3.2 MB 7.7 MB/s eta 0:00:00
Collecting mypy-extensions>=0.4.3
  Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
Collecting pathspec>=0.9.0
  Downloading pathspec-0.11.1-py3-none-any.whl (29 kB)
Collecting platformdirs>=2
  Downloading platformdirs-3.2.0-py3-none-any.whl (14 kB)
Collecting iniconfig
  Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Collecting pluggy<2.0,>=0.12
  Downloading pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting py-cpuinfo
  Downloading py_cpuinfo-9.0.0-py3-none-any.whl (22 kB)
Collecting smmap<6,>=3.0.1
  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)
Collecting googleapis-common-protos<2.0dev,>=1.56.2
  Downloading googleapis_common_protos-1.59.0-py2.py3-none-any.whl (223 kB)
     ---------------------------------------- 223.6/223.6 kB 6.7 MB/s eta 0:00:00
Collecting protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5
  Downloading protobuf-4.22.3-cp310-abi3-win_amd64.whl (420 kB)
     ---------------------------------------- 420.6/420.6 kB 8.7 MB/s eta 0:00:00
Collecting cachetools<6.0,>=2.0.0
  Downloading cachetools-5.3.0-py3-none-any.whl (9.3 kB)
Collecting pyasn1-modules>=0.2.1
  Downloading pyasn1_modules-0.3.0-py2.py3-none-any.whl (181 kB)
     ---------------------------------------- 181.3/181.3 kB 5.3 MB/s eta 0:00:00
Collecting six>=1.9.0
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting rsa<5,>=3.1.4
  Downloading rsa-4.9-py3-none-any.whl (34 kB)
Collecting pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2
  Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB)
Collecting win32-setctime>=1.0.0
  Downloading win32_setctime-1.1.0-py3-none-any.whl (3.6 kB)
Collecting blis<0.8.0,>=0.7.8
  Downloading blis-0.7.9-cp311-cp311-win_amd64.whl (7.0 MB)
     ---------------------------------------- 7.0/7.0 MB 6.2 MB/s eta 0:00:00
Collecting confection<1.0.0,>=0.0.1
  Downloading confection-0.0.4-py3-none-any.whl (32 kB)
Collecting sortedcontainers
  Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
Collecting async-generator>=1.9
  Downloading async_generator-1.10-py3-none-any.whl (18 kB)
Collecting outcome
  Downloading outcome-1.2.0-py2.py3-none-any.whl (9.7 kB)
Collecting sniffio
  Downloading sniffio-1.3.0-py3-none-any.whl (10 kB)
Collecting cffi>=1.14
  Using cached cffi-1.15.1-cp311-cp311-win_amd64.whl (179 kB)
Collecting exceptiongroup
  Downloading exceptiongroup-1.1.1-py3-none-any.whl (14 kB)
Collecting wsproto>=0.14
  Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)
Collecting PySocks!=1.5.7,<2.0,>=1.5.6
  Downloading PySocks-1.7.1-py3-none-any.whl (16 kB)
Collecting distlib<1,>=0.3.6
  Downloading distlib-0.3.6-py2.py3-none-any.whl (468 kB)
     ---------------------------------------- 468.5/468.5 kB 7.4 MB/s eta 0:00:00
Collecting filelock<4,>=3.11
  Downloading filelock-3.12.0-py3-none-any.whl (10 kB)
Collecting multidict<7.0,>=4.5
  Downloading multidict-6.0.4-cp311-cp311-win_amd64.whl (28 kB)
Collecting yarl<2.0,>=1.0
  Downloading yarl-1.9.1-cp311-cp311-win_amd64.whl (60 kB)
     ---------------------------------------- 60.1/60.1 kB 1.6 MB/s eta 0:00:00
Collecting frozenlist>=1.1.1
  Downloading frozenlist-1.3.3-cp311-cp311-win_amd64.whl (32 kB)
Collecting aiosignal>=1.1.2
  Downloading aiosignal-1.3.1-py3-none-any.whl (7.6 kB)
Collecting MarkupSafe>=2.0
  Using cached MarkupSafe-2.1.2-cp311-cp311-win_amd64.whl (16 kB)
Collecting pycparser
  Using cached pycparser-2.21-py2.py3-none-any.whl (118 kB)
Collecting pyasn1<0.6.0,>=0.4.6
  Downloading pyasn1-0.5.0-py2.py3-none-any.whl (83 kB)
     ---------------------------------------- 83.9/83.9 kB 4.6 MB/s eta 0:00:00
Collecting h11<1,>=0.9.0
  Downloading h11-0.14.0-py3-none-any.whl (58 kB)
     ---------------------------------------- 58.3/58.3 kB 3.0 MB/s eta 0:00:00
Installing collected packages: wasabi, sortedcontainers, pywin32, py-cpuinfo, playsound, distlib, cymem, win32-setctime, websocket-client, urllib3, uritemplate, typing-extensions, spacy-loggers, spacy-legacy, soupsieve, sniffio, smmap, smart-open, six, regex, pyyaml, python-dotenv, pytest-integration, PySocks, pyrsistent, pyparsing, pyflakes, pycparser, pycodestyle, pyasn1, protobuf, pluggy, platformdirs, Pillow, pathspec, packaging, orjson, oauthlib, numpy, nodeenv, mypy-extensions, murmurhash, multidict, mccabe, MarkupSafe, lxml, langcodes, isort, iniconfig, idna, identify, h11, frozenlist, filelock, exceptiongroup, dnspython, cssselect, coverage, colorama, charset-normalizer, chardet, cfgv, certifi, catalogue, cachetools, attrs, asynctest, async-timeout, async-generator, yarl, wsproto, virtualenv, tqdm, srsly, rsa, requests, redis, readability-lxml, python-dateutil, pytest, pydantic, pyasn1-modules, preshed, outcome, loguru, jsonschema, jinja2, httplib2, googleapis-common-protos, gitdb, flake8, click, cffi, blis, beautifulsoup4, aiosignal, webdriver-manager, typer, trio, tiktoken, requests-oauthlib, pytest-mock, pytest-cov, pytest-benchmark, pytest-asyncio, pre-commit, pinecone-client, gTTS, google-auth, gitpython, duckduckgo-search, docker, confection, black, aiohttp, tweepy, trio-websocket, thinc, pathy, openai, google-auth-httplib2, google-api-core, spacy, selenium, google-api-python-client, en_core_web_sm
Successfully installed MarkupSafe-2.1.2 Pillow-9.5.0 PySocks-1.7.1 aiohttp-3.8.4 aiosignal-1.3.1 async-generator-1.10 async-timeout-4.0.2 asynctest-0.13.0 attrs-23.1.0 beautifulsoup4-4.12.2 black-23.3.0 blis-0.7.9 cachetools-5.3.0 catalogue-2.0.8 certifi-2022.12.7 cffi-1.15.1 cfgv-3.3.1 chardet-5.1.0 charset-normalizer-3.1.0 click-8.1.3 colorama-0.4.6 confection-0.0.4 coverage-7.2.3 cssselect-1.2.0 cymem-2.0.7 distlib-0.3.6 dnspython-2.3.0 docker-6.0.1 duckduckgo-search-2.8.6 en_core_web_sm-3.4.0 exceptiongroup-1.1.1 filelock-3.12.0 flake8-6.0.0 frozenlist-1.3.3 gTTS-2.3.1 gitdb-4.0.10 gitpython-3.1.31 google-api-core-2.11.0 google-api-python-client-2.86.0 google-auth-2.17.3 google-auth-httplib2-0.1.0 googleapis-common-protos-1.59.0 h11-0.14.0 httplib2-0.22.0 identify-2.5.22 idna-3.4 iniconfig-2.0.0 isort-5.12.0 jinja2-3.1.2 jsonschema-4.17.3 langcodes-3.3.0 loguru-0.7.0 lxml-4.9.2 mccabe-0.7.0 multidict-6.0.4 murmurhash-1.0.9 mypy-extensions-1.0.0 nodeenv-1.7.0 numpy-1.24.2 oauthlib-3.2.2 openai-0.27.2 orjson-3.8.10 outcome-1.2.0 packaging-23.1 pathspec-0.11.1 pathy-0.10.1 pinecone-client-2.2.1 platformdirs-3.2.0 playsound-1.2.2 pluggy-1.0.0 pre-commit-3.2.2 preshed-3.0.8 protobuf-4.22.3 py-cpuinfo-9.0.0 pyasn1-0.5.0 pyasn1-modules-0.3.0 pycodestyle-2.10.0 pycparser-2.21 pydantic-1.10.7 pyflakes-3.0.1 pyparsing-3.0.9 pyrsistent-0.19.3 pytest-7.3.1 pytest-asyncio-0.21.0 pytest-benchmark-4.0.0 pytest-cov-4.0.0 pytest-integration-0.2.3 pytest-mock-3.10.0 python-dateutil-2.8.2 python-dotenv-1.0.0 pywin32-306 pyyaml-6.0 readability-lxml-0.8.1 redis-4.5.4 regex-2023.3.23 requests-2.28.2 requests-oauthlib-1.3.1 rsa-4.9 selenium-4.9.0 six-1.16.0 smart-open-6.3.0 smmap-5.0.0 sniffio-1.3.0 sortedcontainers-2.4.0 soupsieve-2.4.1 spacy-3.4.4 spacy-legacy-3.0.12 spacy-loggers-1.0.4 srsly-2.4.6 thinc-8.1.9 tiktoken-0.3.3 tqdm-4.65.0 trio-0.22.0 trio-websocket-0.10.2 tweepy-4.13.0 typer-0.7.0 typing-extensions-4.5.0 uritemplate-4.1.1 urllib3-1.26.15 virtualenv-20.22.0 wasabi-0.10.1 webdriver-manager-3.8.6 websocket-client-1.5.1 win32-setctime-1.1.0 wsproto-1.2.0 yarl-1.9.1
```
没有错误即表明所有库安装成功。

5. 配置 Auto-GPT:
   i. 找到文件名为 `.env.template` 的文件在主文件夹中 /Auto-GPT 。 这个文件可能会因为前缀是点符号而在某些操作系统中默认隐藏起来。若要显示隐藏的文件，请按照您特定操作系统的指示进行操作（例如，在Windows中，单击“文件资源管理器”中的“查看”选项卡并勾选“隐藏项目”框；在macOS中，按下Cmd + Shift + .）。
   ii. 创建此文件的副本，并通过删除扩展名来调用它。最简单的方法是在命令提示符/终端窗口中执行此操作 `cp .env.template .env`。
   iii. 打开 `.env` 文件在文本编辑器中。
   iv. 找到行 `OPENAI_API_KEY=`.
   v. 在 `"="`后面， 输入您唯一的 OpenAI API 密钥（不含任何引号或空格）。如果您没有OpenAI API密钥，请访问 https://beta.openai.com/ 以获取一个。
   vi. E输入您要使用的服务的任何其他 API 密钥或令牌。
   vii. 保存并关闭 `.env` 文件。

   完成这些步骤后，您将正确配置项目的 API 密钥。
   
## 🔧 用法

1. 在终端中运行 `autogpt` Python 模块。
    * 在 Linux/MacOS:
    ```bash
    ./run.sh
    ```
    * 在 Windows:
    ```bash
    .\run.bat
    ```
    在 `.\run.bat` 后面加上 `--help` 可以列出您可以传递的所有可能的命令行参数。
2. 每次 Auto-GPT 响应后，从选项中选择授权命令，退出程序或向 AI 提供反馈。
    i. 通过输入 `y` 授权单个命令。
    ii. 通过输入 `y -N` 授权一系列连续的 _N_ 命令。例如，输入 `y -10` 将运行 10 次自动迭代。
    iii. 输入任何自由文本以向 Auto-GPT 提供反馈。
    iv. 通过输入 `n` 退出程序。


### 日志

活动和错误日志位于 `./output/logs`

打印出调试日志：

```
python -m autogpt --debug
```