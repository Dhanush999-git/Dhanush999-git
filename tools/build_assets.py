#!/usr/bin/env python3
"""
tools/build_assets.py

Cyber Obsidian × Electric Prismatic Asset Builder for Dhanush M D's GitHub Profile.
Generates all SVGs for hero, sections, badges, and project cards with valid XML,
SMIL animations, high-contrast typography, and GitHub camo compatibility.
"""

import os
import xml.etree.ElementTree as ET

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def validate_svg(svg_content, filepath):
    try:
        ET.fromstring(svg_content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"[OK] Valid XML written to {filepath}")
        return True
    except ET.ParseError as e:
        print(f"[ERROR] XML Parse Error in {filepath}: {e}")
        return False

# ==============================================================================
# 1. HERO BANNER
# ==============================================================================
def generate_hero_banner():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 420" width="1000" height="420" role="img" aria-label="Dhanush M D - Full Stack Developer and AI/ML Engineer">
  <title>Dhanush M D — Full Stack Developer · AI/ML Engineer · Creative Technologist</title>
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="hero-bg" cx="50%" cy="30%" r="90%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="60%" stop-color="#080C14"/>
      <stop offset="100%" stop-color="#04060A"/>
    </radialGradient>

    <!-- Prismatic Core Gradients -->
    <linearGradient id="cyan-glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="50%" stop-color="#4FACFE"/>
      <stop offset="100%" stop-color="#7928CA"/>
    </linearGradient>

    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="40%" stop-color="#E2E8F0"/>
      <stop offset="70%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#00F2FE"/>
    </linearGradient>

    <linearGradient id="holo-violet" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7928CA"/>
      <stop offset="100%" stop-color="#B800FF"/>
    </linearGradient>

    <linearGradient id="emerald-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>

    <linearGradient id="sheen" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0"/>
      <stop offset="45%" stop-color="#00F2FE" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="1"/>
      <stop offset="55%" stop-color="#7928CA" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#7928CA" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-800 0; 800 0; 800 0" dur="5s" repeatCount="indefinite"/>
    </linearGradient>

    <!-- Filters -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="soft-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="10" result="blur"/>
    </filter>

    <!-- Clip Paths -->
    <clipPath id="hero-card"><rect width="1000" height="420" rx="16"/></clipPath>
    <clipPath id="avatar-clip"><circle cx="810" cy="180" r="100"/></clipPath>
  </defs>

  <g clip-path="url(#hero-card)">
    <!-- Base Canvas -->
    <rect width="1000" height="420" fill="url(#hero-bg)"/>

    <!-- Subtle Cyber Grid Background -->
    <g opacity="0.12" stroke="#1E293B" stroke-width="1">
      <line x1="0" y1="60" x2="1000" y2="60"/>
      <line x1="0" y1="120" x2="1000" y2="120"/>
      <line x1="0" y1="180" x2="1000" y2="180"/>
      <line x1="0" y1="240" x2="1000" y2="240"/>
      <line x1="0" y1="300" x2="1000" y2="300"/>
      <line x1="0" y1="360" x2="1000" y2="360"/>
      <line x1="120" y1="0" x2="120" y2="420"/>
      <line x1="240" y1="0" x2="240" y2="420"/>
      <line x1="360" y1="0" x2="360" y2="420"/>
      <line x1="480" y1="0" x2="480" y2="420"/>
      <line x1="600" y1="0" x2="600" y2="420"/>
      <line x1="720" y1="0" x2="720" y2="420"/>
      <line x1="840" y1="0" x2="840" y2="420"/>
      <line x1="960" y1="0" x2="960" y2="420"/>
    </g>

    <!-- Ambient Glow Orbs -->
    <circle cx="810" cy="180" r="140" fill="#7928CA" opacity="0.22" filter="url(#soft-glow)"/>
    <circle cx="200" cy="80" r="110" fill="#00F2FE" opacity="0.12" filter="url(#soft-glow)"/>
    <circle cx="500" cy="350" r="120" fill="#10B981" opacity="0.08" filter="url(#soft-glow)"/>

    <!-- Tech Circuit Traces Left -->
    <path d="M-20,100 L80,100 L120,140 L280,140" stroke="#00F2FE" stroke-width="1.2" fill="none" opacity="0.25"/>
    <circle cx="280" cy="140" r="3" fill="#00F2FE" opacity="0.6"/>
    <path d="M-20,320 L140,320 L180,280 L340,280" stroke="#7928CA" stroke-width="1.2" fill="none" opacity="0.3"/>
    <circle cx="340" cy="280" r="3" fill="#7928CA" opacity="0.6"/>

    <!-- Terminal Command Pill -->
    <g transform="translate(48, 38)">
      <rect x="0" y="0" width="310" height="32" rx="16" fill="#0B1322" stroke="#1E293B" stroke-width="1.2"/>
      <circle cx="18" cy="16" r="4.5" fill="#10B981" filter="url(#glow)">
        <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="32" y="21" font-family="'SF Mono', 'JetBrains Mono', 'Fira Code', monospace" font-size="12" fill="#E2E8F0">~/dhanush $ build --intelligent</text>
    </g>

    <!-- Eyebrow Tag -->
    <g transform="translate(48, 102)">
      <line x1="0" y1="-5" x2="32" y2="-5" stroke="#00F2FE" stroke-width="2"/>
      <text x="42" y="0" font-family="'SF Mono', 'JetBrains Mono', 'Fira Code', monospace" font-size="12" letter-spacing="2.5" fill="#00F2FE" font-weight="600">ENGINEERING INTELLIGENT SYSTEMS</text>
    </g>

    <!-- Main Name Heading -->
    <text x="46" y="180" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-weight="900" font-size="68" letter-spacing="-1.5" fill="url(#name-grad)">DHANUSH M D</text>

    <!-- Traveling Gradient Underline Bar -->
    <rect x="48" y="200" width="480" height="3" rx="1.5" fill="#1E293B"/>
    <rect x="48" y="200" width="480" height="3" rx="1.5" fill="url(#sheen)"/>

    <!-- Subtitle and Roles -->
    <text x="48" y="238" font-family="'SF Mono', 'JetBrains Mono', 'Fira Code', monospace" font-size="13.5" letter-spacing="1.2" fill="#E2E8F0" font-weight="600">FULL STACK DEVELOPER · AI/ML ENGINEER · CREATIVE TECHNOLOGIST</text>

    <!-- Tagline Philosophy -->
    <text x="48" y="274" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-style="italic" font-size="16" fill="#94A3B8">"Building intelligent systems, engineering meaningful digital experiences, and transforming ideas into reality."</text>

    <!-- Key Metrics / Capability Badges Row -->
    <g transform="translate(48, 308)">
      <!-- Badge 1: VeriFact -->
      <g transform="translate(0, 0)">
        <rect width="132" height="28" rx="6" fill="#091824" stroke="#00F2FE" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="12" cy="14" r="3.5" fill="#00F2FE"/>
        <text x="24" y="18" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" fill="#E2E8F0" font-weight="600">VERIFACT CORE</text>
      </g>
      <!-- Badge 2: Neural ML -->
      <g transform="translate(144, 0)">
        <rect width="138" height="28" rx="6" fill="#160E29" stroke="#7928CA" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="12" cy="14" r="3.5" fill="#A855F7"/>
        <text x="24" y="18" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" fill="#E2E8F0" font-weight="600">AI / MULTI-MODAL</text>
      </g>
      <!-- Badge 3: Full Stack -->
      <g transform="translate(294, 0)">
        <rect width="118" height="28" rx="6" fill="#0C1D18" stroke="#10B981" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="12" cy="14" r="3.5" fill="#10B981"/>
        <text x="24" y="18" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" fill="#E2E8F0" font-weight="600">FULL STACK</text>
      </g>
      <!-- Badge 4: Creative AE -->
      <g transform="translate(424, 0)">
        <rect width="116" height="28" rx="6" fill="#1B1224" stroke="#B800FF" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="12" cy="14" r="3.5" fill="#F43F5E"/>
        <text x="24" y="18" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" fill="#E2E8F0" font-weight="600">DHANUSH AE</text>
      </g>
    </g>

    <!-- RIGHT SECTION: Futuristic Holographic Neural Core / Abstract Avatar -->
    <g transform="translate(810, 180)">
      <!-- Outer Rotating Orbital Ring 1 -->
      <circle cx="0" cy="0" r="140" fill="none" stroke="#00F2FE" stroke-width="1" stroke-opacity="0.4" stroke-dasharray="12 16">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="25s" repeatCount="indefinite"/>
      </circle>

      <!-- Middle Counter-Rotating Orbital Ring 2 -->
      <circle cx="0" cy="0" r="118" fill="none" stroke="#7928CA" stroke-width="1.5" stroke-opacity="0.6" stroke-dasharray="8 10">
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="20s" repeatCount="indefinite"/>
      </circle>

      <!-- Inner Pulsing Ring 3 -->
      <circle cx="0" cy="0" r="96" fill="none" stroke="#00F2FE" stroke-width="1.2" stroke-opacity="0.75" stroke-dasharray="4 6">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="14s" repeatCount="indefinite"/>
      </circle>

      <!-- Prismatic Hexagon Shield -->
      <polygon points="0,-72 62,-36 62,36 0,72 -62,36 -62,-36" fill="#0C1527" stroke="url(#cyan-glow)" stroke-width="2" filter="url(#glow)"/>

      <!-- Inner Holographic Prism Nodes -->
      <polygon points="0,-48 42,-24 42,24 0,48 -42,24 -42,-24" fill="#0E1A33" stroke="#7928CA" stroke-width="1.5" opacity="0.8"/>
      
      <!-- Central Neural Core -->
      <circle cx="0" cy="0" r="22" fill="url(#cyan-glow)" filter="url(#glow)">
        <animate attributeName="r" values="20;25;20" dur="3.5s" repeatCount="indefinite"/>
      </circle>
      <circle cx="0" cy="0" r="9" fill="#FFFFFF"/>

      <!-- Connecting Neural Nodes & Lines -->
      <line x1="0" y1="0" x2="0" y2="-72" stroke="#00F2FE" stroke-width="1" opacity="0.6"/>
      <line x1="0" y1="0" x2="62" y2="-36" stroke="#00F2FE" stroke-width="1" opacity="0.6"/>
      <line x1="0" y1="0" x2="62" y2="36" stroke="#00F2FE" stroke-width="1" opacity="0.6"/>
      <line x1="0" y1="0" x2="0" y2="72" stroke="#00F2FE" stroke-width="1" opacity="0.6"/>
      <line x1="0" y1="0" x2="-62" y2="36" stroke="#00F2FE" stroke-width="1" opacity="0.6"/>
      <line x1="0" y1="0" x2="-62" y2="-36" stroke="#00F2FE" stroke-width="1" opacity="0.6"/>

      <!-- Floating Orbital Labels -->
      <!-- Label 1: FULL STACK (Top) -->
      <g transform="translate(0, -156)">
        <rect x="-44" y="-12" width="88" height="24" rx="12" fill="#091424" stroke="#00F2FE" stroke-width="1.2"/>
        <text x="0" y="4" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#00F2FE" font-weight="700">FULL STACK</text>
      </g>

      <!-- Label 2: AI / ML (Right) -->
      <g transform="translate(156, 0)">
        <rect x="-34" y="-12" width="68" height="24" rx="12" fill="#160B26" stroke="#7928CA" stroke-width="1.2"/>
        <text x="0" y="4" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#C084FC" font-weight="700">AI / ML</text>
      </g>

      <!-- Label 3: CREATIVE (Bottom) -->
      <g transform="translate(0, 156)">
        <rect x="-40" y="-12" width="80" height="24" rx="12" fill="#1C1026" stroke="#B800FF" stroke-width="1.2"/>
        <text x="0" y="4" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#E879F9" font-weight="700">CREATIVE</text>
      </g>

      <!-- Label 4: VERIFACT (Left) -->
      <g transform="translate(-156, 0)">
        <rect x="-42" y="-12" width="84" height="24" rx="12" fill="#0B1A1E" stroke="#10B981" stroke-width="1.2"/>
        <text x="0" y="4" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#34D399" font-weight="700">VERIFACT</text>
      </g>
    </g>

    <!-- Bottom Status Rule & Bar -->
    <rect x="0" y="378" width="1000" height="42" fill="#060910" stroke="#1E293B" stroke-width="1"/>
    
    <g transform="translate(48, 404)">
      <circle cx="0" cy="-4" r="4" fill="#10B981" filter="url(#glow)">
        <animate attributeName="opacity" values="1;0.3;1" dur="1.8s" repeatCount="indefinite"/>
      </circle>
      <text x="14" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11.5" letter-spacing="1" fill="#E2E8F0" font-weight="600">SYSTEM: ONLINE</text>
      <text x="150" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11.5" letter-spacing="1" fill="#64748B">|</text>
      <text x="170" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11.5" letter-spacing="1" fill="#94A3B8">ENGINEERING INTELLIGENT SYSTEMS</text>
      <text x="440" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11.5" letter-spacing="1" fill="#64748B">|</text>
      <text x="460" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11.5" letter-spacing="1" fill="#00F2FE">NODE: INDIA</text>
    </g>

    <g transform="translate(952, 404)">
      <text x="0" y="0" text-anchor="end" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" letter-spacing="1.5" fill="#64748B">PORTFOLIO ARCHITECTURE v2.0</text>
    </g>

    <!-- Outer Card Border -->
    <rect x="0.5" y="0.5" width="999" height="419" rx="16" fill="none" stroke="#1E293B" stroke-width="1"/>
    <rect x="0.5" y="0.5" width="999" height="419" rx="16" fill="none" stroke="#00F2FE" stroke-width="1.5" stroke-opacity="0.3"/>
  </g>
