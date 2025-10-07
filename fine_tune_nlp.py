import os
import argparse
from tinker_cookbook import cli_utils, model_info
from tinker_cookbook.renderers import TrainOnWhat
from tinker_cookbook.supervised import train
from tinker_cookbook.supervised.data import FromConversationFileBuilder
from tinker_cookbook.supervised.types import ChatDatasetBuilderCommonConfig


def build_config(dataset_path: str) -> train.Config:
    """
    Builds the configuration for the fine-tuning job.

    The Tinker API uses LoRa (Low-Rank Adaptation) by default for fine-tuning,
    which is an efficient way to adapt large language models. This is handled
    by the Tinker backend and does not require explicit configuration in this script.
    """
    # Specify the base model to fine-tune.
    # You can find a list of available models in the Tinker documentation.
    model_name = "meta-llama/Llama-3.1-8B"

    # Get the recommended renderer for the chosen model.
    # The renderer is responsible for formatting the data into the model's expected format.
    renderer_name = model_info.get_recommended_renderer_name(model_name)

    # Common configuration for the dataset builder.
    common_config = ChatDatasetBuilderCommonConfig(
        model_name_for_tokenizer=model_name,
        renderer_name=renderer_name,
        max_length=32768,
        batch_size=128,
        train_on_what=TrainOnWhat.ALL_ASSISTANT_MESSAGES,
    )

    # Create a dataset builder from the provided JSONL file.
    dataset = FromConversationFileBuilder(
        common_config=common_config, file_path=dataset_path
    )

    # Configuration for the training process.
    return train.Config(
        log_path="/tmp/tinker-examples/sl_basic",
        model_name=model_name,
        dataset_builder=dataset,
        learning_rate=2e-4,
        lr_schedule="linear",
        num_epochs=1,
        eval_every=8,
    )


def main():
    """
    Main function to run the fine-tuning process.
    """
    parser = argparse.ArgumentParser(
        description="Fine-tune a language model using the Tinker API."
    )
    parser.add_argument(
        "--dataset_path",
        type=str,
        required=True,
        help="Path to the JSONL file containing the training data.",
    )
    args = parser.parse_args()

    # Build the configuration.
    config = build_config(args.dataset_path)

    # Check if the log directory already exists and ask for user confirmation to overwrite.
    # This prevents accidentally overwriting previous training logs.
    cli_utils.check_log_dir(config.log_path, behavior_if_exists="ask")

    # Start the training process.
    train.main(config)


if __name__ == "__main__":
    main()