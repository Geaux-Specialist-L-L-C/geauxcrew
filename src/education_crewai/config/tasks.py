from crewai import Task
from .agents import researcher, compiler, downloader

# Task for the Researcher Agent
research_task = Task(
    description=(
        "Identify grade-appropriate curriculum materials for a student. "
        "This includes textbooks, online courses, and other educational content relevant to the student's grade level. "
        "Focus on gathering comprehensive, reliable, and engaging resources. "
        "Save the results to a text file named 'curriculum_urls.txt'."
    ),
    expected_output="A list of resources with links and brief descriptions.",
    agent=researcher,
    output_file="curriculum_urls.txt",  # Save the output to this file
)

# Task for the Compiler Agent
compilation_task = Task(
    description=(
        "Using the gathered materials, organize them into a structured educational program for the student. "
        "The program should cover all necessary subjects and be easy to follow."
    ),
    expected_output="A structured educational program in a detailed format, such as a syllabus or weekly plan.",
    agent=compiler,
)

# Task for the Downloader Agent
download_task = Task(
    description=(
        "For each URL listed in 'curriculum_urls.txt', download the content, process it with OpenAI, and store it in a cloud bucket or vector store. "
        "Organize the content by subject and grade level."
    ),
    expected_output="Downloaded, processed, and categorized educational content.",
    agent=downloader,
    input_file="curriculum_urls.txt",  # Use this file as input for the URLs
)
