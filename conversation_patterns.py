"""
Conversation patterns and responses for the chatbot
"""

PATTERNS = [
    {
        'keywords': ['weather', 'temperature', 'climate'],
        'responses': [
            "I don't have access to real-time weather data, but I can discuss weather in general!",
            "Weather is quite an interesting topic! What would you like to know?",
            "I wish I could tell you the weather, but I'm just a simple chatbot."
        ]
    },
    {
        'keywords': ['name', 'who are you', 'what are you'],
        'responses': [
            "I'm an AI chatbot created to help and chat with you!",
            "You can call me ChatBot. I'm here to assist you!",
            "I'm your friendly neighborhood AI assistant!"
        ]
    },
    {
        'keywords': ['help', 'assist', 'support'],
        'responses': [
            "I'll do my best to help you! What do you need?",
            "I'm here to help! What can I do for you?",
            "Let me know what you need help with!"
        ]
    },
    {
        'keywords': ['joke', 'funny', 'humor'],
        'responses': [
            "I'm not very good at jokes, but I can try to make you smile!",
            "Why did the AI cross the road? To get to the other dataset!",
            "I'm still working on my sense of humor!"
        ]
    },
    {
        'keywords': ['time', 'date', 'day'],
        'responses': [
            "I don't have access to real-time information, but I can chat about time management!",
            "Time flies when you're having fun chatting!",
            "I wish I could tell you the time, but I'm not connected to a clock!"
        ]
    }
]
