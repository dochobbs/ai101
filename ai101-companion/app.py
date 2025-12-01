"""
Spark - AI Learning Assistant Chatbot
A friendly mentor to help new AI users learn prompting and AI concepts
"""

from flask import Flask, render_template, jsonify, request
import json
import os
import re

app = Flask(__name__)


def load_json(filename):
  data_path = os.path.join(os.path.dirname(__file__), 'data', filename)
  with open(data_path, 'r') as f:
    return json.load(f)


# Load knowledge base at startup
GLOSSARY = load_json('glossary.json')
PROMPTS = load_json('prompts.json')
TOOLS = load_json('tools.json')

# Spark's personality and responses
SPARK_INTRO = """Hi! I'm Spark, your AI learning assistant. I'm here to help you become confident using AI tools.

I can help you with:
- Writing better prompts (just paste one and I'll give feedback!)
- Understanding AI terms and concepts
- Finding the right AI tool for your needs
- Getting prompt templates for common tasks

What would you like to explore?"""


def get_spark_response(message):
  """Generate Spark's response based on user message"""
  msg_lower = message.lower().strip()

  # Greeting detection
  greetings = ['hi', 'hello', 'hey', 'howdy', 'greetings', 'sup', "what's up"]
  if any(msg_lower == g or msg_lower.startswith(g + ' ') or msg_lower.startswith(g + ',') for g in greetings):
    return {
      'message': "Hello! Great to meet you. I'm Spark, and I'm here to help you learn AI. Are you looking to improve your prompts, learn some AI concepts, or find the right tool for a task?",
      'suggestions': ['Help me write better prompts', 'Explain AI terms to me', 'Find me an AI tool']
    }

  # Help / what can you do
  if any(phrase in msg_lower for phrase in ['help', 'what can you', 'what do you', 'how do you work']):
    return {
      'message': """I'd love to help! Here's what I can do:

**Prompt Help** - Paste any prompt and I'll analyze it with specific tips to make it better.

**AI Concepts** - Ask me "what is [term]?" for plain-English explanations of AI jargon like LLM, tokens, hallucinations, etc.

**Tool Recommendations** - Tell me what you want to accomplish and I'll suggest AI tools that fit.

**Prompt Templates** - Ask for a template for common tasks like writing emails, summarizing, coding help, etc.

Just type naturally - I'm here to help!""",
      'suggestions': ['Analyze my prompt', 'What is an LLM?', 'I need help with writing']
    }

  # Definition requests - "what is X", "define X", "explain X"
  definition_patterns = [
    r"what (?:is|are) (?:an? )?(.+?)[\?\.]?$",
    r"define (.+?)[\?\.]?$",
    r"explain (.+?)[\?\.]?$",
    r"what does (.+?) mean[\?\.]?$",
    r"tell me about (.+?)[\?\.]?$"
  ]

  for pattern in definition_patterns:
    match = re.search(pattern, msg_lower)
    if match:
      term_query = match.group(1).strip()
      result = find_glossary_term(term_query)
      if result:
        response = f"**{result['term']}**\n\n{result['definition']}"
        if result.get('example'):
          response += f"\n\n*Example: {result['example']}*"
        response += "\n\nWant me to explain any related concepts?"
        return {
          'message': response,
          'suggestions': get_related_terms(result['term'])
        }
      else:
        return {
          'message': f"I don't have a specific definition for '{term_query}' in my knowledge base, but I can try to explain!\n\nCould you tell me more about the context where you encountered this term?",
          'suggestions': ['Show me all AI terms', 'What is an LLM?', 'What are tokens?']
        }

  # Tool recommendations
  tool_triggers = ['recommend', 'suggest', 'tool for', 'app for', 'best for', 'help with', 'i need', 'i want to', 'how can i']
  if any(trigger in msg_lower for trigger in tool_triggers):
    tools_response = recommend_tools(msg_lower)
    if tools_response:
      return tools_response

  # Prompt template requests
  template_triggers = ['template', 'example prompt', 'prompt for', 'how to prompt', 'write a prompt']
  if any(trigger in msg_lower for trigger in template_triggers):
    return find_prompt_template(msg_lower)

  # Show all terms
  if 'all terms' in msg_lower or 'all concepts' in msg_lower or 'glossary' in msg_lower or 'list terms' in msg_lower:
    terms_list = ', '.join(sorted([t['term'] for t in GLOSSARY]))
    return {
      'message': f"Here are all the AI terms I can explain:\n\n{terms_list}\n\nJust ask 'What is [term]?' for any of these!",
      'suggestions': ['What is an LLM?', 'What is a token?', 'What is hallucination?']
    }

  # Show all tools
  if 'all tools' in msg_lower or 'list tools' in msg_lower:
    tools_list = '\n'.join([f"- **{t['name']}**: {t['description'][:60]}..." for t in TOOLS])
    return {
      'message': f"Here are AI tools I know about:\n\n{tools_list}\n\nTell me what you want to accomplish and I'll recommend the best fit!",
      'suggestions': ['I want to write better', 'I need help coding', 'I want to make images']
    }

  # Prompt analysis - if it looks like a prompt (longer text, or explicit request)
  analyze_triggers = ['analyze', 'review', 'feedback', 'improve', 'better', 'check this', 'rate this']
  if any(trigger in msg_lower for trigger in analyze_triggers) or len(message) > 80:
    return analyze_prompt(message)

  # Category browsing
  categories = ['writing', 'coding', 'learning', 'research', 'career', 'daily life', 'health', 'social media', 'creativity']
  for cat in categories:
    if cat in msg_lower:
      return get_templates_for_category(cat)

  # Default - try to be helpful
  return {
    'message': f"I want to make sure I help you with the right thing! Are you looking to:\n\n1. **Get feedback on a prompt** - Just paste it and I'll analyze it\n2. **Learn an AI concept** - Ask 'What is [term]?'\n3. **Find an AI tool** - Tell me what you want to accomplish\n4. **Get a prompt template** - Ask for templates by category\n\nWhat sounds most helpful?",
    'suggestions': ['Analyze my prompt', 'What is an LLM?', 'Help me find an AI tool', 'Show me writing templates']
  }


