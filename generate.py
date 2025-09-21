from __future__ import annotations
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from jinja_markdown2 import MarkdownExtension


env = Environment(loader=FileSystemLoader('templates'))
env.add_extension(MarkdownExtension)
public_dir = Path('public')
public_dir.mkdir(exist_ok=True)

template = env.get_template('index.html.j2')
data = yaml.safe_load(Path('data.yaml').read_text())
content = template.render(**data)
Path('public', 'index.html').write_text(content)

template = env.get_template('markdown.html.j2')

data = Path("privacy-policy.md").read_text()
content = template.render(dict(content=data))
Path('public', 'privacy-policy.html').write_text(content)

data = Path("terms-and-conditions.md").read_text()
content = template.render(dict(content=data))
Path('public', 'terms-and-conditions.html').write_text(content)
