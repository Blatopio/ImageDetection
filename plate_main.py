import gradio as gr
from detections import detect_plateNumber

with gr.Blocks() as demo:
    gr.Markdown("## Plate Number Detection System")
    gr.Markdown("This application uses a YOLO-based model to detect plate numbers in images. Upload an image to detect any plate numbers. The model will highlight detected plate numbers and provide a summary of the findings.")
    gr.Markdown("Upload an image to detect any plate numbers. The model will highlight detected plate numbers and provide a summary of the findings.")
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Upload Image", type="pil")
            detect_button = gr.Button("Detect Plate Numbers")
        with gr.Column():
            output_image = gr.Image(label="Detection Result")
            summary_image = gr.Image(label="Summary")
            status_box = gr.Textbox(label="Status", lines=1)

    detect_button.click(
        fn=detect_plateNumber,
        inputs=input_image,
        outputs=[output_image, summary_image, status_box]
    )

demo.launch()