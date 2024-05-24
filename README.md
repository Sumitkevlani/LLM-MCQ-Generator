# LLM-MCQ-Generator

Create a virtual environment for your application using python

1. python -m venv env
2. cd env/Scripts
3. activate(use .\activate if activate does not work)

Create a virtual environment for your application using anaconda

1. conda create -p env python=<python_version_name> -y
2. source activate ./env

## Notes and Learnings

This section contains the extra information and notes you want to retain.

### Learnings

- **setup.py**: This file contains metadata related to the project which contains project name,author,author name,author email,etc.
- **find_packages()**: This method will discover all the local packages in the project directory.
- **init.py**: This file is used to create a local package for a directory.
- To install all the packages we use pip install -r requirements.txt
- To install the local packages in the virtual environment use -e .
- traceback module is used to do the work of logging and debugging.
- **os.getenv("VAR")**: are used to get environment variables that are either specified in the system environment variables or in the local environment using .env file or using EXPORT keyword in the terminal.
- **OpenAI**: OpenAI class is used to interact with the models of the OpenAI class. It works as a wrapper over the OpenAI API.
- **PromptTemplate**: PromptTemplate class is used to create a parameterized and reusable prompt template.
- **LLMChain**: LLMChain class is used to create a chain of operations that involves LLM.
- **SequentialChain**: SequentialChain is used to create a sequence of chains in which the output of one operation will be served as the input for the other operation.
- **get_openai_callback()**: Here this function is used to get the information regarding number of tokens used and the number of prompt tokens used. So, basically the total cost associated with the API call can be achieved.
- **Difference between response['quiz'] and response.get('quiz')**:
  Here we have a difference between both the approaches that is that if the key does not exist in the dictionary the first method raises KeyError but the second method returns None or optionally it can return a default value if specified. Example: response.get('quiz',default)
- **json.dumps() and json.loads()**:
  In Python Json module, we have two functions:
  json.dumps(): Serializing the Python object to JSON string
  json.loads(): Deserialize the JSON string to Python object
