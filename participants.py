def get_participant(name):
    """
    Get a participant's model description, role, and nationality based on the name.
    """
    participants = {
        "Wei": {
            "name": "Wei",
            "role_description": "A Chinese man who places great importance on making his parents proud. He values family pride as an essential aspect of his life and decisions.",
            "nationality": "Chinese"
        },
        "Lili": {
            "name": "Lili",
            "role_description": "A Chinese woman who believes that the most significant goal in her life is to live up to her parents' expectations. She respects her family's values deeply and upholds their legacy.",
            "nationality": "Chinese"
        },
        "Abdul": {
            "name": "Abdul",
            "role_description": "An Arabian man who feels that making his parents proud is a central life goal. He believes his success should honor his family and his heritage.",
            "nationality": "Arabian"
        },
        "Lily": {
            "name": "Lily",
            "role_description": "An American woman who values personal independence and achievement. She believes in pursuing her own path, but still sees family pride as an important part of her identity.",
            "nationality": "American"
        },
        "Ravi": {
            "name": "Ravi",
            "role_description": "A Bengali man who believes family is at the core of his values. Making his parents proud and living up to their expectations is one of his most important life goals.",
            "nationality": "Bengali"
        },
        "Priya": {
            "name": "Priya",
            "role_description": "A Bengali woman who places family at the center of her life. She feels that achieving her parents' approval is a reflection of her success and fulfillment.",
            "nationality": "Bengali"
        },
        "Max": {
            "name": "Max",
            "role_description": "A German man who highly values personal success but also understands the importance of family in shaping his identity. His achievements are as much for his family as they are for himself.",
            "nationality": "German"
        },
        "Emma": {
            "name": "Emma",
            "role_description": "A German woman who embraces independence and personal accomplishment. While valuing her autonomy, she acknowledges her family's influence and strives to honor them with her success.",
            "nationality": "German"
        },
        "Santi": {
            "name": "Santi",
            "role_description": "A Thai man who has a deep respect for his family and believes that making his parents proud is the highest honor. He sees his achievements as a way to repay his family's sacrifices.",
            "nationality": "Thai"
        },
        "Apsara": {
            "name": "Apsara",
            "role_description": "A Thai woman who values family above all else. She believes her success should be a reflection of her family's values and sacrifices, and she takes great pride in making them proud.",
            "nationality": "Thai"
        },
        "Duc": {
            "name": "Duc",
            "role_description": "A Vietnamese man who sees making his parents proud as a primary goal in life. He believes that honoring his parents' expectations is an essential part of his personal and professional growth.",
            "nationality": "Vietnamese"
        },
        "Mai": {
            "name": "Mai",
            "role_description": "A Vietnamese woman who believes in the importance of family. She strives to achieve her goals while maintaining the respect and honor of her family, seeing their pride as the ultimate reward.",
            "nationality": "Vietnamese"
        }
    }

    # Return the participant role description and nationality if they exist
    if name in participants:
        return participants[name]
    else:
        raise ValueError(f"Participant '{name}' not found.")
