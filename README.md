# fictional-engine
LLM to Read from Documents

# My Python Script: [llama_sidecar.py]

This is a Python script that interacts with an LLM and includes information from local documentation. It requires Python 3.11 and can be run on Windows/MAC/Linux.

**Getting Started**

1. **Install dependencies**: Run the following command in your terminal/command prompt to create a virtual
environment (venv) and install the required packages:
```
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```
This will create a new directory called `myenv` containing the virtual environment, activate it, and then install
all the dependencies listed in the `requirements.txt` file.

2. **Run the script**: Once you've installed the dependencies, you can run the script using:
```
python llama_sidecar.py
```

**Script Requirements**

* Python 3.11
* The following packages are required:
        + llama-index-llms-ollama
        + llama-index
        + llama-index-embeddings-huggingface
        + docx2txt

**License**

This script is released under the unlicense license. See the LICENSE file for more information.
