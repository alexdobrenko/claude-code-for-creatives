# AI Course Research Analysis: "Reflecting on AI in 2025"

**Video:** AI Explained - "Reflecting on AI in 2025"
**Video ID:** 3_71Nog8JZw
**Channel:** AI Explained (Technical AI commentary/analysis channel)
**Analysis Date:** 2025-12-25

---

## Executive Summary

This is a deep technical breakdown of Open Router's 2025 AI usage report. The presenter analyzes real-world LLM usage patterns across 100+ trillion tokens, covering model adoption, use cases, costs, and trends. Heavy focus on open-weight vs closed models, reasoning models, and surprising usage patterns (spoiler: roleplay dominates open-weight models at 52%).

**Key Insight for Course Design:** This video reveals a massive gap between what people *think* AI is used for (productivity, coding) and what it's *actually* used for at scale (creative applications, roleplay, diverse non-coding tasks). An AI course that only focuses on ChatGPT for work tasks misses the broader landscape.

---

## AI Topics & Tools Covered

### Major Models Discussed
- **OpenAI:** GPT-4, GPT-4o, GPT-4.5, GPT-4o mini, o1 (reasoning)
- **Anthropic:** Claude 3.5 Sonnet, Claude 3.7, Claude 4, Claude 4.5 (heavy emphasis on tool calling dominance)
- **Google:** Gemini 2.5 Pro, Gemini Flash models, Gemma 3/4
- **Chinese Open-Weight:** DeepSeek (V3, R1, 3.1, 3.2), Qwen 3, Kimmy K2, MiniMax M2, GLM models
- **Meta:** Llama models
- **xAI:** Grok (repeatedly mentioned as "free to drive adoption")
- **Mistral:** Various Mistral models

### Infrastructure & Platforms
- **Open Router** - Central platform analyzed (routes to all models)
- **LM Studio** - Local model running
- **Cursor, Windsurf** - AI coding tools
- **T3 Chat** - Creator's own chat platform (mentions $8/month pricing constraint)

### Technical Concepts Explained
- **Reasoning models** - O1, DeepSeek R1 (multi-step deliberation vs single-pass generation)
- **Open-weight vs closed-weight models** - Distinction emphasized throughout
- **Tool calling** - Models invoking external functions/APIs
- **Agentic inference** - AI making sequential decisions, using tools, persisting state
- **Token economics** - Prompt tokens vs completion tokens, reasoning tokens
- **Context windows** - Longer sequences for complex interactions
- **Unified memory** - MacBook M4 Max RAM = VRAM advantage for local models
- **VRAM limitations** - Desktop GPU constraints vs Mac unified memory

---

## Frameworks & Mental Models

### 1. **The Open-Weight Ecosystem Framework**
- **Definition Split:** Small (<15B params), Medium (15-70B), Large (70B+)
- **Key Insight:** Medium models finding "market fit" - best price/performance sweet spot
- **Market Dynamic:** Rapid innovation cycles, no guaranteed leadership, constant competitive pressure
- **Analogy:** "Feels like the early days of closed-weight models in the open-weight world"

### 2. **The Three Types of Model Usage**
1. **Creative/Roleplay** - Largest open-weight use case (52%), price-sensitive, less content filtering needed
2. **Programming** - High token counts, specialized models, tool calling heavy
3. **Knowledge/Productivity** - General Q&A, analysis, translation

### 3. **Cost vs Capability Matrix**
- Cost does NOT significantly drive usage (weak correlation)
- "Being cheap isn't enough. A model must be differentiable and sufficiently capable."
- Quality > Price for most use cases
- Exception: Roleplay community is highly price-sensitive (uses free models)

### 4. **The Agentic Shift**
- **Old:** Simple question → simple answer (single-pass)
- **New:** Structured agent loops → reasoning → tool invocation → multi-step completion
- **Evidence:** 50%+ of tokens now go through reasoning models
- **Implication:** "The median LLM request is no longer a simple question"

### 5. **The "Free Model Trap" Pattern**
- When models are free → adoption spikes massively
- When pricing starts → usage vanishes immediately
- Example: Grok 4.1 Fast chart showing 100% → 0% usage post-pricing
- Lesson: Early adoption doesn't mean product-market fit

### 6. **Infrastructure Determines Usage** (Open Router Bias)
- Models that are "hard to use directly" dominate Open Router (Gemini, Grok, GPT-OSS)
- Models with good native APIs (GPT-4, Claude) show lower Open Router usage
- "OpenAI and Anthropic have competent APIs... with Google models, there is basically no competent way to hit them other than Open Router"
- **Business lesson:** Being a wrapper/aggregator is valuable when underlying UX sucks

