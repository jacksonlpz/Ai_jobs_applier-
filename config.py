# In this file, you can set the configurations of the app.

from src.utils.constants import (
    DEBUG, 
    ERROR, 
    # LLM_MODEL, # This is a string 'llm_model', not a model type constant
    OPENAI, 
    CLAUDE, 
    GEMINI, 
    MISTRAL, 
    HUGGINGFACE, 
    PERPLEXITY, 
    OLLAMA,
    GEMINI_MODEL_NAME,
    MISTRAL_MODEL_NAME
)

#config related to logging must have prefix LOG_
LOG_LEVEL = 'ERROR'
LOG_SELENIUM_LEVEL = ERROR
LOG_TO_FILE = False
LOG_TO_CONSOLE = False

MINIMUM_WAIT_TIME_IN_SECONDS = 60

JOB_APPLICATIONS_DIR = "job_applications"
JOB_SUITABILITY_SCORE = 7

JOB_MAX_APPLICATIONS = 5
JOB_MIN_APPLICATIONS = 1

# Supported LLM model types: OPENAI, CLAUDE, GEMINI, MISTRAL, HUGGINGFACE, PERPLEXITY, OLLAMA
LLM_MODEL_TYPE = OPENAI # Default or user-set value. Examples: CLAUDE, GEMINI, MISTRAL

# Specific model names depending on the LLM_MODEL_TYPE
# For OPENAI: 'gpt-4o-mini', 'gpt-4', 'gpt-3.5-turbo', etc.
# For MISTRAL: MISTRAL_MODEL_NAME ('pixtral-large-2411')
# For GEMINI: GEMINI_MODEL_NAME ('gemini-2.5-flash-preview-05-20')
# For CLAUDE: 'claude-3-opus-20240229', 'claude-3-sonnet-20240229', 'claude-2.1', etc.
# For OLLAMA: 'llama2', 'mistral', etc. (ensure the model is pulled in your Ollama instance)
# For PERPLEXITY: 'llama-3-sonar-small-32k-chat', 'mistral-7b-instruct', etc.
# For HUGGINGFACE: e.g. 'mistralai/Mistral-7B-Instruct-v0.1'
LLM_MODEL = 'gpt-4o-mini' # Default or user-set value

# Only required for OLLAMA models
LLM_API_URL = ''
