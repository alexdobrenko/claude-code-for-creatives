# Simon Willison's Tools — Example of Building with AI

**Source:** [tools.simonwillison.net](https://tools.simonwillison.net/)
**Highlights post:** [simonwillison.net/2025/Sep/4/highlighted-tools](https://simonwillison.net/2025/Sep/4/highlighted-tools/)

---

## Why This Matters

Simon Willison is a prolific builder who uses AI (Claude, GPT-4, etc.) to create small, useful tools. His collection demonstrates:

1. **Volume over perfection** — Dozens of single-purpose tools, not one monolithic app
2. **Real problems** — Each tool solves something he actually needed
3. **AI-assisted development** — Many built quickly with LLM help
4. **Browser-first** — Most run entirely client-side (no backend needed)

**Key insight:** You don't need to build an app. You can build a collection of tools.

---

## Highlighted Tools (Best Examples)

These are the ones Simon specifically called out as favorites:

| Tool | What It Does | Why It's Interesting |
|------|--------------|---------------------|
| **OCR PDFs and Images** | Extracts text from PDFs/images in-browser | Uses PDF.js + Tesseract.js, no server |
| **Image Resize Quality Comparison** | Drag image → compare sizes/quality | Quick visual tool |
| **Social Media Card Cropper** | Crop to 2:1 for Twitter/Bluesky | Solves a specific annoying problem |
| **SVG to JPEG/PNG** | Converts SVG to raster formats | Built with prompt-based development |
| **Encrypt/Decrypt Message** | Encrypt with passphrase → shareable URL | Used in workshops for API keys |
| **Jina Reader** | Webpage → clean data on clipboard | Wrapper with copy button added |
| **llm-prices.com** | LLM pricing comparison + token calc | "Graduated to its own domain" |
| **Open Sauce 2025** | Conference schedule with search/ICS export | Built entirely on a phone with Codex |
| **Incomplete JSON Pretty Printer** | Pretty-prints truncated JSON | Handles edge cases other tools can't |
| **Bluesky WebSocket Firehose** | Watch real-time Bluesky activity | Browser-based API access |

---

## Full Tool Categories

### Image & Media (13 tools)
- Social media cropper (2×1 ratio)
- Image resize and quality comparison
- Image to JPEG converter
- Image to SVG tracer
- SVG to JPEG/PNG renderer
- SVG sandbox (safe display)
- SVG progressive render
- BBox cropper (bounding boxes)
- Mask visualizer
- FFmpeg crop helper
- TIFF orientation viewer
- Avatar web component
- YouTube Thumbnails

### Text & Document (20+ tools)
- OCR (images and PDFs in-browser)
- PDF OCR
- Compare PDFs (visual diff)
- Render Markdown (via GitHub API)
- HTML preview (live)
- RTF to HTML
- Markdown math (LaTeX)
- Reading time calculator
- Word counter
- Clipboard viewer/debugger
- Extract URLs from HTML
- JSON to Markdown transcript
- JSON to YAML converter
- YAML Explorer (collapsible tree)
- JSON schema builder (visual)
- Incomplete JSON printer
- PHP Deserializer
- SQL Pretty Printer
- Pipfile.lock parser

### Data & Time (8 tools)
- Timestamp converter
- Timezone comparison
- Date calculator (days between dates)
- Transfer time estimator
- Token usage calculator (LLM logs)
- LLM prices redirect
- CSV marker map
- Species observation map (iNaturalist)

### GitHub & Dev (8 tools)
- GitHub API write (upload to repos)
- GitHub issue viewer
- GitHub issue to Markdown
- Zip/Wheel explorer (Python packages)
- Ares phonetic alphabet
- Code with Claude 2025 (workflow prototype)
- Side panel dialog demo
- Broadcast channel chat

### Bluesky & Social (7 tools)
- Bluesky WebSocket Firehose
- Bluesky resolve DID
- Bluesky timeline viewer
- Bluesky thread export (to Markdown)
- Bluesky quote finder
- Event planner (localStorage)
- Passkeys demo

### LLM Playgrounds (12 tools)
- Haiku generator (Claude Haiku + webcam)
- Chrome Prompt Playground (Gemini Nano)
- Gemini bounding box visualizer
- Gemini chat client
- Gemini mask visualizer
- Gemini image JSON renderer
- Claude Token Counter
- OpenAI audio input
- OpenAI audio output
- OpenAI WebRTC demo
- GPT-4o Gist audio player
- JSON schema builder

---

## Patterns Worth Stealing

### 1. Single-purpose tools
Each tool does ONE thing. No feature creep. If you need a new thing, make a new tool.

### 2. Client-side first
Most tools run entirely in the browser. No server = no hosting costs = no maintenance.

### 3. Scratch your own itch
Every tool exists because Simon needed it. Not "what would be cool" but "what do I actually need right now."

### 4. Ship fast, iterate later
Many were built in a single session with AI help. Polish comes later (or never).

### 5. Tools as content
Each tool is also a blog post. The building IS the content.

---

## For the Course

This collection demonstrates:
- **What's possible** with AI-assisted development
- **The mindset** of building many small things vs one big thing
- **Real utility** — these aren't demos, they're tools Simon uses
- **Low barrier** — browser-based, no deployment complexity

**Potential module:** "Build 5 tools in 5 days" — use Simon's approach as inspiration

---

## Links

- Main collection: https://tools.simonwillison.net/
- Highlighted tools post: https://simonwillison.net/2025/Sep/4/highlighted-tools/
- Simon's blog: https://simonwillison.net/
- His LLM CLI tool: https://llm.datasette.io/
