import os
from textnode import TextNode, TextType, markdown_to_html_node, extract_title
import shutil
import sys

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

def generate_page(content_entry_path, template_path, dest_path, basepath):
    print(f"Generating page from {content_entry_path} to {dest_path} using {template_path}")

    with open(content_entry_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        print(f"Successfully generated {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, des_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        content_entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(des_dir_path, entry)

        if os.path.isdir(content_entry_path):
            os.makedirs(dest_entry_path, exist_ok=True)
            generate_pages_recursive(content_entry_path, template_path, dest_entry_path, basepath)

        elif entry.endswith(".md"):
            dest_html_path = os.path.join(des_dir_path, "index.html")
            generate_page(content_entry_path, template_path, dest_html_path, basepath)


def main():
    static_dir = "static"
    public_dir = "docs"
    #public_dir = "public"
    #content_md = "content/index.md"
    template_html = "template.html"
    #output_html = "public/index.html"
    content_dir = "content"

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    print("Copying static files...")
    copy_static_files(static_dir, public_dir)

    print("Generating site pages...")
    #generate_page(content_md, template_html, output_html)
    generate_pages_recursive(content_dir, template_html, public_dir, basepath)
        
# previous iterations of main.py for testing. 
    #print ("starting static file copy...")
    #copy_static_files(static_dir, public_dir)
    #print("Static file copy complete")

    #node = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev")
    #print(node)

if __name__ == "__main__":
    main()
