from crewai import Agent
from crewai_tools import SerperDevTool
from src.education_crewai.tools.downloader_tool import download_and_process_content

# Define the search tool
search_tool = SerperDevTool()

# Educational Researcher Agent
researcher = Agent(
    role="Educational Researcher",
    goal="Gather grade-appropriate curriculum materials for the student.",
    verbose=True,
    memory=True,
    backstory=(
        "You have a deep understanding of educational resources and know how to find the best "
        "materials suited to a student's grade level."
    ),
    tools=[search_tool],
)

# Curriculum Developer Agent
compiler = Agent(
    role="Curriculum Developer",
    goal="Organize the researched materials into a comprehensive study program for the student.",
    verbose=True,
    memory=True,
    backstory=(
        "You excel at organizing educational content into structured programs that students can easily follow."
    ),
)

# Content Downloader Agent
downloader = Agent(
    role="Content Downloader",
    goal="Visit each URL provided, download the curriculum, process it with OpenAI, and store it in the cloud bucket by subject and grade level.",
    verbose=True,
    memory=True,
    backstory=(
        "You are skilled in gathering and organizing educational materials. "
        "Your mission is to collect, process, and store curriculum content effectively."
    ),
    tools=[download_and_process_content],  # Tool to download and process content
)
