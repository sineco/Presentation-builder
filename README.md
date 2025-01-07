# Presentation Builder

This repository contains a Python script that uses an LLM (Language Model) to generate **Markdown-based** slides for **Marp**, then converts the resulting `.md` file into a PowerPoint (`.pptx`) presentation.  

## Overview

- **generate_slide_markdown()**  
  Prompts an LLM to create Markdown slides.  
- **prepend_marp_front_matter()**  
  Ensures Marp front matter is prepended to the Markdown for proper slide rendering.  
- **save_markdown()**  
  Saves the combined Markdown (with front matter) to `slides.md`.  
- **convert_markdown_to_pptx()**  
  Invokes the Marp CLI to convert `slides.md` into a PowerPoint file (`slides.pptx`).

**End Result**: You get an automated pipeline where an LLM generates the bulk of your presentation content, and Marp provides a quick conversion to `.pptx`.

## Prerequisites

1. **Python** (3.8+ recommended)
2. **OpenAI Python Library**  
   - Ensure you have the correct client installed (the official `openai` library, if you’re using `import openai`, or `from openai import OpenAI` if you have a different/older client).
3. **Node.js & npm**  
   - Required for installing Marp CLI (see below).
4. **Marp CLI**  
   ```bash
   npm install -g @marp-team/marp-cli
