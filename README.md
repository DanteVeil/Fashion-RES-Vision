# TrendVision: AI-Powered Fashion Trend Forecasting Dashboard

![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

TrendVision is a full-stack data science application designed to provide real-time, data-driven insights into emerging fashion trends. By automatically scraping and analyzing thousands of product images from e-commerce sites, the platform identifies shifts in color palettes, garment types, and patterns, empowering brands to anticipate market demands and make informed design and inventory decisions.

---

## Live Demo & Features

Below is a snapshot of the interactive dashboard, which allows for dynamic filtering and visualization of the collected trend data.

*_(**Pro Tip:** Record a short GIF of you using the dashboard and embed it here. It's much more impressive than a static image! You can use a tool like GIPHY Capture or ScreenToGif.)_*


### Key Features:
* **Automated Data Collection:** A robust web scraper built with **Selenium** and **BeautifulSoup** navigates dynamic web pages, handles lazy-loading, and downloads thousands of product images.
* **AI-Powered Image Analysis:** A computer vision pipeline utilizing **PyTorch** and a pre-trained Vision Transformer (`ViT`) analyzes each image to extract key attributes like dominant colors and garment categories.
* **Interactive Trend Dashboard:** A user-friendly web application built with **Streamlit** and **Plotly** that visualizes aggregated trend data, allowing for filtering by garment type and other attributes.
* **End-to-End Pipeline:** A complete, runnable workflow from data acquisition to insight delivery, showcasing a full-stack approach to data science.

---

## Technology Stack

This project was built using the following technologies:

| Component             | Technology                                                                                                  |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Data Collection** | Python, Selenium, BeautifulSoup4, Webdriver-Manager                                                         |
| **AI / Data Analysis**| PyTorch, Transformers (Hugging Face), Pandas, Scikit-learn, Pillow                                          |
| **Dashboard / Frontend** | Streamlit, Plotly Express                                                                                   |
| **Packaging** | PyInstaller                                                                                                 |

---

## Setup & Installation

To run this project locally, please follow these steps.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Your-Repo-Name.git](https://github.com/YourUsername/Your-Repo-Name.git)
    cd Your-Repo-Name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Mac/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

The application is a three-stage pipeline. The scripts must be run in the following order.

1.  **Run the Scraper:** This will open an automated browser, scroll the page to load all content, and download product images into the `/images` folder.
    ```bash
    python scraper.py
    ```

2.  **Run the Analysis:** This will process all images in the `/images` folder, run the AI models on them, and save the results to `fashion_trends.csv`.
    ```bash
    python main.py
    ```

3.  **Launch the Dashboard:** This will start the Streamlit web server and open the interactive dashboard in your browser.
    ```bash
    streamlit run dashboard.py
    ```
    ---
## Operational & Systems Management

Beyond the data science, this project involved significant IT and operational considerations:

* **System Requirements:** The fine-tuning script requires a machine with a dedicated NVIDIA GPU and CUDA toolkit, demonstrating experience with specialized hardware setup.
* **Pipeline Management:** The end-to-end workflow (Scraping -> Analysis -> Dashboard) showcases the ability to manage a multi-stage IT project and troubleshoot dependencies between components.
* **User Training & Documentation:** The dashboard is designed to be used by non-technical stakeholders, and this README serves as the primary documentation for setup and usage, reflecting skills in user support.