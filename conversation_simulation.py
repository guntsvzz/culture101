import argparse
import random
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from participants import get_participant  # Import the function to get participant details
from utils import *


# Load environment variables
load_dotenv('.env')
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_VERSION = os.getenv('OPENAI_API_VERSION')
OPENAI_API_ORG = os.getenv('OPENAI_API_ORG')
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')

def initialize_participant(name, role_description, model_name="gpt-4o-mini", use_openai=False):
    """
    Initialize a participant with a specific role description and model.
    Switch between OpenAI and Azure based on the `use_openai` flag.
    """
    if use_openai:
        # Use OpenAI model
        model = ChatOpenAI(
            api_key=OPENAI_API_KEY,
            organization=OPENAI_API_ORG,
            model=model_name,
            temperature=0.7,
            max_tokens=128
        )
    else:
        # Default to Azure model
        model = AzureChatOpenAI(
            api_key=AZURE_OPENAI_API_KEY,
            api_version=OPENAI_API_VERSION,
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            model=model_name,
            temperature=0.7,
            max_tokens=128
        )

    prompt = f"""
    You are {name}. {role_description}
    Always respond from your perspective. Keep your responses short and simple.
    """
    return model, prompt

def prompt_agent(agent_name, model, prompt_template, conversation_history):
    """
    Generate a response for a single agent.
    """
    pipeline = prompt_template | model
    response = pipeline.invoke({
        "prompt": agent_name["prompt"],
        "conversation_history": conversation_history
    })
    return response.content

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Simulate a conversation between two agents.")
    parser.add_argument('--p1', required=True, help="Name of the first participant.")
    parser.add_argument('--p2', required=True, help="Name of the second participant.")
    parser.add_argument('--questions_file', default='questions.txt', help="Path to the file with predefined questions.")
    parser.add_argument('--use_openai', action='store_true', help="Use OpenAI instead of Azure for the models.")

    args = parser.parse_args()

    # Get participants dynamically
    participant_1_name = args.p1
    participant_2_name = args.p2
    use_openai = args.use_openai  # Whether to use OpenAI or Azure

    # Get participant details
    participant_1 = get_participant(participant_1_name)
    participant_2 = get_participant(participant_2_name)

    # Initialize all participants
    models_and_prompts = {
        participant_1_name: {
            "model": initialize_participant(participant_1_name, participant_1["role_description"], use_openai=use_openai)[0],
            "prompt": initialize_participant(participant_1_name, participant_1["role_description"], use_openai=use_openai)[1],
        },
        participant_2_name: {
            "model": initialize_participant(participant_2_name, participant_2["role_description"], use_openai=use_openai)[0],
            "prompt": initialize_participant(participant_2_name, participant_2["role_description"], use_openai=use_openai)[1],
        }
    }

    # Load questions from file
    questions = load_questions_from_file(args.questions_file)

    # Define the chat prompt template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "{prompt}"),
        ("user", "{conversation_history}")
    ])

    # Initial conversation setup
    conversation_history = random.choice(questions)  # Pick a random question from the file

    # Simulate a dialogue loop
    conversation_turns = 5  # Number of turns
    participant_names = [participant_1_name, participant_2_name]  # Dynamic participant names

    for turn in range(conversation_turns):
        for participant in participant_names:
            other_participant = participant_names[1 - participant_names.index(participant)]
            # Prepare conversation history for the current participant
            current_history = f"{other_participant} said: {conversation_history}" if turn > 0 else conversation_history

            # Generate response
            agent_response = prompt_agent(
                {"model": models_and_prompts[participant]["model"],
                 "prompt": models_and_prompts[participant]["prompt"]},
                models_and_prompts[participant]["model"],
                prompt_template,
                current_history
            )

            # Print the agent's response
            print(f"{participant}: {agent_response}")

            # Update conversation history
            conversation_history += f"\n{participant}: {agent_response}"

    # Optionally save the conversation to a file
    save_conversation_to_file(conversation_history, participant_1_name, participant_2_name)


if __name__ == "__main__":
    main()
