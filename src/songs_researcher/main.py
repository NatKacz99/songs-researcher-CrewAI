#!/usr/bin/env python
import sys
import warnings
import os

from songs_researcher.crew import SongsResearcherCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the leading songs research crew.
    """
    inputs = {
        # Example input for genre-based research
        'genre': 'rap'
    }

    # Kickoff the crew with inupts
    try:
        result = SongsResearcherCrew().crew().kickoff(inputs=inputs)

        # Print aggregated raw output
        print("===FINAL REPORT===\n")
        print(result.raw)

        print("\nReports have been saved to the 'output/' directory:")
        print(" - trending_songs.md")
        print(" - top_rock_performers.md")
        print(" - genre_research.md")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == '__main__':
    run()