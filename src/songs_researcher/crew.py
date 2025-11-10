from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class SongsResearcherCrew():
    """Songs market research crew"""

    @agent
    def trending_songs_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['trending_songs_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def top_rock_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['top_rock_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def genre_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['genre_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @task
    def trending_topics_task(self) -> Task:
        return Task(
            config=self.tasks_config['trending_topics_task']
        )

    @task
    def top_rock_performers_task(self) -> Task:
        return Task(
            config=self.tasks_config['top_rock_performers_task']
        )

    @task
    def genre_task(self) -> Task:
        return Task(
            config=self.tasks_config['genre_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the research crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )