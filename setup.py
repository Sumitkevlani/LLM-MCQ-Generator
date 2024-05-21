from setuptools import find_packages,setup

setup(
    name = "mcq_generator",
    version = "0.1",
    author="Sumit Kevlani",
    author_email = "kevlanisumit2004@gmail.com",
    description = "This is a package to generate MCQ",
    url = "https://github.com/Sumitkevlani/LLM-MCQ-Generator",
    license = "MIT",
    install_requires = ["openai","langchain","python-dotenv","streamlit","PyPDF2"],
    packages = find_packages(),
)