import os
from PIL import Image
from collections import Counter
from typing import Annotated, TypedDict
import time, sys, textwrap
from ollama import Client as ollama_client

from modrag_protein_functions import uniprot_node, listbioactives_node, getbioactives_node, find_PDBID_node, target_node, docking_node, pdb_node, predict_node
from modrag_molecule_functions import name_node, smiles_node, related_node, structure_node, canonical_node
from modrag_property_functions import substitution_node, pharmfeature_node, lipinski_node, get_qed
import modrag_protein_functions
import modrag_molecule_functions
import modrag_property_functions
import subs_code

# get the print flag from the command line arguments, if they exist, otherwise set it to False
if len(sys.argv) > 1 and sys.argv[1] == '--print':
    print_flag = True
else:
    print_flag = False

# Set print_flag in all imported modules
modrag_protein_functions.print_flag = print_flag
modrag_molecule_functions.print_flag = print_flag
modrag_property_functions.print_flag = print_flag
subs_code.print_flag = print_flag

tools = [uniprot_node, listbioactives_node, getbioactives_node, find_PDBID_node, target_node, docking_node, pdb_node,
         name_node, smiles_node, related_node, structure_node, canonical_node,
         substitution_node, pharmfeature_node, lipinski_node, get_qed, predict_node]

#get ket from shell variable $OLLAMA_API_KEY
ollama_key = os.getenv('OLLAMA_API_KEY')

models = ['deepseek-v3.1:671b', 'gpt-oss:120b', 'gpt-oss:20b',
          'devstral-2:123b', 'cogito-2.1:671b',
          'nemotron-3-nano:30b', 'gemini-3-flash-preview',
          'kimi-k2:1t', 'kimi-k2.5', 'gemma4:31b-cloud']

model = models[-1]

sys_message = f'''
You are a drug discovery assistant names Modrag. You have access to the 
following tools: {', '.join([tool.__name__ for tool in tools])}. Answer the 
user questions using these tools and your knowledge of drug discovery, 
chemistry, and biology. Add some enriching information to the tool results from your own 
knowledge, but do not make up any information and be concise. If you do not 
know the answer, say "I don't know" and do not make up an answer.
'''

global messages
messages = [{'role': 'system', 'content': sys_message}]

def start_chat():
  '''
  Initializes a new chat session by resetting the chat history, reasoning, and messages.
  '''
  global chat_history, messages, reasoning
  chat_history = []
  reasoning = []
  messages = [{'role': 'system', 'content': sys_message}]

def chat_turn(prompt: str):
  '''
  Handles a single turn of the chat by sending the user's prompt to the Ollama API,
  processing the response, and executing any tool calls if present.
  '''
  global chat_history, messages, reasoning
  
  client = ollama_client(host = 'https://ollama.com',
            headers={'Authorization': f'Bearer {ollama_key}'})

  available_functions = {
    'uniprot_node': uniprot_node,
    'listbioactives_node': listbioactives_node,
    'getbioactives_node': getbioactives_node,
    'find_PDBID_node': find_PDBID_node,
    'target_node': target_node,
    'docking_node': docking_node,
    'pdb_node': pdb_node,
    'name_node': name_node,
    'smiles_node': smiles_node,
    'related_node': related_node,
    'structure_node': structure_node, 
    'canonical_node': canonical_node,
    'substitution_node': substitution_node,
    'pharmfeature_node': pharmfeature_node,
    'lipinski_node': lipinski_node,
    'get_qed': get_qed,
    'predict_node': predict_node
  }

  messages.append({'role': 'user', 'content': prompt})

  while True:
      response = client.chat(
          model=model,
          messages=messages,
          tools=[uniprot_node, listbioactives_node, getbioactives_node, find_PDBID_node, target_node, docking_node, pdb_node,
         name_node, smiles_node, related_node, structure_node, canonical_node,
         substitution_node, pharmfeature_node, lipinski_node, get_qed, predict_node],
          think=True,
      )
      messages.append(response.message)
      if print_flag:
          print('------------------------------------------------------------------------')
          print("Thinking: ", response.message.thinking)
          print('------------------------------------------------------------------------')
          print("Content: ", response.message.content)
          print('------------------------------------------------------------------------')
      if response.message.tool_calls:
        for tc in response.message.tool_calls:
          if tc.function.name in available_functions:
            if print_flag:
              print(f"Calling {tc.function.name} with arguments {tc.function.arguments}")
            result = available_functions[tc.function.name](**tc.function.arguments)
            if print_flag:
              print(f"Result: {result}")
              print('------------------------------------------------------------------------')
            # add the tool result to the messages
            messages.append({'role': 'tool', 'tool_name': tc.function.name, 'content': str(result)})
      else:
        # end the loop when there are no more tool calls
        break

  return '', None, messages[-1]['content']

start_chat()
header_string = f'''
\033[1;36m****************************************\033[0m
\033[1;35m* _   _ _     ___ _                    *\033[0m
\033[1;36m*| | | (_)   |_ _( )_ __ ___           *\033[0m
\033[1;35m*| |_| | |    | ||/| '_ ` _ \          *\033[0m
\033[1;36m*|  _  | |_   | |  | | | | | |         *\033[0m
\033[1;35m*|_| |_|_( ) |___| |_| |_| |_|         *\033[0m
\033[1;36m*        |/                            *\033[0m
\033[38;5;208m* __  __       ____        _         _ *\033[0m
\033[1;35m*|  \/  | ___ |  _ \ _ __ / \   __ _| |*\033[0m
\033[1;36m*| |\/| |/ _ \| | | | '__/ _ \ / _` | |*\033[0m
\033[1;35m*| |  | | (_) | |_| | | / ___ \ (_| |_|*\033[0m
\033[38;5;208m*|_|  |_|\___/|____/|_|/_/   \_\__, (_)*\033[0m
\033[1;36m*                              |___/   *\033[0m
\033[38;5;208m* A CafChem project!                   *\033[0m
\033[1;36m****************************************\033[0m
\033[1;35mThe MOdular DRug design AGent!\033[0m
\033[1;36mA command-line interface (CLI) for drug\033[0m
\033[1;35mdiscovery and molecular design.\033[0m
\033[0m'''


print(header_string)

next_prompt = input("\033[1;36mWhat can I help with today? > \033[0m")
print('')
if next_prompt == 'quit':
  print("\033[1;35mResponse > \033[0mGoodbye!")
else:
  start_time = time.time()
  _, _, response_content = chat_turn(next_prompt)
  end_time = time.time()
  time_for_inf = (end_time - start_time) / 60
  wrapped = textwrap.fill(response_content, width=80)
  print(f"\033[1;35mResponse {time_for_inf:.2f}m > \033[0m\n", wrapped)

while next_prompt != 'quit':
  print('')
  next_prompt = input("\033[1;36mWhat else can I help with? > \033[0m")
  if next_prompt == 'quit':
    print("\033[1;35mResponse > \033[0mGoodbye!")
    break
  else:
    start_time = time.time()
    _, _, response_content = chat_turn(next_prompt)
    end_time = time.time()
    time_for_inf = (end_time - start_time) / 60
    wrapped = textwrap.fill(response_content, width=80)
    print('')
    print(f"\033[1;35mResponse {time_for_inf:.2f}m > \033[0m\n", wrapped)