def find_glossary_term(query):
  """Find a matching glossary term"""
  query = query.lower().strip()
  # Remove common words
  query = re.sub(r'^(an?|the)\s+', '', query)

  for term in GLOSSARY:
    term_lower = term['term'].lower()
    # Direct match
    if query == term_lower:
      return term
    # Partial match
    if query in term_lower or term_lower in query:
      return term
    # Acronym match
    if '(' in term['term']:
      acronym = term['term'].split('(')[0].strip().lower()
      if query == acronym:
        return term
  return None


def get_related_terms(current_term):
  """Suggest related terms to explore"""
  related = []
  current_lower = current_term.lower()

  # Simple keyword matching for related concepts
  if 'llm' in current_lower or 'language model' in current_lower:
    related = ['What are tokens?', 'What is a transformer?', 'What is fine-tuning?']
  elif 'token' in current_lower:
    related = ['What is context window?', 'What is an LLM?', 'What is inference?']
  elif 'prompt' in current_lower:
    related = ['What is prompt engineering?', 'What is few-shot?', 'What is chain of thought?']
  elif 'hallucination' in current_lower:
    related = ['What are guardrails?', 'What is RAG?', 'What is alignment?']
  else:
    # Default suggestions
    related = ['What is an LLM?', 'What is a prompt?', 'What is hallucination?']

  return related[:3]


