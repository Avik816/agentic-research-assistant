const API_BASE = "http://localhost:8000";


/* Send user research query */
export async function sendQuery(query) {

    const response = await fetch(
        `${API_BASE}/query`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                query: query
            })
        }
    );

    if (!response.ok) {
        throw new Error(
            `Backend Error: ${response.status}`
        );
    }

    return await response.json();
}