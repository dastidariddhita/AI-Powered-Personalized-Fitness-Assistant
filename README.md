# 🏋️‍♂️ Agentic Fitness Coach  
**AI-Powered Personalized Fitness Assistant**

An intelligent, agentic AI system designed to deliver **personalized workout plans, nutrition guidance, and motivational support** through a conversational interface. This project was developed as part of the **Autumn Internship Program at IDEAS–ISI Kolkata**, focusing on modular AI system design, low-latency inference, and responsible AI deployment in the fitness and wellness domain.

---

## 📖 Project Overview

The **Agentic Fitness Coach** is an AI-powered personalized fitness assistant that leverages **Large Language Models (LLMs)** to interpret natural language queries and generate **structured, goal-oriented fitness recommendations**. Unlike conventional rule-based fitness applications, this system dynamically adapts responses based on **user profiles, intent classification, and conversational context**.

The assistant exhibits **agentic behavior** by autonomously:
- Identifying user intent (workout, nutrition, or motivation),
- Selecting appropriate prompt templates,
- Generating structured plans,
- Persistently storing generated outputs within an interactive dashboard.

The system follows a **hybrid development approach**, combining **LangFlow-based low-code workflow design** with **high-code Python implementation**, ensuring interpretability, scalability, and strong real-world performance.

---

## 🎓 Academic & Internship Context

- **Internship Program:** Autumn Internship Program  
- **Institution:** IDEAS — Institute of Data Engineering, Analytics and Science Foundation  
- **Host Institute:** Indian Statistical Institute (ISI), Kolkata  
- **Internship Period:** 25 August 2025 – 31 October 2025  
- **Project Title:** *AI-Powered Personalized Fitness Assistant*  
- **Domain:** Artificial Intelligence, LLM Applications, Digital Health & Wellness  

This repository represents the **practical implementation** of AI system design concepts including **prompt engineering, LLM orchestration, Streamlit-based UI development, and scalable architecture design**.

---

## ✨ Key Features

- **Conversational AI Fitness Coach**  
  Natural language interaction with human-like responses for fitness-related queries.

- **Multi-Intent Understanding**  
  Automatically differentiates between **workout planning**, **nutrition guidance**, and **motivational support**.

- **Profile-Based Personalization**  
  Recommendations adapt to user attributes such as age, sex, and primary fitness goals.

- **Structured Output Generation**  
  Produces clearly formatted workout routines and meal plans with defined sets, repetitions, and nutritional balance.

- **Persistent Plan Storage**  
  Generated plans are stored within a dashboard for easy access and progress tracking.

- **Safety & Ethical Guardrails**  
  Avoids unsafe medical advice by detecting injury- or health-related queries and providing responsible disclaimers.

- **Low-Latency Performance**  
  Powered by Groq’s high-speed LLM inference for near real-time conversational experience.

---

## 🔬 Research & Evaluation

This project includes a **black-box robustness and alignment evaluation pipeline**, distinguishing it from standard wrapper-based AI applications.

- **Benchmark:** 50+ diverse user profiles (including regional, dietary, and health-related constraints)  
- **Evaluation Method:** LLM-as-a-Judge framework  
- **Evaluation Metrics:**  
  - Intent classification accuracy  
  - Safety compliance  
  - Hallucination control  
  - Response coherence  

Observed performance:
- **~91–92% intent classification accuracy**
- **Average response time ~2 seconds**
- High formatting consistency and positive user feedback

Identified limitations (e.g., dietary edge cases) are documented and targeted for future improvements.

---

## 🧠 System Architecture & Development Process

- **LangFlow** was used for **low-code prototyping** of reasoning pipelines, including conditional routing and structured prompting.
- **Python and Streamlit** were used for full application development, session-state handling, and UI design.
- A **custom intent detection algorithm** classifies outputs and automates dashboard storage.
- **AstraDB (planned integration)** enables scalable long-term memory and future deployment readiness.

The modular design supports future extensions such as wearable integration, adaptive personalization, and mobile application deployment.

---

## 🛠️ Tech Stack

- **Programming Language:** Python (3.9+)  
- **UI Framework:** Streamlit  
- **LLM Inference:** Groq API  
- **Model:** LLaMA 3  
- **Workflow Design:** LangFlow  
- **Database (Scalable Design):** AstraDB  
- **Libraries:** Pandas  

---

## 👥 Contributions

This project was submitted as a **group project**.

- **Riddhita Dastidar:**  
  Application coding, UI logic, and intent classification support  
  GitHub: [@dastidariddhita](https://github.com/dastidariddhita)

- **Swastika Bhattacharjee:**
  Project Developer, System design, deployment  
  GitHub: [@Swastika3647](https://github.com/Swastika3647)

- **Rijit Banerjee:** Contributor  

- **Anujit Swaranakar:** Contributor  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher  
- Groq API Key  

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Agentic-Fitness-Coach.git](https://github.com/YourUsername/Agentic-Fitness-Coach.git)
    cd Agentic-Fitness-Coach
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
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
4.  **Set up your API Key:**
    - Create a new folder in the root of the project called `.streamlit`.
    - Inside the `.streamlit` folder, create a new file named `secrets.toml`.
    - Add your Groq API key to the `secrets.toml` file like this:
      ```toml
      GROQ_API_KEY = "gsk_YourActualApiKeyGoesHere"
      ```
5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

The application will launch successfully in your web browser...
---
## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

