# Classification Evaluation Metrics

A coursework exercise calculating micro and macro precision, recall, and F1 for genre predictions. It makes the aggregation steps inspectable, then compares the manual calculations with scikit-learn metrics.

## My contribution

I implemented the preprocessing and metric functions in the [course starter](https://github.com/gi11ikin/problem-set-3). The repository includes the prediction and genre CSV files used by the exercise.

## What to inspect

- [Preprocessing](src/preprocessing.py) parses genre lists and counts true and false positives.
- [Metrics](src/metrics_calculation.py) calculates aggregate scores and calls scikit-learn for comparison.
- [Entry point](main.py) prints both sets of results for review.

## Run locally

Create a fresh Python environment, install `requirements.txt`, and run `python main.py` from the repository root. Inputs are read from `data/`. The program produces console output; it does not have a graphical interface. This exercise evaluates supplied predictions and does not train a genre classifier.

<details>
<summary>Original course assignment</summary>

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

![Decorative project banner: Precision, recall, and the way we count errors.](docs/readme/footer.svg)

---

## Author

**Kenneth Yeaher**  
Master of Information Management  
University of Maryland, College Park  
[![LinkedIn: Kenneth Yeaher](https://img.shields.io/badge/LinkedIn-Kenneth_Yeaher-0A66C2?style=flat)](https://www.linkedin.com/in/kennethyeaher/)

`Python` · `Precision and Recall`
