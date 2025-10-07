# Tinker API NLP Fine-Tuning Example

This project provides a simple example of how to use the Tinker API to fine-tune a large language model for a natural language processing (NLP) task. The example is based on the `tinker-cookbook` and demonstrates a supervised fine-tuning task.

The Tinker API uses LoRa (Low-Rank Adaptation) by default for fine-tuning, which is an efficient way to adapt large language models. This is handled by the Tinker backend and does not require explicit configuration in this script.

## Setup

1.  **Clone the `tinker-cookbook` repository and install it:**

    ```bash
    git clone https://github.com/thinking-machines-lab/tinker-cookbook
    cd tinker-cookbook
    pip install -e .
    cd ..
    ```

2.  **Install the `tinker` library:**

    ```bash
    pip install tinker
    ```

## Running the Fine-Tuning Script

To run the fine-tuning script, you need to have a Tinker API key. You can sign up for the waitlist on the [Tinker website](https://thinkingmachines.ai/tinker).

1.  **Set your Tinker API key:**

    Export your API key as an environment variable.

    ```bash
    export TINKER_API_KEY="YOUR_API_KEY"
    ```

2.  **Run the script:**

    Execute the `fine_tune_nlp.py` script, providing the path to your dataset. You can use the example dataset from the `tinker-cookbook` repository.

    ```bash
    python fine_tune_nlp.py --dataset_path /path/to/your/dataset.jsonl
    ```

    For example, if you cloned `tinker-cookbook` in the same directory as this project, you can run:

    ```bash
    python fine_tune_nlp.py --dataset_path tinker-cookbook/example-data/conversations.jsonl
    ```

    The script will start a fine-tuning job on the Tinker platform. You can monitor the progress of the job in the Tinker console.

## Using Your Own Dataset

To fine-tune the model on your own dataset, you need to create a JSONL file where each line is a JSON object representing a conversation. The format should be the same as the `tinker-cookbook/example-data/conversations.jsonl` file.

Once you have your dataset, you can run the `fine_tune_nlp.py` script and provide the path to your file using the `--dataset_path` argument.