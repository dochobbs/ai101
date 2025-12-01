// Spark - AI Learning Assistant
// Frontend JavaScript

const messagesContainer = document.getElementById('chat-messages');
const suggestionsBar = document.getElementById('suggestions-bar');
const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');

// Initialize chat
document.addEventListener('DOMContentLoaded', () => {
  loadIntro();
  setupEventListeners();
});

function setupEventListeners() {
  // Auto-resize textarea
  messageInput.addEventListener('input', () => {
    messageInput.style.height = 'auto';
    messageInput.style.height = Math.min(messageInput.scrollHeight, 150) + 'px';
  });

  // Send on Enter (but not Shift+Enter)
  messageInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });
}

async function loadIntro() {
  try {
    const response = await fetch('/api/intro');
    const data = await response.json();
    addMessage(data.message, 'spark');
    updateSuggestions(data.suggestions);
  } catch (error) {
    console.error('Error loading intro:', error);
    addMessage("Hi! I'm Spark, your AI learning assistant. How can I help you today?", 'spark');
  }
}

async function sendMessage() {
  const message = messageInput.value.trim();
  if (!message) return;

  // Clear input
  messageInput.value = '';
  messageInput.style.height = 'auto';

  // Add user message
  addMessage(message, 'user');

  // Clear suggestions while loading
  suggestionsBar.innerHTML = '';

  // Show typing indicator
  showTypingIndicator();

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });

    const data = await response.json();

    // Remove typing indicator
    removeTypingIndicator();

    // Add Spark's response
    addMessage(data.message, 'spark');

    // Update suggestions
    if (data.suggestions) {
      updateSuggestions(data.suggestions);
    }
  } catch (error) {
    console.error('Error sending message:', error);
    removeTypingIndicator();
    addMessage("I'm having trouble connecting right now. Please try again!", 'spark');
  }
}

function addMessage(content, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${sender}`;

  const avatar = document.createElement('div');
  avatar.className = 'message-avatar';
  avatar.innerHTML = sender === 'spark' ? '&#10024;' : '&#128100;';

  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  contentDiv.innerHTML = formatMessage(content);

  messageDiv.appendChild(avatar);
  messageDiv.appendChild(contentDiv);

  messagesContainer.appendChild(messageDiv);
  scrollToBottom();
}

function formatMessage(text) {
  // Convert markdown-style formatting to HTML

  // Code blocks (```)
  text = text.replace(/```([\s\S]*?)```/g, '<pre>$1</pre>');

  // Inline code (`)
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');

  // Bold (**)
  text = text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

  // Italic (*)
  text = text.replace(/\*([^*]+)\*/g, '<em>$1</em>');

  // Convert newlines to breaks
  text = text.replace(/\n/g, '<br>');

  // Convert bullet points
  text = text.replace(/<br>- /g, '<br>• ');

  return text;
}

function showTypingIndicator() {
  const typingDiv = document.createElement('div');
  typingDiv.className = 'message spark';
  typingDiv.id = 'typing-indicator';

  const avatar = document.createElement('div');
  avatar.className = 'message-avatar';
  avatar.innerHTML = '&#10024;';

  const indicator = document.createElement('div');
  indicator.className = 'typing-indicator';
  indicator.innerHTML = '<span></span><span></span><span></span>';

  typingDiv.appendChild(avatar);
  typingDiv.appendChild(indicator);

  messagesContainer.appendChild(typingDiv);
  scrollToBottom();
}

function removeTypingIndicator() {
  const indicator = document.getElementById('typing-indicator');
  if (indicator) {
    indicator.remove();
  }
}

function updateSuggestions(suggestions) {
  suggestionsBar.innerHTML = '';

  if (!suggestions || suggestions.length === 0) return;

  suggestions.forEach(suggestion => {
    const chip = document.createElement('button');
    chip.className = 'suggestion-chip';
    chip.textContent = suggestion;
    chip.onclick = () => {
      messageInput.value = suggestion;
      sendMessage();
    };
    suggestionsBar.appendChild(chip);
  });
}

function scrollToBottom() {
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Helper function to handle clicking suggestion chips
function handleSuggestion(text) {
  messageInput.value = text;
  sendMessage();
}
