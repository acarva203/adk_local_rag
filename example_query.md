# terminal log

## query
### [user]:  how can you implement inline citations? 

11:11:08 - LiteLLM:INFO: utils.py:3831 -

LiteLLM completion() model= gemini-2.5-pro; provider = openai

[Document_RAG_Agent]: {"functionCall": {"name": "search_document", "args": {"query": "inline citations"}}}

11:11:17 - LiteLLM:INFO: utils.py:3831 -

LiteLLM completion() model= gemini-2.5-pro; provider = openai

11:11:23 - LiteLLM:INFO: utils.py:1470 - Wrapper: Completed Call, calling success_handler

11:11:23 - LiteLLM:INFO: utils.py:3831 -

LiteLLM completion() model= gemini-2.5-pro; provider = openai

11:11:32 - LiteLLM:INFO: utils.py:1470 - Wrapper: Completed Call, calling success_handler

11:11:32 - LiteLLM:INFO: utils.py:3831 -

LiteLLM completion() model= gemini-2.5-pro; provider = openai

## response 

### [Document_RAG_Agent]: 
Grounding with Google Search provides the specific source details from `grounding_metadata` needed to showaccurate citations. This grounding support should be displayed both inline within the response and in an aggregate list at the end.

An example of a citation in the aggregate list is:
```
Citations:
Wikipedia. "2026 FIFA World Cup." Retrieved February 11, 2026. (https://en.wikipedia.org/wiki/2026_FIFA_World_Cup)
```