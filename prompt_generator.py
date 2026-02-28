import json
import os
from jinja2 import Environment, FileSystemLoader

class PromptGenerator:
    def __init__(self, template_folder='templates'):
        # 1. Setup the Template Engine (The Machine)
        self.loader = FileSystemLoader(template_folder)
        self.env = Environment(loader=self.loader)

    def generate(self, methodology, input_data):
        """
        Takes the method name and data, returns the string prompt.
        """
        try:
            # Handle if user types "heuristic_evaluation" or "heuristic_evaluation.j2"
            if not methodology.endswith('.j2'):
                template_name = f"{methodology}.j2"
            else:
                template_name = methodology

            # 2. Select Template
            template = self.env.get_template(template_name)

            # 3. Render (Fill in the blanks)
            final_prompt = template.render(input_data)
            return final_prompt

        except Exception as e:
            return f"Error generating prompt: {str(e)}"

# --- THIS PART RUNS ONLY IF YOU RUN 'python main.py' DIRECTLY ---
if __name__ == "__main__":
    # Load dummy data for testing
    try:
        with open('input_data.json', 'r') as f:
            data = json.load(f)
            
        # Create the Generator
        my_generator = PromptGenerator()
        
        # Run it
        methodology = data.get('methodology', 'heuristic_evaluation')
        result = my_generator.generate(methodology, data)
        
        print("--- STANDALONE TEST OUTPUT ---")
        print(result)
        print("------------------------------")
        
    except FileNotFoundError:
        print("Error: input_data.json not found! Please create it.")