def recommend_tools(message):
  """Recommend tools based on user's needs"""
  msg_lower = message.lower()

  matched_tools = []

  # Match by use case
  use_case_keywords = {
    'writing': ['write', 'writing', 'email', 'content', 'blog', 'document', 'text'],
    'coding': ['code', 'coding', 'programming', 'developer', 'software', 'debug'],
    'images': ['image', 'picture', 'photo', 'art', 'visual', 'design', 'graphic'],
    'research': ['research', 'search', 'find', 'learn', 'study', 'information'],
    'productivity': ['productive', 'organize', 'notes', 'meeting', 'schedule']
  }

  detected_use_case = None
  for use_case, keywords in use_case_keywords.items():
    if any(kw in msg_lower for kw in keywords):
      detected_use_case = use_case
      break

  if detected_use_case:
    for tool in TOOLS:
      if detected_use_case in tool.get('use_cases', []):
        matched_tools.append(tool)

  if matched_tools:
    # Sort by beginner-friendliness for new users
    matched_tools.sort(key=lambda t: 0 if t.get('skill_level') == 'beginner' else 1)
    top_tools = matched_tools[:3]

    response = f"For {detected_use_case}, here are my top recommendations:\n\n"
    for tool in top_tools:
      free_tag = " (has free tier)" if tool.get('has_free_tier') else ""
      response += f"**{tool['name']}**{free_tag}\n{tool['description']}\n\n"

    response += "Would you like more details about any of these, or help with something else?"

    return {
      'message': response,
      'suggestions': [f"Tell me more about {top_tools[0]['name']}", 'Show me all tools', 'Help me write a prompt']
    }

  return None


def find_prompt_template(message):
  """Find relevant prompt templates"""
  msg_lower = message.lower()

  # Match by category
  category_keywords = {
    'Writing': ['email', 'writing', 'write', 'document', 'summary', 'feedback'],
    'Coding': ['code', 'debug', 'programming', 'developer'],
    'Learning': ['learn', 'study', 'explain', 'understand', 'teach'],
    'Career': ['job', 'career', 'interview', 'resume', 'cover letter'],
    'Research': ['research', 'compare', 'analyze'],
    'Daily Life': ['recipe', 'travel', 'decision', 'plan'],
    'Health': ['health', 'workout', 'medical', 'symptom'],
    'Social Media': ['social media', 'post', 'content', 'instagram', 'twitter'],
    'Creativity': ['creative', 'brainstorm', 'idea']
  }

  matched_category = None
  for category, keywords in category_keywords.items():
    if any(kw in msg_lower for kw in keywords):
      matched_category = category
      break

  if matched_category:
    templates = [p for p in PROMPTS if p['category'] == matched_category]
    if templates:
      response = f"Here are some {matched_category.lower()} prompt templates:\n\n"
      for t in templates[:3]:
        response += f"**{t['title']}**\n```\n{t['prompt']}\n```\n\n"
      response += "Just copy and customize the [bracketed] parts! Want me to explain how to modify these for your specific situation?"

      return {
        'message': response,
        'suggestions': ['Show me more templates', 'Analyze my prompt', 'Explain prompt structure']
      }

  # Default template response
  categories = sorted(list(set(p['category'] for p in PROMPTS)))
  return {
    'message': f"I have prompt templates for these categories:\n\n{', '.join(categories)}\n\nWhich category interests you? Or tell me what you're trying to accomplish!",
    'suggestions': [f'Show me {categories[0]} templates', f'Show me {categories[1]} templates', 'Help me with email writing']
  }


def get_templates_for_category(category):
  """Get templates for a specific category"""
  # Normalize category name
  cat_map = {
    'writing': 'Writing',
    'coding': 'Coding',
    'learning': 'Learning',
    'research': 'Research',
    'career': 'Career',
    'daily life': 'Daily Life',
    'health': 'Health',
    'social media': 'Social Media',
    'creativity': 'Creativity'
  }

  normalized = cat_map.get(category.lower(), category.title())
  templates = [p for p in PROMPTS if p['category'] == normalized]

  if templates:
    response = f"Here are {normalized} prompt templates:\n\n"
    for t in templates[:3]:
      response += f"**{t['title']}**\n```\n{t['prompt']}\n```\n\n"

    if len(templates) > 3:
      response += f"...and {len(templates) - 3} more! Ask if you want to see the rest.\n\n"

    response += "Copy any template and replace the [bracketed] sections with your details!"

    return {
      'message': response,
      'suggestions': ['Show me more', 'Different category', 'Analyze my prompt']
    }

  return {
    'message': f"I don't have templates specifically for '{category}', but I might have something similar. What are you trying to accomplish?",
    'suggestions': ['Writing help', 'Coding help', 'Learning something new']
  }


