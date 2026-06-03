<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,20&height=280&section=header&text=%F0%9F%8C%90%20Translator%20Hub&fontSize=48&fontColor=fff&animation=twinkling&fontAlignY=38&desc=A%20multi-translator%20web%20app%20featuring%20custom%20linguistic%20patterns%20and%20themes!&descSize=16&descAlignY=55&descColor=ccc"/>

<img src="https://img.shields.io/badge/Next.js-16-black?style=for-the-badge&logo=next.js" alt="Next.js"/>
<img src="https://img.shields.io/badge/TypeScript-5.0-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript"/>
<img src="https://img.shields.io/badge/Three.js-r184-000000?style=for-the-badge&logo=three.js" alt="Three.js"/>
<img src="https://img.shields.io/badge/Tailwind_CSS-4.0-38B2AC?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS"/>
<img src="https://img.shields.io/badge/Zustand-5.0-7B3FE0?style=for-the-badge&logo=react&logoColor=white" alt="Zustand"/>

<br><br>

> **Eight tongues, one workshop.**
> A surreal 3D typography & translation interface with custom conlangs, glass tiles, and dynamic themes.

[Preview](#preview) &nbsp;&middot;&nbsp; [Languages](#-languages--rules) &nbsp;&middot;&nbsp; [Features](#-features) &nbsp;&middot;&nbsp; [Themes](#-themes) &nbsp;&middot;&nbsp; [Getting Started](#-getting-started)

</div>

---

## Preview

<div align="center">

<br>

```text
  ╔══════════════════════════════════════════╗
  ║                                          ║
  ║    ☁️ Floating glass tiles orbiting       ║
  ║    in a 3D cluster that unfurls           ║
  ║    into an interactive carousel            ║
  ║                                          ║
  ║    ❄️ Eis    👌 Buwgeh   🦷 Toothie      ║
  ║    🦵 Thighs 🥜 Nuss     😩 Agh          ║
  ║    🎵 Aynanana  🌍 All                   ║
  ║                                          ║
  ╚══════════════════════════════════════════╝
```

</div>

---

## 📖 Languages & Rules

Each tongue applies a unique phonetic or morphological transformation to English text:

| # | Language | Tag | Transformation | Example |
|:-:|:---------|:---:|:----------------|:--------|
| 1 | ❄️ **Eis** | `phonetic` | `what → ani les`, `sh → s`, `ch → ts`, `j/soft-g → dz` | *What should we do?* → *Ani les sould we dzoo?* |
| 2 | 👌 **Buwgeh** | `rhotic` | `r (final) → h`, `r (elsewhere) → w` | *River* → *Wiveh* |
| 3 | 🦷 **Toothie** | `dental` | Appends `th` to every word | *Hello* → *Helloth* |
| 4 | 🦵 **Thighs** | `sibilant` | Replaces trailing `s` with `th` | *Yes* → *Yeth* |
| 5 | 🥜 **Nuss** | `bisection` | Cuts words in half + adds `nuss` | *Stuff* → *Stnuss* |
| 6 | 😩 **Agh** | `wail` | Appends `aghhhhh` to every word | *Hello* → *Helloaghhhhh* |
| 7 | 🎵 **Aynanana** | `chant` | Appends `aynanana` to every word | *Hello* → *Helloaynanana* |
| 8 | 🌍 **All** | `unified` | Chains all 7 tongues in sequence | *The river flows* → *... (7 transforms layered)* |

> **Note:** In "All" mode, Agh and Nuss only apply with a **20% chance** when the word contains the letter `a`.

---

## ✨ Features

### Core
- 🔄 **Bi-directional Translation** — Swap between English and your custom language instantly
- 🌐 **All-in-One Mode** — A unified tile that chains all 7 tongues together
- 🎯 **Real-time Typing** — See translations appear as you type, with keystroke ripple effects
- 📋 **Copy to Clipboard** — One-click copy of translated text

### 3D Experience
- 🪟 **Glass Tiles** — `MeshPhysicalMaterial` with transmission, refraction, and clearcoat
- 🎨 **Dynamic Color Cycling** — Per-tile sin-wave color oscillation between primary and alternate hues
- 💫 **Breathing Cluster** — Tiles gently orbit and breathe in an organic cluster formation
- 🎠 **Carousel Unfurl** — Scroll to unfurl the cluster into an interactive ring carousel
- 🫧 **Floating Glyphs** — Ambient phonetic symbols drifting through 3D space
- ✨ **Particle System** — Additive-blended particles with radial gradient textures

### UI / UX
- 🌗 **3 Distinct Themes** — Cream, Ink, and Void
- 📱 **Fully Responsive** — Mobile-first design, touch-friendly targets
- 🎭 **Suggestion Samples** — Pre-written phrases to test each tongue
- ⌨️ **Keyboard Ripple** — Visual pulse feedback on every keystroke

---

## 🎨 Themes

| Theme | Style | Background | Accent | Mood |
|:-----:|:------|:----------|:------|:-----|
| **Cream** | Warm parchment | `#F1EDE3` | 🟢 `#D9FF3A` | Cozy, literary, ink-on-paper |
| **Ink** | Dark warm sepia | `#1c1410` | 🟠 `#FF8844` | Dim candlelight, ancient scrolls |
| **Void** | Cold blue-black | `#020208` | 🔵 `#00FFAA` | Cosmic, cyberpunk, deep space |

<br>

<div align="center">

```
   CREAM              INK               VOID
  ┌────────┐      ┌────────┐      ┌────────┐
  │ ☁️ 🟢  │      │ 🕯️ 🟠  │      │ 🌌 🔵  │
  │ Warm   │      │ Dark    │      │ AMOLED │
  │ Paper  │      │ Sepia   │      │ Deep   │
  │  Light │      │  Theme  │      │  Space │
  └────────┘      └────────┘      └────────┘
```

</div>

---

## 🚀 Getting Started

### Prerequisites

- [Bun](https://bun.sh/) (recommended) or Node.js 18+
- A modern browser with WebGL 2.0 support

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/translator-hub.git
cd translator-hub

# Install dependencies
bun install

# Start the development server
bun run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Available Scripts

| Command | Description |
|:--------|:------------|
| `bun run dev` | Start dev server on port 3000 |
| `bun run build` | Production build |
| `bun run lint` | Run ESLint |
| `bun run db:push` | Push Prisma schema to database |

---

## 🏗️ Tech Stack

| Technology | Purpose |
|:-----------|:--------|
| [Next.js 16](https://nextjs.org/) | React framework with App Router |
| [TypeScript 5](https://www.typescriptlang.org/) | Type-safe development |
| [Three.js](https://threejs.org/) + `@react-three/fiber` | 3D rendering & WebGL |
| `@react-three/drei` | Three.js helpers (Text, RoundedBox) |
| [Tailwind CSS 4](https://tailwindcss.com/) | Utility-first styling |
| [Framer Motion](https://www.framer.com/motion/) | UI animations & transitions |
| [Zustand](https://zustand-demo.pmnd.rs/) | Lightweight state management |
| [Prisma](https://www.prisma.io/) | ORM & database (SQLite) |

---

## 📁 Project Structure

```
src/
├── app/
│   ├── page.tsx              # Entry point (renders TranslatorApp)
│   ├── layout.tsx            # Root layout
│   └── globals.css           # Global styles
│
├── components/
│   ├── translator/
│   │   ├── TranslatorApp.tsx  # Main app shell (themes, overlay, footer)
│   │   └── Scene3D.tsx       # 3D scene (tiles, particles, glyphs)
│   └── ui/                    # shadcn/ui components
│
├── lib/
│   └── translator.ts         # Language definitions, rules, themes, translate()
│
└── stores/
    └── translator-store.ts    # Zustand store (viewState, selection, theme)
```

---

## 🧩 How Translations Work

Each language defines a **forward** (`fwd`) and **reverse** (`rev`) transformation using regex pattern matching:

```
English  ──[fwd]──►  Conlang  ──[rev]──►  English
```

**Example — Buwgeh:**
```
Forward:  r (final) → h,  r → w
Reverse:  w → r,  h → r  (simplified)

Input:    "The river flows gently"
Forward:  "The wiveh flows gently"
Reverse:  "The river flows gently"
```

**All Mode Pipeline:**
```
Eis → Buwgeh → Toothie → Thighs → Nuss(20%) → Agh(20%) → Aynanana
```

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,20&height=100&section=footer"/>

<br>

Built with ❤️ by **Translator Hub**

</div>
