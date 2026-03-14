import gradio as gr
from orchestration.orchestrator import run_pipeline


async def generate_email(prompt: str):
    result = await run_pipeline(prompt)
    return result


def build_interface():
    with gr.Blocks() as app:

        gr.Markdown("# Cold Email Drafter")
        gr.Markdown("Generate a cold outreach email using multiple AI agents.")

        prompt_input = gr.Textbox(
            label="Describe your product and target customer",
            placeholder="Example: Write a cold email selling an AI scheduling tool to small law firms"
        )

        generate_button = gr.Button("Generate Email")

        output_box = gr.Textbox(
            label="Generated Email",
            lines=12
        )

        generate_button.click(
            fn=generate_email,
            inputs=prompt_input,
            outputs=output_box
        )

    return app


def launch_ui():
    app = build_interface()
    app.launch()
