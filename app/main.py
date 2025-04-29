from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from .utils import generate_nda

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_form():
    return """
    <html>
        <head>
            <title>NDA Generator</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    background-color: #f5f5f5;
                }
                h1 {
                    color: #333;
                }
                form {
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                    max-width: 600px;
                }
                label {
                    display: block;
                    margin-top: 15px;
                    font-weight: bold;
                }
                input, select {
                    width: 100%;
                    padding: 8px;
                    margin-top: 5px;
                    margin-bottom: 10px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 15px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    margin-top: 10px;
                }
                button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <h1>Create a Mutual NDA</h1>
            <form action="/generate_nda/" method="post">
                <label>Party 1 Name:</label>
                <input type="text" name="party1_name" required>

                <label>Party 1 Address:</label>
                <input type="text" name="party1_address" required>

                <label>Party 1 State of Incorporation:</label>
                <input type="text" name="party1_state" required>

                <label>Party 1 Entity Type:</label>
                <select name="party1_entity" required>
                    <option value="Individual">Individual</option>
                    <option value="Corporation">Corporation</option>
                    <option value="Limited Liability Company">Limited Liability Company</option>
                    <option value="Partnership">Partnership</option>
                </select>

                <label>Party 2 Name:</label>
                <input type="text" name="party2_name" required>

                <label>Party 2 Address:</label>
                <input type="text" name="party2_address" required>

                <label>Party 2 State of Incorporation:</label>
                <input type="text" name="party2_state" required>

                <label>Party 2 Entity Type:</label>
                <select name="party2_entity" required>
                    <option value="Individual">Individual</option>
                    <option value="Corporation">Corporation</option>
                    <option value="Limited Liability Company">Limited Liability Company</option>
                    <option value="Partnership">Partnership</option>
                </select>

                <button type="submit">Generate NDA</button>
            </form>
        </body>
    </html>
    """

@app.post("/generate_nda/")
async def create_nda(
    party1_name: str = Form(...),
    party1_address: str = Form(...),
    party1_state: str = Form(...),
    party1_entity: str = Form(...),
    party2_name: str = Form(...),
    party2_address: str = Form(...),
    party2_state: str = Form(...),
    party2_entity: str = Form(...)
):
    output_path = generate_nda(
        party1_name, party1_address, party1_state, party1_entity,
        party2_name, party2_address, party2_state, party2_entity
    )
    return FileResponse(
        path=output_path,
        filename="Generated_NDA.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
