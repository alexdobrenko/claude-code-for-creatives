// Sends email notification when someone completes the intake form

export async function handler(event) {
    if (event.httpMethod !== 'POST') {
        return { statusCode: 405, body: 'Method not allowed' };
    }

    const RESEND_API_KEY = process.env.RESEND_API_KEY;

    try {
        const data = JSON.parse(event.body);
        const summary = formatIntakeSummary(data);

        console.log('=== NEW INTAKE SUBMISSION ===');
        console.log(summary);

        // Send email via Resend
        if (RESEND_API_KEY) {
            const emailResponse = await fetch('https://api.resend.com/emails', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${RESEND_API_KEY}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    from: 'Code for Creatives <onboarding@resend.dev>',
                    to: 'alex.dobrenko@gmail.com',
                    subject: `New Intake: ${data.name}`,
                    text: summary,
                    html: formatIntakeHTML(data)
                })
            });

            const emailResult = await emailResponse.json();
            console.log('Resend response:', emailResponse.status, JSON.stringify(emailResult));

            if (!emailResponse.ok) {
                console.error('Resend error:', emailResult);
                return {
                    statusCode: 200,
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ success: true, emailError: emailResult })
                };
            }

            return {
                statusCode: 200,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ success: true, emailSent: true, emailId: emailResult.id })
            };
        } else {
            console.log('No RESEND_API_KEY set');
            return {
                statusCode: 200,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ success: true, emailSent: false, reason: 'No API key' })
            };
        }

    } catch (error) {
        console.error('Intake notification error:', error);
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Failed to process intake' })
        };
    }
}

function formatIntakeSummary(data) {
    const techLevelMap = {
        'never': "Never opened a terminal",
        'dabbled': "Dabbled in Claude Code / Cursor",
        'comfortable': "Comfortable, wants to go deeper"
    };

    const helpWithMap = {
        'content': "Writing & content workflows",
        'business': "Business ops",
        'tools': "Building personal tools",
        'organizing': "Organizing files/ideas",
        'social': "Social media & repurposing",
        'explore': "Wants to see what's possible"
    };

    let summary = `
NEW INTAKE: ${data.name}
Email: ${data.email || 'Not provided'}
Time: ${data.timestamp}
========================================

TECHNICAL LEVEL: ${techLevelMap[data.techLevel] || data.techLevel || 'Not specified'}

INTERESTED IN:
${(data.helpWith || []).map(h => `  - ${helpWithMap[h] || h}`).join('\n') || '  Not specified'}
`;

    if (data.vent) {
        summary += `
WHAT THEY SAID:
"${data.vent}"
`;
    }

    if (data.followUpResponses && data.followUpResponses.length > 0) {
        summary += `
FOLLOW-UP RESPONSES:
${data.followUpResponses.map((r, i) => `  ${i + 1}. "${r}"`).join('\n')}
`;
    }

    if (data.conversationHistory && data.conversationHistory.length > 0) {
        summary += `
FULL CONVERSATION:
${data.conversationHistory.map(m => `  [${m.role}]: ${m.content}`).join('\n')}
`;
    }

    return summary;
}

function formatIntakeHTML(data) {
    const techLevelMap = {
        'never': "Never opened a terminal",
        'dabbled': "Dabbled in Claude Code / Cursor",
        'comfortable': "Comfortable, wants to go deeper"
    };

    const helpWithMap = {
        'content': "Writing & content workflows",
        'business': "Business ops",
        'tools': "Building personal tools",
        'organizing': "Organizing files/ideas",
        'social': "Social media & repurposing",
        'explore': "Wants to see what's possible"
    };

    let html = `
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto;">
        <h1 style="color: #B85C38; margin-bottom: 8px;">New Intake: ${data.name}</h1>
        <p style="color: #666; margin-top: 0;"><a href="mailto:${data.email}">${data.email || 'No email'}</a> • ${data.timestamp}</p>

        <div style="background: #FAF8F5; padding: 20px; border-radius: 12px; margin: 20px 0;">
            <h3 style="margin-top: 0; color: #2D2A26;">Technical Level</h3>
            <p style="margin-bottom: 0;">${techLevelMap[data.techLevel] || data.techLevel || 'Not specified'}</p>
        </div>

        <div style="background: #FAF8F5; padding: 20px; border-radius: 12px; margin: 20px 0;">
            <h3 style="margin-top: 0; color: #2D2A26;">Interested In</h3>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                ${(data.helpWith || []).map(h => `<li>${helpWithMap[h] || h}</li>`).join('') || '<li>Not specified</li>'}
            </ul>
        </div>
    `;

    if (data.vent || (data.followUpResponses && data.followUpResponses.length > 0)) {
        html += `
        <div style="background: #FAF8F5; padding: 20px; border-radius: 12px; margin: 20px 0;">
            <h3 style="margin-top: 0; color: #2D2A26;">What They Said</h3>
        `;

        if (data.vent) {
            html += `<p style="font-style: italic; border-left: 3px solid #B85C38; padding-left: 12px;">"${data.vent}"</p>`;
        }

        if (data.followUpResponses && data.followUpResponses.length > 0) {
            html += `<h4>Follow-up responses:</h4>`;
            data.followUpResponses.forEach((r, i) => {
                html += `<p style="font-style: italic; border-left: 3px solid #7A8B6F; padding-left: 12px; margin: 8px 0;">"${r}"</p>`;
            });
        }

        html += `</div>`;
    }

    if (data.conversationHistory && data.conversationHistory.length > 0) {
        html += `
        <div style="background: #f5f5f5; padding: 20px; border-radius: 12px; margin: 20px 0;">
            <h3 style="margin-top: 0; color: #2D2A26;">Full Conversation</h3>
            ${data.conversationHistory.map(m => `
                <p style="margin: 8px 0;">
                    <strong style="color: ${m.role === 'user' ? '#B85C38' : '#3D6B6B'};">${m.role === 'user' ? data.name : 'Alex'}:</strong>
                    ${m.content}
                </p>
            `).join('')}
        </div>
        `;
    }

    html += `</div>`;
    return html;
}
