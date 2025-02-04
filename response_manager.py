"""
Response Manager module for generating appropriate responses
"""

import random
from conversation_patterns import PATTERNS

class ResponseManager:
    def __init__(self):
        """Initialize the response manager"""
        self.patterns = PATTERNS
    
    def generate_response(self, processed_input, context):
        """
        Generate a response based on processed input and context
        
        Args:
            processed_input (dict): Processed text information from NLPProcessor
            context (dict): Conversation context
            
        Returns:
            str: Generated response
        """
        # Extract relevant information
        tokens = processed_input['filtered_tokens']
        original_text = processed_input['original_text'].lower()
        
        # Check for greetings
        if self._is_greeting(tokens):
            return self._get_greeting_response()
        
        # Check for farewell
        if self._is_farewell(tokens):
            return self._get_farewell_response()
        
        # Check for gratitude
        if self._is_gratitude(tokens):
            return self._get_gratitude_response()
        
        # Check for questions
        if '?' in processed_input['original_text']:
            return self._handle_question(tokens, original_text)
        
        # Pattern matching
        for pattern in self.patterns:
            if any(keyword in original_text for keyword in pattern['keywords']):
                return random.choice(pattern['responses'])
        
        # Default response
        return self._get_default_response()
    
    def _is_greeting(self, tokens):
        """Check if the input is a greeting"""
        greetings = {'hello', 'hi', 'hey', 'greetings', 'morning', 'afternoon', 'evening'}
        return any(token.lower() in greetings for token in tokens)
    
    def _is_farewell(self, tokens):
        """Check if the input is a farewell"""
        farewells = {'bye', 'goodbye', 'farewell', 'see you', 'later'}
        return any(token.lower() in farewells for token in tokens)
    
    def _is_gratitude(self, tokens):
        """Check if the input expresses gratitude"""
        gratitude = {'thanks', 'thank', 'appreciate', 'grateful'}
        return any(token.lower() in gratitude for token in tokens)
    
    def _get_greeting_response(self):
        """Return a random greeting response"""
        responses = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Greetings! How may I assist you?",
            "Hello! I'm here to help!"
        ]
        return random.choice(responses)
    
    def _get_farewell_response(self):
        """Return a random farewell response"""
        responses = [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Farewell! Come back soon!",
            "Bye! It was nice talking to you!"
        ]
        return random.choice(responses)
    
    def _get_gratitude_response(self):
        """Return a random response to gratitude"""
        responses = [
            "You're welcome!",
            "Glad I could help!",
            "My pleasure!",
            "Anytime!"
        ]
        return random.choice(responses)
    
    def _handle_question(self, tokens, original_text):
        """Handle question-type inputs"""
        # Basic question handling logic
        if 'what' in tokens:
            return "I'll do my best to explain that."
        elif 'how' in tokens:
            return "Let me help you understand the process."
        elif 'why' in tokens:
            return "That's an interesting question. Let me try to explain."
        else:
            return "I'm not sure about that, but I'll try to help."
    
    def _get_default_response(self):
        """Return a random default response"""
        responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more about that.",
            "I'm still learning. Could you elaborate?",
            "Let me think about that for a moment."
        ]
        return random.choice(responses)
