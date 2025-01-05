from openai import OpenAI
import subprocess
import os
from helper import get_openai_api_key



GPT_MODEL = 'gpt-4o-mini'
O1_MODEL = "gpt-4o-mini"#'01-mini'

def generate_slide_markdown():
    """Ask the LLM to produce slides in Markdown format using the Marp style."""
    prompt = (
        "Create a short Marp presentation about Convolutional Neural Networks. "
        "Use '---' to separate slides. Include a title slide, some bullet points, "
        "and at least one image reference. Provide the final answer in valid Markdown."
    )
    # 1. Configure your OpenAI API key
    openai_api_key = get_openai_api_key()
    client = OpenAI(api_key=openai_api_key)
    
    response = client.chat.completions.create(
        model=O1_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    # Extract the text (Markdown) from the response
    return response.choices[0].message.content

def prepend_marp_front_matter(md_content):
    """
    Prepend the necessary Marp front matter to the Markdown content.
    """
    front_matter = """---
marp: true
paginate: true
theme: default
---
"""
    # Combine front matter + the LLM’s Markdown (trim extra whitespace at the end).
    return front_matter + "\n" + md_content.strip()

def save_markdown(md_content, filename="slides.md"):
    """Write the LLM's Markdown content into a local file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content.strip())

def convert_markdown_to_pptx(input_md="slides.md", output_pptx="output/slides.pptx"):
    """
    Use Marp CLI to convert the Markdown file to a PPTX.
    Ensure you have marp-cli installed:
        npm install -g @marp-team/marp-cli
    """
    # Make sure output folder exists
    os.makedirs(os.path.dirname(output_pptx), exist_ok=True)
    
    command = [
        "marp",
        input_md,
        "--pptx",
        "-o",
        output_pptx
    ]
    subprocess.run(command, check=True)
    print(f"Presentation generated: {output_pptx}")

if __name__ == "__main__":
    print("Generating slides via LLM...")
    md_slides = generate_slide_markdown()

    # Insert the Marp front matter at the top:
    md_slides_with_front_matter = prepend_marp_front_matter(md_slides)
    
    print("\nSaving slides.md...")
    save_markdown(md_slides_with_front_matter, "slides.md")
    
    print("Converting slides.md to slides.pptx...")
    convert_markdown_to_pptx("slides.md", "output/slides.pptx")
    
    print("All done! Check the output folder for slides.pptx.")