### 7. **The Glass Slipper Effect** (Author's skepticism noted)
- Theory: Early adopters of models stick around longer
- Users who find a model that solves a *previously unsolvable problem* have high retention
- Author is skeptical: "I really just don't buy this part"

---

## Language & Explanation Style

### Tone & Approach
- **Very technical but accessible** - Assumes audience knows what LLMs are, but explains reasoning models, token types, etc.
- **Data-driven storytelling** - "Let me show you the chart... you're probably thinking it's coding, right? NOPE, it's roleplay"
- **Sarcastic/irreverent** - "Good luck with all those calls if you're not using WorkOS" / "The weebs cannot be stopped"
- **Opinionated** - Doesn't hide preferences (loves Kimmy K2, hates 2.5 Pro, thinks GPT-OSS is "criminally underrated")
- **Personal anecdotes** - References his own T3 Chat product, his MacBook setup, his 5090 desktop

### Explanation Patterns
1. **Show the mystery first** - "Guess what this yellow category is... between 40-80% usage..."
2. **Challenge assumptions** - "You'd think it's code, right? Reality is always more interesting"
3. **Explain through contrast** - Open-weight vs closed, prompt tokens vs completion tokens, RAM vs VRAM
4. **Use analogies** - "Your lawyer's cheaper than your Dungeons & Dragons DM"
5. **Call out biases explicitly** - Repeatedly mentions Open Router data is biased toward certain use cases

### Effective Phrasing
- "Holy shit there's something special happening" (DeepSeek V3 moment)
- "If you know, you know" (insider knowledge signal)
- "Criminally underrated" (GPT-OSS)
- "The weebs cannot be stopped" (roleplay dominance)
- "Shut the fuck up" (addressing hypothetical audience questions about T3 Chat features)
- "This is nuts" / "That's crazy" (genuine surprise at data)

### What Resonates (Based on Emphasis)
1. **Surprising data reveals** - Roleplay being #1, reasoning tokens >50%, Chinese models rising
2. **Cost analysis** - Deep dive into why certain business models work/don't work
3. **Technical deep dives** - Unified memory explanation, token economics, tool calling
4. **Calling out bullshit** - Google's terrible APIs, free models gaming charts, skepticism of "glass slipper effect"
5. **Practical applications** - Why he uses different models for different tasks

---

## Gaps & Opportunities for an AI Course

### Gap 1: **The Non-Coding Majority**
- **Problem:** Most AI courses focus on productivity/coding (ChatGPT for work)
- **Reality:** 52% of open-weight usage is roleplay/creative applications
- **Opportunity:** Course module on creative AI use cases (storytelling, character creation, worldbuilding, creative writing)
- **Market:** Massively underserved creative community already using AI heavily

### Gap 2: **Model Selection Framework**
- **Problem:** People default to ChatGPT for everything
- **Reality:** "There's good use cases and bad use cases for all of these. You just got to play with them to know."
- **Opportunity:** Teach a decision framework:
  - When to use reasoning models vs fast models
  - When to use open-weight vs closed
  - When to use local vs API
  - Cost/speed/quality tradeoffs
- **Example from video:** "I like talking to Kimmy K2, but I like doing data analysis with GPT-OSS"

### Gap 3: **Local vs Cloud Economics**
- **Problem:** No one teaches the RAM/VRAM tradeoff
- **Reality:** MacBook with 128GB unified memory runs 120B models faster than RTX 5090
- **Opportunity:** Module on when/why to run models locally
  - Privacy concerns
  - Cost at scale
  - Hardware requirements (RAM is the bottleneck, not just GPU)
  - Use cases (offline work, sensitive data)

### Gap 4: **Agentic AI Workflows**
- **Problem:** Courses teach "ask ChatGPT a question, get an answer"
- **Reality:** "The median LLM request is no longer a simple question. It's part of a structured agent-like loop"
- **Opportunity:** Course focused on building agent workflows:
  - Tool calling
  - Multi-step reasoning
  - Context persistence
  - Tokens you'll never read (AI-to-AI communication)

### Gap 5: **Open-Weight Ecosystem**
- **Problem:** Most people have never heard of DeepSeek, Qwen, Kimmy K2
- **Reality:** 30%+ of inference is open-weight, Chinese models dominating that space
- **Opportunity:** Introduction to open-weight models
  - What they are, how to access them
  - When they're better than GPT/Claude
  - How to use Open Router or similar aggregators
  - Understanding model sizes and hardware requirements

