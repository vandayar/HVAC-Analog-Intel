"""
HVAC-Intel: Multimodal Fault Detection
Author: Phartheeb Tanjore Kandasamy
"""
import google.generativeai as genai

class HVAC_Agent:
    def __init__(self, api_key="YOUR_API_KEY"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def run_field_diag(self, img_path):
        # Reasoning for non-IoT blink codes
        prompt = """
        AI Field Service Agent: 
        1. Identify HVAC model from label/board.
        2. Detect LED Blink Code (Color/Frequency).
        3. Match to Service Manual: Provide Fault, Safety Steps, and Part #.
        """
        # Process image input from technician
        response = self.model.generate_content([prompt, img_path])
        return response.text

if __name__ == "__main__":
    # Simulate a technician's field upload
    print(HVAC_Agent().run_field_diag("control_board_error.jpg"))