</svg>'''
    return svg

# ==============================================================================
# 2. SOCIAL BADGES
# ==============================================================================
def generate_badge(name, icon_svg, label, value, stroke_color, text_color):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 210 44" width="210" height="44" role="img" aria-label="{label}: {value}">
  <title>{label}: {value}</title>
  <defs>
    <linearGradient id="badge-bg-{name}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E1726"/>
      <stop offset="100%" stop-color="#080D17"/>
    </linearGradient>
    <filter id="glow-{name}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="210" height="44" rx="8" fill="url(#badge-bg-{name})" stroke="{stroke_color}" stroke-width="1.2" stroke-opacity="0.7"/>
  <g transform="translate(14, 12)">
    {icon_svg}
  </g>
  <text x="44" y="19" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="9" letter-spacing="1.2" fill="#94A3B8" font-weight="600">{label.upper()}</text>
  <text x="44" y="32" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" letter-spacing="0.5" fill="{text_color}" font-weight="700">{value}</text>
</svg>'''
    return svg

def build_all_badges():
    # GitHub Octocat
    gh_icon = '<path fill="#00F2FE" d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 4.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.942.359.31.678.921.678 1.856 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0020 10.017C20 4.484 15.522 0 10 0z"/>'
    validate_svg(generate_badge("github", gh_icon, "GitHub", "Dhanush999-git", "#00F2FE", "#FFFFFF"), "assets/badges/github.svg")

    # LinkedIn
    in_icon = '<path fill="#38BDF8" d="M19 0h-18c-.55 0-1 .45-1 1v18c0 .55.45 1 1 1h18c.55 0 1-.45 1-1v-18c0-.55-.45-1-1-1zm-11 17h-3v-9h3v9zm-1.5-10.27c-.97 0-1.75-.79-1.75-1.76s.78-1.75 1.75-1.75 1.75.78 1.75 1.75-.78 1.76-1.75 1.76zm11.5 10.27h-3v-4.6c0-1.1-.02-2.52-1.54-2.52-1.54 0-1.77 1.2-1.77 2.44v4.68h-3v-9h2.88v1.23h.04c.4-.76 1.38-1.56 2.84-1.56 3.04 0 3.6 2 3.6 4.61v4.72z"/>'
    validate_svg(generate_badge("linkedin", in_icon, "LinkedIn", "Dhanush M D", "#38BDF8", "#FFFFFF"), "assets/badges/linkedin.svg")

    # Portfolio
    port_icon = '<path fill="#7928CA" d="M10 0C4.48 0 0 4.48 0 10s4.48 10 10 10 10-4.48 10-10S15.52 0 10 0zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v2.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V4h2c1.1 0 2-.9 2-2v-.41C16.92 3.2 19 6.35 19 10c0 2.27-.92 4.33-2.1 5.39z"/>'
    validate_svg(generate_badge("portfolio", port_icon, "Showcase", "Dhanush Portfolio", "#A855F7", "#FFFFFF"), "assets/badges/portfolio.svg")

    # Email
    mail_icon = '<path fill="#10B981" d="M18 0H2C.9 0 0 .9 0 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V2c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V2l8 5 8-5v2z"/>'
    validate_svg(generate_badge("email", mail_icon, "Direct Dispatch", "mddhanush6@gmail.com", "#10B981", "#34D399"), "assets/badges/email.svg")

# ==============================================================================
# 3. SECTION 01: ABOUT ME (TERMINAL INTERFACE)
# ==============================================================================
def generate_about_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 520" width="1000" height="520" role="img" aria-label="About Dhanush M D - Terminal Interface">
  <title>01 / ABOUT ME — Developer Terminal</title>
  <defs>
    <linearGradient id="abt-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B111E"/>
      <stop offset="100%" stop-color="#060A12"/>
    </linearGradient>

    <linearGradient id="abt-term-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080D18"/>
      <stop offset="100%" stop-color="#04070D"/>
    </linearGradient>

    <linearGradient id="abt-side-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D1629"/>
      <stop offset="100%" stop-color="#080E1A"/>
    </linearGradient>

    <filter id="abt-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="abt-card"><rect width="1000" height="520" rx="16"/></clipPath>
    <clipPath id="term-clip"><rect width="630" height="395" rx="8"/></clipPath>
  </defs>

  <g clip-path="url(#abt-card)">
    <!-- Base Canvas -->
    <rect width="1000" height="520" fill="url(#abt-bg)"/>

    <!-- Section Header Bar -->
    <g transform="translate(40, 42)">
      <text x="0" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="12" letter-spacing="3" fill="#00F2FE" font-weight="700">01 / ABOUT ME</text>
      <text x="920" y="0" text-anchor="end" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" letter-spacing="2" fill="#64748B">PROFILE IDENTITY // WHOAMI</text>
      <line x1="0" y1="14" x2="920" y2="14" stroke="#1E293B" stroke-width="1"/>
    </g>

    <!-- LEFT: Main Terminal Window (630x400) -->
    <g transform="translate(40, 80)">
      <!-- Terminal Frame -->
      <rect width="630" height="400" rx="10" fill="url(#abt-term-bg)" stroke="#1E293B" stroke-width="1.2"/>
      
      <!-- Terminal Top Bar -->
      <rect width="630" height="34" rx="10" fill="#0E1729"/>
      <rect y="24" width="630" height="10" fill="#0E1729"/>
      <line x1="0" y1="34" x2="630" y2="34" stroke="#1E293B" stroke-width="1"/>
      
      <!-- Window Controls -->
      <circle cx="20" cy="17" r="5" fill="#EF4444"/>
      <circle cx="36" cy="17" r="5" fill="#F59E0B"/>
      <circle cx="52" cy="17" r="5" fill="#10B981"/>
      
      <!-- Terminal Window Title -->
      <text x="315" y="22" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#94A3B8">dhanush@developer: ~ (zsh)</text>

      <!-- Terminal Body Content -->
      <!-- Command 1: whoami -->
      <text x="24" y="66" font-family="'SF Mono', monospace" font-size="12.5" fill="#00F2FE" font-weight="600">dhanush@developer:~$ <tspan fill="#FFFFFF">whoami</tspan></text>
      <text x="24" y="90" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" fill="#FFFFFF" font-weight="700">Dhanush M D</text>
      <text x="24" y="112" font-family="'SF Mono', monospace" font-size="11.5" fill="#38BDF8">Full Stack Developer | AI/ML Engineer | Creative Technologist</text>

      <!-- Command 2: cat interests.txt -->
      <text x="24" y="148" font-family="'SF Mono', monospace" font-size="12.5" fill="#00F2FE" font-weight="600">dhanush@developer:~$ <tspan fill="#FFFFFF">cat interests.txt</tspan></text>
      <g transform="translate(24, 168)" font-family="'SF Mono', monospace" font-size="11" fill="#E2E8F0">
        <text x="0" y="0"><tspan fill="#10B981">&#x25B8;</tspan> Full Stack Development &amp; Web Applications</text>
        <text x="0" y="18"><tspan fill="#10B981">&#x25B8;</tspan> Artificial Intelligence &amp; Machine Learning</text>
        <text x="0" y="36"><tspan fill="#10B981">&#x25B8;</tspan> Multi-Modal Verification &amp; Computer Vision</text>
        <text x="0" y="54"><tspan fill="#10B981">&#x25B8;</tspan> Python Architecture &amp; Scalable REST APIs</text>
        <text x="0" y="72"><tspan fill="#10B981">&#x25B8;</tspan> Video Editing, Motion Graphics &amp; Creative Tech</text>
      </g>

      <!-- Command 3: cat philosophy.txt -->
      <text x="24" y="278" font-family="'SF Mono', monospace" font-size="12.5" fill="#00F2FE" font-weight="600">dhanush@developer:~$ <tspan fill="#FFFFFF">cat philosophy.txt</tspan></text>
      <text x="24" y="302" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-style="italic" font-size="13" fill="#94A3B8">"Building intelligent systems, engineering meaningful digital experiences, and</text>
      <text x="24" y="322" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-style="italic" font-size="13" fill="#94A3B8">transforming ideas into reality."</text>

      <!-- Command 4: echo $STATUS -->
      <text x="24" y="356" font-family="'SF Mono', monospace" font-size="12.5" fill="#00F2FE" font-weight="600">dhanush@developer:~$ <tspan fill="#FFFFFF">echo $STATUS</tspan></text>
      <rect x="24" y="368" width="310" height="22" rx="4" fill="#0E231F" stroke="#10B981" stroke-width="0.8"/>
      <circle cx="34" cy="379" r="3.5" fill="#10B981" filter="url(#abt-glow)">
        <animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite"/>
      </circle>
      <text x="44" y="383" font-family="'SF Mono', monospace" font-size="11" fill="#34D399" font-weight="700">CONTINUOUSLY LEARNING AND BUILDING.</text>
    </g>

    <!-- RIGHT: Telemetry & Core Disciplines Card (270x400) -->
    <g transform="translate(690, 80)">
      <rect width="270" height="400" rx="10" fill="url(#abt-side-bg)" stroke="#1E293B" stroke-width="1.2"/>
      
      <!-- Card Header -->
      <g transform="translate(20, 26)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="10.5" letter-spacing="1.5" fill="#7928CA" font-weight="700">SYSTEM TELEMETRY</text>
        <circle cx="225" cy="-4" r="4" fill="#10B981"/>
      </g>
      <line x1="20" y1="38" x2="250" y2="38" stroke="#1E293B" stroke-width="1"/>

      <!-- Telemetry Items -->
      <g transform="translate(20, 64)" font-family="'SF Mono', monospace">
        <!-- Item 1 -->
        <text x="0" y="0" font-size="9.5" fill="#64748B" letter-spacing="1">LOCATION</text>
        <text x="0" y="18" font-size="12" fill="#E2E8F0" font-weight="600">India · Remote</text>

        <!-- Item 2 -->
        <text x="0" y="48" font-size="9.5" fill="#64748B" letter-spacing="1">CORE FOCUS</text>
        <text x="0" y="66" font-size="12" fill="#00F2FE" font-weight="600">AI / ML + Full Stack</text>

        <!-- Item 3 -->
        <text x="0" y="96" font-size="9.5" fill="#64748B" letter-spacing="1">FLAGSHIP SYSTEM</text>
        <text x="0" y="114" font-size="12" fill="#34D399" font-weight="600">VeriFact Verification</text>

        <!-- Item 4 -->
        <text x="0" y="144" font-size="9.5" fill="#64748B" letter-spacing="1">CREATIVE VENTURE</text>
        <text x="0" y="162" font-size="12" fill="#C084FC" font-weight="600">Dhanush AE Store</text>

        <!-- Item 5 -->
        <text x="0" y="192" font-size="9.5" fill="#64748B" letter-spacing="1">PRIMARY RUNTIMES</text>
        <text x="0" y="210" font-size="12" fill="#E2E8F0" font-weight="600">Python 3 · Node · Vite</text>
      </g>

      <!-- Bottom Status Pill in Card -->
      <g transform="translate(20, 320)">
        <rect width="230" height="52" rx="6" fill="#070D18" stroke="#1E293B" stroke-width="1"/>
        <text x="14" y="20" font-family="'SF Mono', monospace" font-size="9.5" fill="#94A3B8">COLLABORATION STATUS</text>
        <circle cx="20" cy="36" r="3.5" fill="#10B981" filter="url(#abt-glow)"/>
        <text x="30" y="40" font-family="'SF Mono', monospace" font-size="11" fill="#34D399" font-weight="700">Open to Projects</text>
      </g>
    </g>

    <!-- Outer Card Border -->
    <rect x="0.5" y="0.5" width="999" height="519" rx="16" fill="none" stroke="#1E293B" stroke-width="1"/>
  </g>
