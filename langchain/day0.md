## LangChain
- concept of chains 
- Model Agnostic development 
- Complete ecosystem 
- Memory and state handling 

#### What can you build?
- Coversational chatbot 
- AI knowledge assistant 
- AI Agents 
- Workflow automation 
- Summarization/Research Helpers 

#### Alternatives 
- Llamalndex 
- Haystack

### Components:
1. Models 
- These act as the interface for interacting with various AI models (like OpenAI or Anthropic). They solve the issue of non-standardized APIs, allowing developers to switch between different model providers with minimal code changes. The video distinguishes between Language Models (text-in/text-out) and Embedding Models (text-in/vector-out).
2. Prompts 
- This component manages the inputs sent to LLMs. The video emphasizes the importance of Prompt Engineering and demonstrates how LangChain enables dynamic, reusable, role-based, and few-shot prompting techniques to improve model output quality.
3. Chains 
- Representing the namesake of the framework, this component allows developers to build pipelines where the output of one step automatically becomes the input for the next, reducing the need for manual orchestration.
4. Memory
-  LLM APIs are inherently stateless. The Memory component adds the ability to retain conversational history, preventing the model from "forgetting" previous exchanges. Common types include ConversationBufferMemory and ConversationBufferWindowMemory
5. Index 
- These connect applications to external data sources (e.g., PDFs, databases). It involves four sub-components: Document Loaders, Text Splitters, Vector Stores, and Retrievers to enable semantic search over private data.
6. Agents 
- These are LLMs with reasoning capabilities and access to external tools. An Agent can decide which tool to call to complete a task (e.g., using a calculator or a weather API) to perform actions beyond just generating text.

