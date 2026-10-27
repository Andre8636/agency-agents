#!/usr/bin/env python3
"""Build the /Agent discovery index from the checked-in Codex role config (Python 3.11+)."""
import argparse
import json
import pathlib
import re
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = ROOT / '.codex/config.toml'
OUTPUT = ROOT / '.codex/agent-index.json'


def build():
    config = tomllib.loads(CONFIG.read_text(encoding='utf-8'))
    entries = []
    seen = set()
    for agent_id, config_entry in sorted(config['agents'].items()):
        relative = pathlib.PurePosixPath(config_entry['config_file'])
        if relative.is_absolute() or '..' in relative.parts or relative.parts[0] != 'agents':
            raise ValueError(f'Invalid agent path for {agent_id}: {relative}')
        path = ROOT / '.codex' / relative
        if path in seen:
            raise ValueError(f'Duplicate agent path: {relative}')
        seen.add(path)
        data = tomllib.loads(path.read_text(encoding='utf-8'))
        instructions = data['developer_instructions']
        if not isinstance(instructions, str) or not instructions.strip():
            raise ValueError(f'Empty instructions: {relative}')
        title = re.search(r'^#\s+(.+?)\s*$', instructions, re.MULTILINE)
        role = re.search(r'^-\s+\*\*Role\*\*:\s*(.+)$', instructions, re.MULTILINE | re.IGNORECASE)
        name = re.sub(r'\s+Agent Personality\s*$', '', title.group(1)).strip() if title else agent_id.replace('-', ' ').title()
        description = data.get('description', config_entry['description'])
        entries.append({'id': agent_id, 'name': data.get('name', name), 'description': description,
                        'domain': role.group(1).strip() if role else description,
                        'path': (path.relative_to(ROOT)).as_posix()})
    actual = set((ROOT / '.codex/agents').glob('*.toml'))
    if seen != actual:
        raise ValueError(f'Config/TOML mismatch: unregistered={sorted(str(p.relative_to(ROOT)) for p in actual - seen)}, missing={sorted(str(p.relative_to(ROOT)) for p in seen - actual)}')
    return json.dumps({'version': 1, 'agents': entries}, ensure_ascii=False, indent=2) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='fail if the committed index is stale')
    args = parser.parse_args()
    result = build()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding='utf-8') != result:
            print(f'{OUTPUT.relative_to(ROOT)} is stale; run {pathlib.Path(__file__).relative_to(ROOT)}', file=sys.stderr)
            return 1
        print(f'Index is current: {len(json.loads(result)["agents"])} agents')
    else:
        OUTPUT.write_text(result, encoding='utf-8')
        print(f'Wrote {OUTPUT.relative_to(ROOT)}: {len(json.loads(result)["agents"])} agents')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
