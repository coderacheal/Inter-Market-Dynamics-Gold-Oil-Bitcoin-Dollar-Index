<a name="readme-top"></a>

<div align="center">
  <h1><b>Inter-Market Dynamics: Exploring Relationships Between the U.S. Dollar Index and Key Commodities</b></h1>
</div>


<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Inter-Market Dynamics](#sunday-)
  - [🛠 Built With ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
    - [Link to Model](#Link-to-Mode)
    - [Spin Up Docker containerl](#Spin-Up-Docker-container)
  - [👥 Authors ](#-authors-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Inter-Market Dynamics <a name="about-project"></a>

This project investigates the inter-market dynamics between gold, crude oil, and Bitcoin, examining their collective influence on the U.S. Dollar Index (DXY). Using daily price data spanning the past decade (2014–2024), the study seeks to uncover critical patterns and dependencies among these assets and to construct a predictive model for the dollar index. Such a model could be instrumental in evaluating and mitigating portfolio risk.


**Note that is a pure application is designed and built for eduction and academic purposes not for real investment**

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>Best Models</summary>
  <ul>
    <li>Random Forest</li>
    <li>Stacking Classifier</li>
  </ul>
</details>

<details>
  <summary>Front end</summary>
  <ul>
    <li><a href="https://docs.streamlit.io/get-started">Streamlit</a></li>
  </ul>
</details>

<details>
  <summary>API</summary>
  <ul>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
  </ul>
</details>

<details>
  <summary>Methodology</summary>
  <ul>
    <li><a href="https://www.datascience-pm.com/crisp-dm-2/">CRISP-DM</a></li>
  </ul>
</details>

<details>
  <summary>Version Control</summary>
    <ul>
      <li>Git & GitHUb</li>
    </ul>
  </details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Key Features <a name="key-features"></a>

- **Predict movement in the in the dollar price index**
- **Calculate the weight of every commodity in a portfolio**
- **Save portfolio Information**


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

 - Streamlit

Example command:


### Setup

Command to clone this repository to your desired folder:

```sh
  cd my-project
  git clone https://github.com/coderacheal/Inter-Market-Dynamics-Gold-Oil-Bitcoin-Dollar-Index

```

### Install

Install this project with:

```sh
  cd Inter-Market-Dynamics-Gold-Oil-Bitcoin-Dollar-Index

```

### Install dependencies

```sh
  pip install requirements.txt

```


### Usage

**Command To run the app:**

```sh

  streamlit run 🏠_Home.py

OR

  python -m streamlit run 🏠_Home.py

```


### Live Link (App)

Please find a link to the app here [here](https://inter-market-dynamics-gold-oil-bitcoin.onrender.com)




### API

**Command To run the API:**

```sh

  uvicorn api.ml_endpoints:app --reload

OR

  python -m uvicorn api.ml_endpoints:app --reload

```
![image](https://github.com/user-attachments/assets/39c1f268-4311-4c55-b00d-0c89b630f8e5)


## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Appiah-kubi Racheal**

- GitHub: [GitHub Profile](https://github.com/coderacheal)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/racheal-appiah-kubi/)

🕵🏽‍♀️ **Dominguez Faraco Alfredo**

- GitHub: [GitHub Profile](https://github.com/alfdomi)
- LinkedIn: [LinkedIn Profile](hhttps://www.linkedin.com/in/alfaraco/)

🕵🏽‍♀️ **Hemmati Hamed**

- GitHub: [GitHub Profile](https://github.com/hamed-hemmati)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/hhmmti)

🕵🏽‍♀️ **Hosseini Mahla**

- GitHub: [GitHub Profile](https://github.com/mahlahsn)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/mahlahosseinin/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show us some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

We would like to thank all the free available resource made available online 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