</svg>'''
    return svg

# ==============================================================================
# 4. SECTION 02: PROFESSIONAL NARRATIVE & THREE PILLARS
# ==============================================================================
def generate_narrative_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 460" width="1000" height="460" role="img" aria-label="Engineering Philosophy - Three Core Pillars">
  <title>02 / ENGINEERING PHILOSOPHY — Three Core Disciplines</title>
  <defs>
    <linearGradient id="nar-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090E1A"/>
      <stop offset="100%" stop-color="#05080E"/>
    </linearGradient>

    <!-- Pillar 1: AI (Cyan/Blue) -->
    <linearGradient id="p1-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E1E33"/>
      <stop offset="100%" stop-color="#08101E"/>
    </linearGradient>

    <!-- Pillar 2: Full Stack (Violet) -->
    <linearGradient id="p2-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#190F2E"/>
      <stop offset="100%" stop-color="#0D0719"/>
    </linearGradient>

    <!-- Pillar 3: Creative (Emerald) -->
    <linearGradient id="p3-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E241E"/>
      <stop offset="100%" stop-color="#07130F"/>
    </linearGradient>

    <filter id="nar-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="nar-card"><rect width="1000" height="460" rx="16"/></clipPath>
  </defs>

  <g clip-path="url(#nar-card)">
    <!-- Base Canvas -->
    <rect width="1000" height="460" fill="url(#nar-bg)"/>

    <!-- Section Header -->
    <g transform="translate(40, 42)">
      <text x="0" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="12" letter-spacing="3" fill="#00F2FE" font-weight="700">02 / ENGINEERING PHILOSOPHY</text>
      <text x="920" y="0" text-anchor="end" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" letter-spacing="2" fill="#64748B">THREE CORE PILLARS</text>
      <line x1="0" y1="14" x2="920" y2="14" stroke="#1E293B" stroke-width="1"/>
    </g>

    <!-- Introductory Editorial Quote -->
    <g transform="translate(40, 88)">
      <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="700" fill="#E2E8F0">Bridging Algorithmic Intelligence, Robust Architecture &amp; Creative Motion</text>
      <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" fill="#94A3B8">Engineering systems that do not merely execute logic, but deliver meaningful, authentic, and visual impact.</text>
    </g>

    <!-- THREE PILLAR CARDS -->
    <!-- PILLAR 1: INTELLIGENT SYSTEMS (Cyan Accent) -->
    <g transform="translate(40, 140)">
      <rect width="288" height="280" rx="12" fill="url(#p1-grad)" stroke="#00F2FE" stroke-width="1.2" stroke-opacity="0.4"/>
      
      <!-- Number & Icon Header -->
      <g transform="translate(20, 24)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="11" letter-spacing="1.5" fill="#00F2FE" font-weight="700">PILLAR 01</text>
        <circle cx="236" cy="-4" r="8" fill="#0B1C2E" stroke="#00F2FE" stroke-width="1.2"/>
        <circle cx="236" cy="-4" r="3" fill="#00F2FE"/>
      </g>
      
      <text x="20" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="700" fill="#FFFFFF">Intelligent Systems</text>
      <text x="20" y="88" font-family="'SF Mono', monospace" font-size="10.5" fill="#38BDF8">AI · ML · DEEP LEARNING</text>
      <line x1="20" y1="102" x2="268" y2="102" stroke="#1E293B" stroke-width="1"/>

      <g transform="translate(20, 126)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#94A3B8">
        <text x="0" y="0">Architecting AI-powered platforms,</text>
        <text x="0" y="20">neural classification microservices,</text>
        <text x="0" y="40">multi-modal fact verification, and</text>
        <text x="0" y="60">computer vision pipelines.</text>
      </g>

      <!-- Tech tags bottom -->
      <g transform="translate(20, 226)">
        <rect x="0" y="0" width="68" height="22" rx="4" fill="#091829" stroke="#1E3A5F" stroke-width="0.8"/>
        <text x="34" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#00F2FE">PyTorch</text>
        <rect x="74" y="0" width="86" height="22" rx="4" fill="#091829" stroke="#1E3A5F" stroke-width="0.8"/>
        <text x="117" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#00F2FE">Transformers</text>
        <rect x="166" y="0" width="68" height="22" rx="4" fill="#091829" stroke="#1E3A5F" stroke-width="0.8"/>
        <text x="200" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#00F2FE">FastAPI</text>
      </g>
    </g>

    <!-- PILLAR 2: FULL STACK ENGINEERING (Violet Accent) -->
    <g transform="translate(356, 140)">
      <rect width="288" height="280" rx="12" fill="url(#p2-grad)" stroke="#7928CA" stroke-width="1.2" stroke-opacity="0.4"/>
      
      <!-- Number & Icon Header -->
      <g transform="translate(20, 24)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="11" letter-spacing="1.5" fill="#C084FC" font-weight="700">PILLAR 02</text>
        <circle cx="236" cy="-4" r="8" fill="#1C0E33" stroke="#7928CA" stroke-width="1.2"/>
        <circle cx="236" cy="-4" r="3" fill="#C084FC"/>
      </g>
      
      <text x="20" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="700" fill="#FFFFFF">Full Stack Engineering</text>
      <text x="20" y="88" font-family="'SF Mono', monospace" font-size="10.5" fill="#C084FC">REACT · NODE · TYPESCRIPT</text>
      <line x1="20" y1="102" x2="268" y2="102" stroke="#1E293B" stroke-width="1"/>

      <g transform="translate(20, 126)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#94A3B8">
        <text x="0" y="0">Developing production web apps</text>
        <text x="0" y="20">with type safety, responsive state,</text>
        <text x="0" y="40">modular REST API gateways, and</text>
        <text x="0" y="60">scalable database schemas.</text>
      </g>

      <!-- Tech tags bottom -->
      <g transform="translate(20, 226)">
        <rect x="0" y="0" width="56" height="22" rx="4" fill="#1A0D30" stroke="#4C1D95" stroke-width="0.8"/>
        <text x="28" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#C084FC">React</text>
        <rect x="62" y="0" width="60" height="22" rx="4" fill="#1A0D30" stroke="#4C1D95" stroke-width="0.8"/>
        <text x="92" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#C084FC">Next.js</text>
        <rect x="128" y="0" width="64" height="22" rx="4" fill="#1A0D30" stroke="#4C1D95" stroke-width="0.8"/>
        <text x="160" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#C084FC">Node.js</text>
        <rect x="198" y="0" width="50" height="22" rx="4" fill="#1A0D30" stroke="#4C1D95" stroke-width="0.8"/>
        <text x="223" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#C084FC">SQL</text>
      </g>
    </g>

    <!-- PILLAR 3: CREATIVE TECHNOLOGY (Emerald Accent) -->
    <g transform="translate(672, 140)">
      <rect width="288" height="280" rx="12" fill="url(#p3-grad)" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.4"/>
      
      <!-- Number & Icon Header -->
      <g transform="translate(20, 24)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="11" letter-spacing="1.5" fill="#34D399" font-weight="700">PILLAR 03</text>
        <circle cx="236" cy="-4" r="8" fill="#0C261E" stroke="#10B981" stroke-width="1.2"/>
        <circle cx="236" cy="-4" r="3" fill="#34D399"/>
      </g>
      
      <text x="20" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="700" fill="#FFFFFF">Creative Technology</text>
      <text x="20" y="88" font-family="'SF Mono', monospace" font-size="10.5" fill="#34D399">MOTION · VIDEO · UI/UX</text>
      <line x1="20" y1="102" x2="268" y2="102" stroke="#1E293B" stroke-width="1"/>

      <g transform="translate(20, 126)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#94A3B8">
        <text x="0" y="0">Uniting technical development with</text>
        <text x="0" y="20">cinematic visual storytelling, motion</text>
        <text x="0" y="40">graphics design, and commercial</text>
        <text x="0" y="60">video preset engineering.</text>
      </g>

      <!-- Tech tags bottom -->
      <g transform="translate(20, 226)">
        <rect x="0" y="0" width="80" height="22" rx="4" fill="#092019" stroke="#065F46" stroke-width="0.8"/>
        <text x="40" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#34D399">After Effects</text>
        <rect x="86" y="0" width="76" height="22" rx="4" fill="#092019" stroke="#065F46" stroke-width="0.8"/>
        <text x="124" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#34D399">Premiere</text>
        <rect x="168" y="0" width="74" height="22" rx="4" fill="#092019" stroke="#065F46" stroke-width="0.8"/>
        <text x="205" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#34D399">DaVinci</text>
      </g>
    </g>

    <!-- Outer Card Border -->
    <rect x="0.5" y="0.5" width="999" height="459" rx="16" fill="none" stroke="#1E293B" stroke-width="1"/>
  </g>
</svg>'''
    return svg

# ==============================================================================
# 5. SECTION 03: FLAGSHIP PROJECT – VERIFACT
# ==============================================================================
def generate_verifact_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 780" width="1000" height="780" role="img" aria-label="Flagship Project VeriFact - Multi-Modal AI Content Verification System">
  <title>FLAGSHIP PROJECT — VERIFACT (Multi-Modal AI Content Authenticity Verification)</title>
  <defs>
    <!-- Backgrounds -->
    <linearGradient id="vf-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080F1D"/>
      <stop offset="50%" stop-color="#060A13"/>
      <stop offset="100%" stop-color="#04060A"/>
    </linearGradient>

    <linearGradient id="node-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E192D"/>
      <stop offset="100%" stop-color="#080E1A"/>
    </linearGradient>

    <linearGradient id="mod-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0D2121"/>
      <stop offset="100%" stop-color="#081414"/>
    </linearGradient>

    <!-- Accents -->
    <linearGradient id="emerald-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#00F2FE"/>
    </linearGradient>

    <!-- Filters -->
    <filter id="vf-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="vf-card"><rect width="1000" height="780" rx="16"/></clipPath>
  </defs>

  <g clip-path="url(#vf-card)">
    <!-- Base Canvas -->
    <rect width="1000" height="780" fill="url(#vf-bg)"/>

    <!-- Section Header Bar -->
    <g transform="translate(40, 42)">
      <text x="0" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="12" letter-spacing="3" fill="#10B981" font-weight="700">03 / FLAGSHIP SYSTEM SHOWCASE</text>
      <text x="920" y="0" text-anchor="end" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" letter-spacing="2" fill="#00F2FE">AI-POWERED FORENSICS</text>
      <line x1="0" y1="14" x2="920" y2="14" stroke="#1E293B" stroke-width="1"/>
    </g>

    <!-- Main Title & Abstract Verification Shield -->
    <g transform="translate(40, 84)">
      <!-- Abstract Hex Shield Logo -->
      <g transform="translate(24, 24)">
        <polygon points="0,-24 21,-12 21,12 0,24 -21,12 -21,-12" fill="#0E2822" stroke="#10B981" stroke-width="2" filter="url(#vf-glow)"/>
        <!-- Shield Checkmark -->
        <path d="M-8,-1 L-2,6 L10,-6" stroke="#00F2FE" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </g>

      <text x="64" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="34" font-weight="900" letter-spacing="1" fill="#FFFFFF">VERIFACT</text>
      <rect x="238" y="6" width="168" height="22" rx="4" fill="#0B231D" stroke="#10B981" stroke-width="0.8"/>
      <circle cx="250" cy="17" r="3.5" fill="#10B981">
        <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="260" y="21" font-family="'SF Mono', monospace" font-size="10.5" fill="#34D399" font-weight="700">MULTI-MODAL AUTHENTICITY</text>

      <text x="64" y="48" font-family="'SF Mono', monospace" font-size="12" letter-spacing="1" fill="#38BDF8" font-weight="600">MULTI-MODAL AI-POWERED CONTENT AUTHENTICITY VERIFICATION SYSTEM</text>
      <text x="64" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" fill="#94A3B8">
        VeriFact is an AI-powered platform designed to analyze and verify the authenticity of digital content across multiple modalities,
      </text>
      <text x="64" y="90" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" fill="#94A3B8">
        including text, images, videos, and URLs, identifying manipulated, misleading, deepfake, or suspicious media with forensic confidence scoring.
      </text>
    </g>

    <!-- ARCHITECTURE DIAGRAM CONTAINER (920 x 300) -->
    <g transform="translate(40, 206)">
      <rect width="920" height="300" rx="10" fill="#070D18" stroke="#1E293B" stroke-width="1.2"/>
      
      <!-- Diagram Title -->
      <g transform="translate(20, 24)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="11" letter-spacing="2" fill="#00F2FE" font-weight="700">ACTUAL PRODUCTION ARCHITECTURE PIPELINE</text>
        <text x="880" y="0" text-anchor="end" font-family="'SF Mono', monospace" font-size="10" fill="#64748B">END-TO-END DATA FLOW</text>
      </g>
      <line x1="20" y1="34" x2="900" y2="34" stroke="#162338" stroke-width="1"/>

      <!-- PIPELINE STEP 1: CLIENT USER (x=30, y=70, w=150, h=64) -->
      <g transform="translate(30, 70)">
        <rect width="150" height="64" rx="8" fill="url(#node-grad)" stroke="#38BDF8" stroke-width="1.2"/>
        <text x="14" y="24" font-family="'SF Mono', monospace" font-size="9" letter-spacing="1" fill="#38BDF8" font-weight="700">01 · FRONTEND CLIENT</text>
        <text x="14" y="42" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">React + TypeScript</text>
        <text x="14" y="56" font-family="'SF Mono', monospace" font-size="9.5" fill="#94A3B8">Vite · Tailwind CSS</text>
      </g>

      <!-- Connecting Line 1 -> 2 -->
      <path d="M180,102 L225,102" stroke="#00F2FE" stroke-width="2" stroke-dasharray="4 4">
        <animate attributeName="stroke-dashoffset" values="8;0" dur="1s" repeatCount="indefinite"/>
      </path>
      <polygon points="225,102 217,98 217,106" fill="#00F2FE"/>

      <!-- PIPELINE STEP 2: API GATEWAY (x=230, y=70, w=160, h=64) -->
      <g transform="translate(230, 70)">
        <rect width="160" height="64" rx="8" fill="url(#node-grad)" stroke="#10B981" stroke-width="1.2"/>
        <text x="14" y="24" font-family="'SF Mono', monospace" font-size="9" letter-spacing="1" fill="#10B981" font-weight="700">02 · API GATEWAY</text>
        <text x="14" y="42" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">Node.js + Express 5</text>
        <text x="14" y="56" font-family="'SF Mono', monospace" font-size="9.5" fill="#94A3B8">REST API · Auth Guard</text>
      </g>

      <!-- Connecting Line 2 -> 3 -->
      <path d="M390,102 L435,102" stroke="#10B981" stroke-width="2" stroke-dasharray="4 4">
        <animate attributeName="stroke-dashoffset" values="8;0" dur="1s" repeatCount="indefinite"/>
      </path>
      <polygon points="435,102 427,98 427,106" fill="#10B981"/>

      <!-- PIPELINE STEP 3: ML MICROSERVICE (x=440, y=70, w=180, h=64) -->
      <g transform="translate(440, 70)">
        <rect width="180" height="64" rx="8" fill="url(#node-grad)" stroke="#7928CA" stroke-width="1.4" filter="url(#vf-glow)"/>
        <text x="14" y="24" font-family="'SF Mono', monospace" font-size="9" letter-spacing="1" fill="#C084FC" font-weight="700">03 · ML MICROSERVICE</text>
        <text x="14" y="42" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">Python + FastAPI</text>
        <text x="14" y="56" font-family="'SF Mono', monospace" font-size="9.5" fill="#94A3B8">PyTorch · Transformers</text>
      </g>

      <!-- Connecting Line 3 -> 4 Modules Fanout -->
      <path d="M620,102 L660,102" stroke="#7928CA" stroke-width="2"/>
      <line x1="660" y1="56" x2="660" y2="242" stroke="#7928CA" stroke-width="1.5"/>

      <!-- Branch Lines into 4 Modules -->
      <path d="M660,68 L680,68" stroke="#00F2FE" stroke-width="1.5"/>
      <path d="M660,126 L680,126" stroke="#10B981" stroke-width="1.5"/>
      <path d="M660,184 L680,184" stroke="#F59E0B" stroke-width="1.5"/>
      <path d="M660,242 L680,242" stroke="#38BDF8" stroke-width="1.5"/>

      <!-- 4 VERIFICATION ENGINES (Right Stack) -->
      <!-- Engine 1: Text Verification -->
      <g transform="translate(680, 48)">
        <rect width="210" height="42" rx="6" fill="#0A1826" stroke="#00F2FE" stroke-width="1"/>
        <text x="12" y="18" font-family="'SF Mono', monospace" font-size="9" fill="#00F2FE" font-weight="700">01 · TEXT VERIFICATION</text>
        <text x="12" y="32" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#E2E8F0">NLI · Claim Checking · Fact Evidence</text>
      </g>

      <!-- Engine 2: Image Verification -->
      <g transform="translate(680, 106)">
        <rect width="210" height="42" rx="6" fill="#091D1A" stroke="#10B981" stroke-width="1"/>
        <text x="12" y="18" font-family="'SF Mono', monospace" font-size="9" fill="#10B981" font-weight="700">02 · IMAGE VERIFICATION</text>
        <text x="12" y="32" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#E2E8F0">Noise Forensics · CNN Deepfake Detector</text>
      </g>

      <!-- Engine 3: Video Verification -->
      <g transform="translate(680, 164)">
        <rect width="210" height="42" rx="6" fill="#1C180E" stroke="#F59E0B" stroke-width="1"/>
        <text x="12" y="18" font-family="'SF Mono', monospace" font-size="9" fill="#F59E0B" font-weight="700">03 · VIDEO VERIFICATION</text>
        <text x="12" y="32" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#E2E8F0">VideoMAE · OpenCV Frame Sampling</text>
      </g>

      <!-- Engine 4: URL Verification -->
      <g transform="translate(680, 222)">
        <rect width="210" height="42" rx="6" fill="#091726" stroke="#38BDF8" stroke-width="1"/>
        <text x="12" y="18" font-family="'SF Mono', monospace" font-size="9" fill="#38BDF8" font-weight="700">04 · URL VERIFICATION</text>
        <text x="12" y="32" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#E2E8F0">Domain Scraping · Source Cross-Check</text>
      </g>

      <!-- Bottom Integration Row: Storage & Report Generation -->
      <g transform="translate(30, 172)">
        <rect width="360" height="92" rx="8" fill="#0B1322" stroke="#1E293B" stroke-width="1"/>
        <text x="16" y="24" font-family="'SF Mono', monospace" font-size="10" letter-spacing="1" fill="#10B981" font-weight="700">DATABASE &amp; AUTHENTICATION TIERS</text>
        <g transform="translate(16, 44)">
          <rect width="156" height="34" rx="4" fill="#0E1E2E" stroke="#1E3A5F" stroke-width="0.8"/>
          <text x="10" y="16" font-family="'SF Mono', monospace" font-size="10" fill="#38BDF8" font-weight="600">MongoDB</text>
          <text x="10" y="28" font-family="'SF Mono', monospace" font-size="8.5" fill="#94A3B8">Scan History &amp; Reports</text>

          <rect x="168" width="156" height="34" rx="4" fill="#0C201C" stroke="#0D4738" stroke-width="0.8"/>
          <text x="178" y="16" font-family="'SF Mono', monospace" font-size="10" fill="#34D399" font-weight="600">Supabase</text>
          <text x="178" y="28" font-family="'SF Mono', monospace" font-size="8.5" fill="#94A3B8">Auth &amp; User Sessions</text>
        </g>
      </g>

      <!-- Forensic Report Generation Box -->
      <g transform="translate(410, 172)">
        <rect width="210" height="92" rx="8" fill="#0F172A" stroke="#00F2FE" stroke-width="1.2"/>
        <text x="14" y="24" font-family="'SF Mono', monospace" font-size="9.5" letter-spacing="1" fill="#00F2FE" font-weight="700">RESULT ENSEMBLE ENGINE</text>
        <text x="14" y="44" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">Forensic Report Output</text>
        <text x="14" y="60" font-family="'SF Mono', monospace" font-size="9" fill="#94A3B8">Confidence Score · Verdict</text>
        <text x="14" y="74" font-family="'SF Mono', monospace" font-size="9" fill="#10B981">&#x2714; REAL / FAKE / SUSPICIOUS</text>
      </g>
    </g>

    <!-- KEY FEATURES & METRICS GRID (Bottom Row: 920px total) -->
    <g transform="translate(40, 526)">
      <!-- Feature Card 1 -->
      <g transform="translate(0, 0)">
        <rect width="215" height="150" rx="8" fill="#0A1220" stroke="#1E293B" stroke-width="1"/>
        <circle cx="20" cy="24" r="4" fill="#00F2FE"/>
        <text x="32" y="28" font-family="'SF Mono', monospace" font-size="10.5" fill="#00F2FE" font-weight="700">SCAN HISTORY</text>
        <text x="20" y="58" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">Persistent Telemetry</text>
        <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">Maintains auditable history</text>
        <text x="20" y="98" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">of all forensic verification</text>
        <text x="20" y="116" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">scans and evidence trails.</text>
      </g>

      <!-- Feature Card 2 -->
      <g transform="translate(235, 0)">
        <rect width="215" height="150" rx="8" fill="#0A1220" stroke="#1E293B" stroke-width="1"/>
        <circle cx="20" cy="24" r="4" fill="#10B981"/>
        <text x="32" y="28" font-family="'SF Mono', monospace" font-size="10.5" fill="#10B981" font-weight="700">CONFIDENCE SCORE</text>
        <text x="20" y="58" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">Probabilistic Fusion</text>
        <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">Ensemble aggregation of</text>
        <text x="20" y="98" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">multi-modal model scores</text>
        <text x="20" y="116" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">yielding unified verdicts.</text>
      </g>

      <!-- Feature Card 3 -->
      <g transform="translate(470, 0)">
        <rect width="215" height="150" rx="8" fill="#0A1220" stroke="#1E293B" stroke-width="1"/>
        <circle cx="20" cy="24" r="4" fill="#F59E0B"/>
        <text x="32" y="28" font-family="'SF Mono', monospace" font-size="10.5" fill="#F59E0B" font-weight="700">TEMPORAL ANALYSIS</text>
        <text x="20" y="58" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">VideoMAE Deepfakes</text>
        <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">Frame-level OpenCV</text>
        <text x="20" y="98" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">sampling combined with</text>
        <text x="20" y="116" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">temporal aggregation.</text>
      </g>

      <!-- Feature Card 4 -->
      <g transform="translate(705, 0)">
        <rect width="215" height="150" rx="8" fill="#0A1220" stroke="#1E293B" stroke-width="1"/>
        <circle cx="20" cy="24" r="4" fill="#7928CA"/>
        <text x="32" y="28" font-family="'SF Mono', monospace" font-size="10.5" fill="#C084FC" font-weight="700">FORENSIC REPORTING</text>
        <text x="20" y="58" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">Comprehensive Export</text>
        <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">Automated generation of</text>
        <text x="20" y="98" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">forensic dossier, claims</text>
        <text x="20" y="116" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">evidence &amp; web verification.</text>
      </g>
    </g>

    <!-- Bottom Action & Repository Badge -->
    <g transform="translate(40, 700)">
      <rect width="920" height="52" rx="8" fill="#0C1527" stroke="#1E293B" stroke-width="1"/>
      
      <g transform="translate(20, 31)">
        <circle cx="0" cy="0" r="4" fill="#10B981" filter="url(#vf-glow)"/>
        <text x="14" y="4" font-family="'SF Mono', monospace" font-size="11" fill="#E2E8F0" font-weight="700">STATUS: CORE PIPELINE ACTIVE</text>
        <text x="240" y="4" font-family="'SF Mono', monospace" font-size="11" fill="#64748B">|</text>
        <text x="256" y="4" font-family="'SF Mono', monospace" font-size="11" fill="#94A3B8">GITHUB REPO: Dhanush999-git/MAJOR-PROJECT</text>
      </g>

      <!-- View Source Pill -->
      <g transform="translate(760, 13)">
        <rect width="144" height="26" rx="6" fill="#10B981" opacity="0.15"/>
        <rect width="144" height="26" rx="6" fill="none" stroke="#10B981" stroke-width="1.2"/>
        <text x="72" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="10.5" fill="#34D399" font-weight="700">FLAGSHIP REPO &#x2197;</text>
      </g>
    </g>

    <!-- Outer Card Border -->
    <rect x="0.5" y="0.5" width="999" height="779" rx="16" fill="none" stroke="#1E293B" stroke-width="1"/>
  </g>
</svg>'''
    return svg

# ==============================================================================
# 6. SECTION 04: OTHER PROJECT SHOWCASE
# ==============================================================================
def generate_projects_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 580" width="1000" height="580" role="img" aria-label="Selected Engineering Projects">
  <title>03 / SELECTED PROJECTS — Software &amp; Creative Portfolio</title>
  <defs>
    <linearGradient id="prj-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0F1D"/>
      <stop offset="100%" stop-color="#050810"/>
    </linearGradient>

    <linearGradient id="c1-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#140D26"/>
      <stop offset="100%" stop-color="#0A0714"/>
    </linearGradient>

    <linearGradient id="c2-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0D1E2D"/>
      <stop offset="100%" stop-color="#071018"/>
    </linearGradient>

    <linearGradient id="c3-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E241E"/>
      <stop offset="100%" stop-color="#081411"/>
    </linearGradient>

    <clipPath id="prj-card"><rect width="1000" height="580" rx="16"/></clipPath>
  </defs>

  <g clip-path="url(#prj-card)">
    <!-- Base Canvas -->
    <rect width="1000" height="580" fill="url(#prj-bg)"/>

    <!-- Section Header -->
    <g transform="translate(40, 42)">
      <text x="0" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="12" letter-spacing="3" fill="#00F2FE" font-weight="700">04 / SELECTED PROJECTS</text>
      <text x="920" y="0" text-anchor="end" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" letter-spacing="2" fill="#64748B">PRODUCTION REPOSITORIES</text>
      <line x1="0" y1="14" x2="920" y2="14" stroke="#1E293B" stroke-width="1"/>
    </g>

    <g transform="translate(40, 84)">
      <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="700" fill="#E2E8F0">Engineered Software &amp; Digital Products</text>
      <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" fill="#94A3B8">Curated production repositories highlighting full stack web applications, AI models, and creative storefronts.</text>
    </g>

    <!-- PROJECT CARDS ROW (3 cards, 288px width each) -->
    <!-- CARD 01: DHANUSH AE (Creative & E-Commerce Flagship) -->
    <g transform="translate(40, 134)">
      <rect width="288" height="400" rx="12" fill="url(#c1-bg)" stroke="#7928CA" stroke-width="1.2" stroke-opacity="0.5"/>
      
      <!-- Card Badge -->
      <g transform="translate(20, 24)">
        <rect width="96" height="22" rx="4" fill="#1C0E36" stroke="#7928CA" stroke-width="0.8"/>
        <text x="48" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#C084FC" font-weight="700">PROJECT 01</text>
        <circle cx="236" cy="11" r="4" fill="#C084FC"/>
      </g>

      <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">DHANUSH AE</text>
      <text x="20" y="100" font-family="'SF Mono', monospace" font-size="10.5" fill="#E879F9">CREATIVE STORE &amp; PORTFOLIO</text>
      <line x1="20" y1="114" x2="268" y2="114" stroke="#1E293B" stroke-width="1"/>

      <!-- Description -->
      <g transform="translate(20, 138)" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12.5" fill="#94A3B8">
        <text x="0" y="0">A creative portfolio and digital</text>
        <text x="0" y="18">storefront designed to showcase high-</text>
        <text x="0" y="36">end video editing work and sell</text>
        <text x="0" y="54">custom motion presets, transitions,</text>
        <text x="0" y="72">and VFX asset bundles.</text>
      </g>

      <!-- Key Capabilities -->
      <g transform="translate(20, 238)" font-family="'SF Mono', monospace" font-size="10.5" fill="#C084FC">
        <text x="0" y="0">&#x25B8; E-Commerce Preset Shop</text>
        <text x="0" y="18">&#x25B8; Framer Motion + GSAP Animations</text>
        <text x="0" y="36">&#x25B8; Prisma ORM + PostgreSQL</text>
      </g>

      <!-- Tech Stack -->
      <g transform="translate(20, 310)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="9.5" fill="#64748B" letter-spacing="1">STACK</text>
        <g transform="translate(0, 10)">
          <rect x="0" y="0" width="58" height="20" rx="4" fill="#1B0F2E" stroke="#4C1D95" stroke-width="0.8"/>
          <text x="29" y="13" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#C084FC">Next.js</text>
          <rect x="64" y="0" width="76" height="20" rx="4" fill="#1B0F2E" stroke="#4C1D95" stroke-width="0.8"/>
          <text x="102" y="13" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#C084FC">TypeScript</text>
          <rect x="146" y="0" width="56" height="20" rx="4" fill="#1B0F2E" stroke="#4C1D95" stroke-width="0.8"/>
          <text x="174" y="13" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#C084FC">Prisma</text>
        </g>
      </g>

      <!-- Repo Button -->
      <g transform="translate(20, 356)">
        <rect width="248" height="28" rx="6" fill="#1E1033" stroke="#7928CA" stroke-width="1"/>
        <text x="124" y="18" text-anchor="middle" font-family="'SF Mono', monospace" font-size="10.5" fill="#C084FC" font-weight="700">EDITING-WEBSITE &#x2197;</text>
      </g>
    </g>

    <!-- CARD 02: ID CARD DETECTION & OCR (Computer Vision) -->
    <g transform="translate(356, 134)">
      <rect width="288" height="400" rx="12" fill="url(#c2-bg)" stroke="#00F2FE" stroke-width="1.2" stroke-opacity="0.5"/>
      
      <!-- Card Badge -->
      <g transform="translate(20, 24)">
        <rect width="96" height="22" rx="4" fill="#0A1C2C" stroke="#00F2FE" stroke-width="0.8"/>
        <text x="48" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#00F2FE" font-weight="700">PROJECT 02</text>
        <circle cx="236" cy="11" r="4" fill="#00F2FE"/>
      </g>

      <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF">ID CARD OCR</text>
      <text x="20" y="100" font-family="'SF Mono', monospace" font-size="10.5" fill="#38BDF8">COMPUTER VISION PIPELINE</text>
      <line x1="20" y1="114" x2="268" y2="114" stroke="#1E293B" stroke-width="1"/>

      <!-- Description -->
      <g transform="translate(20, 138)" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12.5" fill="#94A3B8">
        <text x="0" y="0">An automated computer vision</text>
        <text x="0" y="18">framework for detecting identification</text>
        <text x="0" y="36">cards, correcting 4-point perspective</text>
        <text x="0" y="54">warp, and extracting text fields via</text>
        <text x="0" y="72">optical character recognition.</text>
      </g>

      <!-- Key Capabilities -->
      <g transform="translate(20, 238)" font-family="'SF Mono', monospace" font-size="10.5" fill="#38BDF8">
        <text x="0" y="0">&#x25B8; Contour &amp; Boundary Localization</text>
        <text x="0" y="18">&#x25B8; Perspective Warp Correction</text>
        <text x="0" y="36">&#x25B8; Structured Field Extraction</text>
      </g>

      <!-- Tech Stack -->
      <g transform="translate(20, 310)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="9.5" fill="#64748B" letter-spacing="1">STACK</text>
        <g transform="translate(0, 10)">
          <rect x="0" y="0" width="58" height="20" rx="4" fill="#0A1E30" stroke="#0284C7" stroke-width="0.8"/>
          <text x="29" y="13" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#38BDF8">Python</text>
          <rect x="64" y="0" width="60" height="20" rx="4" fill="#0A1E30" stroke="#0284C7" stroke-width="0.8"/>
          <text x="94" y="13" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#38BDF8">OpenCV</text>
          <rect x="130" y="0" width="50" height="20" rx="4" fill="#0A1E30" stroke="#0284C7" stroke-width="0.8"/>
          <text x="155" y="13" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#38BDF8">OCR</text>
        </g>
      </g>

      <!-- Repo Button -->
      <g transform="translate(20, 356)">
        <rect width="248" height="28" rx="6" fill="#081F33" stroke="#00F2FE" stroke-width="1"/>
        <text x="124" y="18" text-anchor="middle" font-family="'SF Mono', monospace" font-size="10.5" fill="#00F2FE" font-weight="700">ID-CARD-DETECTION &#x2197;</text>
      </g>
    </g>

    <!-- CARD 03: CROP DISEASE DETECTION (Agri AI & Deep Learning) -->
    <g transform="translate(672, 134)">
      <rect width="288" height="400" rx="12" fill="url(#c3-bg)" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.5"/>
      
      <!-- Card Badge -->
      <g transform="translate(20, 24)">
        <rect width="96" height="22" rx="4" fill="#09201A" stroke="#10B981" stroke-width="0.8"/>
        <text x="48" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#34D399" font-weight="700">PROJECT 03</text>
        <circle cx="236" cy="11" r="4" fill="#10B981"/>
      </g>

      <text x="20" y="80" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF">AGRI-VISION AI</text>
      <text x="20" y="100" font-family="'SF Mono', monospace" font-size="10.5" fill="#34D399">PLANT PATHOLOGY CLASSIFIER</text>
      <line x1="20" y1="114" x2="268" y2="114" stroke="#1E293B" stroke-width="1"/>

      <!-- Description -->
      <g transform="translate(20, 138)" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12.5" fill="#94A3B8">
        <text x="0" y="0">Deep learning model trained to</text>
        <text x="0" y="18">diagnose agricultural leaf diseases,</text>
        <text x="0" y="36">providing instant severity assessments,</text>
        <text x="0" y="54">pesticide remedies, and treatment</text>
        <text x="0" y="72">recommendations for farmers.</text>
      </g>

      <!-- Key Capabilities -->
      <g transform="translate(20, 238)" font-family="'SF Mono', monospace" font-size="10.5" fill="#34D399">
        <text x="0" y="0">&#x25B8; Multi-Class Plant Disease CNN</text>
        <text x="0" y="18">&#x25B8; Automated Pesticide Advisory</text>
        <text x="0" y="36">&#x25B8; Fast Inference REST Endpoint</text>
      </g>

      <!-- Tech Stack -->
      <g transform="translate(20, 310)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="9.5" fill="#64748B" letter-spacing="1">STACK</text>
        <g transform="translate(0, 10)">
          <rect x="0" y="0" width="58" height="20" rx="4" fill="#0C241D" stroke="#059669" stroke-width="0.8"/>
          <text x="29" y="13" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#34D399">PyTorch</text>
          <rect x="64" y="0" width="70" height="20" rx="4" fill="#0C241D" stroke="#059669" stroke-width="0.8"/>
          <text x="99" y="13" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#34D399">CNN Model</text>
          <rect x="140" y="0" width="56" height="20" rx="4" fill="#0C241D" stroke="#059669" stroke-width="0.8"/>
          <text x="168" y="13" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#34D399">FastAPI</text>
        </g>
      </g>

      <!-- Repo Button -->
      <g transform="translate(20, 356)">
        <rect width="248" height="28" rx="6" fill="#0A241C" stroke="#10B981" stroke-width="1"/>
        <text x="124" y="18" text-anchor="middle" font-family="'SF Mono', monospace" font-size="10.5" fill="#34D399" font-weight="700">CROP-DISEASE-MODEL &#x2197;</text>
      </g>
    </g>

    <!-- Outer Card Border -->
    <rect x="0.5" y="0.5" width="999" height="579" rx="16" fill="none" stroke="#1E293B" stroke-width="1"/>
  </g>
</svg>'''
    return svg

# ==============================================================================
# 7. SECTION 05: TECHNICAL TOOLKIT
# ==============================================================================
def generate_toolkit_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="1000" height="620" role="img" aria-label="Technical Ecosystem - Engineering and Creative Stack">
  <title>04 / TECHNOLOGY ECOSYSTEM — Dual Engineering &amp; Creative Stack</title>
  <defs>
    <linearGradient id="tk-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080D18"/>
      <stop offset="100%" stop-color="#04070D"/>
    </linearGradient>

    <linearGradient id="pnl-eng" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0C182B"/>
      <stop offset="100%" stop-color="#070E1A"/>
    </linearGradient>

    <linearGradient id="pnl-crt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0D26"/>
      <stop offset="100%" stop-color="#0E0716"/>
    </linearGradient>

    <clipPath id="tk-card"><rect width="1000" height="620" rx="16"/></clipPath>
  </defs>

  <g clip-path="url(#tk-card)">
    <!-- Base Canvas -->
    <rect width="1000" height="620" fill="url(#tk-bg)"/>

    <!-- Section Header -->
    <g transform="translate(40, 42)">
      <text x="0" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="12" letter-spacing="3" fill="#00F2FE" font-weight="700">04 / TECHNOLOGY ECOSYSTEM</text>
      <text x="920" y="0" text-anchor="end" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" letter-spacing="2" fill="#64748B">ENGINEERING &amp; CREATIVE MATRIX</text>
      <line x1="0" y1="14" x2="920" y2="14" stroke="#1E293B" stroke-width="1"/>
    </g>

    <g transform="translate(40, 84)">
      <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="700" fill="#E2E8F0">Comprehensive Technical Matrix</text>
      <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" fill="#94A3B8">Combining disciplined software architecture with high-fidelity motion graphics and creative production.</text>
    </g>

    <!-- LEFT PANEL: ENGINEERING STACK (600px width) -->
    <g transform="translate(40, 134)">
      <rect width="600" height="446" rx="12" fill="url(#pnl-eng)" stroke="#00F2FE" stroke-width="1.2" stroke-opacity="0.4"/>
      
      <!-- Panel Header -->
      <g transform="translate(24, 26)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="11" letter-spacing="2" fill="#00F2FE" font-weight="700">PANEL A · SOFTWARE &amp; AI ENGINEERING STACK</text>
        <circle cx="550" cy="-4" r="4" fill="#00F2FE"/>
      </g>
      <line x1="24" y1="36" x2="576" y2="36" stroke="#1E293B" stroke-width="1"/>

      <!-- Category 1: Languages -->
      <g transform="translate(24, 60)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="10.5" letter-spacing="1" fill="#64748B" font-weight="700">01 / PROGRAMMING LANGUAGES</text>
        <g transform="translate(0, 12)">
          <rect x="0" y="0" width="72" height="26" rx="4" fill="#0A1E33" stroke="#0284C7" stroke-width="0.8"/>
          <text x="36" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#FFFFFF" font-weight="600">Python</text>
          <rect x="80" y="0" width="60" height="26" rx="4" fill="#0A1E33" stroke="#0284C7" stroke-width="0.8"/>
          <text x="110" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#FFFFFF" font-weight="600">Java</text>
          <rect x="148" y="0" width="94" height="26" rx="4" fill="#0A1E33" stroke="#0284C7" stroke-width="0.8"/>
          <text x="195" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#FFFFFF" font-weight="600">JavaScript</text>
          <rect x="250" y="0" width="94" height="26" rx="4" fill="#0A1E33" stroke="#0284C7" stroke-width="0.8"/>
          <text x="297" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#FFFFFF" font-weight="600">TypeScript</text>
          <rect x="352" y="0" width="68" height="26" rx="4" fill="#0A1E33" stroke="#0284C7" stroke-width="0.8"/>
          <text x="386" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#FFFFFF" font-weight="600">HTML5</text>
          <rect x="428" y="0" width="62" height="26" rx="4" fill="#0A1E33" stroke="#0284C7" stroke-width="0.8"/>
          <text x="459" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#FFFFFF" font-weight="600">CSS3</text>
          <rect x="498" y="0" width="54" height="26" rx="4" fill="#0A1E33" stroke="#0284C7" stroke-width="0.8"/>
          <text x="525" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#FFFFFF" font-weight="600">SQL</text>
        </g>
      </g>

      <!-- Category 2: AI & Machine Learning -->
      <g transform="translate(24, 134)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="10.5" letter-spacing="1" fill="#64748B" font-weight="700">02 / AI &amp; MACHINE LEARNING</text>
        <g transform="translate(0, 12)">
          <rect x="0" y="0" width="76" height="26" rx="4" fill="#1C1033" stroke="#7928CA" stroke-width="0.8"/>
          <text x="38" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#E879F9" font-weight="600">PyTorch</text>
          <rect x="84" y="0" width="108" height="26" rx="4" fill="#1C1033" stroke="#7928CA" stroke-width="0.8"/>
          <text x="138" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#E879F9" font-weight="600">Transformers</text>
          <rect x="200" y="0" width="132" height="26" rx="4" fill="#1C1033" stroke="#7928CA" stroke-width="0.8"/>
          <text x="266" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#E879F9" font-weight="600">Computer Vision</text>
          <rect x="340" y="0" width="54" height="26" rx="4" fill="#1C1033" stroke="#7928CA" stroke-width="0.8"/>
          <text x="367" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#E879F9" font-weight="600">NLP</text>
          <rect x="402" y="0" width="150" height="26" rx="4" fill="#1C1033" stroke="#7928CA" stroke-width="0.8"/>
          <text x="477" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#E879F9" font-weight="600">Multi-Modal Models</text>
        </g>
      </g>

      <!-- Category 3: Frontend & Backend -->
      <g transform="translate(24, 208)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="10.5" letter-spacing="1" fill="#64748B" font-weight="700">03 / WEB ARCHITECTURE &amp; APIS</text>
        <g transform="translate(0, 12)">
          <rect x="0" y="0" width="76" height="26" rx="4" fill="#0A241F" stroke="#10B981" stroke-width="0.8"/>
          <text x="38" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#34D399" font-weight="600">React.js</text>
          <rect x="84" y="0" width="74" height="26" rx="4" fill="#0A241F" stroke="#10B981" stroke-width="0.8"/>
          <text x="121" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#34D399" font-weight="600">Next.js</text>
          <rect x="166" y="0" width="74" height="26" rx="4" fill="#0A241F" stroke="#10B981" stroke-width="0.8"/>
          <text x="203" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#34D399" font-weight="600">Node.js</text>
          <rect x="248" y="0" width="94" height="26" rx="4" fill="#0A241F" stroke="#10B981" stroke-width="0.8"/>
          <text x="295" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#34D399" font-weight="600">Express.js</text>
          <rect x="350" y="0" width="76" height="26" rx="4" fill="#0A241F" stroke="#10B981" stroke-width="0.8"/>
          <text x="388" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#34D399" font-weight="600">FastAPI</text>
          <rect x="434" y="0" width="118" height="26" rx="4" fill="#0A241F" stroke="#10B981" stroke-width="0.8"/>
          <text x="493" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#34D399" font-weight="600">Tailwind CSS</text>
        </g>
      </g>

      <!-- Category 4: Databases & DevOps Tools -->
      <g transform="translate(24, 282)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="10.5" letter-spacing="1" fill="#64748B" font-weight="700">04 / DATABASES &amp; DEVELOPER TOOLS</text>
        <g transform="translate(0, 12)">
          <rect x="0" y="0" width="82" height="26" rx="4" fill="#0A1B29" stroke="#1E3A5F" stroke-width="0.8"/>
          <text x="41" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#38BDF8" font-weight="600">MongoDB</text>
          <rect x="90" y="0" width="68" height="26" rx="4" fill="#0A1B29" stroke="#1E3A5F" stroke-width="0.8"/>
          <text x="124" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#38BDF8" font-weight="600">MySQL</text>
          <rect x="166" y="0" width="94" height="26" rx="4" fill="#0A1B29" stroke="#1E3A5F" stroke-width="0.8"/>
          <text x="213" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#38BDF8" font-weight="600">PostgreSQL</text>
          <rect x="268" y="0" width="82" height="26" rx="4" fill="#0A1B29" stroke="#1E3A5F" stroke-width="0.8"/>
          <text x="309" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#38BDF8" font-weight="600">Supabase</text>
          <rect x="358" y="0" width="50" height="26" rx="4" fill="#0A1B29" stroke="#1E3A5F" stroke-width="0.8"/>
          <text x="383" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#38BDF8" font-weight="600">Git</text>
          <rect x="416" y="0" width="68" height="26" rx="4" fill="#0A1B29" stroke="#1E3A5F" stroke-width="0.8"/>
          <text x="450" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#38BDF8" font-weight="600">VS Code</text>
          <rect x="492" y="0" width="60" height="26" rx="4" fill="#0A1B29" stroke="#1E3A5F" stroke-width="0.8"/>
          <text x="522" y="17" text-anchor="middle" font-family="'SF Mono', monospace" font-size="11" fill="#38BDF8" font-weight="600">Postman</text>
        </g>
      </g>

      <!-- Panel Footer Status -->
      <g transform="translate(24, 380)">
        <rect width="552" height="42" rx="6" fill="#050912" stroke="#162338" stroke-width="0.8"/>
        <text x="16" y="26" font-family="'SF Mono', monospace" font-size="10.5" fill="#94A3B8">SOFTWARE ARCHITECTURE // FULL SYSTEM INTEGRATION CAPABILITY</text>
      </g>
    </g>

    <!-- RIGHT PANEL: CREATIVE SUITE STACK (304px width) -->
    <g transform="translate(656, 134)">
      <rect width="304" height="446" rx="12" fill="url(#pnl-crt)" stroke="#7928CA" stroke-width="1.2" stroke-opacity="0.4"/>
      
      <!-- Panel Header -->
      <g transform="translate(20, 26)">
        <text x="0" y="0" font-family="'SF Mono', monospace" font-size="11" letter-spacing="1.5" fill="#E879F9" font-weight="700">PANEL B · CREATIVE STACK</text>
        <circle cx="264" cy="-4" r="4" fill="#E879F9"/>
      </g>
      <line x1="20" y1="36" x2="284" y2="36" stroke="#1E293B" stroke-width="1"/>

      <!-- Creative Tool 1: After Effects -->
      <g transform="translate(20, 60)">
        <rect width="264" height="74" rx="8" fill="#150B24" stroke="#7928CA" stroke-width="0.8"/>
        <text x="16" y="24" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">Adobe After Effects</text>
        <text x="16" y="42" font-family="'SF Mono', monospace" font-size="10" fill="#E879F9">MOTION GRAPHICS &amp; VFX</text>
        <text x="16" y="60" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#94A3B8">Kinetic Typography, Presets, Compositing</text>
      </g>

      <!-- Creative Tool 2: Premiere Pro -->
      <g transform="translate(20, 150)">
        <rect width="264" height="74" rx="8" fill="#150B24" stroke="#7928CA" stroke-width="0.8"/>
        <text x="16" y="24" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">Adobe Premiere Pro</text>
        <text x="16" y="42" font-family="'SF Mono', monospace" font-size="10" fill="#E879F9">LONG-FORM &amp; PRO EDITING</text>
        <text x="16" y="60" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#94A3B8">Pacing, Sound Design, Narrative Flow</text>
      </g>

      <!-- Creative Tool 3: DaVinci Resolve -->
      <g transform="translate(20, 240)">
        <rect width="264" height="74" rx="8" fill="#150B24" stroke="#7928CA" stroke-width="0.8"/>
        <text x="16" y="24" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">DaVinci Resolve</text>
        <text x="16" y="42" font-family="'SF Mono', monospace" font-size="10" fill="#E879F9">COLOR GRADING &amp; FINISHING</text>
        <text x="16" y="60" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#94A3B8">Color Science, LUTs, Dynamic Grading</text>
      </g>

      <!-- Creative Commercial Presets Box -->
      <g transform="translate(20, 330)">
        <rect width="264" height="92" rx="8" fill="#0C0714" stroke="#331A4D" stroke-width="0.8"/>
        <text x="16" y="24" font-family="'SF Mono', monospace" font-size="10" letter-spacing="1" fill="#C084FC" font-weight="700">DHANUSH AE STOREFRONT</text>
        <text x="16" y="46" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Commercial Preset Packs</text>
        <text x="16" y="66" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#94A3B8">Custom AE scripts, seamless zooms,</text>
        <text x="16" y="82" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#94A3B8">glitch maps &amp; motion graphics.</text>
      </g>
    </g>

    <!-- Outer Card Border -->
    <rect x="0.5" y="0.5" width="999" height="619" rx="16" fill="none" stroke="#1E293B" stroke-width="1"/>
  </g>
</svg>'''
    return svg

# ==============================================================================
# 8. SECTION 06: CERTIFICATIONS
# ==============================================================================
def generate_certifications_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 520" width="1000" height="520" role="img" aria-label="Certifications and Professional Development">
  <title>06 / CERTIFICATIONS &amp; PROFESSIONAL DEVELOPMENT</title>
  <defs>
    <linearGradient id="cert-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080E1B"/>
      <stop offset="100%" stop-color="#04070D"/>
    </linearGradient>

    <linearGradient id="c-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E182A"/>
      <stop offset="100%" stop-color="#090F1B"/>
    </linearGradient>

    <clipPath id="cert-card"><rect width="1000" height="520" rx="16"/></clipPath>
  </defs>

  <g clip-path="url(#cert-card)">
    <!-- Base Canvas -->
    <rect width="1000" height="520" fill="url(#cert-bg)"/>

    <!-- Section Header -->
    <g transform="translate(40, 42)">
      <text x="0" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="12" letter-spacing="3" fill="#10B981" font-weight="700">06 / CERTIFICATIONS &amp; CREDENTIALS</text>
      <text x="920" y="0" text-anchor="end" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" letter-spacing="2" fill="#64748B">CONTINUOUS LEARNING INVENTORY</text>
      <line x1="0" y1="14" x2="920" y2="14" stroke="#1E293B" stroke-width="1"/>
    </g>

    <g transform="translate(40, 84)">
      <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="700" fill="#E2E8F0">Verified Technical Training &amp; Specializations</text>
      <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" fill="#94A3B8">Demonstrated competencies across database architecture, artificial intelligence, full stack, and cybersecurity.</text>
    </g>

    <!-- 6 CERTIFICATION CARDS (2 rows x 3 columns) -->
    <!-- ROW 1 -->
    <!-- Card 1: SQL & DBMS -->
    <g transform="translate(40, 134)">
      <rect width="288" height="154" rx="10" fill="url(#c-card-bg)" stroke="#1E293B" stroke-width="1.2"/>
      <g transform="translate(18, 22)">
        <rect width="64" height="20" rx="4" fill="#0A202A" stroke="#00F2FE" stroke-width="0.8"/>
        <text x="32" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#00F2FE" font-weight="700">DATABASE</text>
        <circle cx="236" cy="10" r="4" fill="#10B981"/>
      </g>
      <text x="18" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">SQL &amp; DBMS with Project</text>
      <text x="18" y="90" font-family="'SF Mono', monospace" font-size="10" fill="#38BDF8">Relational Schemas · Queries · Project</text>
      <text x="18" y="112" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">Advanced database design, normalization, complex joins &amp; stored procedures.</text>
    </g>

    <!-- Card 2: AI Internship CODSOFT -->
    <g transform="translate(356, 134)">
      <rect width="288" height="154" rx="10" fill="url(#c-card-bg)" stroke="#1E293B" stroke-width="1.2"/>
      <g transform="translate(18, 22)">
        <rect width="90" height="20" rx="4" fill="#1B1030" stroke="#7928CA" stroke-width="0.8"/>
        <text x="45" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#C084FC" font-weight="700">AI INTERNSHIP</text>
        <circle cx="236" cy="10" r="4" fill="#10B981"/>
      </g>
      <text x="18" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">AI Internship – CODSOFT</text>
      <text x="18" y="90" font-family="'SF Mono', monospace" font-size="10" fill="#C084FC">Machine Learning · Chatbots · Vision</text>
      <text x="18" y="112" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">Applied machine learning algorithms, NLP chatbots, and recommendation tasks.</text>
    </g>

    <!-- Card 3: Python Full Stack Internship -->
    <g transform="translate(672, 134)">
      <rect width="288" height="154" rx="10" fill="url(#c-card-bg)" stroke="#1E293B" stroke-width="1.2"/>
      <g transform="translate(18, 22)">
        <rect width="80" height="20" rx="4" fill="#0A241F" stroke="#10B981" stroke-width="0.8"/>
        <text x="40" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#34D399" font-weight="700">FULL STACK</text>
        <circle cx="236" cy="10" r="4" fill="#10B981"/>
      </g>
      <text x="18" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">Python Full Stack Internship</text>
      <text x="18" y="90" font-family="'SF Mono', monospace" font-size="10" fill="#34D399">End-to-End Web App Development</text>
      <text x="18" y="112" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">Building scalable backend architectures, APIs, and responsive frontends with Python.</text>
    </g>

    <!-- ROW 2 -->
    <!-- Card 4: NoSQL MongoDB -->
    <g transform="translate(40, 312)">
      <rect width="288" height="154" rx="10" fill="url(#c-card-bg)" stroke="#1E293B" stroke-width="1.2"/>
      <g transform="translate(18, 22)">
        <rect width="84" height="20" rx="4" fill="#0A2024" stroke="#00F2FE" stroke-width="0.8"/>
        <text x="42" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#00F2FE" font-weight="700">NOSQL DATA</text>
        <circle cx="236" cy="10" r="4" fill="#10B981"/>
      </g>
      <text x="18" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">NoSQL MongoDB</text>
      <text x="18" y="90" font-family="'SF Mono', monospace" font-size="10" fill="#38BDF8">Document Stores · Aggregation · Indexing</text>
      <text x="18" y="112" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">Schema design for high-throughput unstructured data and rapid query aggregation.</text>
    </g>

    <!-- Card 5: Blockchain Virtual Internship -->
    <g transform="translate(356, 312)">
      <rect width="288" height="154" rx="10" fill="url(#c-card-bg)" stroke="#1E293B" stroke-width="1.2"/>
      <g transform="translate(18, 22)">
        <rect width="84" height="20" rx="4" fill="#1B1030" stroke="#7928CA" stroke-width="0.8"/>
        <text x="42" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#C084FC" font-weight="700">BLOCKCHAIN</text>
        <circle cx="236" cy="10" r="4" fill="#10B981"/>
      </g>
      <text x="18" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">Blockchain Virtual Internship</text>
      <text x="18" y="90" font-family="'SF Mono', monospace" font-size="10" fill="#C084FC">Distributed Ledgers · Smart Contracts</text>
      <text x="18" y="112" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">Decentralized protocols, cryptographic verification &amp; consensus algorithms.</text>
    </g>

    <!-- Card 6: Networking & Cybersecurity -->
    <g transform="translate(672, 312)">
      <rect width="288" height="154" rx="10" fill="url(#c-card-bg)" stroke="#1E293B" stroke-width="1.2"/>
      <g transform="translate(18, 22)">
        <rect width="94" height="20" rx="4" fill="#0A241F" stroke="#10B981" stroke-width="0.8"/>
        <text x="47" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#34D399" font-weight="700">CYBERSECURITY</text>
        <circle cx="236" cy="10" r="4" fill="#10B981"/>
      </g>
      <text x="18" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">Networking &amp; Security</text>
      <text x="18" y="90" font-family="'SF Mono', monospace" font-size="10" fill="#34D399">Cyber Professionals · Defense</text>
      <text x="18" y="112" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" fill="#94A3B8">TCP/IP protocols, threat vectors, perimeter defense &amp; network security fundamentals.</text>
    </g>

    <!-- Outer Card Border -->
    <rect x="0.5" y="0.5" width="999" height="519" rx="16" fill="none" stroke="#1E293B" stroke-width="1"/>
  </g>
</svg>'''
    return svg

