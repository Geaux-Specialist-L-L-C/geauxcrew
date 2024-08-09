# src/education_crewai/tools/downloader_tool.py
import os
import requests
import boto3
import openai
from crewai_tools import tool

# Initialize the S3 client
s3 = boto3.client("s3")

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")


@tool
def download_and_process_content(url, bucket_name, subject, grade_level):
    """
    Downloads content from the given URL, processes it using OpenAI,
    and stores the processed content in the specified S3 bucket, organized by subject and grade level.
    """
    try:
        # Download the content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Process content using OpenAI (e.g., summarization)
        content_summary = (
            openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Summarize the following content: {response.text}",
                max_tokens=150,
            )
            .choices[0]
            .text.strip()
        )

        # Generate a filename based on the URL
        filename = url.split("/")[-1] or "processed_content"

        # Determine the S3 key (path in the bucket)
        s3_key = f"{subject}/{grade_level}/{filename}.txt"

        # Upload the summary to S3
        s3.put_object(
            Bucket=bucket_name, Key=s3_key, Body=content_summary.encode("utf-8")
        )

        return f"Successfully processed and stored content in {bucket_name}/{s3_key}"

    except requests.exceptions.RequestException as e:
        return f"Failed to download content from {url}: {e}"
    except openai.error.OpenAIError as e:
        return f"Failed to process content using OpenAI: {e}"
    except Exception as e:
        return f"Failed to store content in S3: {e}"