### Gap 6: **Infrastructure & Developer Experience**
- **Problem:** People assume all AI APIs are the same
- **Reality:** "Google's APIs are the stupidest, most miserable fucking thing... I would gladly pay 3-5% to route through Open Router"
- **Opportunity:** Module on AI infrastructure basics
  - Why API wrappers exist and when to use them
  - Understanding rate limits, costs, data retention
  - Authentication, billing, SDK quality
  - When to use Claude Code, Cursor, vs native APIs

### Gap 7: **Token Economics & Cost Management**
- **Problem:** "Why don't you add coding to T3 Chat?" "Because it would 4-6x our costs and we charge $8/month. Shut the fuck up."
- **Reality:** Coding uses 4-6x more tokens than chat, prompt tokens vs completion tokens matter
- **Opportunity:** Course module on managing AI costs
  - Understanding token pricing
  - Why certain use cases are expensive (coding, long context)
  - How reasoning tokens affect pricing
  - Building sustainable pricing models if selling AI products

### Gap 8: **Bias in AI Benchmarks & Reports**
- **Problem:** People read one report and assume it's universal truth
- **Reality:** Author repeatedly calls out Open Router data biases (free models spike, hard-to-use models overrepresented)
- **Opportunity:** Critical thinking module
  - How to read AI benchmarks skeptically
  - Understanding selection bias in usage reports
  - Why "most popular" != "best"
  - Free tier effects on adoption metrics

### Gap 9: **Practical Tool Calling & Multi-Modal**
- **Problem:** Most courses don't teach tool calling beyond theory
- **Reality:** Claude owns 60%+ of programming spend, dominates tool calling charts
- **Opportunity:** Hands-on workshop on:
  - Building functions that LLMs can call
  - Error handling in agentic workflows
  - MCP (Model Context Protocol) servers
  - Authentication for AI-powered tools

### Gap 10: **The "Why" Behind Model Releases**
- **Problem:** People don't understand the competitive dynamics
- **Reality:** "DeepSeek V3 was the 'holy shit there's something special' moment, not R1"
- **Opportunity:** Industry context module
  - Why labs release open-weight models (data collection, market pressure)
  - Understanding model release cadence
  - How to evaluate new model announcements
  - Following AI news without hype

---

## Course Structure Ideas (Based on Video Insights)

### Module 1: **Beyond ChatGPT - The AI Landscape**
- Open-weight vs closed models
- Major players: OpenAI, Anthropic, Google, Chinese labs
- Using Open Router or similar aggregators
- Activity: Try 5 different models on the same task, compare results

### Module 2: **Model Selection Decision Framework**
- Cost/speed/quality tradeoffs
- When to use reasoning models
- Task-specific model recommendations (coding, creative, analysis, chat)
- Lab: Build a flowchart for your use cases

### Module 3: **Creative AI Use Cases**
- Storytelling, worldbuilding, character development
- Why roleplay dominates open-weight models
- Ethical considerations and content filtering
- Project: Build a creative writing assistant

### Module 4: **Agentic Workflows & Tool Calling**
- What is agentic inference?
- Building tool-calling functions
- Multi-step reasoning patterns
- Project: Create an AI that can research and summarize

### Module 5: **Local AI & Hardware**
- RAM vs VRAM, unified memory
- Running models on Mac vs PC vs cloud
- When local makes sense (privacy, cost, offline)
- Lab: Run a local model in LM Studio

### Module 6: **Token Economics & Cost Management**
- Understanding prompt/completion/reasoning tokens
- Why coding is expensive (4-6x token usage)
- Estimating costs for projects
- Building cost-effective AI products

### Module 7: **Advanced Infrastructure**
- API wrappers and why they exist
- Understanding rate limits, quotas, authentication
- MCP servers and Claude Code
- WorkOS-style auth for AI apps (sponsor in video)

### Module 8: **Critical AI Literacy**
- Reading benchmarks skeptically
- Understanding usage biases
- Free model effects on adoption
- Separating hype from reality

---

## Notable Quotes for Marketing/Course Content

1. **On underestimating AI use cases:**
   - "You've got to be thinking stuff like code or maybe chat... Reality is always more interesting cuz that is the roleplaying category."

2. **On model diversity:**
   - "There's good use cases and bad use cases for all of these. You just got to play with them to know."

3. **On the agentic shift:**
   - "The median LLM request is no longer a simple question or an isolated instruction. It's part of a structured agent-like loop."

4. **On cost vs quality:**
   - "Being cheap isn't enough. A model must be differentiable and sufficiently capable."

5. **On developer experience:**
   - "OpenAI and Anthropic have competent APIs... With Google models, there is basically no competent way to hit them other than Open Router."

