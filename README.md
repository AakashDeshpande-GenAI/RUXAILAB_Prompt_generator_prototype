# RUXAILAB_Prompt_generator_prototype
A small prototype Proof-of-Concept(PoC) for 'Study-Aware Prompt Generation System for AI Assisted Evaluation'
# Study-Aware Prompt Generation System (PoC)

A modular templating engine designed for RUXAILAB to standardize AI prompts for UX evaluation methodologies.

## 🌟 Why this Architecture?
This project uses **Separation of Concerns**:
1. **`prompt_engine.py`**: A Jinja2-based factory that dynamically assembles methodology-specific prompts using structured JSON data. It is model-agnostic.
2. **`test_pipeline.py`**: An execution pipeline that parses the generated prompt into `System Instructions` and `User Tasks`, and runs them against an LLM (currently configured for **Gemini 2.5 Flash**).

## 🚀 How to Run
1. Install dependencies: `pip install jinja2 google-generativeai python-dotenv rich`
2. Add your Google API key to a `.env` file: `GOOGLE_API_KEY="your_key"`
3. Run the pipeline:
   ```bash
   python test_pipeline.py
## Demo
![Prompt_generator](https://raw.githubusercontent.com/AakashDeshpande-GenAI/RUXAILAB_Prompt_generator_prototype/refs/heads/main/Images/Prompt_generator_output.png?token=GHSAT0AAAAAADS3LXKUCA3WNOOKCHKQYGEK2NDHIYA)
![Test_pipeline](https://raw.githubusercontent.com/AakashDeshpande-GenAI/RUXAILAB_Prompt_generator_prototype/refs/heads/main/Images/Test_LLM_output.png?token=GHSAT0AAAAAADS3LXKVL4IBFU7SGEPNYBAU2NDHJSA)
