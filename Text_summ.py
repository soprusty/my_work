{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7f4de7cd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6fb6f55b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting openai\n",
      "  Downloading openai-0.27.8-py3-none-any.whl (73 kB)\n",
      "Requirement already satisfied: requests>=2.20 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from openai) (2.27.1)\n",
      "Requirement already satisfied: tqdm in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from openai) (4.64.0)\n",
      "Requirement already satisfied: aiohttp in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from openai) (3.8.1)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (3.3)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (1.26.9)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (2.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (2021.10.8)\n",
      "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from aiohttp->openai) (4.0.1)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from aiohttp->openai) (1.2.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from aiohttp->openai) (5.1.0)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from aiohttp->openai) (21.4.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from aiohttp->openai) (1.2.0)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from aiohttp->openai) (1.6.3)\n",
      "Requirement already satisfied: typing-extensions>=3.6.5 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from async-timeout<5.0,>=4.0.0a3->aiohttp->openai) (4.1.1)\n",
      "Requirement already satisfied: colorama in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from tqdm->openai) (0.4.4)\n",
      "Installing collected packages: openai\n",
      "Successfully installed openai-0.27.8\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install openai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "13fb04ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "import openai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ef86e695",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Input \u001b[1;32mIn [8]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "17c52329",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Downloading streamlit-1.23.1-py2.py3-none-any.whl (8.9 MB)\n",
      "Collecting blinker<2,>=1.0.0\n",
      "  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.0.1 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (4.1.1)\n",
      "Collecting tzlocal<5,>=1.1\n",
      "  Downloading tzlocal-4.3-py3-none-any.whl (20 kB)\n",
      "Requirement already satisfied: toml<2 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: numpy<2,>=1 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (1.21.5)\n",
      "Collecting pympler<2,>=0.9\n",
      "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
      "Requirement already satisfied: packaging<24,>=14.1 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: pandas<3,>=0.25 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (1.4.2)\n",
      "Collecting altair<6,>=4.0\n",
      "  Downloading altair-5.0.1-py3-none-any.whl (471 kB)\n",
      "Requirement already satisfied: python-dateutil<3,>=2 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Collecting pyarrow>=4.0\n",
      "  Downloading pyarrow-12.0.1-cp39-cp39-win_amd64.whl (21.5 MB)\n",
      "Collecting gitpython!=3.1.19,<4,>=3\n",
      "  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)\n",
      "Requirement already satisfied: importlib-metadata<7,>=1.4 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (4.11.3)\n",
      "Collecting pydeck<1,>=0.1.dev5\n",
      "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: tenacity<9,>=8.0.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (8.0.1)\n",
      "Requirement already satisfied: watchdog in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: pillow<10,>=6.2.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (9.0.1)\n",
      "Collecting rich<14,>=10.11.0\n",
      "  Downloading rich-13.4.2-py3-none-any.whl (239 kB)\n",
      "Requirement already satisfied: requests<3,>=2.4 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from streamlit) (2.27.1)\n",
      "Collecting protobuf<5,>=3.20\n",
      "  Downloading protobuf-4.23.3-cp39-cp39-win_amd64.whl (422 kB)\n",
      "Collecting validators<1,>=0.2\n",
      "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
      "Requirement already satisfied: toolz in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.11.2)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.4.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.4)\n",
      "Collecting gitdb<5,>=4.0.1\n",
      "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
      "Collecting smmap<6,>=3.0.1\n",
      "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from importlib-metadata<7,>=1.4->streamlit) (3.7.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from packaging<24,>=14.1->streamlit) (3.0.4)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from pandas<3,>=0.25->streamlit) (2021.3)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from python-dateutil<3,>=2->streamlit) (1.16.0)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from requests<3,>=2.4->streamlit) (1.26.9)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from requests<3,>=2.4->streamlit) (3.3)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from requests<3,>=2.4->streamlit) (2.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from requests<3,>=2.4->streamlit) (2021.10.8)\n",
      "Collecting markdown-it-py>=2.2.0\n",
      "  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)\n",
      "Collecting pygments<3.0.0,>=2.13.0\n",
      "  Downloading Pygments-2.15.1-py3-none-any.whl (1.1 MB)\n",
      "Collecting mdurl~=0.1\n",
      "  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
      "Collecting tzdata\n",
      "  Downloading tzdata-2023.3-py2.py3-none-any.whl (341 kB)\n",
      "Collecting pytz-deprecation-shim\n",
      "  Downloading pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\soprusty\\anaconda3\\lib\\site-packages (from validators<1,>=0.2->streamlit) (5.1.1)\n",
      "Building wheels for collected packages: validators\n",
      "  Building wheel for validators (setup.py): started\n",
      "  Building wheel for validators (setup.py): finished with status 'done'\n",
      "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19582 sha256=d232a7e53621279a40aaafa711b3ac08d1642dbce0d1a7cef86f014b10cb5d50\n",
      "  Stored in directory: c:\\users\\soprusty\\appdata\\local\\pip\\cache\\wheels\\2d\\f0\\a8\\1094fca7a7e5d0d12ff56e0c64675d72aa5cc81a5fc200e849\n",
      "Successfully built validators\n",
      "Installing collected packages: tzdata, smmap, mdurl, pytz-deprecation-shim, pygments, markdown-it-py, gitdb, validators, tzlocal, rich, pympler, pydeck, pyarrow, protobuf, gitpython, blinker, altair, streamlit\n",
      "  Attempting uninstall: pygments\n",
      "    Found existing installation: Pygments 2.11.2\n",
      "    Uninstalling Pygments-2.11.2:\n",
      "      Successfully uninstalled Pygments-2.11.2\n",
      "  Attempting uninstall: protobuf\n",
      "    Found existing installation: protobuf 3.19.1\n",
      "    Uninstalling protobuf-3.19.1:\n",
      "      Successfully uninstalled protobuf-3.19.1\n",
      "Successfully installed altair-5.0.1 blinker-1.6.2 gitdb-4.0.10 gitpython-3.1.31 markdown-it-py-3.0.0 mdurl-0.1.2 protobuf-4.23.3 pyarrow-12.0.1 pydeck-0.8.1b0 pygments-2.15.1 pympler-1.0.1 pytz-deprecation-shim-0.1.0.post0 rich-13.4.2 smmap-5.0.0 streamlit-1.23.1 tzdata-2023.3 tzlocal-4.3 validators-0.20.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
      "spyder 5.1.5 requires pyqt5<5.13, which is not installed.\n",
      "spyder 5.1.5 requires pyqtwebengine<5.13, which is not installed.\n",
      "jupyter-server 1.13.5 requires pywinpty<2; os_name == \"nt\", but you have pywinpty 2.0.2 which is incompatible.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e8a8948a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fa9182e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-06-16 22:55:14.586 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\soprusty\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.header(\"summrize app\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d4099fff",
   "metadata": {},
   "outputs": [],
   "source": [
    "article_text = st.text_area(\"Enter text here which you want to summrize\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5234eafa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
