#!/usr/bin/env python3
"""Build project role files into a new directory from convert.sh output."""
import argparse
import json
from pathlib import Path
import tomllib

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('converted_agents', type=Path, help='codex/agents directory produced by convert.sh --out')
parser.add_argument('output', type=Path, help='new directory to receive config.toml and agents/')
args = parser.parse_args()
files = sorted(args.converted_agents.glob('*.toml'))
if not files:
    parser.error('no converted TOML files found')
if args.output.exists():
    parser.error('output already exists; choose a new directory to avoid overwriting files')
args.output.mkdir(parents=True)
(args.output / 'agents').mkdir()
config = ['# Project-level custom agent roles. Paths are relative to this file.\n']
for path in files:
    agent = tomllib.loads(path.read_text(encoding='utf-8'))
    dump = lambda value: json.dumps(value, ensure_ascii=False)
    (args.output / 'agents' / path.name).write_text(
        'developer_instructions = ' + dump(agent['developer_instructions']) + '\n', encoding='utf-8')
    config.extend(['[agents.' + dump(path.stem) + ']\n',
                   'description = ' + dump(agent['description']) + '\n',
                   'config_file = ' + dump('agents/' + path.name) + '\n\n'])
(args.output / 'config.toml').write_text(''.join(config).rstrip() + '\n', encoding='utf-8')
print(f'Prepared {len(files)} roles in {args.output}')
