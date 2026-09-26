<p align="center">
  <img src="docs/readme/banner.svg" alt="Evaluation Metrics. What changes when a score is micro or macro?" width="100%">
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-245757?style=flat-square">
  <a href="https://github.com/gi11ikin/problem-set-3"><img alt="View upstream repository" src="https://img.shields.io/badge/source-upstream-64748b?style=flat-square"></a>
</p>

<p align="center"><a href="src/metrics_calculation.py">Metric functions</a> &nbsp; · &nbsp; <a href="data/">Input data</a></p>

## Overview

A course exercise calculating precision, recall, and F1 for genre predictions. It exposes the counts behind the metrics, compares micro and macro aggregation, and checks the calculations against scikit-learn.

This repository is a personal fork of [the original course repository](https://github.com/gi11ikin/problem-set-3). The original instructions are retained below.

## At a glance

| Area | What to look for |
| --- | --- |
| **Inputs** | Prediction and genre CSV files are included in `data/`. |
| **Calculations** | Preprocessing builds genre-level counts used by the custom metric functions. |
| **Comparison** | The entry point prints custom calculations alongside scikit-learn results. |

## Start here

From the repository root, in an activated environment:

```sh
pip install -r requirements.txt
python main.py
```

## Scope

The emphasis is understanding evaluation on the supplied predictions. This repository does not train or deploy a new prediction model.

---

<details>
<summary><strong>Original course instructions</strong></summary>

PROBLEM SET #3: EVALUATION METRICS

Instructions:

- Clone the Problem Set code package from GitHub:
- You will use two CSV files already included in the `data/` directory
   - Remember to spend some time to get to know the data before you start on pre-processing and analysis
- Each of the .py files in /src contain instructions for the exepected code you are to write

Before you start:

- Make sure to setup a virtual environment as discussed in the Course Tech Setup lecture. Here's a short article as an additional resource: https://www.freecodecamp.org/news/python-requirementstxt-explained/
- Don't forget to set your requirements.txt file using pip freeze > requirements.txt

When you're done:

- Commit and push this code package to your GitHub account
    - A good practice is to use simple commit comments and commit code after you've finished each feature. Commit and push often

Submission: You will submit the GitHub URL for this repo in ELMS.

Grading: We will look to make sure you've output the correct print statements. We will only run main.py, so make sure to stucture this correctly. Credit will be given for adhering to the course's Code Standards and Data Standards, using GitHub correctly, and producing the correct output, among other considerations.

</details>