# ==============================================================================
# 9. SECTION 07: CONNECTIVITY HUB
# ==============================================================================
def generate_connect_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 440" width="1000" height="440" role="img" aria-label="Let's Connect - Connectivity Hub">
  <title>07 / LET'S CONNECT — Professional Connectivity Hub</title>
  <defs>
    <linearGradient id="cnt-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080D1A"/>
      <stop offset="100%" stop-color="#04060C"/>
    </linearGradient>

    <linearGradient id="cnt-card-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E182A"/>
      <stop offset="100%" stop-color="#080E18"/>
    </linearGradient>

    <filter id="cnt-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="cnt-card"><rect width="1000" height="440" rx="16"/></clipPath>
  </defs>

  <g clip-path="url(#cnt-card)">
    <!-- Base Canvas -->
    <rect width="1000" height="440" fill="url(#cnt-bg)"/>

    <!-- Section Header -->
    <g transform="translate(40, 42)">
      <text x="0" y="0" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="12" letter-spacing="3" fill="#00F2FE" font-weight="700">07 / LET'S CONNECT</text>
      <text x="920" y="0" text-anchor="end" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11" letter-spacing="2" fill="#64748B">INTERACTIVE HUB</text>
      <line x1="0" y1="14" x2="920" y2="14" stroke="#1E293B" stroke-width="1"/>
    </g>

    <g transform="translate(40, 84)">
      <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">Initiate A Connection</text>
      <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" fill="#94A3B8">Interested in building an intelligent AI system, a production full stack application, or collaborating on creative motion?</text>
    </g>

    <!-- 4 LARGE INTERACTIVE CONTACT CARDS (4 x 215px) -->
    <!-- Card 1: GitHub -->
    <g transform="translate(40, 134)">
      <rect width="215" height="180" rx="10" fill="url(#cnt-card-bg)" stroke="#00F2FE" stroke-width="1.2" stroke-opacity="0.4"/>
      <g transform="translate(20, 24)">
        <circle cx="16" cy="16" r="16" fill="#091A2E" stroke="#00F2FE" stroke-width="1"/>
        <path fill="#00F2FE" transform="translate(6, 6) scale(0.6)" d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 4.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.942.359.31.678.921.678 1.856 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0020 10.017C20 4.484 15.522 0 10 0z"/>
      </g>
      <text x="20" y="80" font-family="'SF Mono', monospace" font-size="10" letter-spacing="1" fill="#64748B">SOURCE VAULT</text>
      <text x="20" y="102" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">GitHub</text>
      <text x="20" y="122" font-family="'SF Mono', monospace" font-size="10.5" fill="#38BDF8">@Dhanush999-git</text>
      <g transform="translate(20, 138)">
        <rect width="175" height="24" rx="4" fill="#0A2033" stroke="#00F2FE" stroke-width="0.8"/>
        <text x="87" y="16" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#00F2FE" font-weight="700">EXPLORE CODE &#x2197;</text>
      </g>
    </g>

    <!-- Card 2: LinkedIn -->
    <g transform="translate(275, 134)">
      <rect width="215" height="180" rx="10" fill="url(#cnt-card-bg)" stroke="#38BDF8" stroke-width="1.2" stroke-opacity="0.4"/>
      <g transform="translate(20, 24)">
        <circle cx="16" cy="16" r="16" fill="#091A2E" stroke="#38BDF8" stroke-width="1"/>
        <path fill="#38BDF8" transform="translate(7, 7) scale(0.65)" d="M19 0h-18c-.55 0-1 .45-1 1v18c0 .55.45 1 1 1h18c.55 0 1-.45 1-1v-18c0-.55-.45-1-1-1zm-11 17h-3v-9h3v9zm-1.5-10.27c-.97 0-1.75-.79-1.75-1.76s.78-1.75 1.75-1.75 1.75.78 1.75 1.75-.78 1.76-1.75 1.76zm11.5 10.27h-3v-4.6c0-1.1-.02-2.52-1.54-2.52-1.54 0-1.77 1.2-1.77 2.44v4.68h-3v-9h2.88v1.23h.04c.4-.76 1.38-1.56 2.84-1.56 3.04 0 3.6 2 3.6 4.61v4.72z"/>
      </g>
      <text x="20" y="80" font-family="'SF Mono', monospace" font-size="10" letter-spacing="1" fill="#64748B">PROFESSIONAL</text>
      <text x="20" y="102" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">LinkedIn</text>
      <text x="20" y="122" font-family="'SF Mono', monospace" font-size="10.5" fill="#38BDF8">Dhanush M D</text>
      <g transform="translate(20, 138)">
        <rect width="175" height="24" rx="4" fill="#0A2033" stroke="#38BDF8" stroke-width="0.8"/>
        <text x="87" y="16" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#38BDF8" font-weight="700">CONNECT &#x2197;</text>
      </g>
    </g>

    <!-- Card 3: Portfolio -->
    <g transform="translate(510, 134)">
      <rect width="215" height="180" rx="10" fill="url(#cnt-card-bg)" stroke="#7928CA" stroke-width="1.2" stroke-opacity="0.4"/>
      <g transform="translate(20, 24)">
        <circle cx="16" cy="16" r="16" fill="#1A0D30" stroke="#7928CA" stroke-width="1"/>
        <path fill="#C084FC" transform="translate(7, 7) scale(0.65)" d="M10 0C4.48 0 0 4.48 0 10s4.48 10 10 10 10-4.48 10-10S15.52 0 10 0zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v2.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V4h2c1.1 0 2-.9 2-2v-.41C16.92 3.2 19 6.35 19 10c0 2.27-.92 4.33-2.1 5.39z"/>
      </g>
      <text x="20" y="80" font-family="'SF Mono', monospace" font-size="10" letter-spacing="1" fill="#64748B">DIGITAL SHOWCASE</text>
      <text x="20" y="102" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">Portfolio</text>
      <text x="20" y="122" font-family="'SF Mono', monospace" font-size="10.5" fill="#C084FC">Dhanush.dev</text>
      <g transform="translate(20, 138)">
        <rect width="175" height="24" rx="4" fill="#1C0F33" stroke="#7928CA" stroke-width="0.8"/>
        <text x="87" y="16" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#C084FC" font-weight="700">LAUNCH SHOWCASE &#x2197;</text>
      </g>
    </g>

    <!-- Card 4: Email Direct -->
    <g transform="translate(745, 134)">
      <rect width="215" height="180" rx="10" fill="url(#cnt-card-bg)" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.4"/>
      <g transform="translate(20, 24)">
        <circle cx="16" cy="16" r="16" fill="#0B231B" stroke="#10B981" stroke-width="1"/>
        <path fill="#34D399" transform="translate(7, 7) scale(0.65)" d="M18 0H2C.9 0 0 .9 0 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V2c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V2l8 5 8-5v2z"/>
      </g>
      <text x="20" y="80" font-family="'SF Mono', monospace" font-size="10" letter-spacing="1" fill="#64748B">DIRECT DISPATCH</text>
      <text x="20" y="102" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">Email</text>
      <text x="20" y="122" font-family="'SF Mono', monospace" font-size="9" fill="#34D399">mddhanush6@gmail.com</text>
      <g transform="translate(20, 138)">
        <rect width="175" height="24" rx="4" fill="#0A241B" stroke="#10B981" stroke-width="0.8"/>
        <text x="87" y="16" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" fill="#34D399" font-weight="700">DISPATCH EMAIL &#x2197;</text>
      </g>
    </g>

    <!-- Bottom Status Banner -->
    <g transform="translate(40, 344)">
      <rect width="920" height="56" rx="8" fill="#0B1322" stroke="#1E293B" stroke-width="1"/>
      <circle cx="28" cy="28" r="5" fill="#10B981" filter="url(#cnt-glow)">
        <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="44" y="32" font-family="'SF Mono', monospace" font-size="11.5" letter-spacing="1" fill="#34D399" font-weight="700">CURRENT STATUS:</text>
      <text x="176" y="32" font-family="'SF Mono', monospace" font-size="11.5" letter-spacing="0.8" fill="#E2E8F0">OPEN TO LEARNING, ENGINEERING OPPORTUNITIES &amp; COLLABORATIONS</text>
    </g>

    <!-- Outer Card Border -->
    <rect x="0.5" y="0.5" width="999" height="439" rx="16" fill="none" stroke="#1E293B" stroke-width="1"/>
  </g>
</svg>'''
    return svg

# ==============================================================================
# 10. SECTION 08: SIGNATURE FOOTER
# ==============================================================================
def generate_footer_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 220" width="1000" height="220" role="img" aria-label="Dhanush M D - Signature Footer">
  <title>Dhanush M D — Engineering Intelligence. Building Experiences. Creating Impact.</title>
  <defs>
    <linearGradient id="ftr-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080D18"/>
      <stop offset="100%" stop-color="#030508"/>
    </linearGradient>

    <linearGradient id="ftr-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0"/>
      <stop offset="25%" stop-color="#00F2FE" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#7928CA" stop-opacity="1"/>
      <stop offset="75%" stop-color="#10B981" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0"/>
    </linearGradient>

    <filter id="ftr-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="ftr-card"><rect width="1000" height="220" rx="16"/></clipPath>
  </defs>

  <g clip-path="url(#ftr-card)">
    <!-- Base Canvas -->
    <rect width="1000" height="220" fill="url(#ftr-bg)"/>

    <!-- Subtle Ambient Prismatic Beam -->
    <line x1="100" y1="36" x2="900" y2="36" stroke="url(#ftr-line)" stroke-width="1.5" filter="url(#ftr-glow)"/>

    <!-- Signature Quote -->
    <text x="500" y="82" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-style="italic" font-size="18" fill="#E2E8F0">
      "Engineering intelligence. Building experiences. Creating impact."
    </text>

    <!-- Sign-off Name -->
    <text x="500" y="126" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="28" letter-spacing="3" fill="#FFFFFF">
      DHANUSH M D
    </text>

    <!-- Subtitle Meta -->
    <text x="500" y="156" text-anchor="middle" font-family="'SF Mono', 'JetBrains Mono', monospace" font-size="11.5" letter-spacing="2.5" fill="#00F2FE" font-weight="600">
      FULL STACK · AI/ML ENGINEER · CREATIVE TECHNOLOGIST
    </text>

    <!-- Copyright / Node Identity -->
    <text x="500" y="188" text-anchor="middle" font-family="'SF Mono', monospace" font-size="10" letter-spacing="1.5" fill="#64748B">
      DESIGNED &amp; ARCHITECTED WITH PRECISION // CYBER OBSIDIAN &#x00D7; ELECTRIC PRISMATIC
    </text>

    <!-- Outer Card Border -->
    <rect x="0.5" y="0.5" width="999" height="219" rx="16" fill="none" stroke="#1E293B" stroke-width="1"/>
  </g>
</svg>'''
    return svg

# ==============================================================================
# 11. SECTION HEADER: ACTIVITY HEADER
# ==============================================================================
def generate_activity_header_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 90" width="1000" height="90" role="img" aria-label="Development Activity Header">
  <title>05 / DEVELOPMENT ACTIVITY</title>
  <defs>
    <linearGradient id="act-hdr-bg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#080D18"/>
      <stop offset="100%" stop-color="#050810"/>
    </linearGradient>
    <clipPath id="act-hdr-clip"><rect width="1000" height="90" rx="12"/></clipPath>
  </defs>
  <g clip-path="url(#act-hdr-clip)">
    <rect width="1000" height="90" fill="url(#act-hdr-bg)" stroke="#1E293B" stroke-width="1"/>
    <text x="32" y="36" font-family="'SF Mono', monospace" font-size="11.5" letter-spacing="3" fill="#00F2FE" font-weight="700">05 / DEVELOPMENT ACTIVITY</text>
    <text x="968" y="36" text-anchor="end" font-family="'SF Mono', monospace" font-size="11" letter-spacing="2" fill="#64748B">CONTINUOUS COMMIT TELEMETRY</text>
    <line x1="32" y1="48" x2="968" y2="48" stroke="#1E293B" stroke-width="1"/>
    <text x="32" y="72" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600" fill="#E2E8F0">Real-Time GitHub Activity &amp; Engineering Contributions</text>
    <text x="968" y="72" text-anchor="end" font-family="'SF Mono', monospace" font-size="10.5" fill="#10B981">&#x25CF; AUTOMATED PIPELINE SYNCHRONIZED</text>
  </g>
</svg>'''
    return svg

def main():
    print("Building Cyber Obsidian × Electric Prismatic Assets...")
    
    # 1. Hero
    validate_svg(generate_hero_banner(), "assets/hero/hero-banner.svg")
    validate_svg(generate_hero_banner(), "assets/hero-banner.svg")

    # 2. Badges
    build_all_badges()

    # 3. Sections
    validate_svg(generate_about_svg(), "assets/sections/about.svg")
    validate_svg(generate_narrative_svg(), "assets/sections/narrative.svg")
    validate_svg(generate_verifact_svg(), "assets/sections/verifact.svg")
    validate_svg(generate_verifact_svg(), "assets/cards/verifact-card.svg")
    validate_svg(generate_projects_svg(), "assets/sections/projects.svg")
    validate_svg(generate_projects_svg(), "assets/cards/project-cards.svg")
    validate_svg(generate_toolkit_svg(), "assets/sections/toolkit.svg")
    validate_svg(generate_certifications_svg(), "assets/sections/certifications.svg")
    validate_svg(generate_connect_svg(), "assets/sections/connect.svg")
    validate_svg(generate_footer_svg(), "assets/sections/footer.svg")
    validate_svg(generate_activity_header_svg(), "assets/sections/activity-header.svg")

    print("[SUCCESS] All SVG assets built and validated successfully.")

if __name__ == "__main__":
    main()

