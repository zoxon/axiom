#!/usr/bin/env node
import { cpSync, mkdirSync, rmSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import process from 'node:process'
import { fileURLToPath } from 'node:url'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const source = join(root, 'skills', 'design-tokens')
const home = process.env.HOME || process.env.USERPROFILE || ''
const args = process.argv.slice(2)

const usage = `Usage:
  axiom-skill install claude
  axiom-skill install codex
  axiom-skill install all
  axiom-skill install --dest ./.agents/skills

Installs the design-tokens skill from @zoxon/axiom.`

if (args.includes('-h') || args.includes('--help') || args[0] !== 'install') {
  process.stdout.write(`${usage}\n`)
  process.exit(args[0] === 'install' ? 1 : 0)
}

const destIndex = args.indexOf('--dest')
const explicitDest = destIndex === -1 ? null : args[destIndex + 1]
const target = args.find(arg => !['install', '--dest', explicitDest].includes(arg)) || 'all'

if (destIndex !== -1 && !explicitDest) {
  console.error('Missing path after --dest')
  process.exit(1)
}

const destinations = explicitDest
  ? [resolve(explicitDest, 'design-tokens')]
  : target === 'claude'
    ? [join(home, '.claude', 'skills', 'design-tokens')]
    : target === 'codex'
      ? [
          join(home, '.agents', 'skills', 'design-tokens'),
          join(home, '.codex', 'skills', 'design-tokens'),
        ]
      : target === 'all'
        ? [
            join(home, '.claude', 'skills', 'design-tokens'),
            join(home, '.agents', 'skills', 'design-tokens'),
            join(home, '.codex', 'skills', 'design-tokens'),
          ]
        : null

if (!destinations) {
  console.error(`Unknown target: ${target}`)
  console.error(usage)
  process.exit(1)
}

for (const destination of destinations) {
  mkdirSync(dirname(destination), { recursive: true })
  rmSync(destination, { recursive: true, force: true })
  cpSync(source, destination, {
    recursive: true,
    filter: path => !path.endsWith('.DS_Store'),
  })
  process.stdout.write(`Installed design-tokens skill to ${destination}\n`)
}
