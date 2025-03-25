# utils/agent_handler.py
# Description: This file contains the Agent_Handler class which is responsible for handling the agents in the simulation.

# Importing Libraries
# Importing Libraries
# Importing Libraries
import google.generativeai as genai
import os
from smolagents.agents import CodeAgent


# Configure Google API
genai.configure(api_key= 'AIzaSyCO8rW1eWbshh9nQ5fOxIGUX_v64zrSUuk')

# Initiate CodeAgent with correct parameters
agent = CodeAgent(
    name="Customer Support Agent",
    model="gemini-1.5-flash",  # Specify the Gemini model
    tools=[] # Provide tools if needed (empty for now)
)

# Define a function to get Gemini AI responses
def get_gemini_response(user_query):
    """This function takes a user query as input and returns the response from the Gemini agent."""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_query)
        return response.text
    except Exception as e:
        return f"❗ Error fetching response: {str(e)}"

# Define a function to handle user queries using CodeAgent and Gemini AI
def agent_handler(user_query):
    """Handle user queries using CodeAgent and Gemini AI."""
    
    # Define agent's action mappings
    actions = {
        'faq': lambda query: get_gemini_response(query),
        'task': lambda query: f"Performing task: {query}"
    }

    # Analyze the query and route to the appropriate action
    if 'price' in user_query.lower():
        return actions['faq'](user_query)
    elif 'schedule' in user_query.lower():
        return actions['task'](user_query)
    else:
        return get_gemini_response(user_query)

if __name__ == "__main__":
    # Test with a sample query
    query = "What is the price of the Apple Mobile product?"
    response = agent_handler(query)
    print(response)