6. **On sustainable business:**
   - "If we let you bring your codebase, we're just going to increase our cost by four to 6x. Go use Cursor. It's a good tool."

7. **On underrated models:**
   - "GPT-OSS criminally underrated... if you know, you know."

8. **On the roleplay community:**
   - "The weebs cannot be stopped."

9. **On token visibility:**
   - "The average token isn't read by a human... Those tokens for reasoning are making the actual answer more likely to be better."

10. **On DeepSeek's importance:**
    - "V3 was the holy shit there's something special happening here moment."

---

## Audience Insights

### Who This Channel Serves
- **Developers/technical users** building with AI
- **Power users** who want to understand the ecosystem deeply
- **Cost-conscious builders** concerned with token economics
- **People who've moved beyond ChatGPT basics**

### What They Value
- Data-driven analysis over hype
- Technical depth with practical application
- Honest takes (skepticism of marketing, willingness to criticize)
- Real-world usage patterns vs benchmarks
- Cost/performance tradeoffs

### Language Level
- Assumes knowledge of: tokens, APIs, parameters, VRAM, context windows
- Explains: reasoning models, tool calling, agentic inference, unified memory
- Tone: Technical friend explaining charts over coffee (with swearing)

---

## Application to Your AI Course

### Key Takeaway 1: **Widen the Use Case Aperture**
Don't just teach "AI for productivity." The data shows massive creative usage. Include modules on:
- AI for writing/storytelling
- AI for creative projects
- AI for entertainment and exploration
- **Frame:** "AI isn't just a work tool - it's a creative partner"

### Key Takeaway 2: **Teach Model Selection, Not Just Model Usage**
- Stop defaulting to ChatGPT for everything
- Build a decision framework based on task, cost, speed, quality
- Introduce Open Router or similar tools early
- **Frame:** "The right model for the right job"

### Key Takeaway 3: **Infrastructure Matters**
- Don't skip the "boring" stuff like APIs, authentication, cost management
- Show why some tools suck and alternatives exist
- Teach token economics from day one
- **Frame:** "Understanding infrastructure saves you money and headaches"

### Key Takeaway 4: **Move Beyond Question/Answer**
- Agentic workflows are the future
- Tool calling is becoming standard
- Multi-step reasoning is growing
- **Frame:** "From asking questions to building AI agents"

### Key Takeaway 5: **Critical Thinking About AI**
- Don't trust every benchmark or usage report
- Understand biases (free tiers, API quality, selection effects)
- Question marketing claims
- **Frame:** "How to separate AI signal from noise"

---

## Next Steps for Course Development

1. **Survey potential students:** Are they aware of open-weight models? Do they know about tool calling?
2. **Map use cases:** Beyond coding/productivity, what creative applications interest them?
3. **Test model selection:** Give students a task, have them try 3-5 different models, discuss differences
4. **Build cost calculator:** Tool to estimate token costs for different use cases
5. **Create infrastructure module:** How to set up Open Router, understand APIs, manage auth
6. **Develop critical literacy exercises:** Analyze AI reports/benchmarks for biases
7. **Design agentic project:** Something that requires tool calling and multi-step reasoning
8. **Consider local AI workshop:** For privacy-conscious or offline users

---

## Technical Details Worth Teaching

### From Video Demonstrations
1. **MacBook unified memory advantage** - 128GB RAM = VRAM, can run 120B models at 71 TPS (faster than cloud GPT-4.5)
2. **Token speed matters** - GPT-OSS on Cerebras: 2000 TPS (enables new use cases like real-time sentiment analysis)
3. **Tool calling dominance** - Claude 4.5 owns this category, worth understanding why
4. **Prompt token growth** - 4x increase over 2025 (driven by coding use cases)
5. **Reasoning token overhead** - 50%+ of tokens now go through reasoning models
6. **Geographic distribution** - Still 80%+ English, North America-dominant
7. **Open-weight growth** - From ~5% to 30%+ of inference in one year

---

## Conclusion

This video is a goldmine for understanding:
1. **What people actually use AI for** (not just what tech media says)
2. **Why certain models/platforms win** (developer experience > features)
3. **The economics of AI** (token costs, free tiers, pricing pressure)
4. **The technical landscape** (open vs closed, reasoning, tool calling)
5. **How to think critically** about AI reports and benchmarks

**Best opportunity for your course:** Fill the gap between "ChatGPT basics" and "build your own LLM from scratch." Teach the middle layer:
- Model selection
- Infrastructure/APIs
- Cost management
- Agentic workflows
- Creative applications
- Critical literacy

The audience exists (Open Router handles 100+ trillion tokens), and they're hungry for practical, honest guidance beyond marketing hype.