def analyze_prompt(message):
  """Analyze a prompt and give friendly feedback"""
  # Strip analysis trigger words to get the actual prompt
  prompt = message
  triggers = ['analyze', 'review', 'check', 'feedback on', 'improve', 'rate', 'help with']
  for trigger in triggers:
    prompt = re.sub(rf'^{trigger}\s*(this|my)?\s*(prompt)?:?\s*', '', prompt, flags=re.IGNORECASE)

  prompt = prompt.strip()
  if not prompt:
    return {
      'message': "I'd love to analyze your prompt! Just paste it here and I'll give you specific feedback on how to make it more effective.",
      'suggestions': ['Show me example prompts', 'What makes a good prompt?', 'Give me a template']
    }

  feedback = []
  tips = []
  strengths = []

  # Length analysis
  word_count = len(prompt.split())
  if word_count < 10:
    feedback.append("Your prompt is quite short. Adding more detail usually gets better results.")
    tips.append("Try adding context about your situation or what you'll use this for.")
  elif word_count > 20:
    strengths.append("Good length! You've included helpful detail.")

  # Specificity check
  vague_words = ['something', 'anything', 'stuff', 'things', 'whatever', 'good', 'nice']
  found_vague = [w for w in vague_words if w in prompt.lower()]
  if found_vague:
    feedback.append(f"I noticed some vague words ({', '.join(found_vague)}). Being more specific usually gets better results.")
    tips.append("Instead of 'something good', try describing exactly what you want.")

  # Context check
  context_indicators = ['i am', "i'm", 'my', 'we', 'our', 'for', 'because', 'as a']
  has_context = any(ind in prompt.lower() for ind in context_indicators)
  if has_context:
    strengths.append("Great job including context about yourself or your situation!")
  else:
    tips.append("Consider adding who you are or why you need this - it helps AI tailor the response.")

  # Format check
  format_words = ['list', 'bullet', 'paragraph', 'steps', 'table', 'brief', 'detailed', 'format', 'concise']
  has_format = any(word in prompt.lower() for word in format_words)
  if has_format:
    strengths.append("You specified a format - that's a pro move!")
  else:
    tips.append("Try specifying how you want the answer (bullet points, paragraph, steps, etc.)")

  # Role check
  role_words = ['act as', 'you are', 'pretend', 'imagine', 'as a', 'expert', 'professional']
  has_role = any(word in prompt.lower() for word in role_words)
  if has_role:
    strengths.append("Using role-setting (like 'act as an expert') can improve quality!")

  # Build response
  response = "Here's my analysis of your prompt:\n\n"

  if strengths:
    response += "**What's working well:**\n"
    for s in strengths:
      response += f"- {s}\n"
    response += "\n"

  if feedback:
    response += "**Areas to consider:**\n"
    for f in feedback:
      response += f"- {f}\n"
    response += "\n"

  if tips:
    response += "**Tips to try:**\n"
    for t in tips:
      response += f"- {t}\n"
    response += "\n"

  if not feedback and not tips:
    response += "This looks like a solid prompt! The main ways to improve would be:\n"
    response += "- Add an example of what you want if possible\n"
    response += "- Specify any constraints (length, tone, audience)\n\n"

  response += "Want me to help you rewrite this prompt with these improvements?"

  return {
    'message': response,
    'suggestions': ['Help me rewrite it', 'Show me a template', 'Explain prompt structure']
  }


# Routes
@app.route('/')
def index():
  return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
  data = request.get_json()
  message = data.get('message', '').strip()

  if not message:
    return jsonify({
      'message': SPARK_INTRO,
      'suggestions': ['Help me write better prompts', 'Explain AI terms to me', 'Find me an AI tool']
    })

  response = get_spark_response(message)
  return jsonify(response)


@app.route('/api/intro')
def intro():
  return jsonify({
    'message': SPARK_INTRO,
    'suggestions': ['Help me write better prompts', 'Explain AI terms to me', 'Find me an AI tool']
  })


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050, debug=True)
