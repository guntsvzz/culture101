import argparse
import random
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from participants import get_participant  # Import the function to get participant details

# Load environment variables
load_dotenv('.env')
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
OPENAI_API_VERSION = os.getenv('OPENAI_API_VERSION')
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')

# Define the folder where you want to save the conversation history
SAVE_FOLDER = 'saved_conversations'  # You can change this folder path as needed

# Ensure the folder exists
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def initialize_participant(name, role_description, model_name="gpt-4o-mini"):
    """
    Initialize a participant with a specific role description and model.
    """
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


def save_conversation_to_file(conversation_history, participant_1_name, participant_2_name):
    """
    Save the conversation history to a file in the specified folder.
    The filename will include the names of both participants.
    """
    # Create a filename based on the participant names
    file_name = f"{participant_1_name}_vs_{participant_2_name}_conversation.txt"
    file_path = os.path.join(SAVE_FOLDER, file_name)
    
    # Open the file and append the conversation history
    with open(file_path, 'a') as file:
        file.write(conversation_history + '\n\n')  # Append the conversation history


def load_questions_from_file(file_path="questions.txt"):
    """
    Load questions from a file. Each question should be on a new line.
    """
    with open(file_path, 'r') as file:
        questions = file.readlines()
    return [question.strip() for question in questions if question.strip()]


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Simulate a conversation between two agents.")
    parser.add_argument('--p1', required=True, help="Name of the first participant.")
    parser.add_argument('--p2', required=True, help="Name of the second participant.")
    parser.add_argument('--questions_file', default='questions.txt', help="Path to the file with predefined questions.")

    args = parser.parse_args()

    # Get participants dynamically
    participant_1_name = args.p1
    participant_2_name = args.p2

    # Get participant details
    participant_1 = get_participant(participant_1_name)
    participant_2 = get_participant(participant_2_name)

    # Initialize all participants
    models_and_prompts = {
        participant_1_name: {
            "model": initialize_participant(participant_1_name, participant_1["role_description"])[0],
            "prompt": initialize_participant(participant_1_name, participant_1["role_description"])[1],
        },
        participant_2_name: {
            "model": initialize_participant(participant_2_name, participant_2["role_description"])[0],
            "prompt": initialize_participant(participant_2_name, participant_2["role_description"])[1],
        }
    }

    # Load questions from file
    questions = load_questions_from_file(args.questions_file)

    # Define the chat prompt template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "{prompt}"),
        ("user", "{conversation_history}")
    ])

    # Simulate a dialogue loop
    conversation_turns = 5  # Number of turns
    participant_names = [participant_1_name, participant_2_name]  # Dynamic participant names

    for turn in range(conversation_turns):
        for participant in participant_names:
            # Randomly pick a question from the loaded questions
            selected_question = random.choice(questions)
            current_history = selected_question

            # Generate response for the current participant
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
            conversation_history = f"{participant}: {agent_response}"

            # Save the conversation history to a file
            save_conversation_to_file(conversation_history, participant_1_name, participant_2_name)


if __name__ == "__main__":
    main()
