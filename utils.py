import os

# Define the folder where you want to save the conversation history
SAVE_FOLDER = 'saved_conversations'  # You can change this folder path as needed

# Ensure the folder exists
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)
    
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
