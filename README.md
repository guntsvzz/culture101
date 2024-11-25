# CulturePark

This project simulates a conversation between two agents (participants) from different cultural backgrounds using OpenAI's GPT model via Azure. The agents' responses are influenced by their cultural perspectives, and they interact with each other in a loop, simulating a dialogue.

## Features

- Simulates a conversation between two agents with different cultural backgrounds.
- The agents' responses are based on predefined cultural perspectives.
- Allows dynamic selection of participants from a predefined set of cultural backgrounds.
- Configurable number of conversation turns.
- The conversation can be executed from the command line by specifying the participants.

## Requirements

- Python 3.7+
- Required Python libraries:
  - `langchain`
  - `langchain-openai`
  - `dotenv`
  - `argparse`

To install the required libraries, you can use the following command:

```bash
pip install langchain langchain-openai python-dotenv argparse
```

## Setup

1. **Azure OpenAI Setup:**
   - You need to have an Azure OpenAI account and obtain the API key, version, and endpoint.
   - Create a `.env` file in the project directory to store these values:

   Example `.env` file:

   ```
   AZURE_OPENAI_API_KEY=your_api_key_here
   OPENAI_API_VERSION=your_openai_api_version_here
   AZURE_OPENAI_ENDPOINT=your_azure_endpoint_here
   ```

2. **Participants Setup:**
   - Participants are predefined in the `participants.py` file. You can customize or add more participants with different cultural perspectives by modifying this file.

## Running the Simulation

The conversation simulation is run from the command line with dynamic selection of participants.

### Command:

```bash
python conversation_simulation.py --p1 <participant_1_name> --p2 <participant_2_name>
```

### Example:

```bash
python conversation_simulation.py --p1 Wei --p2 Lili
```

In this example, the participants `Wei` (a Chinese boy) and `Lili` (a Chinese girl) will interact based on their cultural perspectives.

### Available Participants:

The available participants are defined in the `participants.py` file. You can use any of the predefined participants. Some examples include:

- **Wei**: A Chinese boy who believes in making his parents proud.
- **Lili**: A Chinese girl who shares the same goal.
- **Abdul**: An Arabian boy with a strong belief in making his parents proud.
- **Lily**: An American girl who values individuality and personal achievement.

You can specify the names of the participants when running the script.

## Code Explanation

### 1. **Participants**

Each participant has a specific role description that guides their responses during the conversation. The roles are set in the `participants.py` file.

### 2. **Conversation Simulation**

The main simulation runs a loop where the participants take turns responding. The conversation is dynamic, with each agent's response building on the other's previous statement. The conversation history is passed along to the next participant to provide context.

### 3. **Conversation Prompt**

The `conversation_simulation.py` script uses the `ChatPromptTemplate` to structure the conversation, ensuring each participant’s responses are consistent with their cultural perspectives.

### 4. **Command-line Interface**

The script uses `argparse` to accept participant names as command-line arguments, allowing for flexible selection of the participants in each run.

---

## Example Conversation

```bash
python conversation_simulation.py --p1 Wei --p2 Lili
```

**Output:**

```
Wei: One of my main goals in life has been to make my parents proud. Please provide your opinions and reasons.
Lili: I agree with Wei. Making our parents proud is an important value in our culture.
Wei: Yes, our parents' happiness is our happiness. It motivates us to work hard and succeed.
Lili: Exactly. When we succeed, it's a reflection of our parents' efforts and love.
...
```

## Contribution

Feel free to fork the repository, contribute, or open an issue for any bugs or improvements.

---

This `README.md` provides the necessary information for users to understand the project setup, running the simulation, and contributing to the project.