image.png# Comparing_Explainable_Artificial_Intelligence_Methods_LIME_and_SHAP
This repository is the contribution the the paper "Comparing Explainable Artificial Intelligence Methods LIME and SHAP" for the bachelor seminar.

# Getting started
To reproduce the results presented in the paper, the following steps must be followed:

1. Clone the repository:
    ```
    >>> git clone https://github.com/MartinWohlan/Comparing_Explainable_Artificial_Intelligence_Methods_LIME_and_SHAP.git
    ```

2. Create an environment using conda. Therefore conda must be [installed](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). If already installed you can skip this step.
3. After installing conda you can create an environment that contains all the packages needed by executing the following command in your terminal (before executing navigate into the directory of the cloned repository):
    ```
    >>> conda env create -f environment.yaml
    ```
    Afterwards you can activate the environment:<br>
    ```
    >>> conda activate XAI
    ```
4. When executing the Jupyter Notebook in an IDE select the XAI environment as kernel.
5. Run the respective Jupyter Notebooks.