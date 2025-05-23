
<div align="center">


# AIHawk – the first Jobs Applier AI Agent

(IAMA,Stefano was Here :))

AIHawk's core architecture remains **open source**, allowing developers to inspect and extend the codebase. However, due to copyright considerations, we have removed all third‑party provider plugins from this repository.

For a fully integrated experience, including managed provider connections: check out **[laboro.co](https://laboro.co/)** an AI‑driven job board where the agent **automatically applies to jobs** for you.


---


AIHawk has been featured by major media outlets for revolutionizing how job seekers interact with the job market:

[**Business Insider**](https://www.businessinsider.com/aihawk-applies-jobs-for-you-linkedin-risks-inaccuracies-mistakes-2024-11)
[**TechCrunch**](https://techcrunch.com/2024/10/10/a-reporter-used-ai-to-apply-to-2843-jobs/)
[**Semafor**](https://www.semafor.com/article/09/12/2024/linkedins-have-nots-and-have-bots)
[**Dev.by**](https://devby.io/news/ya-razoslal-rezume-na-2843-vakansii-po-17-v-chas-kak-ii-boty-vytesnyaut-ludei-iz-protsessa-naima.amp)
[**Wired**](https://www.wired.it/article/aihawk-come-automatizzare-ricerca-lavoro/)
[**The Verge**](https://www.theverge.com/2024/10/10/24266898/ai-is-enabling-job-seekers-to-think-like-spammers)
[**Vanity Fair**](https://www.vanityfair.it/article/intelligenza-artificiale-candidature-di-lavoro)
[**404 Media**](https://www.404media.co/i-applied-to-2-843-roles-the-rise-of-ai-powered-job-application-bots/)


## Configuration

Configuring AIHawk involves setting up your preferred Large Language Model (LLM) provider and other operational parameters.

### LLM Provider Setup

You can choose which LLM provider and model AIHawk uses for its operations. This is configured in the `config.py` file.

1.  **Select your LLM Provider and Model**:
    Open `config.py` and modify the following variables:
    *   `LLM_MODEL_TYPE`: Set this to the provider you want to use.
    *   `LLM_MODEL`: Set this to the specific model from the chosen provider.

    **Examples**:

    *   **For MistralAI**:
        ```python
        # In config.py
        from src.utils.constants import MISTRAL, MISTRAL_MODEL_NAME
        # ...
        LLM_MODEL_TYPE = MISTRAL
        LLM_MODEL = MISTRAL_MODEL_NAME # This is 'pixtral-large-2411'
        ```

    *   **For Google Gemini**:
        ```python
        # In config.py
        from src.utils.constants import GEMINI, GEMINI_MODEL_NAME
        # ...
        LLM_MODEL_TYPE = GEMINI
        LLM_MODEL = GEMINI_MODEL_NAME # This is 'gemini-2.5-flash-preview-05-20'
        ```
    *   Other supported providers include OpenAI, Claude, Ollama, HuggingFace, and Perplexity. Refer to the comments in `config.py` for more examples.

2.  **Set API Keys**:
    API keys for the LLM providers are managed via environment variables or a `secrets.yaml` file.
    *   Create a `secrets.yaml` file in a `data_folder` directory at the root of the project (i.e., `data_folder/secrets.yaml`). You can copy `data_folder_example/secrets.yaml` as a template.
    *   Add your API key to this file. For example:
        *   For MistralAI, add: `MISTRAL_API_KEY: 'your_mistral_api_key_here'`
        *   For Google Gemini, add: `GEMINI_API_KEY: 'your_google_gemini_api_key_here'`
    *   Alternatively, set these as environment variables (e.g., `export MISTRAL_API_KEY='your_key'`). The application uses `python-dotenv` to load these variables.

    Ensure the API key for the selected `LLM_MODEL_TYPE` is correctly set up for AIHawk to function.

