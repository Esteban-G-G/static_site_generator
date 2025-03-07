import os
from textnode import TextNode, TextType, markdown_to_html_node, extract_title
import shutil

def copy_static_files(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)  

    os.makedirs(dest, exist_ok=True)  

    for item in os.listdir(src):
        if item.startswith("."):  
            continue

        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path):  
            os.makedirs(dest_path, exist_ok=True)
            copy_static_files(src_path, dest_path)  
        elif os.path.isfile(src_path):  
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        print(f"Successfully generated {dest_path}")

def main():
    static_dir = "static"
    public_dir = "public"
    content_md = "content/index.md"
    template_html = "template.html"
    output_html = "public/index.html"

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    print("Copying static files...")
    copy_static_files(static_dir, public_dir)

    print("Generating homepage...")
    generate_page(content_md, template_html, output_html)
        
# previous iterations of main.py for testing. 
    #print ("starting static file copy...")
    #copy_static_files(static_dir, public_dir)
    #print("Static file copy complete")

    #node = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev")
    #print(node)

if __name__ == "__main__":
    main()
