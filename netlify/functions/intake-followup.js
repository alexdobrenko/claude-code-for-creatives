// Generates follow-up questions using Claude API

export async function handler(event) {
    if (event.httpMethod !== 'POST') {
        return { statusCode: 405, body: 'Method not allowed' };
    }

    const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;

    if (!ANTHROPIC_API_KEY) {
        console.error('Missing ANTHROPIC_API_KEY');
        return {
            statusCode: 200,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ followUp: null })
        };
    }

    try {
        const { name, conversation } = JSON.parse(event.body);

        const systemPrompt = `You are Alex, helping someone figure out how to use AI tools for their creative work. You're doing an intake call to understand what they need.

Your job: Ask ONE short, clarifying follow-up question to better understand:
- What specific problem they're trying to solve
- What they've tried before
- What success would look like for them

Keep it conversational and warm. One question only. No pleasantries or filler - just the question.

If you feel you understand their situation well enough (they've given specific details about their problem, what they want, and context), respond with just: DONE

Examples of good follow-up questions:
- "What does a typical day look like when this problem hits you?"
- "When you say [X], what does that actually look like in practice?"
- "What have you tried so far to solve this?"
- "If this worked perfectly, what would be different?"`;

        const messages = conversation.map(m => ({
            role: m.role === 'user' ? 'user' : 'assistant',
            content: m.content
        }));

        const response = await fetch('https://api.anthropic.com/v1/messages', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-api-key': ANTHROPIC_API_KEY,
                'anthropic-version': '2023-06-01'
            },
            body: JSON.stringify({
                model: 'claude-3-5-haiku-20241022',
                max_tokens: 150,
                system: systemPrompt,
                messages: messages
            })
        });

        if (!response.ok) {
            throw new Error(`Anthropic API error: ${response.status}`);
        }

        const data = await response.json();
        const reply = data.content[0]?.text?.trim();

        // If Claude says DONE or gives an empty response, finish the conversation
        if (!reply || reply === 'DONE' || reply.includes('DONE')) {
            return {
                statusCode: 200,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ followUp: null })
            };
        }

        return {
            statusCode: 200,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ followUp: reply })
        };

    } catch (error) {
        console.error('Follow-up error:', error);
        return {
            statusCode: 200,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ followUp: null })
        };
    }
}
