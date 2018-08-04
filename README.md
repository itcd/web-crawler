# web-crawler
## A simple web spider with Scrapy and Python 3
Note the ordered mode is slower than the unordered mode.

### Prerequisite
Python 3  
scrapy  
unidecode  

### Installation
Install Anaconda 4 with Python 3 and then install the Python packages via the conda command:  
conda install scrapy -c conda-forge  
conda install unidecode  

### A potential problem on Windows
Some people might encounter the following problem on Windows.  
ImportError: DLL load failed: The operating system cannot run %1.  

Reinstalling cryptography may solve the problem:  
pip uninstall cryptography  
pip install cryptography  
